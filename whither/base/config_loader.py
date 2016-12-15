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

# 3rd Party Libs
import ruamel.yaml as yaml

# This Lib
from .object import BaseObject

CONFIG_FB = '/home/dustin/github/antergos/cnchi/cnchi/ui/dev/whither/dist/whither.yml'


class ConfigLoader(BaseObject):
    config_path = '/etc/whither.yml'  # type: str
    config_path_fallback = CONFIG_FB  # type: str
    config = {}                       # type: dict

    def __init__(self, app_name, config_file_path='') -> None:
        super().__init__(name='config_loader')

        if config_file_path:
            self.config_path = config_file_path

        self.load_config(app_name)

        self._config = self.config

    def load_config(self, app_name) -> None:
        config_paths = [self.config_path, self.config_path_fallback]
        config_files = [p for p in config_paths if p and os.path.exists(p)]

        if not any(config_files):
            self._logger.error('Config file not found (load_config() failed!)')
            return

        data = open(config_files[0], 'r').read()
        config = yaml.safe_load(data)
        config = config[app_name]

        self.config = {key: value for key, value in config.items()}
