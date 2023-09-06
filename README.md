# Description
This project aims to provide a dashboard for searching for insights and have a whole picture of the current secondary real estate market trends and patterns in Tbilisi based on the data from korter.ge website.   
⚠️**The project is no longer maintained because the automatic update does not work, and I can no longer pay for the server.**

The 🔗[link](https://public.tableau.com/app/profile/volodymyr.khudokormov/viz/korter_geSecondaryRealEstateMarketAnalysis/Dashboard1?publish=yes) 
to the actual dashboard version. The screenshot is also clickable

[![Link](https://i.ibb.co/473pfGQ/chrome-Jl-Rwm-Uhl-Fz.png)](https://public.tableau.com/app/profile/volodymyr.khudokormov/viz/korter_geSecondaryRealEstateMarketAnalysis/Dashboard1?publish=yes)

It should be refreshed daily (⚠️unfortunately, it doesn't refresh daily).   
🔴**There is some bug on the Tableau side**. The request to solve the problem is created and can be accessed by the [link](https://community.tableau.com/s/feed/0D58b0000AhNxrlCQC)

# Summary
I developed and implemented a complete ETL process (it's my first independent project). I scraped the website  http://www.korter.ge to retrieve the relevant data. After parsing, it's transformed using Pandas and stored in a Google Spreadsheet. The Python script used for the ETL process is hosted on AWS and version-controlled on GitHub for easy updates. The script is running daily through a bash script and scheduled using crontab.

To complete this project, I utilized several technologies and libraries, including:

## Python libraries:
* Selenium for website scraping
* BeautifulSoup for data parsing
* Pandas for data transformation
* Gspread and gspread_dataframe for working with Google Spreadsheet API

## Cloud services:
* AWS for hosting the Python script
* Google Spreadsheet for storing the processed data

## Tools:
* Tableau for visualization
* GitHub for version control of the Python script
* Bash script for downloading the script from GitHub
* Crontab for scheduling the scripts run

# Personal
It was a challenging task as I am new in this field; however, I liked to work on the different technologies and connect various tools to make a meaningful, valuable result.
