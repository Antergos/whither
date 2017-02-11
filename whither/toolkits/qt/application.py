#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# application.py
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

# 3rd-Party Libs
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication

# This Lib
from whither.base.objects import Application


class QtApplication(Application):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(name='_app', *args, **kwargs)

        self.widget = QApplication([])
        self.is_qt, self.is_gtk = True, False
        self.desktop = self.widget.desktop()

        self.widget.setAttribute(Qt.AA_EnableHighDpiScaling)

    def _set_window_size_position(self) -> None:
        if self._config.window.no_desktop_env is False:
            return

        self._main_window.widget.setGeometry(self.desktop.availableGeometry())

    def run(self) -> int:
        self._set_window_size_position()

        return self.widget.exec_()
