#!/usr/bin/env python
# CheerLights.py - a simple class to get the most recent cheerlight colours
# Copyright 2014 by Simon Walters from code by Carl Monk https://github.com/ForToffee/CheerLights
#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

import urllib2
import json


class CheerLights():
    def __init__(self):
        self.lastID = 0
        self.urlRoot = "http://api.thingspeak.com/channels/1417/"
        self.colours = []

    # retrieve and load the JSON data into a JSON object
    def getJSON(self, url):
        jsonFeed = urllib2.urlopen(self.urlRoot + url)
        feedData = jsonFeed.read()
        # print feedData
        jsonFeed.close()
        data = json.loads(feedData)
        # data = feedData
        return data

    # read the last entry_id
    def getEntryID(self, feed):
        return int(feed["entry_id"])

    def get_colours(self):
        last = self.getJSON("field/1/last.json")
        if self.getEntryID(last) > self.lastID:   # Have processed this entry_id before?
            self.colours = []
            data = self.getJSON("feed.json")
            for feed in data["feeds"]:
                self.colours = [str(feed["field1"])] + self.colours
                self.lastID = self.getEntryID(feed)
        return self.colours            
