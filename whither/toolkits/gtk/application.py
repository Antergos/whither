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

""" Wrapper for Gtk.Application """

# 3rd-Party Libs
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# This Library
from whither.base.objects import Application


class GtkApplication(Application):

    def __init__(self, name: str = 'application', *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self.widget = Gtk.Application()        # type: Gtk.Application
        self.is_qt, self.is_gtk = False, True  # type: bool

    def run(self) -> int:
        return self.widget.run(None)
