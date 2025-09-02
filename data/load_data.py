# Run this script to import transfermarkt data from Kaggle

file_path = "clubs.csv" #set the path to the file you'd like to load
csv_name = 'data/df_clubs.csv' #set the name of the resulting file
# no more info needed. Just run the script.

# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "davidcariboo/player-scores",
  file_path,
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:\n", df.head())

df.to_csv(csv_name)
