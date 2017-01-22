#!/usr/bin/python3
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
from typing import Tuple

# 3rd-Party Libs
from PyQt5.QtWebEngineWidgets import (
    QWebEnginePage,
    QWebEngineView,
    QWebEngineSettings,
    QWebEngineScript,
)
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtCore import QUrl, QFile

# This Library
from whither.base.objects import WebContainer

# Typing Helpers
BridgeObjects = Tuple['BridgeObject']


class QtWebContainer(WebContainer):

    def __init__(self,
                 name: str = 'web_container',
                 bridge_objs: BridgeObjects = None, debug: bool = False, *args, **kwargs) -> None:

        super().__init__(name=name, bridge_objs=bridge_objs, *args, **kwargs)

        if debug:
            os.environ['QTWEBENGINE_REMOTE_DEBUGGING'] = '1234'

        self.page = QWebEnginePage(self._main_window.widget)  # type: QWebEnginePage
        self.view = QWebEngineView(self._main_window.widget)  # type: QWebEngineView
        self.channel = QWebChannel(self.page)                 # type: QWebChannel

        self._initialize()

        self._init_bridge_channel()

        if self._config.entry_point.autoload:
            self.load()

        self.view.show()
        self._main_window.widget.setCentralWidget(self.view)

    @staticmethod
    def _get_channel_api_script() -> QWebEngineScript:
        script = QWebEngineScript()
        script_file = QFile(':/qtwebchannel/qwebchannel.js')

        if script_file.open(QFile.ReadOnly):
            script_string = str(script_file.readAll(), 'utf-8')

            script.setInjectionPoint(QWebEngineScript.DocumentReady)
            script.setName('QWebChannel API')
            script.setWorldId(QWebEngineScript.MainWorld)
            script.setSourceCode(script_string)

        return script

    def _init_bridge_channel(self) -> None:
        self.page.setWebChannel(self.channel)
        self.page.scripts().insert(self._get_channel_api_script())

        self.initialize_bridge_objects()

    def _initialize(self) -> None:
        page_settings = self.page.settings().globalSettings()

        self.page.setView(self.view)

        page_settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        page_settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        page_settings.setAttribute(QWebEngineSettings.ScrollAnimatorEnabled, True)

    def initialize_bridge_objects(self) -> None:
        registered_objects = self.channel.registeredObjects()

        for obj in self.bridge_objects:
            if obj not in registered_objects:
                self.channel.registerObject(obj._name, obj)

    def load(self, url: str = '') -> None:
        url = url if url else self._config.entry_point.url

        self.page.load(QUrl(url))
