# Formula1 (Statistically) Who is the GOAT?
## Exploritory Study to Frame the GOAT question in future anaysis

![F1DataScience](F1DataSciencelegacy.png)Exploritory analysis of F1 Team Succes, results, Recency Bias

# Introduction
Arguing over which Formula 1 team or driver is the “Greatest of All Time” is a perennial fan discussion.  
This study approaches that question as a measurement problem, exploring how changes to Formula 1’s points system introduced structural recency bias when comparing driver or team performance across eras.

Since 1950, both the value of a race win and the number of point-scoring opportunities have steadily increased, with major inflection points in 2010 (25-point wins), 2019 (fastest-lap points), and 2021 (sprint races). As a result, a driver could earn a maximum of 9 points in a 1950 race weekend, compared to as many as 34 points in 2024. This analysis documents these rule changes and examines how they reshape longitudinal comparisons.

Relies on data at kaggle.com     

### Repository Contents

| File | Description |
|-----|-------------|
| [F1CalendarInflation.png](F1CalendarInflation.png) | Bar chart showing the increase in races per season over time |
| [F1DataScienceLegacy.png](F1DataScienceLegacy.png) | Banner graphic used in the README |
| [F1_CalendarInflationWB.ipynb](F1_CalendarInflationWB.ipynb) | Jupyter notebook that generates calendar inflation bar charts |
| [f1-mostpoints.ipynb](f1-mostpoints.ipynb) | Notebook of analysis and commentary|

## Research Question
Explore the difference between raw points awarded per Grand Prix Race vs normalized scoring system.

The new comers Mercedes and RedBulls' performance as reflected by points suggests the impact of recency bias.

# Culmulative Championship Points 1950-2004
| Constructor | Points| Debut Year
|------------|-------------------------|-----------|
| Ferrari    | 11,091.27               |1950       |
| Mercedes   | 7,730.64                |1959 / 2009|
| Red Bull   | 7,673.00                |2005
| McLaren    | 7,022.50                |1966       |
| Williams   | 3,641.00                |1975

Note:  Mercedes left F1 in 1955 and rejoined in 2009


## Hypothesis
Informal - Raw championship points embed era-dependent inflation, biasing cumulative comparisons in favor of newer teams over legacy constructors like McLaren.

## Data
Formula 1 constructors, races, driver, team statistics at kaggle.com     

## Methodology 
# Data Preparation
normalized data sets to create analytical (flat) panda data frame replacing forieng keys with descriptive / catagorical names.
# Analytical Approach
1.  Controled opportunity to score by only measuring performance in the GrandPrix race removing the impact of qualifying points and sprint weekends  
2. Applied a standardized points system for the first 10 places
# Tools
Python Juptyter Notebook: Pandas, Numpy  
## Results and Analyis
| Constructor| Revised Points | Raw Points |
|:-----------|----------------|----------- |
| Ferrari    | 11,568         | 11,091
| McLaren    | 7,607          |  7,023
| Williams   | 4,834          |  3,641
| Red Bull   | 4,072          |  7,673
| Mercedes   | 3,949          |  7,731

Rescoring benefits the legacy teams, particularly Williams who won 9 championships from 1980 - 1997 but whose last race victory was in 2012.  

## Conlcusion 

One key outcome of this exploration is the recognition that team and driver performance is inherently relative to contemporaneous peers rather than an absolute accumulation of points. Subsequent work builds on this insight by using distributional analysis to frame well-posed inferential questions, rather than presupposing them.

# Next Step


