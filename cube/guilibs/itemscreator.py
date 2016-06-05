#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from cube.guilibs import graphics

class ItemCreator:
    def __init__(self, geometry, image_dir):
        self.image_dir = image_dir
        self.geometry = geometry



    def item(self, name):
        path = os.path.join(self.image_dir, name)
        item = graphics.GraficsImage(path, name)
        item.set_geometry(self.geometry)