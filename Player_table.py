from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QLineEdit, QTableWidgetItem, QPushButton, QApplication, QHeaderView, QErrorMessage
from PyQt5.QtCore import Qt
import csv
import sys
import os

class PlayerTable(QWidget):
    def __init__(self):
        super(PlayerTable, self).__init__()
        self.setWindowTitle("Player Table")
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
        path = os.path.join(os.path.dirname(__file__), "nba_player_stats.csv")# Use relative path
        try:
            with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                read_csv = csv.reader(csvfile)
                list_values = list(read_csv)

            if not list_values:
                print("CSV file is empty")
                return

            self.table_widget.setRowCount(len(list_values) - 1)
            self.table_widget.setColumnCount(len(list_values[0]))
            self.table_widget.setHorizontalHeaderLabels(list_values[0])

            row = 0
            for value_tuple in list_values[1:]:
                column = 0
                for value in value_tuple:
                    self.table_widget.setItem(row, column, QTableWidgetItem(str(value)))
                    column += 1
                row += 1

            # Auto-resize columns
            self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            
            self.status_label.setText(f"Loaded {self.table_widget.rowCount()} players")
            
        except FileNotFoundError:
            self.status_label.setText(f"Error: File '{path}' not found")
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
    main_window = PlayerTable()
    main_window.showMaximized()
    sys.exit(app.exec_())