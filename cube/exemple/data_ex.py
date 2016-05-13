#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import yaml

from cube import paths
from cube.libs import data

data_geometry_set = os.path.join(paths.data, 'base_geometry_dict.json')

print(data_geometry_set)


def get_data(path):
    with open(path, "r") as obj:
        return yaml.load(obj)

print(get_data(data_geometry_set)['0'])