import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, commonplayerinfo
from PyQt5 import QtWidgets
import time

def collect_nba_player_stats(season='2024-25', output_file='nba_player_stats.csv'):

    print(f"Season = {season}, output file = {output_file}") # terminal read during testing 
    
    try:
        # Step 1: Fetch player stats for the specified season using leaguedashplayerstats
        stats = leaguedashplayerstats.LeagueDashPlayerStats(
            season=season,
            per_mode_detailed='PerGame', # Get per game stats for easier fantasy point calculation
            season_type_all_star='Regular Season' # Only regular season stats, exclude pre-season and playoffs
        )
        
        df = stats.get_data_frames()[0] # Get the first DataFrame which contains player stats

        
        # Step 2: Get positions for each player using commonplayerinfo        
        position_map = {} # Dictionary to store player ID to position mapping
        total_players = len(df) # Total number of players to process
        
        # Loop through each player and fetch their position
        for idx, player_id in enumerate(df['PLAYER_ID'], 1):
            try:
                if idx % 50 == 0:
                    print(f"Progress: {idx}/{total_players}") #Progress update every 50 players
                player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id) # Make API call to get player info, including position
                player_info_df = player_info.get_data_frames()[0] # Get the first DataFrame which contains player info
                
                if not player_info_df.empty and 'POSITION' in player_info_df.columns: # Check if the DataFrame is not empty and contains the POSITION column
                    position = player_info_df['POSITION'].iloc[0] # Get the position of the player
                    position_map[player_id] = position
                else:
                    position_map[player_id] = 'N/A' # If position is not available, set it to 'N/A'
                
                # Rate limiting so API calls dont get blocked
                time.sleep(0.6)
                
            except Exception as e:
                error_dialog = QtWidgets.QErrorMessage()
                error_dialog.showMessage(f'Error fetching position for player ID {player_id}: {e}')
                error_dialog.exec_()
                continue
        
        print(f"Successfully fetched positions for {len(position_map)} players") # Debug statement to check how many positions were fetched
        
        # Step 3: Select required columns
        player_data = df[[
            'PLAYER_ID',
            'PLAYER_NAME',
            'TEAM_ABBREVIATION',
            'PTS',
            'REB',
            'AST',
            'STL',
            'BLK',
            'TOV'
        ]].copy()
        
        # Step 4: Add position using the mapping
        player_data['Position'] = player_data['PLAYER_ID'].map(position_map)
        
        # Fill missing positions
        player_data['Position'] = player_data['Position'].fillna('N/A')
        
        positions_found = player_data['Position'].notna().sum()
        print(f"Positions matched for {positions_found} out of {len(player_data)} players")
        
        # Step 5: Rename columns
        player_data.columns = [
            'NBA_ID',
            'Full_Name',
            'Team',
            'Points',
            'Rebounds',
            'Assists',
            'Steals',
            'Blocks',
            'Turnovers',
            'Position'
        ]
        
        # Step 6: Reorder columns
        player_data = player_data[[
            'NBA_ID',
            'Full_Name',
            'Team',
            'Position',
            'Points',
            'Rebounds',
            'Assists',
            'Steals',
            'Blocks',
            'Turnovers'
        ]]
    
        # This process can be further optimized by fetching all player info in bulk if the API supports it

        # Step 7: Calculate fantasy points
        # FP = POINTS + (1.2 * REB) + (1.5 * AST) + (3 * STL) + (3 * BLK) – TOV
        player_data['Fantasy_Points'] = (
            player_data['Points'] + 
            (1.2 * player_data['Rebounds']) + 
            (1.5 * player_data['Assists']) + 
            (3 * player_data['Steals']) + 
            (3 * player_data['Blocks']) - 
            player_data['Turnovers']
        )
        
        # Round fantasy points to 2 decimal places
        player_data['Fantasy_Points'] = player_data['Fantasy_Points'].round(2)
        
        # Step 8: Sort by fantasy points
        player_data = player_data.sort_values('Fantasy_Points', ascending=False)
        
        # Reset index
        player_data = player_data.reset_index(drop=True)
        
        # Step 9: Save to CSV
        player_data.to_csv(output_file, index=False)

        success_dialog = QtWidgets.QErrorMessage()
        success_dialog.showMessage('Player list updated successfully.')
        success_dialog.exec_()
        
        return player_data
        
    except Exception as e:
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(f'Error updating player list: {e}')
        error_dialog.exec_()

        import traceback
        traceback.print_exc()
        return None
