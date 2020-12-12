import pandas as pd
import glob

path = r'C:\Users\merma\Code\Basketball_Reference_Web_Scraper\Yearly_Player_Statistics_Data'
all_files = glob.glob(path + "/*.csv")

li = []
year = 2001
for filename in all_files:
    
    df = pd.read_csv(filename, index_col=None, header=0)
    df['season'] = year
    li.append(df)
    year += 1

season_stats = pd.concat(li, axis = 0, ignore_index=True)

print(season_stats)