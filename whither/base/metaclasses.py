# -*- coding: utf-8 -*-
#
# metaclasses.py
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
import types


class PEP487Shim(type):
    """ This metaclass adds support for PEP 487 to Python 3.1+ """

    def __new__(mcs, *args, **kwargs):
        if len(args) != 3:
            return super().__new__(mcs, *args)

        name, bases, classdict = args
        init_subclass = classdict.get('__init_subclass__')

        if isinstance(init_subclass, types.FunctionType):
            classdict['__init_subclass__'] = classmethod(init_subclass)

        self = super().__new__(mcs, name, bases, classdict)

        for key, value in self.__dict__.items():
            func = getattr(value, '__set_name__', None)
            if func is not None:
                func(self, key)

        super(self, self).__init_subclass__(**kwargs)

        return self

    def __init__(self, name, bases, classdict, **kwargs):
        super().__init__(name, bases, classdict)
