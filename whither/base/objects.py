#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# objects.py
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

""" Bases Classes (for future flexibility) """

# Standard Lib
from typing import Type, Tuple

# This Lib
from .data import SharedData, AttributeDict

# Typing Helpers
BridgeObjs = Tuple[Type['BridgeObjectBase']]

# Application class is a singleton
_APP_INSTANCE = None


class BaseObject:
    _app = SharedData('_app')                      # type: Type['Application']
    _config = SharedData('_config')                # type: Type[AttributeDict]
    _logger = SharedData('_logger')                # type: Type['Logger']
    _main_window = SharedData('_main_window')      # type: Type['Window']
    _web_container = SharedData('_web_container')  # type: Type['WebContainer']

    config = SharedData('config')                  # type: Type[AttributeDict]
    is_gtk = None                                  # type: bool
    is_qt = None                                   # type: bool

    def __init__(self, name: str = 'base_object', *args, **kwargs) -> None:
        self.widget = None  # type: object
        self.name = name

    def _register_main_component(self, name: str) -> None:
        attrib = getattr(self, name)

        if attrib is None:
            setattr(self, name, self)


class Application(BaseObject):

    windows = None  # type: list

    def __init__(self, name: str = 'application', *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        global _APP_INSTANCE
        if _APP_INSTANCE is None:
            _APP_INSTANCE = self
            self.windows = []

        self._register_main_component('_app')

    def run(self) -> int:
        raise NotImplementedError()


class WebContainer(BaseObject):

    def __init__(self,
                 name: str = 'web_container',
                 bridge_objs: BridgeObjs = None, *args, **kwargs) -> None:

        super().__init__(name=name, *args, **kwargs)

        self._register_main_component('_web_container')

        self.bridge_objects = bridge_objs or ()  # type: tuple

    def initialize_bridge_objects(self) -> None:
        raise NotImplementedError()

    def load(self, url: str) -> None:
        raise NotImplementedError


class Window(BaseObject):

    states = SharedData('states')  # type: AttributeDict
    state = None                   # type: int

    def __init__(self, name: str = 'main_window', *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self._register_main_component('_main_window')

    def _initialize(self) -> None:
        raise NotImplementedError()

    def show(self) -> None:
        raise NotImplementedError()

    def set_state(self, state: int) -> None:
        raise NotImplementedError()
