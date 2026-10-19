from nba_api.stats.endpoints import commonplayerinfo

player_id = 2544  # LeBron James
info = commonplayerinfo.CommonPlayerInfo(player_id)

df = info.get_data_frames()[0]
print(df[["DISPLAY_FIRST_LAST", "POSITION"]])
print(df)