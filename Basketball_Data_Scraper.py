import pandas as pd
from basketball_reference_web_scraper.data import League
from basketball_reference_web_scraper import client
from basketball_reference_web_scraper.data import OutputType

# Output all advanced player season totals for the 2001-2020 season in CSV format

# While loop to create csv files for each year. 
year = 2001
while year < 2021:

    client.players_season_totals(season_end_year=year, output_type=OutputType.CSV, output_file_path=f"{year}_player_season_totals.csv")
    year += 1


### Need to add code to read csv, clean data, add column for data year,then build data frame for all data 2001-2020

