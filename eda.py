from utils import *

df_transfer = pd.read_csv('data/df_transfer.csv', sep=',', index_col=[0])
print(df_transfer.info())
print(df_transfer.head())

# Explore df_transfer columns
print(f'Nmber of unique players: {df_transfer['player_id'].nunique()}')
print(f'Number of unique departing clubs: {df_transfer['from_club_id'].nunique()}')
print(f'Number of unique arriving clubs: {df_transfer['to_club_id'].nunique()}')
print(f'Number of unique seasons: {df_transfer['transfer_season'].nunique()}')

print(df_transfer['transfer_season'].value_counts())

# for my curiousity
print(df_transfer[df_transfer['transfer_season'] == '26/27'])
print(df_transfer[df_transfer['from_club_name'] == 'Retired'])  #Szczesny!

print(df_transfer[['transfer_fee', 'market_value_in_eur']].describe())
create_plot('box', df_transfer['transfer_fee'], 'Distribution of transfer fee', '', '', 'Distribution_transfer_fee.png', rotation=0, bottom=0.1, grid=True)
create_plot('box', df_transfer['market_value_in_eur'], 'Distribution of market value in eur', '', '', 'Distribution_market_value_in_eur.png', rotation=0, bottom=0.1, grid=True)

# number of transfers per season
df_transfer['transfer_season_complete'] = np.where(df_transfer['transfer_season'].str.startswith('9'), '19'+df_transfer['transfer_season'], '20'+df_transfer['transfer_season'])
print(df_transfer[['transfer_season', 'transfer_season_complete']].head())
print(df_transfer['transfer_season_complete'].value_counts().sort_index())
num_transfers_per_season = df_transfer['transfer_season_complete'].value_counts().sort_index()
create_plot('line', num_transfers_per_season, 'Number of transfers per season', 'Season', 'Number of transfers', 'Num_transfers_per_season.png', rotation=90, bottom=0.2, grid=True)