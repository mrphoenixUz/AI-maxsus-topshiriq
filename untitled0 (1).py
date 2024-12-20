# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1k4PayiXXp5L3n0JLVhhi_CzboXit009F
"""

import pandas as pd

file_path = 'WHO-COVID-19-cases.csv'

try:
    df = pd.read_csv(file_path)
    country_name = "Afghanistan"
    filtered_df = df[df['Country'] == country_name]
    print(filtered_df.head())
except FileNotFoundError:
    print(f"Error: File not found at '{file_path}'. Please check the file path.")
except KeyError:
  print(f"Error: 'Country' column not found in the CSV file. Please check the file structure.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")