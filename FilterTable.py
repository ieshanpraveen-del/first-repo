from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QLineEdit, QTableWidgetItem, QPushButton, QApplication, QHeaderView, QCheckBox
from PyQt5.QtCore import Qt
import csv
import sys
import os

class FilterTable(QWidget):


    def __init__(self):
        super(FilterTable, self).__init__()
        self.setWindowTitle("Filter Table")
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

        self.filter_button = QPushButton("Apply Filters")
        self.filter_button.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.filter_button.clicked.connect(self.apply_filters)  # Apply filters
        search_layout.addWidget(self.filter_button)

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

    def apply_filters(self):
        included_players = []
        excluded_players = []
                
        for row in range(self.table_widget.rowCount()):
            include_checkbox = self.table_widget.cellWidget(row, self.table_widget.columnCount() - 2)
            exclude_checkbox = self.table_widget.cellWidget(row, self.table_widget.columnCount() - 1)
            player_name_item = self.table_widget.item(row, 0)  #returns NBA_ID of player to make it easier to filter later on
            
            if player_name_item:
                player_name = player_name_item.text()
                
                if include_checkbox and include_checkbox.isChecked():
                    included_players.append(int(player_name))
                if exclude_checkbox and exclude_checkbox.isChecked():
                    excluded_players.append(int(player_name))
        print(f"Included Players: {included_players}")
        print(f"Excluded Players: {excluded_players}")
        return included_players, excluded_players

    def load_data(self):    
        path = os.path.join(os.path.dirname(__file__), "nba_player_stats.csv")# Use relative path
        try:
            with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                read_csv = csv.reader(csvfile)
                list_values = list(read_csv)

            if not list_values:
                print("CSV file is empty")
                return

            self.table_widget.setRowCount(len(list_values) - 1)
            # Add 2 extra columns for checkboxes
            self.table_widget.setColumnCount(len(list_values[0]) + 2)
            
            # Set headers with checkbox columns
            headers = list_values[0] + ["Include", "Exclude"]
            self.table_widget.setHorizontalHeaderLabels(headers)

            row = 0
            for value_tuple in list_values[1:]:
                column = 0
                # Add data columns
                for value in value_tuple:
                    self.table_widget.setItem(row, column, QTableWidgetItem(str(value)))
                    column += 1
                
                # Add two checkboxes in the last two columns
                # First checkbox
                IncludeCheckbox = QCheckBox()
                IncludeCheckbox.setStyleSheet("margin-left:50%; margin-right:50%;")
                self.table_widget.setCellWidget(row, column, IncludeCheckbox)
                column += 1
                
                # Second checkbox
                ExcludeCheckbox = QCheckBox()
                ExcludeCheckbox.setStyleSheet("margin-left:50%; margin-right:50%;")
                self.table_widget.setCellWidget(row, column, ExcludeCheckbox)
                
                row += 1

            # Auto-resize columns
            self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            
            self.status_label.setText(f"Loaded {self.table_widget.rowCount()} players")
            
        except FileNotFoundError:
            self.status_label.setText(f"Error: File '{path}' not found")
        except Exception as e:
            self.status_label.setText(f"Error loading data: {e}")

    def search_table(self):

        search_text = self.search_bar.text().strip().lower()
        
        if not search_text:
            self.status_label.setText("Please enter search text")
            return
        
        matches_found = 0
        
        # Search through all rows
        for row in range(self.table_widget.rowCount()):
            row_matches = False
            
            # Check all columns in the row (excluding checkbox columns)
            for column in range(self.table_widget.columnCount() - 2):
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
    main_window = FilterTable()
    main_window.showMaximized()
    sys.exit(app.exec_())