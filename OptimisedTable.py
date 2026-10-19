from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QLineEdit, QTableWidgetItem, QPushButton, QApplication, QHeaderView, QCheckBox, QFileDialog, QErrorMessage
from PyQt5.QtCore import Qt
import openpyxl
import os
import csv
import sys
import json

class OptimisedTable(QWidget):
    def __init__(self):
        super(OptimisedTable, self).__init__()
        self.setWindowTitle("Optimised Table")
        self.resize(1098, 852)

        layout = QVBoxLayout()  
        self.setLayout(layout)

        # Create a horizontal layout for search bar and button
        search_layout = QHBoxLayout()
        
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Enter player name, position, or any text...")
        self.search_bar.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.search_bar.returnPressed.connect(self.search_table)  # Search on Enter key
        search_layout.addWidget(self.search_bar)

        self.search_button = QPushButton("Search")
        self.search_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.search_button.clicked.connect(self.search_table)  # Connected to search function
        search_layout.addWidget(self.search_button)

        self.clear_button = QPushButton("Clear")
        self.clear_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.clear_button.clicked.connect(self.clear_search)  # Clear search
        search_layout.addWidget(self.clear_button)

        self.save_csv_button = QPushButton("Save as CSV")
        self.save_csv_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        search_layout.addWidget(self.save_csv_button)
        self.save_csv_button.clicked.connect(self.save_csv)  # Save selected players

        self.save_json_button = QPushButton("Save as JSON")
        self.save_json_button.clicked.connect(self.save_json)  # Save selected players
        self.save_json_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        search_layout.addWidget(self.save_json_button)

        layout.addLayout(search_layout)

        self.table_widget = QTableWidget()
        self.table_widget.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        layout.addWidget(self.table_widget)

        # Status label to show search results
        self.status_label = QLineEdit()
        self.status_label.setReadOnly(True)
        self.status_label.setStyleSheet("font: 10pt \"MS Shell Dlg 2\"; background-color: #f0f0f0;")
        layout.addWidget(self.status_label)

        self.load_data()

    def ExceptionError(self):      
        error_dialog = QErrorMessage()
        error_dialog.showMessage('Error loading data.')
        error_dialog.exec_()

    def load_data(self):    
        path = os.path.join(os.path.dirname(__file__), "fantasy_lineups.xlsx")# Use relative path
        try:
            workbook = openpyxl.load_workbook(path)
            sheet = workbook.active

            list_values = list(sheet.values)


            if not list_values:
                print("Excel file is empty")
                return

            self.table_widget.setRowCount(len(list_values) - 1)
            self.table_widget.setColumnCount(len(list_values[0]) + 1)  # Extra column for Save checkbox
            headers = list(list_values[0]) + ["Save"]
            self.table_widget.setHorizontalHeaderLabels(headers)

            row = 0
            for value_tuple in list_values[1:]:
                column = 0
                for value in value_tuple:
                    self.table_widget.setItem(row, column, QTableWidgetItem(str(value)))
                    column += 1

                SaveCheckbox = QCheckBox()
                SaveCheckbox.setStyleSheet("margin-left:50%; margin-right:50%;")
                self.table_widget.setCellWidget(row, column, SaveCheckbox)
                column += 1
                row += 1

            # Auto-resize columns
            self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            
            self.status_label.setText(f"Loaded {self.table_widget.rowCount()} players")
            
        except FileNotFoundError:
            self.status_label.setText(f"Error: File '{path}' not found")
        except Exception as e:
            self.status_label.setText(f"Error loading data: {e}")

    def save_csv(self):
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Selected Players", "", "CSV Files (*.csv);;All Files (*)")
        if not output_file:
            return  # User cancelled the dialog
        
        try:
            selected_players = []
            headers = [self.table_widget.horizontalHeaderItem(col).text() for col in range(self.table_widget.columnCount() - 1)]  # Exclude Save column
            selected_players.append(headers)
            
            for row in range(self.table_widget.rowCount()):
                save_checkbox = self.table_widget.cellWidget(row, self.table_widget.columnCount() - 1)
                if save_checkbox.isChecked():
                    player_data = []
                    for col in range(self.table_widget.columnCount() - 1):  # Exclude Save column
                        item = self.table_widget.item(row, col)
                        player_data.append(item.text() if item else "")
                    selected_players.append(player_data)
            
            if not selected_players or len(selected_players) == 1:
                error_dialog = QErrorMessage()
                error_dialog.showMessage("No players selected to save.")
                error_dialog.exec_()
                return
            
            with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(selected_players)
            
            self.status_label.setText(f"Successfully saved {len(selected_players) - 1} players to {output_file}")
        
        except Exception as e:
            self.ExceptionError()

    def save_json(self):
        output_file, _ = QFileDialog.getSaveFileName(self, "Save Selected Players", "", "JSON Files (*.json);;All Files (*)")
        if not output_file:
            return  # User cancelled the dialog
        
        try:
            selected_players = []
            headers = [self.table_widget.horizontalHeaderItem(col).text() for col in range(self.table_widget.columnCount() - 1)]  # Exclude Save column
            
            for row in range(self.table_widget.rowCount()):
                save_checkbox = self.table_widget.cellWidget(row, self.table_widget.columnCount() - 1)
                if save_checkbox.isChecked():
                    player_data = {}
                    for col in range(self.table_widget.columnCount() - 1):  # Exclude Save column
                        item = self.table_widget.item(row, col)
                        player_data[headers[col]] = item.text() if item else ""
                    selected_players.append(player_data)
            
            if not selected_players:
                error_dialog = QErrorMessage()
                error_dialog.showMessage("No players selected to save.")
                error_dialog.exec_()
                return
            
            with open(output_file, 'w', encoding='utf-8') as jsonfile:
                json.dump(selected_players, jsonfile, indent=4)
            
            self.status_label.setText(f"Successfully saved {len(selected_players)} players to {output_file}")
        
        except Exception as e:
            self.ExceptionError()
            
    def search_table(self):
        search_text = self.search_bar.text().strip().lower()
        
        if not search_text:
            self.status_label.setText("Please enter search text")
            return
        
        matches_found = 0
        
        # Search through all rows
        for row in range(self.table_widget.rowCount()):
            row_matches = False
            
            # Check all columns in the row
            for column in range(self.table_widget.columnCount()):
                item = self.table_widget.item(row, column)
                if item and search_text in item.text().lower():
                    row_matches = True
                    break
            
            # Show rows that match, hide rows that don't
            if row_matches:
                self.table_widget.setRowHidden(row, False)
                matches_found += 1
            else:
                self.table_widget.setRowHidden(row, True)
        
        # Update status
        if matches_found == 0:
            self.status_label.setText(f"No results found for '{self.search_bar.text()}'")
        else:
            self.status_label.setText(f"Found {matches_found} player(s) matching '{self.search_bar.text()}'")

    def clear_search(self):

        self.search_bar.clear()
        
        # Show all rows
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHidden(row, False)
        
        self.status_label.setText(f"Showing all {self.table_widget.rowCount()} players")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = OptimisedTable()
    main_window.showMaximized()
    sys.exit(app.exec_())