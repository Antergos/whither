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
from logging import (
    getLogger,
    DEBUG,
    Formatter,
    StreamHandler,
)
from typing import (
    ClassVar,
    Tuple,
    Type,
    TypeVar,
)

# This Lib
from .data import (
    AttributeDict,
    SharedData,
)

# Typing Helpers
BridgeObjects = Tuple[Type['BridgeObjectBase']]
Widget = TypeVar('Widget', 'QObject', 'GObject')

# Application class is a singleton
_APP_INSTANCE = None

_MAIN_COMPONENTS = (
    '_app',
    '_config',
    '_logger',
    '_main_window',
    '_web_container',
    'config',
)


class BaseObject:
    _app = SharedData()            # type: ClassVar[Type['Application']]
    _config = SharedData()         # type: ClassVar[Type[AttributeDict]]
    _main_window = SharedData()    # type: ClassVar[Type['Window']]
    _web_container = SharedData()  # type: ClassVar[Type['WebContainer']]

    config = SharedData()          # type: ClassVar[Type[AttributeDict]]
    is_gtk = None                  # type: ClassVar[bool]
    is_qt = None                   # type: ClassVar[bool]
    logger = SharedData()          # type: ClassVar[Type['Logger']]
    windows = SharedData()         # type: ClassVar[list]

    def __init__(self, name: str, *args, **kwargs) -> None:
        self.name = name    # type: str
        self.widget = None  # type: Widget

        if name in _MAIN_COMPONENTS:
            self._register_main_component(name)

    def __init_subclass__(cls, **kwargs) -> None:
        super().__init_subclass__()
        cls.__pre_init__()

    @classmethod
    def __pre_init__(cls):
        pass

    def _register_main_component(self, name: str) -> None:
        attrib = getattr(self, name)

        if attrib is None:
            setattr(self, name, self)

    def _setup_logger(self, name: str):
        log_format = ''.join([
            '%(asctime)s [ %(levelname)s ] %(module)s - %(filename)s:%(',
            'lineno)d : %(funcName)s | %(message)s'
        ])

        formatter = Formatter(fmt=log_format, datefmt="%Y-%m-%d %H:%M:%S")
        stream_handler = StreamHandler()
        self.logger = getLogger()

        stream_handler.setLevel(DEBUG)
        stream_handler.setFormatter(formatter)
        self.logger.setLevel(DEBUG)
        self.logger.addHandler(stream_handler)
        self.logger.debug('Logger is ready.')


class Application(BaseObject):

    windows = []  # type: ClassVar[list]

    def __init__(self, name: str, *args, **kwargs) -> None:
        global _APP_INSTANCE
        if _APP_INSTANCE is not None:
            return

        _APP_INSTANCE = self

        super().__init__(name=name, *args, **kwargs)

    def run(self) -> int:
        raise NotImplementedError()


class WebContainer(BaseObject):

    def __init__(self, name: str, bridge_objs: BridgeObjects = None, *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self.bridge_objects = bridge_objs or ()

    def initialize_bridge_objects(self) -> None:
        raise NotImplementedError()

    def load(self, url: str) -> None:
        raise NotImplementedError


class Window(BaseObject):

    states = SharedData()  # type: ClassVar[AttributeDict]

    def __init__(self, name: str, *args, **kwargs) -> None:
        super().__init__(name=name, *args, **kwargs)

        self.state = 0  # type: int

    def _initialize(self) -> tuple:
        config = self._config.window
        toolbar_config = self._config.toolbar
        initial_state = config.initial_state.upper()

        return config, toolbar_config, initial_state

    def show(self) -> None:
        raise NotImplementedError()

    def set_state(self, state: int) -> None:
        raise NotImplementedError()
