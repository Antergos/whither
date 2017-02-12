#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# config.py
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

# Standard Lib
import os
import pkg_resources
from typing import Callable

# 3rd Party Libs
import ruamel.yaml as yaml


class ConfigLoader:
    _filters = []

    def __init__(self, key: str, path: str = None) -> None:
        self.load_from = path
        self.config = self.load_config(key)

    def _filter_data(self, key: str, data: str) -> str:
        if not self._filters:
            return data

        for callback in self._filters:
            data = callback(key, data)

        return data

    @classmethod
    def add_filter(cls, callback: Callable[[str, str], None]) -> None:
        cls._filters.append(callback)

    def load_config(self, key: str) -> dict:
        try:
            data = pkg_resources.resource_string(self.load_from, 'whither.yml').decode('utf-8')
            data = self._filter_data(key, data)
            config = yaml.safe_load(data)
            config = config[key]
        except Exception:
            data = open(self.load_from, 'r').read()
            data = self._filter_data(key, data)
            config = yaml.safe_load(data)
            config = config[key]

        return {key: value for key, value in config.items()}

    @classmethod
    def remove_filter(cls, callback: Callable[[str, str], None]) -> None:
        cls._filters.remove(callback)
