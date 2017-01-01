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
from typing import Optional, Tuple

# 3rd-Party Libs
from PyQt5.QtWebChannel import QWebChannel
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl, QFile

# This Library
from .._web_container import WebContainer
from .bridge import BridgeObjectBase

# Typing Helpers
BridgeObjects = Optional[Tuple[BridgeObjectBase]]

QWebEngineSettings = QtWebEngineWidgets.QWebEngineSettings
QWebEngineScript = QtWebEngineWidgets.QWebEngineScript


class QtWebContainer(WebContainer):

    def __init__(self, bridge_objects: BridgeObjects = None) -> None:
        super().__init__(bridge_objects)
        self.page = QtWebEngineWidgets.QWebEnginePage(self._main_window.widget)
        self.view = QtWebEngineWidgets.QWebEngineView(self._main_window.widget)
        self.channel = QWebChannel(self.page)

        self._initialize()

        if self.bridge_objects:
            self._init_bridge_channel()

        self.page.load(QUrl(self._config.whither.entry_point))
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

        for obj in self.bridge_objects:
            self.channel.registerObject(obj.name, obj)

    def _initialize(self) -> None:
        page_settings = self.page.settings().globalSettings()

        self.page.setView(self.view)

        page_settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        page_settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        page_settings.setAttribute(QWebEngineSettings.ScrollAnimatorEnabled, True)
