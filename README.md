# ozone
This is a proof-of-concept machine learning project which uses time-series weather data to predict extreme ozone events.

## How to run
This is a simple Python package, tested on Python 3.10.
Please install package dependencies found in requirements.txt, and it should be good to go!

## Input data
The input data is time-series metereological data that can be found at https://archive.ics.uci.edu/ml/datasets/Ozone+Level+Detection. 
An explanation of the data is given there. The goal was to only use the 8hr resolution data set, which is included in this repository under src/data/eighthr.data

## Aims
To predict whether the column 'Ozone' would have a 1 (positive, ozone event, extreme weather day) or a 0 (negative, no ozone event).

## Method
See explanation.pdf!

### Method summary
I used the sklearn StandardScaler and LogisticRegression model to predict a continuous variable for ozone event.
I used balanced class weights to overcome the issue of imbalanced classes (low fraction of days are ozone events), and this improved the log loss by ~10%.
