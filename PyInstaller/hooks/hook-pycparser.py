#-----------------------------------------------------------------------------
# Copyright (c) 2014-2020, PyInstaller Development Team.
#
# Distributed under the terms of the GNU General Public License (version 2
# or later) with exception for distributing the bootloader.
#
# The full license is in the file COPYING.txt, distributed with this software.
#
# SPDX-License-Identifier: (GPL-2.0-or-later WITH Bootloader-exception)
#-----------------------------------------------------------------------------

# pycparser needs two modules -- lextab.py and yacctab.py -- which it
# generates at runtime if they cannot be imported.
#
# Those modules are written to the current working directory for which
# the running process may not have write permissions, leading to a runtime
# exception.
#
# This hook tells pyinstaller about those hidden imports, avoiding the
# possibility of such runtime failures.

from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all('pycparser')

print ("Used custom hook for pycparser")
