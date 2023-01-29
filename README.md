# Description
This project aims to provide a dashboard for searching for insights into the current secondary real estate market trends and patterns.

# Summary
I developed and implemented a complete ETL process (it's my first independent project). I scraped the website  http://www.korter.ge to retrieve the relevant data. After parsing, it's transformed using Pandas and stored in a Google Spreadsheet. The Python script used for the ETL process is hosted on AWS and version-controlled on GitHub for easy updates. The script is running daily through a bash script and scheduled using crontab.

# Tools
To complete this project, I utilized several technologies and libraries, including:

## Python libraries:
Selenium for website scraping
BeautifulSoup for data parsing
Pandas for data transformation
Gspread and gspread_dataframe for working with Google Spreadsheet API

## Cloud services:
AWS for hosting the Python script
Google Spreadsheet for storing the processed data

## Tools:
Tableau for creating the dashboard
GitHub for version control of the Python script
Bash script for downloading the script
Crontab for scheduling the script

I am proud of my work on this project, as it allowed me to demonstrate my web scraping, data processing, cloud computing, and scripting skills. The dashboard will provide valuable insights into the Tbilisi real estate market and be a valuable resource for those interested in this field.
