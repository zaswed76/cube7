#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets

from cube.guilibs import graphics

class Widget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500, 500)