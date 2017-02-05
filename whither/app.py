#!/usr/bin/python3
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

# This Library
from .toolkits.bootstrap import Application, Window, WebContainer
from .base.objects import BridgeObjs
from .base.config_loader import ConfigLoader


class App(Application):

    def __init__(self,
                 app_name,
                 bridge_objects: BridgeObjs = None,
                 debug: bool = False, *args, **kwargs) -> None:

        super().__init__(name=app_name, *args, **kwargs)

        ConfigLoader(app_name)
        Window()
        WebContainer(bridge_objects=bridge_objects, debug=debug)

        self._main_window.show()


if __name__ == '__main__':
    raise RuntimeError('Whither is a library (this module must be imported!)')
