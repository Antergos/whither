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
import pkg_resources

# 3rd Party Libs
import ruamel.yaml as yaml

# This Lib
from .objects import BaseObject


class ConfigLoader(BaseObject):
    load_from = '__main__'

    def __init__(self, app_name: str) -> None:
        super().__init__(name='config_loader')

        config = self.load_config(app_name)

        super().__setattr__('config', config['app'])
        super().__setattr__('_config', config['whither'])

    def load_config(self, app_name: str) -> dict:
        try:
            data = pkg_resources.resource_string(self.load_from, 'whither.yml')
        except Exception:
            data = pkg_resources.resource_string(__file__, 'whither.yml')

        config = yaml.safe_load(data)
        config = config[app_name]

        return {key: value for key, value in config.items()}
