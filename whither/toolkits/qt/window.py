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
from typing import Dict

# 3rd-Party Libs
from PyQt5.QtWidgets import (
    QMainWindow,
    QAction,
    qApp,
    QWidget,
)
from PyQt5.QtCore import (
    QEvent,
    Qt,
)
from PyQt5.QtGui import QIcon

# This Library
from whither.base.objects import Window

# Typing Helpers
QtWindowStatesT = Dict[str, Qt.WindowState]


WINDOW_STATES = {
    'NORMAL': Qt.WindowNoState,
    'MINIMIZED': Qt.WindowMinimized,
    'MAXIMIZED': Qt.WindowMaximized,
    'FULLSCREEN': Qt.WindowFullScreen,
}  # type: QtWindowStatesT


class QtWindow(Window):

    def __init__(self, name: str = '_window', *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self.states = WINDOW_STATES  # type: dict
        self.widget = None           # type: QWidget

        self._initialize()

    def _initialize(self) -> None:
        config, toolbar_config, initial_state = super()._initialize()

        if not self._app.windows:
            self.widget = QMainWindow()
            this_window = 'Main Window'
        else:
            self.widget = QWidget()
            this_window = 'Window'

        self.logger.debug('Initializing %s', this_window)

        self._app.windows.append(self.widget)

        self.widget.setAttribute(Qt.WA_DeleteOnClose)

        if config.title:
            self.widget.setWindowTitle(config.title)

        if config.icon:
            self.widget.setWindowIcon(QIcon(config.icon))

        if config.width and config.height:
            self.widget.setFixedSize(config.width, config.height)

        if config.decorated and toolbar_config.enabled:
            self._init_menu_bar()

        elif not config.decorated:
            self.widget.setWindowFlags(self.widget.windowFlags() | Qt.FramelessWindowHint)

        if config.stays_on_top:
            self.widget.setWindowFlags(
                self.widget.windowFlags() | Qt.WindowStaysOnTopHint
            )

        self.widget.setWindowFlags(
            self.widget.windowFlags() | Qt.MaximizeUsingFullscreenGeometryHint
        )

        self.set_state(self.states[initial_state])

    def _init_menu_bar(self) -> None:
        exit_action = QAction(QIcon('exit.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)

        menu_bar = self.widget.menuBar()

        file_menu = menu_bar.addMenu('&File')
        file_menu.addAction(exit_action)

        edit_menu = menu_bar.addMenu('&Edit')
        edit_menu.addAction(exit_action)

        view_menu = menu_bar.addMenu('&View')
        view_menu.addAction(exit_action)

        about_menu = menu_bar.addMenu('&About')
        about_menu.addAction(exit_action)

    def changeEvent(self, event: QEvent) -> None:
        if event is not QEvent.WindowStateChange:
            return

        try:
            new_window_state = self.widget.windowHandle().windowState()
        except Exception:
            new_window_state = self.widget.windowState()

        if new_window_state & self.states['MAXIMIZED']:
            self.state = self.states['MAXIMIZED']

        elif new_window_state & self.states['FULLSCREEN']:
            self.state = self.states['FULLSCREEN']

        elif new_window_state & self.states['MINIMIZED']:
            self.state = self.states['MINIMIZED']

        else:
            self.state = self.states['NORMAL']

    def show(self) -> None:
        self.widget.show()

    def show_fullscreen(self) -> None:
        try:
            self.widget.windowHandle().showFullScreen()
        except Exception:
            self.widget.showFullScreen()

    def show_maximized(self) -> None:
        try:
            self.widget.windowHandle().showMaximized()
        except Exception:
            self.widget.showMaximized()

    def show_minimized(self) -> None:
        try:
            self.widget.windowHandle().showMinimized()
        except Exception:
            self.widget.showMinimized()

    def set_state(self, new_state: Qt.WindowState) -> None:
        if new_state == self.state:
            return

        try:
            self.widget.windowHandle().setWindowState(new_state)
        except Exception:
            self.widget.setWindowState(new_state)

