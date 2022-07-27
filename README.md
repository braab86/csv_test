# Web Traffic Transformation 

## Introduction

This module downloads data from a series of csv files stored in an AWS S3 bucket. 
It then loads the data into DataFrames, concatenates the DataFrames, pivots 
the DataFrames, then exports as a csv

## Requirements

* Python 3+
* pandas

## Notes

The root url and the list of file names can be modified in csv_test.py

