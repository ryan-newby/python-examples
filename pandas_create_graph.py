#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  6 12:29:33 2023

@author: rynewby
"""

# Source CSV from https://catalog.data.gov/dataset/places-county-data-gis-friendly-format-2020-release-4ae28
import pandas as pd

# Ingest the data through 1 of the provided formats.
input_file = pd.read_csv('PLACES__County_Data__GIS_Friendly_Format___2020_release.csv')

# Create a data structure to store the data.
df = pd.DataFrame(input_file)

# Conduct any cleansing and preprocessing needed
df = df[df['StateAbbr'] == "CO"]

df = df[['StateAbbr', 'CountyName', 'TEETHLOST_AdjPrev']]

print(df)

# Creare graph od first 10 records, X-axis representing county name, Y-axis average number of teeth lost
df_graph = df.head(10).plot.bar(x='CountyName', y='TEETHLOST_AdjPrev')
