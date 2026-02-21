"""
Modern GUI Application using PyQt6
Beautiful, professional interface for People Database Management
"""
import sys
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QComboBox, QFrame, QStackedWidget, QMessageBox, QDialog,
    QFormLayout, QHeaderView, QScrollArea, QGridLayout
)
from PyQt6.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QFont, QIcon, QPalette, QColor, QLinearGradient
from werkzeug.security import check_password_hash, generate_password_hash


class ModernButton(QPushButton):
    """Custom styled button with hover effects"""
    def __init__(self, text, color="#2196F3", hover_color="#1976D2"):
        super().__init__(text)
        self.color = color
        self.hover_color = hover_color
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 8px;
                padding: 10px 20px;
                font-size: 13px;
                font-weight: bold;
                min-width: 100px;
                min-height: 38px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
            QPushButton:pressed {{
                background-color: {color};
                padding-top: 12px;
            }}
        """)


class ModernLineEdit(QLineEdit):
    """Custom styled line edit"""
    def __init__(self, placeholder=""):
        super().__init__()
        self.setPlaceholderText(placeholder)
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #2196F3;
            }
        """)
        self.setMinimumHeight(36)


class ModernComboBox(QComboBox):
    """Custom styled combo box"""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QComboBox {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 8px 12px;
                font-size: 13px;
                background-color: white;
                min-height: 20px;
            }
            QComboBox:focus {
                border: 2px solid #2196F3;
            }
            QComboBox::drop-down {
                border: none;
                width: 30px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #666;
                margin-right: 10px;
            }
        """)


class LoginWindow(QDialog):
    """Modern login dialog"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login - People Database Management")
        self.setFixedSize(450, 550)
        self.user_data = None
        self.db_path = 'instance/people.db'
        self.setup_ui()
        
    def setup_ui(self):
        """Setup login UI"""
        self.setStyleSheet("""
            QDialog {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
            }
        """)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(20)
        
        # Logo/Title area
        title_frame = QFrame()
        title_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
            }
        """)
        title_layout = QVBoxLayout(title_frame)
        title_layout.setContentsMargins(30, 30, 30, 30)
        
        # Icon
        icon_label = QLabel("🔐")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("font-size: 64px; background: transparent;")
        title_layout.addWidget(icon_label)
        
        # Title
        title = QLabel("People Database")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: #333;
            background: transparent;
        """)
        title_layout.addWidget(title)
        
        subtitle = QLabel("Management System")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 16px;
            color: #666;
            background: transparent;
        """)
        title_layout.addWidget(subtitle)
        
        layout.addWidget(title_frame)
        layout.addSpacing(10)
        
        # Login form
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
            }
        """)
        form_layout = QVBoxLayout(form_frame)
        form_layout.setContentsMargins(30, 30, 30, 30)
        form_layout.setSpacing(15)
        
        # Username
        username_label = QLabel("Username")
        username_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #555; background: transparent;")
        form_layout.addWidget(username_label)
        
        self.username_input = ModernLineEdit("Enter your username")
        form_layout.addWidget(self.username_input)
        
        # Password
        password_label = QLabel("Password")
        password_label.setStyleSheet("font-size: 13px; font-weight: bold; color: #555; background: transparent;")
        form_layout.addWidget(password_label)
        
        self.password_input = ModernLineEdit("Enter your password")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(self.password_input)
        
        # Login button
        login_btn = ModernButton("Login", "#667eea", "#5568d3")
        login_btn.clicked.connect(self.login)
        form_layout.addWidget(login_btn)
        
        layout.addWidget(form_frame)
        
        # Info text
        info = QLabel("Default: superadmin / super123")
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setStyleSheet("color: white; font-size: 12px; background: transparent;")
        layout.addWidget(info)
        
        self.setLayout(layout)
        
        # Connect Enter key
        self.password_input.returnPressed.connect(self.login)
        self.username_input.returnPressed.connect(self.login)
    
    def login(self):
        """Authenticate user"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            QMessageBox.warning(self, "Error", "Please enter username and password")
            return
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, username, password, role, province FROM users WHERE username = ?", (username,))
            user = cursor.fetchone()
            conn.close()
            
            if user and check_password_hash(user[2], password):
                self.user_data = {
                    'id': user[0],
                    'username': user[1],
                    'role': user[3],
                    'province': user[4]
                }
                self.accept()
            else:
                QMessageBox.critical(self, "Error", "Invalid username or password")
                self.password_input.clear()
                self.password_input.setFocus()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"Error connecting to database:\n{str(e)}")


class MainWindow(QMainWindow):
    """Main application window"""
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.db_path = 'instance/people.db'
        self.current_page = 1
        self.total_pages = 1
        self.per_page = 100
        
        self.setWindowTitle("People Database Management System")
        self.setMinimumSize(1400, 800)
        
        self.setup_ui()
        self.log_action('login')
        self.search_people()
    
    def setup_ui(self):
        """Setup main UI"""
        # Set modern style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #333;
            }
        """)
        
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Top bar
        self.create_top_bar(main_layout)
        
        # Content area
        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # Left sidebar
        self.create_sidebar(content_layout)
        
        # Right content
        self.create_content_area(content_layout)
        
        main_layout.addWidget(content)
    
    def create_top_bar(self, parent_layout):
        """Create top navigation bar"""
        top_bar = QFrame()
        top_bar.setFixedHeight(70)
        top_bar.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                border: none;
            }
        """)
        
        layout = QHBoxLayout(top_bar)
        layout.setContentsMargins(30, 0, 30, 0)
        
        # Title
        title = QLabel("👥 People Database Management")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        layout.addWidget(title)
        
        layout.addStretch()
        
        # User info
        role_text = self.user_data['role'].replace('_', ' ').title()
        user_info = f"👤 {self.user_data['username']} ({role_text})"
        if self.user_data['province']:
            user_info += f"\n📍 {self.user_data['province']}"
        
        user_label = QLabel(user_info)
        user_label.setStyleSheet("""
            font-size: 13px;
            color: white;
            background: transparent;
            padding: 10px;
        """)
        user_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        layout.addWidget(user_label)
        
        parent_layout.addWidget(top_bar)

    
    def create_sidebar(self, parent_layout):
        """Create left sidebar with search filters"""
        sidebar = QFrame()
        sidebar.setFixedWidth(320)
        sidebar.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
            }
        """)
        
        layout = QVBoxLayout(sidebar)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)
        
        # Search title
        search_title = QLabel("🔍 Search Filters")
        search_title.setStyleSheet("""
            font-size: 18px;
            font-weight: bold;
            color: #333;
            padding: 10px 0;
        """)
        layout.addWidget(search_title)
        
        # Search fields
        self.id_input = ModernLineEdit("🆔 Person ID")
        layout.addWidget(self.id_input)
        
        self.name_input = ModernLineEdit("👤 Name")
        layout.addWidget(self.name_input)
        
        self.gender_combo = ModernComboBox()
        self.gender_combo.addItems(["All Genders", "male", "female"])
        layout.addWidget(self.gender_combo)
        
        self.age_input = ModernLineEdit("🎂 Age")
        layout.addWidget(self.age_input)
        
        self.province_input = ModernLineEdit("🌍 Province")
        # Disable province field for managers - they can only see their province
        if self.user_data['role'] == 'manager' and self.user_data['province']:
            self.province_input.setText(self.user_data['province'])
            self.province_input.setEnabled(False)
            self.province_input.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #FFB74D;
                    border-radius: 8px;
                    padding: 10px 15px;
                    font-size: 13px;
                    background-color: #FFF3E0;
                    color: #E65100;
                    font-weight: bold;
                }
            """)
        layout.addWidget(self.province_input)
        
        self.district_input = ModernLineEdit("📍 District")
        layout.addWidget(self.district_input)
        
        self.commune_input = ModernLineEdit("🏘️ Commune")
        layout.addWidget(self.commune_input)
        
        self.village_input = ModernLineEdit("🏠 Village")
        layout.addWidget(self.village_input)
        
        # Search button
        search_btn = ModernButton("🔍 Search", "#4CAF50", "#45a049")
        search_btn.clicked.connect(self.search_people)
        layout.addWidget(search_btn)
        
        # Clear button
        clear_btn = ModernButton("Clear Filters", "#FF5722", "#E64A19")
        clear_btn.clicked.connect(self.clear_filters)
        layout.addWidget(clear_btn)
        
        layout.addSpacing(20)
        
        # Action buttons
        if self.user_data['role'] == 'super_admin':
            users_btn = ModernButton("👥 Manage Users", "#FF9800", "#F57C00")
            users_btn.clicked.connect(self.show_users_dialog)
            layout.addWidget(users_btn)
        
        history_btn = ModernButton("📜 History", "#9C27B0", "#7B1FA2")
        history_btn.clicked.connect(self.show_history_dialog)
        layout.addWidget(history_btn)
        
        layout.addStretch()
        
        # Logout button
        logout_btn = ModernButton("🚪 Logout", "#607D8B", "#455A64")
        logout_btn.clicked.connect(self.logout)
        layout.addWidget(logout_btn)
        
        parent_layout.addWidget(sidebar)
    
    def create_content_area(self, parent_layout):
        """Create main content area with results table"""
        content = QFrame()
        content.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
            }
        """)
        
        layout = QVBoxLayout(content)
        layout.setContentsMargins(25, 25, 25, 25)
        layout.setSpacing(15)
        
        # Header
        header_layout = QHBoxLayout()
        
        results_title = QLabel("📊 Search Results")
        results_title.setStyleSheet("""
            font-size: 20px;
            font-weight: bold;
            color: #333;
        """)
        header_layout.addWidget(results_title)
        
        header_layout.addStretch()
        
        self.count_label = QLabel("Total: 0")
        self.count_label.setStyleSheet("""
            font-size: 16px;
            color: #666;
            background-color: #E3F2FD;
            padding: 8px 16px;
            border-radius: 8px;
        """)
        header_layout.addWidget(self.count_label)
        
        layout.addLayout(header_layout)
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Gender", "Age", "Province", "District", "Commune", "Village"
        ])
        
        # Table styling
        self.table.setStyleSheet("""
            QTableWidget {
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                background-color: white;
                gridline-color: #E0E0E0;
            }
            QTableWidget::item {
                padding: 8px;
                border-bottom: 1px solid #F0F0F0;
            }
            QTableWidget::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }
            QHeaderView::section {
                background-color: #667eea;
                color: white;
                padding: 12px;
                border: none;
                font-weight: bold;
                font-size: 13px;
            }
        """)
        
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        # Set column widths
        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(2, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Fixed)
        header.setSectionResizeMode(4, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(6, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(7, QHeaderView.ResizeMode.Stretch)
        
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 70)
        
        layout.addWidget(self.table)
        
        # Pagination
        pagination = QHBoxLayout()
        
        self.prev_btn = ModernButton("◀ Previous", "#2196F3", "#1976D2")
        self.prev_btn.clicked.connect(self.prev_page)
        pagination.addWidget(self.prev_btn)
        
        pagination.addStretch()
        
        self.page_label = QLabel("Page 1 / 1")
        self.page_label.setStyleSheet("""
            font-size: 15px;
            font-weight: bold;
            color: #333;
            padding: 10px 20px;
            background-color: #F5F5F5;
            border-radius: 8px;
        """)
        pagination.addWidget(self.page_label)
        
        pagination.addStretch()
        
        self.next_btn = ModernButton("Next ▶", "#2196F3", "#1976D2")
        self.next_btn.clicked.connect(self.next_page)
        pagination.addWidget(self.next_btn)
        
        layout.addLayout(pagination)
        
        parent_layout.addWidget(content)
    
    def search_people(self):
        """Search people in database"""
        offset = (self.current_page - 1) * self.per_page
        
        # Build query
        query = "SELECT id, name, gender, age, province, district, commune, village FROM people WHERE 1=1"
        params = []
        
        # Province restriction for managers
        if self.user_data['role'] == 'manager' and self.user_data['province']:
            query += " AND province = ?"
            params.append(self.user_data['province'])
        
        # Search filters
        if self.id_input.text():
            try:
                query += " AND id = ?"
                params.append(int(self.id_input.text()))
            except ValueError:
                pass
        
        if self.name_input.text():
            query += " AND name LIKE ?"
            params.append(f"%{self.name_input.text()}%")
        
        gender = self.gender_combo.currentText()
        if gender and gender != "All Genders":
            query += " AND gender = ?"
            params.append(gender)
        
        if self.age_input.text():
            try:
                query += " AND age = ?"
                params.append(int(self.age_input.text()))
            except ValueError:
                pass
        
        if self.province_input.text():
            query += " AND province LIKE ?"
            params.append(f"%{self.province_input.text()}%")
        
        if self.district_input.text():
            query += " AND district LIKE ?"
            params.append(f"%{self.district_input.text()}%")
        
        if self.commune_input.text():
            query += " AND commune LIKE ?"
            params.append(f"%{self.commune_input.text()}%")
        
        if self.village_input.text():
            query += " AND village LIKE ?"
            params.append(f"%{self.village_input.text()}%")
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get total count
            count_query = query.replace("SELECT id, name, gender, age, province, district, commune, village", "SELECT COUNT(*)")
            cursor.execute(count_query, params)
            total = cursor.fetchone()[0]
            
            # Get paginated results
            query += f" LIMIT {self.per_page} OFFSET {offset}"
            cursor.execute(query, params)
            results = cursor.fetchall()
            conn.close()
            
            # Update UI
            self.count_label.setText(f"Total: {total:,}")
            self.total_pages = max(1, (total + self.per_page - 1) // self.per_page)
            self.page_label.setText(f"Page {self.current_page} / {self.total_pages}")
            
            # Update table
            self.table.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    self.table.setItem(row_idx, col_idx, item)
            
            # Update button states
            self.prev_btn.setEnabled(self.current_page > 1)
            self.next_btn.setEnabled(self.current_page < self.total_pages)
            
            self.log_action('search', details=f"Found {total} results")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Search error:\n{str(e)}")
    
    def clear_filters(self):
        """Clear all search filters"""
        self.id_input.clear()
        self.name_input.clear()
        self.gender_combo.setCurrentIndex(0)
        self.age_input.clear()
        self.province_input.clear()
        self.district_input.clear()
        self.commune_input.clear()
        self.village_input.clear()
        self.current_page = 1
        self.search_people()
    
    def prev_page(self):
        """Go to previous page"""
        if self.current_page > 1:
            self.current_page -= 1
            self.search_people()
    
    def next_page(self):
        """Go to next page"""
        if self.current_page < self.total_pages:
            self.current_page += 1
            self.search_people()

    
    def show_users_dialog(self):
        """Show user management dialog"""
        dialog = QDialog(self)
        dialog.setWindowTitle("User Management")
        dialog.setMinimumSize(900, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
        """)
        
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("👥 User Management")
        title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #333;
            padding: 10px;
        """)
        layout.addWidget(title)
        
        # Create user form
        form_frame = QFrame()
        form_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        form_layout = QGridLayout(form_frame)
        form_layout.setSpacing(15)
        
        form_title = QLabel("Create New User")
        form_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        form_layout.addWidget(form_title, 0, 0, 1, 4)
        
        # Form fields
        form_layout.addWidget(QLabel("Username:"), 1, 0)
        username_input = ModernLineEdit("Enter username")
        form_layout.addWidget(username_input, 1, 1)
        
        form_layout.addWidget(QLabel("Password:"), 1, 2)
        password_input = ModernLineEdit("Enter password")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(password_input, 1, 3)
        
        form_layout.addWidget(QLabel("Role:"), 2, 0)
        role_combo = ModernComboBox()
        role_combo.addItems(["user", "manager"])
        form_layout.addWidget(role_combo, 2, 1)
        
        form_layout.addWidget(QLabel("Province:"), 2, 2)
        province_combo = ModernComboBox()
        provinces = [
            "", "Banteay Meanchey", "Battambang", "Kampong Cham",
            "Kampong Chhnang", "Kampong Speu", "Kampong Thom",
            "Kampot", "Kandal", "Koh Kong", "Kratie",
            "Mondul Kiri", "Phnom Penh", "Preah Vihear",
            "Prey Veng", "Pursat", "Ratanak Kiri",
            "Siemreap", "Preah Sihanouk", "Stung Treng",
            "Svay Rieng", "Takeo", "Oddar Meanchey",
            "Kep", "Pailin", "Tboung Khmum"
        ]
        province_combo.addItems(provinces)
        form_layout.addWidget(province_combo, 2, 3)
        
        def create_user():
            username = username_input.text().strip()
            password = password_input.text()
            role = role_combo.currentText()
            province = province_combo.currentText() if role == 'manager' else None
            
            if not username or not password:
                QMessageBox.warning(dialog, "Error", "Username and password required")
                return
            
            if role == 'manager' and not province:
                QMessageBox.warning(dialog, "Error", "Province required for managers")
                return
            
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                # Check if username exists
                cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
                if cursor.fetchone():
                    QMessageBox.warning(dialog, "Error", "Username already exists")
                    conn.close()
                    return
                
                # Check if province already has manager
                if role == 'manager':
                    cursor.execute("SELECT username FROM users WHERE role = 'manager' AND province = ?", (province,))
                    existing = cursor.fetchone()
                    if existing:
                        QMessageBox.warning(dialog, "Error", f"Province already has manager: {existing[0]}")
                        conn.close()
                        return
                
                cursor.execute("INSERT INTO users (username, password, role, province) VALUES (?, ?, ?, ?)",
                             (username, generate_password_hash(password), role, province))
                conn.commit()
                conn.close()
                
                QMessageBox.information(dialog, "Success", "User created successfully!")
                username_input.clear()
                password_input.clear()
                province_combo.setCurrentIndex(0)
                refresh_users()
                
            except Exception as e:
                QMessageBox.critical(dialog, "Error", f"Failed to create user:\n{str(e)}")
        
        create_btn = ModernButton("➕ Create User", "#4CAF50", "#45a049")
        create_btn.clicked.connect(create_user)
        form_layout.addWidget(create_btn, 3, 0, 1, 4)
        
        layout.addWidget(form_frame)
        
        # Users table
        table_frame = QFrame()
        table_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        table_layout = QVBoxLayout(table_frame)
        
        table_title = QLabel("All Users")
        table_title.setStyleSheet("font-size: 16px; font-weight: bold; color: #333;")
        table_layout.addWidget(table_title)
        
        users_table = QTableWidget()
        users_table.setColumnCount(5)
        users_table.setHorizontalHeaderLabels(["ID", "Username", "Role", "Province", "Created"])
        users_table.setStyleSheet("""
            QTableWidget {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #E0E0E0;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #FF9800;
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
        """)
        users_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        users_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        header = users_table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        
        table_layout.addWidget(users_table)
        
        def refresh_users():
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, role, province, created_at FROM users ORDER BY id")
                users = cursor.fetchall()
                conn.close()
                
                users_table.setRowCount(len(users))
                for row_idx, user in enumerate(users):
                    for col_idx, value in enumerate(user):
                        display_value = value if value else "-"
                        if col_idx == 4 and value:  # Format datetime
                            display_value = value[:16]
                        item = QTableWidgetItem(str(display_value))
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        users_table.setItem(row_idx, col_idx, item)
            except Exception as e:
                QMessageBox.critical(dialog, "Error", f"Failed to load users:\n{str(e)}")
        
        def delete_user():
            selected = users_table.selectedItems()
            if not selected:
                QMessageBox.warning(dialog, "Warning", "Please select a user to delete")
                return
            
            row = users_table.currentRow()
            user_id = int(users_table.item(row, 0).text())
            username = users_table.item(row, 1).text()
            
            if user_id == self.user_data['id']:
                QMessageBox.warning(dialog, "Error", "Cannot delete yourself")
                return
            
            reply = QMessageBox.question(dialog, "Confirm", f"Delete user '{username}'?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    conn = sqlite3.connect(self.db_path)
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
                    conn.commit()
                    conn.close()
                    QMessageBox.information(dialog, "Success", "User deleted successfully")
                    refresh_users()
                except Exception as e:
                    QMessageBox.critical(dialog, "Error", f"Failed to delete user:\n{str(e)}")
        
        btn_layout = QHBoxLayout()
        refresh_btn = ModernButton("🔄 Refresh", "#2196F3", "#1976D2")
        refresh_btn.clicked.connect(refresh_users)
        btn_layout.addWidget(refresh_btn)
        
        delete_btn = ModernButton("🗑️ Delete Selected", "#f44336", "#d32f2f")
        delete_btn.clicked.connect(delete_user)
        btn_layout.addWidget(delete_btn)
        
        btn_layout.addStretch()
        table_layout.addLayout(btn_layout)
        
        layout.addWidget(table_frame)
        
        refresh_users()
        dialog.exec()
    
    def show_history_dialog(self):
        """Show action history dialog"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Action History")
        dialog.setMinimumSize(900, 600)
        dialog.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
        """)
        
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)
        
        # Title
        title = QLabel("📜 Action History")
        title.setStyleSheet("""
            font-size: 22px;
            font-weight: bold;
            color: #333;
            padding: 10px;
        """)
        layout.addWidget(title)
        
        # History table
        table_frame = QFrame()
        table_frame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        table_layout = QVBoxLayout(table_frame)
        
        history_table = QTableWidget()
        history_table.setColumnCount(5)
        history_table.setHorizontalHeaderLabels(["ID", "User", "Action", "Details", "Timestamp"])
        history_table.setStyleSheet("""
            QTableWidget {
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                gridline-color: #E0E0E0;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QHeaderView::section {
                background-color: #9C27B0;
                color: white;
                padding: 10px;
                border: none;
                font-weight: bold;
            }
        """)
        history_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        history_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        header = history_table.horizontalHeader()
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        
        table_layout.addWidget(history_table)
        layout.addWidget(table_frame)
        
        # Load history
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            query = """
                SELECT h.id, u.username, h.action, h.details, h.timestamp
                FROM edit_history h
                JOIN users u ON h.user_id = u.id
            """
            
            if self.user_data['role'] == 'manager':
                query += " WHERE h.user_id = ?"
                cursor.execute(query + " ORDER BY h.timestamp DESC LIMIT 100", (self.user_data['id'],))
            else:
                cursor.execute(query + " ORDER BY h.timestamp DESC LIMIT 100")
            
            history = cursor.fetchall()
            conn.close()
            
            history_table.setRowCount(len(history))
            for row_idx, row_data in enumerate(history):
                for col_idx, value in enumerate(row_data):
                    display_value = value if value else "-"
                    item = QTableWidgetItem(str(display_value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter if col_idx != 3 else Qt.AlignmentFlag.AlignLeft)
                    history_table.setItem(row_idx, col_idx, item)
                    
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Failed to load history:\n{str(e)}")
        
        dialog.exec()
    
    def log_action(self, action, person_id=None, details=None):
        """Log user action to database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO edit_history (user_id, person_id, action, details, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (self.user_data['id'], person_id, action, details, datetime.now()))
            conn.commit()
            conn.close()
        except:
            pass
    
    def logout(self):
        """Logout current user"""
        reply = QMessageBox.question(self, "Logout", "Are you sure you want to logout?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QMessageBox.StandardButton.Yes:
            self.log_action('logout')
            self.close()
            login = LoginWindow()
            if login.exec() == QDialog.DialogCode.Accepted:
                new_window = MainWindow(login.user_data)
                new_window.show()
                global main_window
                main_window = new_window


def main():
    app = QApplication(sys.argv)
    
    # Set application style
    app.setStyle('Fusion')
    
    # Show login
    login = LoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:
        global main_window
        main_window = MainWindow(login.user_data)
        main_window.show()
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
