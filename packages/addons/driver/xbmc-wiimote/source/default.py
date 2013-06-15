################################################################################
#      This file is part of HoloVisi - http://www.holovisi.com
#      Copyright (C) 2013 Zhu Xiao Bin (zhu_xiao_bin@outlook.com)
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with HoloVisi.com; see the file COPYING.  If not, write to
#  the Free Software Foundation, 51 Franklin Street, Suite 500, Boston, MA 02110, USA.
#  http://www.gnu.org/copyleft/gpl.html
################################################################################

import os
import sys
import xbmcaddon

__scriptname__ = "WiiMote driver"
__author__ = "HoloVisi"
__url__ = "http://www.holovisi.com"
__settings__   = xbmcaddon.Addon(id='driver.remote.xbmc-wiimote')
__cwd__        = __settings__.getAddonInfo('path')
__path__       = xbmc.translatePath( os.path.join( __cwd__, 'bin', "wiimote.service") )

os.system(__path__)