#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from frictionless import Package
from csvs_convert import datapackage_to_sqlite


if len(sys.argv) == 1:
    print("You need to pass a datapackage.json or a csv filename: python load_data.py FILENAME")
    sys.exit()

filename = sys.argv[1]
filename_extension = filename.split('.')[-1]

def load_datapackage(datapackage):
    datapackage_to_sqlite('sqlite.db', datapackage)
    os.system('datasette sqlite.db')

def load_csv(csv_file):
    package = Package(csv_file)
    package.infer()
    package.to_json('datapackage.json')
    load_datapackage('datapackage.json')

    if filename_extension == 'json':
        load_datapackage(filename)
    elif filename_extension == 'csv':
        load_csv(filename)

