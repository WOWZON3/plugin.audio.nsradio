#!/usr/bin/python
# -*- coding: utf-8 -*-
import xbmc, xbmcgui, xbmcaddon, xbmcplugin, os

addon = xbmcaddon.Addon()
addon_path = addon.getAddonInfo('path').decode('utf-8')

name = "NS-RADIO: Völkische Klänge ohne Zensur"
url = "http://nsradio.sytes.net:1488"
iconimage = os.path.join(addon_path,"icon.png")

liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage); liz.setInfo( type="audio", infoLabels={ "Title": name } )
xbmc.Player ().play(url, liz, True)
