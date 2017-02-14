# -*- coding: utf-8 -*-
#
# web_container.py
#
# Copyright © 2016-2017 Antergos
#
# This file is part of whither.
#
# whither is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# whither is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# The following additional terms are in effect as per Section 7 of the license:
#
# The preservation of all legal notices and author attributions in
# the material or in the Appropriate Legal Notices displayed
# by works containing it is required.
#
# You should have received a copy of the GNU General Public License
# along with whither; If not, see <http://www.gnu.org/licenses/>.

# Standard Lib
import os
from typing import (
    Tuple,
    TypeVar,
)

# 3rd-Party Libs
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWebEngineWidgets import (
    QWebEnginePage,
    QWebEngineView,
    QWebEngineSettings,
    QWebEngineScript,
)
from PyQt5.QtCore import (
    QUrl,
    QFile,
)

# This Library
from whither.base.objects import WebContainer
from .devtools import DevTools

# Typing Helpers
BridgeObjects = Tuple['BridgeObject']
Url = TypeVar('Url', str, QUrl)


DEFAULT_ENTRY_POINT = 'Whither: Unable to load entry point.'

DISABLED_SETTINGS = [
    'PluginsEnabled',  # Qt 5.6+
]

ENABLED_SETTINGS = [
    'FocusOnNavigationEnabled',  # Qt 5.8+
    'FullScreenSupportEnabled',  # Qt 5.6+
    'LocalContentCanAccessFileUrls',
    'ScreenCaptureEnabled',      # Qt 5.7+
    'ScrollAnimatorEnabled',
]


class QtWebContainer(WebContainer):

    def __init__(self, bridge_objs: BridgeObjects = None, *args, **kwargs) -> None:
        super().__init__(name='_web_container', bridge_objs=bridge_objs, *args, **kwargs)

        if self._config.debug_mode:
            os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '12345'

        self.view = QWebEngineView(parent=self._main_window.widget)
        self.page = self.view.page()
        self.channel = QWebChannel(self.page)
        self.bridge_initialized = False

        self._initialize_page(self.page)

        if self._config.debug_mode:
            self.devtools = DevTools()

        if self._config.entry_point.autoload:
            self.initialize_bridge_objects()
            self.load()

        self.view.show()
        self._main_window.widget.setCentralWidget(self.view)

    @staticmethod
    def _create_webengine_script(path: Url, name: str) -> QWebEngineScript:
        script = QWebEngineScript()
        script_file = QFile(path)

        if script_file.open(QFile.ReadOnly):
            script_string = str(script_file.readAll(), 'utf-8')

            script.setInjectionPoint(QWebEngineScript.DocumentCreation)
            script.setName(name)
            script.setWorldId(QWebEngineScript.MainWorld)
            script.setSourceCode(script_string)

        return script

    def _get_channel_api_script(self) -> QWebEngineScript:
        return self._create_webengine_script(':/qtwebchannel/qwebchannel.js', 'QWebChannel API')

    def _init_bridge_channel(self) -> None:
        self.page.setWebChannel(self.channel)
        self.page.scripts().insert(self._get_channel_api_script())

        self.bridge_initialized = True

    def _initialize_page(self, page: QWebEnginePage) -> None:
        page_settings = self.page.settings().globalSettings()

        if self._config.allow_remote_urls:
            ENABLED_SETTINGS.append('LocalContentCanAccessRemoteUrls')
        else:
            DISABLED_SETTINGS.append('LocalContentCanAccessRemoteUrls')

        for setting in DISABLED_SETTINGS:
            try:
                page_settings.setAttribute(getattr(QWebEngineSettings, setting), False)
            except AttributeError:
                pass

        for setting in ENABLED_SETTINGS:
            try:
                page_settings.setAttribute(getattr(QWebEngineSettings, setting), True)
            except AttributeError:
                pass

        page.setView(self.view)

    def initialize_bridge_objects(self) -> None:
        if not self.bridge_initialized:
            self._init_bridge_channel()

        registered_objects = self.channel.registeredObjects()

        for obj in self.bridge_objects:
            if obj not in registered_objects:
                self.channel.registerObject(obj._name, obj)

    def load(self, url: str = '') -> None:
        url = url if url else self._config.entry_point.url

        if 'http' not in url and not os.path.exists(url):
            self.page.setHtml(DEFAULT_ENTRY_POINT)
            return

        if not url.startswith('file'):
            url = 'file://{0}'.format(url)

        self.page.load(QUrl(url))

    def load_script(self, path: Url, name: str):
        script = self._create_webengine_script(path, name)
        return self.page.scripts().insert(script)
