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


# 3rd-Party Libs
from PyQt5.QtWebChannel import QWebChannel
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QUrl

# This Library
from whither.base.web_container import WebContainer


class QtWebContainer(WebContainer):

    def __init__(self) -> None:
        super().__init__()
        self.page = QtWebEngineWidgets.QWebEnginePage(self._main_window.widget)
        self.view = QtWebEngineWidgets.QWebEngineView(self._main_window.widget)
        self.channel = QWebChannel(self.page)

        self._initialize()
        self._init_bridge_channel()

        self.page.load(QUrl(self._config.whither.entry_point))
        self.view.show()
        self._main_window.widget.setCentralWidget(self.view)

    def _init_bridge_channel(self):
        self.page.setWebChannel(self.channel)
        # self.channel.registerObject('PoodleBridge', self.bridge)
        # self.channel.registerObject('PoodleBridgeViews', self.views)
        # self.channel.registerObject('PoodleBridgeRouter', self.router)

    def _initialize(self) -> None:
        page_settings = self.page.settings().globalSettings()

        self.page.setView(self.view)

        page_settings.setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessRemoteUrls, True
        )
        page_settings.setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.LocalContentCanAccessFileUrls, True
        )
        page_settings.setAttribute(
            QtWebEngineWidgets.QWebEngineSettings.ScrollAnimatorEnabled, True
        )
