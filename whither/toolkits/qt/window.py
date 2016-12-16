#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# window.py
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

""" Wrapper for QMainWindow """

# Standard Lib
from enum import Enum

# 3rd-Party Libs
from PyQt5.QtWidgets import QMainWindow, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

# This Library
from whither.base.window import Window


class WindowState(Enum):
    NORMAL = Qt.WindowNoState
    MINIMIZED = Qt.WindowMinimized
    MAXIMIZED = Qt.WindowMaximized
    FULLSCREEN = Qt.WindowFullScreen


class QtWindow(Window):

    states = WindowState

    def __init__(self) -> None:
        super().__init__()

        self.widget = QMainWindow()

        self._initialize()

    def _initialize(self) -> None:
        config = self._config.whither.window
        toolbar_config = self._config.whither.toolbar
        state = config.initial_state.upper()

        self.widget.setAttribute(Qt.WA_DeleteOnClose)
        self.widget.setWindowTitle(config.title)
        self.widget.setWindowIcon(QIcon(config.icon))
        self.widget.setFixedSize(config.width, config.height)

        self.set_state(self.states[state])

        if config.decorated and toolbar_config.enabled:
            self.init_toolbar()

    def init_toolbar(self) -> None:
        pass

    def show(self) -> None:
        self.widget.show()

    def set_state(self, state) -> None:
        self.widget.setWindowState(state.value)