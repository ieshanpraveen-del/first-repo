from PyQt5 import QtCore, QtGui, QtWidgets
from functools import total_ordering
import csv
import sys
import os
import openpyxl
import pandas as pd
from nba_api.stats.endpoints import leaguedashplayerstats, commonplayerinfo
import time as time_module
from pulp import *
from OptimisedTable import OptimisedTable
from FilterTable import FilterTable


class Ui_OptimiserScreen(object):
    
    def __init__(self):
        self.included_playerID = [] # List to store player IDs that must be included in the lineup
        self.excluded_playerID = [] # List to store player IDs that must be excluded from the lineup
        self.window = None
        self.filter_window = None

    def OpenOptimiserTable(self): # Opens the optimised lineup window
        self.window = OptimisedTable()
        self.window.show()

    def OpenFilterTable(self): # opens table used to filter players
        self.filter_window = FilterTable()
        self.filter_window.filter_button.clicked.connect(self.get_filtered_players)
        self.filter_window.show() 
  
    def get_filtered_players(self):
        self.included_playerID, self.excluded_playerID = self.filter_window.apply_filters() # Retrieves the included and excluded player IDs from the filter table when the "Apply Filters" button is clicked
        return self.included_playerID, self.excluded_playerID

    def num_lineup_error(self): # error dialog if no lineups are selected
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Please select the number of lineups to generate')
        error_dialog.exec_()

    def postional_value_error(self): # error dialog if positional constraints are not valid (not a number or negative)
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Please enter valid positional constraints')
        error_dialog.exec_()

    def empty_lineup_error(self): # error dialog if positional constraints are empty
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage('Positional constraints cannot be empty')
        error_dialog.exec_()

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
                                time_module.sleep(0.6)
                                
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
                print(f"Positions matched for {positions_found} out of {len(player_data)} players") # Debug statement to check how many players had their positions successfully matched
                
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

    def run_optimiser(self):
        # Select no of lineups
        if self.FiveLineups.isChecked():
                num_lineups = 5
        elif self.TenLineups.isChecked():
                num_lineups = 10
        elif self.TwentyLineups.isChecked():
                num_lineups = 20
        else:
                self.num_lineup_error()
                return
        
        if not (self.PGValue.text().isdigit() and self.SFValue.text().isdigit() and self.CValue.text().isdigit()): # Check if the positional constraints are valid integers
                self.postional_value_error()
                return
        
        if int(self.PGValue.text()) < 0 or int(self.SFValue.text()) < 0 or int(self.CValue.text()) < 0 or (int(self.PGValue.text())+int(self.SFValue.text())+int(self.CValue.text())) > 20: # Check if the positional constraints are non-negative and within bounds
                self.postional_value_error()
                return
        if self.PGValue.text() == "" or self.SFValue.text() == "" or self.CValue.text() == "": # Check if the positional constraints are not empty
                self.empty_lineup_error()
                return
        
        num_g = int(self.PGValue.text()) # Number of guards
        num_f = int(self.SFValue.text()) # Number of forwards
        num_c = int(self.CValue.text()) # Number of centers

        # Load player data
        players = pd.read_csv(os.path.join(os.path.dirname(__file__), "nba_player_stats.csv"))
        
        # Function to expand multi-positional players
        def expand_positions(df):
                expanded_rows = []
                for index, row in df.iterrows():
                        positions = row['Position'].split('-')  # Split multi-positions like "G-F" into ["G", "F"]
                        for pos in positions:
                                secondary_position = row.copy() # Create a copy of the original row for each position
                                secondary_position['Position'] = pos.strip() # Update position to the current one in the loop
                                expanded_rows.append(secondary_position)
                return pd.DataFrame(expanded_rows)
        
        # Expand players with multiple positions
        players_expanded = expand_positions(players)
        
        # Create workbook for output
        wb = openpyxl.Workbook()
        ws = wb.active
        
        headers = []
        for pos, count in [("Guard", num_g), ("Forward", num_f), ("Center", num_c)]: # Create headers like "Guard 1", "Guard 2", etc. based on the number of players required for each position
                for i in range(1, count + 1): # Loop to create headers for each position based on the number of players required
                        headers.append(f"{pos} {i}")
        headers.append("Fantasy Points")

        for col, header in enumerate(headers, 1):
                ws.cell(row=1, column=col).value = header # Write headers to the first row of the Excel sheet
                ws.cell(row=1, column=col).font = openpyxl.styles.Font(bold=True)
        
        # Group players by position and NBA_ID to avoid duplicates 
        availables = players_expanded[['Position', 'NBA_ID', 'Fantasy_Points', 'Full_Name']].copy() # Create a new DataFrame with only the necessary columns for optimization
        
        # Create points dictionary for each position
        points = {}
        for pos in availables.Position.unique():
                availables_pos = availables[availables.Position == pos] # Filter players for the current position
                pos_points = list(availables_pos[['NBA_ID', 'Fantasy_Points']].set_index('NBA_ID').to_dict().values())[0] # Create a dictionary of player ID to fantasy points for the current position
                points[pos] = pos_points
        
        # Dictionary to store the number of players required for each position based on user input
        pos_num_available = { 
                "Guard": num_g,  
                "Forward": num_f,  
                "Center": num_c   
        }
        
        # Generate multiple lineups
        previous_lineups = []
        
        for lineup_num in range(1, num_lineups + 1):
                # Create binary variables for each player in each position
                _vars = {k: LpVariable.dicts(k, v.keys(), cat='Binary') for k, v in points.items()} # Create a dictionary of binary variables for each position and player ID, where the variable is 1 if the player is selected for that position and 0 otherwise
                
                prob = LpProblem("Fantasy Lineups", LpMaximize) # Create a linear programming problem to maximize fantasy points


                # Objective: maximize total points
                total_points = []
                for pos, players_dict in points.items(): # Loop through each position and its corresponding player dictionary to calculate the total fantasy points for the lineup based on the selected players
                        for player_id, player_points in players_dict.items(): 
                                total_points.append(player_points * _vars[pos][player_id]) # Multiply the fantasy points of each player by the corresponding binary variable to include it in the total points calculation only if the player is selected for the lineup
                
                prob += lpSum(total_points)
                
                # Position constraints
                for pos in points.keys():
                        prob += lpSum([_vars[pos][player_id] for player_id in points[pos]]) == pos_num_available[pos] # Ensure that the number of players selected for each position matches the user-defined constraints (e.g., exactly 2 guards, 2 forwards, 1 center)
                
                # CRITICAL: Each player can only be selected once across all positions
                all_player_ids = set()
                for pos in points.keys():
                        all_player_ids.update(points[pos].keys())
                
                for player_id in all_player_ids:
                        player_vars = []
                        for pos in points.keys():
                                if player_id in points[pos]:
                                        player_vars.append(_vars[pos][player_id])
                        if player_vars:
                                prob += lpSum(player_vars) <= 1  # Each player used at most once

                # Include/exclude player constraints
                for included_player_id in self.included_playerID:
                        player_positions = []
                        for pos in points.keys():
                                if included_player_id in points[pos]:
                                        player_positions.append(_vars[pos][included_player_id])
            
                        if player_positions:
                                prob += lpSum(player_positions) == 1  # Must be selected at exactly one position

                # Exclude player constraints
                for excluded_player_id in self.excluded_playerID:
                        for pos in points.keys():
                                if excluded_player_id in points[pos]:
                                        prob += _vars[pos][excluded_player_id] == 0
                
                # Exclude previous lineups
                for prev_lineup in previous_lineups:
                        prob += lpSum([_vars[pos][player_id] for pos, player_id in prev_lineup]) <= len(prev_lineup) - 1
                
                # Solve
                prob.solve()
                
                if prob.status != 1:
                        print(f"No optimal solution found for lineup {lineup_num}")
                        break
                
                # Extract selected players
                selected_players = []
                total_score = 0
                lineup_players = {'Guard': [], 'Forward': [], 'Center': []}
                
                for pos in points.keys():
                        for player_id in points[pos]:
                                if _vars[pos][player_id].varValue == 1:
                                        player_name = availables[(availables.NBA_ID == player_id) & 
                                                (availables.Position == pos)]['Full_Name'].values[0]
                                        player_points = points[pos][player_id]
                        
                                        lineup_players[pos].append(f"{player_name} ({player_points:.1f})")
                                        selected_players.append((pos, player_id))
                                        total_score += player_points
                
                # Write to Excel
                row = lineup_num + 1
                col = 1
                
                for pos in ['Guard', 'Forward', 'Center']:
                        players_in_pos = lineup_players[pos]
                        for i in range(pos_num_available[pos]):
                                if i < len(players_in_pos):
                                        ws.cell(row=row, column=col).value = players_in_pos[i]
                                col += 1
                
                ws.cell(row=row, column=col).value = round(total_score, 2)
                
                previous_lineups.append(selected_players)
                
                # Debug output to terminal
                print(f"Lineup {lineup_num}: Total Fantasy Points = {total_score:.2f}")
                print(f"Guards: {lineup_players['Guard']}")
                print(f"Forwards: {lineup_players['Forward']}")
                print(f"Centers: {lineup_players['Center']}")
        
        wb.save("fantasy_lineups.xlsx")
        self.OpenOptimiserTable()
    
    def setupUi(self, OptimiserScreen):
        OptimiserScreen.setObjectName("OptimiserScreen")
        OptimiserScreen.resize(1098, 852)
        OptimiserScreen.setStyleSheet("background-color: rgb(81, 81, 81);")
        self.centralwidget = QtWidgets.QWidget(OptimiserScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.Heading = QtWidgets.QLabel(self.centralwidget)
        self.Heading.setGeometry(QtCore.QRect(360, 20, 331, 81))
        self.Heading.setStyleSheet("color: rgb(255, 255, 255);\n"
        "text-decoration: underline;\n"
        "font: 8pt \"MS Shell Dlg 2\";\n"
        "font: 24pt \"MS Shell Dlg 2\";")
        self.Heading.setObjectName("Heading")
        self.FiveLineups = QtWidgets.QRadioButton(self.centralwidget)
        self.FiveLineups.setGeometry(QtCore.QRect(250, 250, 121, 21))
        self.FiveLineups.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.FiveLineups.setObjectName("FiveLineups")
        
        self.LineupNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.LineupNumberLabel.setGeometry(QtCore.QRect(30, 240, 171, 41))
        self.LineupNumberLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.LineupNumberLabel.setObjectName("LineupNumberLabel")

        self.PGValue = QtWidgets.QLineEdit(self.centralwidget)
        self.PGValue.setGeometry(QtCore.QRect(150, 420, 41, 22))
        self.PGValue.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.PGValue.setPlaceholderText("2")
        self.PGValue.setObjectName("PGValue")

        self.SFValue = QtWidgets.QLineEdit(self.centralwidget)
        self.SFValue.setGeometry(QtCore.QRect(150, 500, 41, 22))
        self.SFValue.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.SFValue.setPlaceholderText("2")
        self.SFValue.setObjectName("SFValue")

        self.CValue = QtWidgets.QLineEdit(self.centralwidget)
        self.CValue.setPlaceholderText("1")
        self.CValue.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.CValue.setGeometry(QtCore.QRect(150, 580, 41, 22))
        self.CValue.setObjectName("CValue")

        self.PGLabel = QtWidgets.QLabel(self.centralwidget)
        self.PGLabel.setGeometry(QtCore.QRect(40, 420, 100, 16))
        self.PGLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.PGLabel.setObjectName("PGLabel")

        self.TenLineups = QtWidgets.QRadioButton(self.centralwidget)
        self.TenLineups.setGeometry(QtCore.QRect(460, 250, 121, 21))
        self.TenLineups.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.TenLineups.setObjectName("TenLineups")

        self.TwentyLineups = QtWidgets.QRadioButton(self.centralwidget)
        self.TwentyLineups.setGeometry(QtCore.QRect(720, 250, 121, 21))
        self.TwentyLineups.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.TwentyLineups.setObjectName("TwentyLineups")

        self.SFLabel = QtWidgets.QLabel(self.centralwidget)
        self.SFLabel.setGeometry(QtCore.QRect(40, 500, 100, 16))
        self.SFLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);")
        self.SFLabel.setObjectName("SFLabel")

        self.CLabel = QtWidgets.QLabel(self.centralwidget)
        self.CLabel.setGeometry(QtCore.QRect(40, 580, 100, 16))
        self.CLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);")
        self.CLabel.setObjectName("CLabel")

        self.CreateLineupButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.run_optimiser())
        self.CreateLineupButton.setGeometry(QtCore.QRect(420, 680, 241, 61))
        self.CreateLineupButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);")
        self.CreateLineupButton.setObjectName("CreateLineupButton")

        self.FilterPlayersButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.OpenFilterTable())
        self.FilterPlayersButton.setGeometry(QtCore.QRect(650, 430, 121, 41))
        self.FilterPlayersButton.setStyleSheet("color: rgb(255, 255, 255);\n"
        "font: 12pt \"MS Shell Dlg 2\";")
        
        self.FilterPlayersButton.setObjectName("FilterPlayersButton")
        self.PositionalConstraintLabel = QtWidgets.QLabel(self.centralwidget)
        self.PositionalConstraintLabel.setGeometry(QtCore.QRect(30, 340, 271, 41))
        self.PositionalConstraintLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "text-decoration: underline;\n"
        "color: rgb(255, 255, 255);")
        self.PositionalConstraintLabel.setObjectName("PositionalConstraintLabel")

        self.PlayerConstraintLabel = QtWidgets.QLabel(self.centralwidget)
        self.PlayerConstraintLabel.setGeometry(QtCore.QRect(630, 340, 271, 41))
        self.PlayerConstraintLabel.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";\n"
        "text-decoration: underline;\n"
        "color: rgb(255, 255, 255);")
        self.PlayerConstraintLabel.setObjectName("PlayerConstraintLabel")

        self.UpdatePlayerLabel = QtWidgets.QLabel(self.centralwidget)
        self.UpdatePlayerLabel.setGeometry(QtCore.QRect(30, 140, 171, 31))
        self.UpdatePlayerLabel.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
        "color: rgb(255, 255, 255);")
        self.UpdatePlayerLabel.setObjectName("UpdatePlayerLabel")

        self.UpdateButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.collect_nba_player_stats())
        self.UpdateButton.setGeometry(QtCore.QRect(230, 140, 111, 31))
        self.UpdateButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.UpdateButton.setObjectName("UpdateButton")

        OptimiserScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(OptimiserScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 26))
        self.menubar.setObjectName("menubar")
        OptimiserScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OptimiserScreen)
        self.statusbar.setObjectName("statusbar")
        OptimiserScreen.setStatusBar(self.statusbar)

        self.retranslateUi(OptimiserScreen)
        QtCore.QMetaObject.connectSlotsByName(OptimiserScreen)

    def retranslateUi(self, OptimiserScreen):                                                           
        _translate = QtCore.QCoreApplication.translate
        OptimiserScreen.setWindowTitle(_translate("OptimiserScreen", "MainWindow"))
        self.Heading.setText(_translate("OptimiserScreen", "Optimiser Settings"))
        self.FiveLineups.setText(_translate("OptimiserScreen", "5"))
        self.LineupNumberLabel.setText(_translate("OptimiserScreen", "Number of lineups"))
        self.PGLabel.setText(_translate("OptimiserScreen", "Guard"))
        self.TenLineups.setText(_translate("OptimiserScreen", "10"))
        self.TwentyLineups.setText(_translate("OptimiserScreen", "20"))
        self.SFLabel.setText(_translate("OptimiserScreen", "Forward"))
        self.CLabel.setText(_translate("OptimiserScreen", "Center"))
        self.CreateLineupButton.setText(_translate("OptimiserScreen", "Create lineup"))
        self.PositionalConstraintLabel.setText(_translate("OptimiserScreen", "Positional Constraints"))
        self.PlayerConstraintLabel.setText(_translate("OptimiserScreen", "Player Constraints"))
        self.UpdatePlayerLabel.setText(_translate("OptimiserScreen", "Update player list"))
        self.UpdateButton.setText(_translate("OptimiserScreen", "Update"))
        self.FilterPlayersButton.setText(_translate("OptimiserScreen", "Filter Players"))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    OptimiserScreen = QtWidgets.QMainWindow()
    ui = Ui_OptimiserScreen()
    ui.setupUi(OptimiserScreen)
    OptimiserScreen.show()
    sys.exit(app.exec_())