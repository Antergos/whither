# -*- coding: utf-8 -*-
#
# app.py
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

""" The primary entry point to the library. """

# Standard Lib
import os
import subprocess

# This Library
from .toolkits.bootstrap import Application, Window, WebContainer
from .base.objects import BridgeObjects
from .base.config_loader import ConfigLoader


class App(Application):

    def __init__(self, app_name, bridge_objects: BridgeObjects = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._wh_load_config(app_name)
        self._maybe_start_accessibility_service()

        self._before_main_window_init()
        Window('_main_window')

        self._before_web_container_init()
        WebContainer(bridge_objects=bridge_objects)

        self._main_window.show()

    def _maybe_start_accessibility_service(self):
        if not self._config.at_spi_service.enabled:
            return

        if os.path.exists(self._config.at_spi_service.command):
            subprocess.run([self._config.at_spi_service.command, self._config.at_spi_service.arg])

    def _wh_load_config(self, key: str) -> None:
        try:
            setattr(self, 'config', ConfigLoader(key, '__main__').config['app'])
            setattr(self, '_config', ConfigLoader(key, '__main__').config['whither'])
        except Exception as err:
            setattr(self, 'config', ConfigLoader(key, __file__).config['app'])
            setattr(self, '_config', ConfigLoader(key, __file__).config['whither'])

    def _before_web_container_init(self):
        pass

    def _before_main_window_init(self):
        pass


if __name__ == '__main__':
    raise RuntimeError('Whither is a library (this module must be imported!)')
