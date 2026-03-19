# source communication for connecting to the NBA API
# all API specific code should be contained to this file
 
# goal of this file is to retrieve data from the API in it's most raw format
# write a program that demionstrates clean "exposed methods" e.g. get_all_players() & get_player_game_logs(player_id, season)

import pandas as pd
from nba_api.stats.endpoints import playergamelog, commonallplayers