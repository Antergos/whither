#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# bootstrap.py
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

""" Bootstraps the application using either Qt (preferred) or Gtk. """

try:
    from .qt.window import QtWindow as Window
    from .qt.application import QtApplication as Application
    from .qt.web_container import QtWebContainer as WebContainer
    from .qt.bridge import Bridge as bridge, BridgeObject
    from .qt.interceptor import QtUrlRequestInterceptor as UrlRequestInterceptor
    from PyQt5.QtCore import QVariant as Variant
except ImportError:
    from .gtk.window import GtkWindow as Window
    from .gtk.application import GtkApplication as Application
    from .gtk.web_container import GtkWebContainer as WebContainer


