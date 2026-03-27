# source communication for connecting to the NBA API
# all API specific code should be contained to this file
# write a program that demonstrates clean "exposed methods" e.g. get_all_players() & get_player_game_logs(player_id, season)

import pandas as pd
from nba_api.stats.endpoints import leaguegamelog

# Get team game logs for a specific season
def get_team_game_logs(season: str, season_type: str = "Regular Season") -> pd.DataFrame:
    gamelog = leaguegamelog.LeagueGameLog(
        season=season,
        season_type_all_star=season_type,
        player_or_team_abbreviation="T"   # "T" for team logs, "P" for player logs
    )
    df = gamelog.get_data_frames()[0]
    return df

# Get player game logs for a specific season
def get_player_game_logs(season: str, season_type: str = "Regular Season") -> pd.DataFrame:
    gamelog = leaguegamelog.LeagueGameLog(
        season=season,
        season_type_all_star=season_type,
        player_or_team_abbreviation="P"   # "T" for team logs, "P" for player logs
    )
    df = gamelog.get_data_frames()[0]
    return df
