# IPL

Analyzing IPL Player Performance Using Pandas Grouping, Merging, and Missing Data Handling.

Problem Statement:

You are a sports data analyst tasked with extracting batting performance insights from IPL match data. You will work with two real-world IPL datasets — ball-by-ball deliveries and match metadata — to compute aggregated statistics, merge datasets, and handle missing values, simulating a realistic data wrangling pipeline.

*************************************Task 1 *************************************

Grouping, Filtering with .isin(), and Strike Rate Calculation

Using the deliveries dataset, identify the most effective death-over batsmen (overs 16–20) by following these steps:

Filter the deliveries dataframe to retain only rows where over is between 16 and 20 (inclusive).
Group by batsman and compute:
total_runs — sum of batsman_runs
balls_faced — count of deliveries
Calculate strike_rate as (total_runs / balls_faced) * 100.
Filter out batsmen who faced fewer than 200 balls in the death overs using .isin() on a list of qualifying batsmen.
Sort by strike_rate descending and display the top 10 results.



************************************** Task 2 *************************************

Merging DataFrames and Multi-Column Grouping

Merge the deliveries and matches dataframes to bring season information into the deliveries data, then identify the top run scorer per season (Orange Cap holder):

Merge deliveries with matches using deliveries['id'] and matches['id'] as the join keys, using a left join.
Group the merged dataframe by season and batsman, and compute the total batsman_runs per combination. Reset the index to produce a flat dataframe.
For each season, extract the batsman with the highest total runs using sorting and duplicate removal.
Display the final result showing one Orange Cap winner per season.

*************************************** Task 3 ***************************************

Handling Missing Values

The matches dataset contains missing values in certain columns. Address them as follows:

Display the count of missing values per column using .isnull().sum().
Drop all rows where every column is null (use the appropriate how parameter in dropna()).
For the city column, fill missing values with the string "Unknown" using fillna().
For the winner column, fill missing values with the string "No Result" using fillna().
Verify no missing values remain in these two columns and display the cleaned value counts for city.
In a markdown cell, explain in 2–3 sentences why you would use fillna() with a placeholder string rather than dropna() for the city and winner columns in this context.
