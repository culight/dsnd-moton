# Seattle Airbnb Analysis

## Dependencies
This project uses the following libraries (along with their dependencies):
- python 3.7.6
- jupyter 1.0.0
- pandas 1.0.1
- notebook 6.0.3
- matplotlib 3.1.3
- plotly_express 0.4.1

_For formatting, I use [Black](https://pypi.org/project/black/)_

## Overview
In this analysis, we would like to see how certain events might have influenced the local Airbnb market in Seattle, WA, USA. Specifically, we will answer the follwing three questions:
1. Which Summer events in Seattle appeard to have had the biggest impact on Seattle's Airbnb market?
2. Which neighborhoods were most impacted by the events?
3. Did fees change during these events?

## Description of Files

### Exploratory Data Analysis (Jupyter Notebook)
- _preproc_airbnb.ipynb_ - Preprocessing jupyter script. Basic data cleaning
- _impact_airbnb.ipynb_ - Finding the impact of certain events during the Summer months
- _nhood_data_airbnb.ipynb_ - Preprocessing map data
- _nhood_map_airbnb.ipynb_ - Creation of map data
- _fees_airbnb.ipynb_ - An analysis of fees during the periods of interest

### Utility Functions
- _utility.py_ - formatting functions
- _map_utility.py_ - formatting/preprocessing for map portion of project
- _dates.py_ - dictionary of various potential periods of interest

## How to interact with projects
- Clone (or download) the Repo
- Use Jupyter Notebook to open the EDA files of interest
  (e.g. _jupyter notebook impact_airbnb.ipynb_)

## Authors
Demerrick Moton - dmoton3.14@gmail.com