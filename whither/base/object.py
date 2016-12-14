#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# object.py
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

""" Whither Base Object """

from typing import Type


class BaseObject:
    _app = None            # type: Type['Application']
    _main_window = None    # type: Type['Window']
    _web_container = None  # type: Type['WebContainer']
    _config = None         # type: Type['Config']
    _logger = None         # type: Type['Logger']

    is_gtk = None          # type: bool
    is_qt = None           # type: bool

    def __init__(self) -> None:
        self.widget = None  # type: object

        if self.is_gtk is None:
            self.__maybe_determine_toolkit_in_use()

    def __maybe_determine_toolkit_in_use(self) -> None:
        name = self.widget.__class__.__name__

        if self.is_gtk is not None:
            return
        elif 'Gtk' not in name and 'Qt' not in name:
            return

        self.is_gtk, self.is_qt = 'Gtk' in name, 'Qt' in name
