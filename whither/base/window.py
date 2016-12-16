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

""" Base class for Window classes """

# Standard Lib
from typing import Type
from enum import Enum

# This Library
from .object import BaseObject, SharedData


class Window(BaseObject):

    states = None  # type: Type[Enum]
    state = None   # type: Type[Enum]

    def __init__(self) -> None:
        super().__init__(name='main_window')

    def _initialize(self) -> None:
        raise NotImplementedError()

    def show(self) -> None:
        raise NotImplementedError()

    def set_state(self) -> None:
        raise NotImplementedError()


