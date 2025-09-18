from utils import pd, np, create_plot

df_transfer = pd.read_csv('data/df_transfer.csv', sep=',', index_col=[0])   # load the dataframe

print("Dataframe info:")
print(df_transfer.info()) #this cannot be written in a file, we just print it on the console

with open('results/other/EDA.txt', 'w') as file:
    file.write(f"### Exploratory data analysis on df_transfer ###")
    file.write(f"\n\nDataframe head:\n{df_transfer.head()}")


# Explore df_transfer columns

with open('results/other/EDA.txt', 'a') as file:
    file.write(f"\n\nNumber of unique players: {df_transfer['player_id'].nunique()}")
    file.write(f"\nNumber of unique departure clubs: {df_transfer['from_club_id'].nunique()}")
    file.write(f"\nNumber of unique arrival clubs: {df_transfer['to_club_id'].nunique()}")
    file.write(f"\nNumber of unique seasons: {df_transfer['transfer_season'].nunique()}")

    # for my curiousity
    file.write(f"\n\nFor my curiosity:")
    file.write(f"\nTransfers 'in the future':\n{df_transfer[df_transfer['transfer_season'] == '26/27']}")
    file.write(f"\n\nRetired players that went 'back in the game':\n{df_transfer[df_transfer['from_club_name'] == 'Retired']}")  #Szczesny!

    file.write(f"\n\nDescription of numerical columns:\n{df_transfer[['transfer_fee', 'market_value_in_eur']].describe()}")

create_plot('box', df_transfer['transfer_fee'], 'Distribution of transfer fee', '', '', 'Distribution_transfer_fee', rotation=0, bottom=0.1, grid=True)
create_plot('box', df_transfer['market_value_in_eur'], 'Distribution of market value in eur', '', '', 'Distribution_market_value_in_eur', rotation=0, bottom=0.1, grid=True)


# Compute the number of transfers per season

df_transfer['transfer_season_complete'] = np.where(df_transfer['transfer_season'].str.startswith('9'), '19'+df_transfer['transfer_season'], '20'+df_transfer['transfer_season'])

with open('results/other/EDA.txt', 'a') as file:
    file.write(f"\n\nAdded a new column transfer_season_complete:\n{df_transfer[['transfer_season', 'transfer_season_complete']].head()}")
    file.write(f"\n\nNumber of transfers per season:\n{df_transfer['transfer_season_complete'].value_counts().reset_index(drop=False).sort_values('transfer_season_complete')}")

num_transfers_per_season = df_transfer['transfer_season_complete'].value_counts().sort_index()
create_plot('line', num_transfers_per_season, 'Number of transfers per season', 'Season', 'Number of transfers', 'Num_transfers_per_season', rotation=90, bottom=0.2, grid=True)


# Now we will answer to the 3 questions suggested by Llama

# 1. Which football clubs have the highest average transfer fee paid for each player?

club_fee = df_transfer[~df_transfer['transfer_fee'].isna()].groupby('to_club_name', as_index=False).agg(average_transfer_fee=('transfer_fee', 'mean')).sort_values('average_transfer_fee', ascending=False).reset_index(drop=True)

with open('results/other/EDA.txt', 'a') as file:
    file.write(f"\n\nAverage transfer fee payed by arrival clubs:\n{club_fee.iloc[:20]}")   #write only the 20 top clubs

# 2. How has the market value of football players changed over time, considering both the average market value and the number of players with a known market value?

season_value = df_transfer[~df_transfer['market_value_in_eur'].isna()].groupby('transfer_season_complete').agg(average_market_value=('market_value_in_eur', 'mean'))

with open('results/other/EDA.txt', 'a') as file:
    file.write(f"\n\nAverage market value in eur per season over the last 20 years:\n{season_value}")   #write only the 20 top clubs

create_plot('line', season_value, 'Average market value in eur per season', 'Season', 'Average market value in eur', 'Average_market_value_in_eur_per_season', rotation=90, bottom=0.2, grid=True)