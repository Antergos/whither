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

""" Wrapper for GtkWindow """

# Standard Lib

# 3rd-Party Libs
import gi
gi.require_versions({'Gtk': '3.0', 'Gdk': '3.0'})
from gi.repository import (
    Gdk,
    Gtk,
)

# This Library
from whither.base.objects import Window


WINDOW_STATES = {
    'NORMAL': 0,
    'MINIMIZED': Gdk.WindowState.ICONIFIED,
    'MAXIMIZED': Gdk.WindowState.MAXIMIZED,
    'FULLSCREEN': Gdk.WindowState.FULLSCREEN,
}


class GtkWindow(Window):

    def __init__(self, name: str = '_window', *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self.states = WINDOW_STATES  # type: dict
        self.widget = None           # type: Gtk.Window

    def _initialize(self) -> None:
        config, toolbar_config, initial_state = super()._initialize()

        if not self._app.windows:
            self.widget = Gtk.ApplicationWindow()
        else:
            self.widget = Gtk.Window()

        self._app.windows.append(self.widget)

        if config.title:
            self.widget.set_title(config.title)

        if config.icon:
            self.widget.set_default_icon_from_file(config.icon)

        if config.width and config.height:
            self.widget.set_size_request(config.width, config.height)

        if config.decorated and toolbar_config.enabled:
            self._init_menu_bar()

        elif not config.decorated:
            self.widget.set_decorated(False)

        if config.stays_on_top:
            self.widget.set_keep_above(True)

        self.set_state(self.states[initial_state])

    def _init_menu_bar(self) -> None:
        pass

    def _set_state_normal(self):
        if self.state is self.states['MAXIMIZED']:
            self.widget.unmaximize()

        elif self.state is self.states['FULLSCREEN']:
            self.widget.unfullscreen()

        elif self.state is self.states['MINIMIZED']:
            self.widget.unfullscreen()

    def _window_state_event_cb(self, window, event, *args):
        if event.new_window_state & self.states['MAXIMIZED']:
            self.state = self.states['MAXIMIZED']

        elif event.new_window_state & self.states['FULLSCREEN']:
            self.state = self.states['FULLSCREEN']

        elif event.new_window_state & self.states['MINIMIZED']:
            self.state = self.states['MINIMIZED']

        else:
            self.state = 0

    def show(self) -> None:
        self.widget.show_all()

    def show_fullscreen(self) -> None:
        self.widget.fullscreen()
        self.widget.show_all()

    def show_maximized(self) -> None:
        self.widget.maximize()
        self.widget.show_all()

    def show_minimized(self) -> None:
        self.widget.iconify()
        self.widget.show_all()

    def set_state(self, new_state: int) -> None:
        if new_state == self.state:
            return

        if new_state is self.states['NORMAL']:
            self._set_state_normal()

        elif new_state is self.states['MAXIMIZED']:
            self.widget.maximize()

        elif new_state is self.states['FULLSCREEN']:
            self.widget.fullscreen()

        elif new_state is self.states['MINIMIZED']:
            self.widget.iconify()


