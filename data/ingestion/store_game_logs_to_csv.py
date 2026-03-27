import nba_api_client

season = "2024-25" # for testing, will add user input functionality later

#Get player game logs from api_client
player_logs_df = nba_api_client.get_player_game_logs(season)

#Save player game logs to csv
player_logs_df.to_csv("data/raw/players/player_game_logs_2024_25.csv", index=False)