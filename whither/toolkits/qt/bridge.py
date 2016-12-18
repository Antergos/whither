#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# bridge.py
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
from typing import Tuple, Union

# 3rd-Party Libs
from PyQt5.QtCore import pyqtWrapperType, pyqtSignal, pyqtSlot, QObject

# This Library
from .._bridge import BridgeObjectBase

BuiltIns = Union[str, int, tuple, list, set, dict]
SignalDef = Tuple[str, str, Tuple[BuiltIns]]


class QtBridgeObjectBase(QObject):
    pass


class QtSignalHelper(pyqtWrapperType):
    """ This is a metaclass that makes it possible to define Qt signals dynamically """

    def __new__(mcs, classname: str, bases: list, classdict: dict):
        signals = classdict.get('_wh_signals', ())  # type: Tuple[SignalDef]

        if signals:
            classdict = mcs.__create_signals(signals, classdict)

        return type.__new__(mcs, classname, bases, classdict)

    def __create_signals(mcs, signals, classdict):
        for signal_name, callback_name, arg_types in signals:
            classdict[signal_name] = pyqtSignal(*arg_types, name=signal_name)
            classdict[callback_name] = pyqtSlot(*arg_types, name=callback_name)

        return classdict


class QtBridgeObject(QtBridgeObjectBase, metaclass=QtSignalHelper):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


