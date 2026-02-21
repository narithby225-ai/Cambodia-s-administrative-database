"""
ULTIMATE Modern GUI - People Database Management
Beautiful animations, easy to use, professional design
"""
import sys
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from werkzeug.security import check_password_hash, generate_password_hash


class AnimatedButton(QPushButton):
    """Button with smooth animation effects"""
    def __init__(self, text, icon="", color="#2196F3", hover_color="#1976D2"):
        super().__init__(f"{icon} {text}" if icon else text)
        self.default_color = color
        self.hover_color = hover_color
        self.current_color = color
        
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {color};
                color: white;
                border: none;
                border-radius: 12px;
                padding: 14px 28px;
                font-size: 15px;
                font-weight: bold;
                min-width: 140px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
                transform: scale(1.05);
            }}
            QPushButton:pressed {{
                background-color: {color};
                padding-top: 16px;
            }}
            QPushButton:disabled {{
                background-color: #CCCCCC;
                color: #666666;
            }}
        """)
        
        # Add shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 4)
        self.setGraphicsEffect(shadow)
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)


class ModernCard(QFrame):
    """Card widget with shadow"""
    def __init__(self, title="", parent=None):
        super().__init__(parent)
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 15px;
                padding: 5px;
            }
        """)
        
        # Add shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 5)
        self.setGraphicsEffect(shadow)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(25, 25, 25, 25)
        self.layout.setSpacing(15)
        
        if title:
            title_label = QLabel(title)
            title_label.setStyleSheet("""
                font-size: 20px;
                font-weight: bold;
                color: #333;
                padding-bottom: 10px;
            """)
            self.layout.addWidget(title_label)


class StyledLineEdit(QLineEdit):
    """Modern line edit with icon support"""
    def __init__(self, placeholder="", icon=""):
        super().__init__()
        self.setPlaceholderText(f"{icon} {placeholder}" if icon else placeholder)
        self.setStyleSheet("""
            QLineEdit {
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                padding: 12px 18px;
                font-size: 14px;
                background-color: #FAFAFA;
                color: #333;
            }
            QLineEdit:focus {
                border: 2px solid #667eea;
                background-color: white;
            }
            QLineEdit:hover {
                border: 2px solid #B0B0B0;
            }
        """)
        self.setMinimumHeight(45)


class StyledComboBox(QComboBox):
    """Modern combo box"""
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QComboBox {
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                padding: 12px 18px;
                font-size: 14px;
                background-color: #FAFAFA;
                min-height: 21px;
            }
            QComboBox:focus {
                border: 2px solid #667eea;
                background-color: white;
            }
            QComboBox:hover {
                border: 2px solid #B0B0B0;
            }
            QComboBox::drop-down {
                border: none;
                width: 35px;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 6px solid transparent;
                border-right: 6px solid transparent;
                border-top: 6px solid #666;
                margin-right: 12px;
            }
            QComboBox QAbstractItemView {
                border: 2px solid #667eea;
                border-radius: 8px;
                background-color: white;
                selection-background-color: #E3F2FD;
                selection-color: #1976D2;
                padding: 5px;
            }
        """)
        self.setCursor(Qt.CursorShape.PointingHandCursor)


class SplashScreen(QSplashScreen):
    """Animated splash screen"""
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 300)
        
        # Create pixmap
        pixmap = QPixmap(500, 300)
        pixmap.fill(Qt.GlobalColor.transparent)
        
        painter = QPainter(pixmap)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Gradient background
        gradient = QLinearGradient(0, 0, 500, 300)
        gradient.setColorAt(0, QColor("#667eea"))
        gradient.setColorAt(1, QColor("#764ba2"))
        painter.setBrush(gradient)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRoundedRect(0, 0, 500, 300, 20, 20)
        
        # Text
        painter.setPen(QColor("white"))
        painter.setFont(QFont("Arial", 28, QFont.Weight.Bold))
        painter.drawText(QRect(0, 80, 500, 50), Qt.AlignmentFlag.AlignCenter, "People Database")
        
        painter.setFont(QFont("Arial", 16))
        painter.drawText(QRect(0, 130, 500, 30), Qt.AlignmentFlag.AlignCenter, "Management System")
        
        painter.setFont(QFont("Arial", 12))
        painter.drawText(QRect(0, 220, 500, 30), Qt.AlignmentFlag.AlignCenter, "Loading... Please wait")
        
        painter.end()
        
        self.setPixmap(pixmap)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)


class LoginWindow(QDialog):
    """Beautiful animated login"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setFixedSize(500, 650)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.user_data = None
        self.db_path = 'instance/people.db'
        self.setup_ui()
        
        # Animation
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        self.animation = QPropertyAnimation(self.opacity, b"opacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()
    
    def setup_ui(self):
        """Setup beautiful login UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Container
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #667eea, stop:1 #764ba2);
                border-radius: 20px;
            }
        """)
        
        # Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setColor(QColor(0, 0, 0, 100))
        shadow.setOffset(0, 10)
        container.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(25)
        
        # Logo
        logo_label = QLabel("🔐")
        logo_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo_label.setStyleSheet("""
            font-size: 80px;
            background: transparent;
        """)
        layout.addWidget(logo_label)
        
        # Title
        title = QLabel("Welcome Back!")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 32px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        layout.addWidget(title)
        
        subtitle = QLabel("Sign in to continue")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 16px;
            color: rgba(255, 255, 255, 0.9);
            background: transparent;
            margin-bottom: 10px;
        """)
        layout.addWidget(subtitle)
        
        # Form card
        form_card = QFrame()
        form_card.setStyleSheet("""
            QFrame {
                background-color: rgba(255, 255, 255, 0.95);
                border-radius: 15px;
            }
        """)
        form_layout = QVBoxLayout(form_card)
        form_layout.setContentsMargins(30, 30, 30, 30)
        form_layout.setSpacing(20)
        
        # Username
        self.username_input = StyledLineEdit("Enter username", "👤")
        form_layout.addWidget(self.username_input)
        
        # Password
        self.password_input = StyledLineEdit("Enter password", "🔒")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(self.password_input)
        
        # Show password checkbox
        show_pass = QCheckBox("Show password")
        show_pass.setStyleSheet("""
            QCheckBox {
                color: #666;
                font-size: 13px;
                background: transparent;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 2px solid #CCC;
            }
            QCheckBox::indicator:checked {
                background-color: #667eea;
                border-color: #667eea;
            }
        """)
        show_pass.toggled.connect(lambda checked: self.password_input.setEchoMode(
            QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
        ))
        form_layout.addWidget(show_pass)
        
        # Login button
        login_btn = AnimatedButton("Login", "🚀", "#667eea", "#5568d3")
        login_btn.clicked.connect(self.login)
        form_layout.addWidget(login_btn)
        
        layout.addWidget(form_card)
        
        # Info
        info = QLabel("💡 Default: superadmin / super123")
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setStyleSheet("""
            color: white;
            font-size: 13px;
            background: transparent;
            padding: 5px;
        """)
        layout.addWidget(info)
        
        # Close button
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(35, 35)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: none;
                border-radius: 17px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)
        close_btn.clicked.connect(self.reject)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        
        # Position close button
        close_btn.setParent(container)
        close_btn.move(455, 10)
        
        main_layout.addWidget(container)
        
        # Connect Enter key
        self.password_input.returnPressed.connect(self.login)
        self.username_input.returnPressed.connect(self.login)
        
        # Focus
        self.username_input.setFocus()
    
    def login(self):
        """Authenticate with loading animation"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            self.shake_animation()
            QMessageBox.warning(self, "Error", "Please enter username and password")
            return
        
        # Show loading
        self.setCursor(Qt.CursorShape.WaitCursor)
        QApplication.processEvents()
        
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
                
                # Success animation
                self.fade_out()
            else:
                self.setCursor(Qt.CursorShape.ArrowCursor)
                self.shake_animation()
                QMessageBox.critical(self, "Login Failed", "Invalid username or password")
                self.password_input.clear()
                self.password_input.setFocus()
        except Exception as e:
            self.setCursor(Qt.CursorShape.ArrowCursor)
            QMessageBox.critical(self, "Database Error", f"Error:\n{str(e)}")
    
    def shake_animation(self):
        """Shake animation for error"""
        animation = QPropertyAnimation(self, b"pos")
        animation.setDuration(500)
        animation.setLoopCount(2)
        
        pos = self.pos()
        animation.setKeyValueAt(0, pos)
        animation.setKeyValueAt(0.1, pos + QPoint(-10, 0))
        animation.setKeyValueAt(0.2, pos + QPoint(10, 0))
        animation.setKeyValueAt(0.3, pos + QPoint(-10, 0))
        animation.setKeyValueAt(0.4, pos + QPoint(10, 0))
        animation.setKeyValueAt(0.5, pos)
        
        animation.start()
    
    def fade_out(self):
        """Fade out animation on success"""
        animation = QPropertyAnimation(self.opacity, b"opacity")
        animation.setDuration(300)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.finished.connect(self.accept)
        animation.start()


class StatCard(QFrame):
    """Animated stat card"""
    def __init__(self, icon, title, value, color):
        super().__init__()
        self.setFixedHeight(120)
        self.setStyleSheet(f"""
            QFrame {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {color}, stop:1 {self.darken_color(color)});
                border-radius: 12px;
            }}
        """)
        
        # Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 4)
        self.setGraphicsEffect(shadow)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 15, 20, 15)
        
        # Icon
        icon_label = QLabel(icon)
        icon_label.setStyleSheet("font-size: 32px; color: white; background: transparent;")
        layout.addWidget(icon_label)
        
        # Value
        self.value_label = QLabel(value)
        self.value_label.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        layout.addWidget(self.value_label)
        
        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            font-size: 13px;
            color: rgba(255, 255, 255, 0.9);
            background: transparent;
        """)
        layout.addWidget(title_label)
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)
    
    def darken_color(self, color):
        """Darken color for gradient"""
        c = QColor(color)
        return c.darker(120).name()
    
    def update_value(self, value):
        """Update value with animation"""
        self.value_label.setText(value)



class MainWindow(QMainWindow):
    """Ultimate main window with animations"""
    def __init__(self, user_data):
        super().__init__()
        self.user_data = user_data
        self.db_path = 'instance/people.db'
        self.current_page = 1
        self.total_pages = 1
        self.per_page = 100
        
        self.setWindowTitle("People Database Management System")
        self.setMinimumSize(1500, 850)
        
        # Remove title bar for custom design
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        
        self.setup_ui()
        self.log_action('login')
        
        # Load initial data
        QTimer.singleShot(100, self.search_people)
        
        # Fade in animation
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        animation = QPropertyAnimation(self.opacity, b"opacity")
        animation.setDuration(500)
        animation.setStartValue(0)
        animation.setEndValue(1)
        animation.start()
    
    def setup_ui(self):
        """Setup ultimate UI"""
        # Central widget
        central = QWidget()
        self.setCentralWidget(central)
        central.setStyleSheet("background-color: #F0F2F5;")
        
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)
        
        # Custom title bar
        self.create_title_bar(main_layout)
        
        # Stats cards
        self.create_stats_section(main_layout)
        
        # Content
        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(20, 10, 20, 20)
        content_layout.setSpacing(20)
        
        # Sidebar
        self.create_sidebar(content_layout)
        
        # Main content
        self.create_content_area(content_layout)
        
        main_layout.addWidget(content)
    
    def create_title_bar(self, parent_layout):
        """Custom title bar with controls"""
        title_bar = QFrame()
        title_bar.setFixedHeight(70)
        title_bar.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                border: none;
            }
        """)
        
        layout = QHBoxLayout(title_bar)
        layout.setContentsMargins(25, 0, 25, 0)
        
        # Title
        title = QLabel("👥 People Database Management")
        title.setStyleSheet("""
            font-size: 26px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        layout.addWidget(title)
        
        layout.addStretch()
        
        # User info
        role_text = self.user_data['role'].replace('_', ' ').title()
        user_info = f"👤 {self.user_data['username']} • {role_text}"
        if self.user_data['province']:
            user_info += f" • 📍 {self.user_data['province']}"
        
        user_label = QLabel(user_info)
        user_label.setStyleSheet("""
            font-size: 14px;
            color: white;
            background: transparent;
            padding: 10px 15px;
            border-radius: 8px;
        """)
        layout.addWidget(user_label)
        
        # Window controls
        btn_style = """
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: none;
                border-radius: 6px;
                font-size: 16px;
                font-weight: bold;
                min-width: 40px;
                max-width: 40px;
                min-height: 40px;
                max-height: 40px;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """
        
        minimize_btn = QPushButton("−")
        minimize_btn.setStyleSheet(btn_style)
        minimize_btn.clicked.connect(self.showMinimized)
        minimize_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(minimize_btn)
        
        maximize_btn = QPushButton("□")
        maximize_btn.setStyleSheet(btn_style)
        maximize_btn.clicked.connect(self.toggle_maximize)
        maximize_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(maximize_btn)
        
        close_btn = QPushButton("✕")
        close_btn.setStyleSheet(btn_style + """
            QPushButton:hover {
                background-color: #f44336;
            }
        """)
        close_btn.clicked.connect(self.close)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        layout.addWidget(close_btn)
        
        parent_layout.addWidget(title_bar)
        
        # Make title bar draggable
        title_bar.mousePressEvent = self.title_bar_mouse_press
        title_bar.mouseMoveEvent = self.title_bar_mouse_move
        self.drag_pos = None
    
    def title_bar_mouse_press(self, event):
        """Handle title bar mouse press"""
        if event.button() == Qt.MouseButton.LeftButton:
            self.drag_pos = event.globalPosition().toPoint()
    
    def title_bar_mouse_move(self, event):
        """Handle title bar mouse move"""
        if event.buttons() == Qt.MouseButton.LeftButton and self.drag_pos:
            self.move(self.pos() + event.globalPosition().toPoint() - self.drag_pos)
            self.drag_pos = event.globalPosition().toPoint()
    
    def toggle_maximize(self):
        """Toggle maximize/restore"""
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()
    
    def create_stats_section(self, parent_layout):
        """Create stats cards section"""
        stats_container = QWidget()
        stats_container.setStyleSheet("background: transparent;")
        stats_layout = QHBoxLayout(stats_container)
        stats_layout.setContentsMargins(20, 15, 20, 10)
        stats_layout.setSpacing(15)
        
        # Total records stat
        self.total_stat = StatCard("📊", "Total Records", "Loading...", "#4CAF50")
        stats_layout.addWidget(self.total_stat)
        
        # Search results stat
        self.results_stat = StatCard("🔍", "Search Results", "0", "#2196F3")
        stats_layout.addWidget(self.results_stat)
        
        # Current page stat
        self.page_stat = StatCard("📄", "Current Page", "1", "#FF9800")
        stats_layout.addWidget(self.page_stat)
        
        # User role stat
        role_icon = "👑" if self.user_data['role'] == 'super_admin' else "👤"
        role_text = self.user_data['role'].replace('_', ' ').title()
        self.role_stat = StatCard(role_icon, "Your Role", role_text, "#9C27B0")
        stats_layout.addWidget(self.role_stat)
        
        parent_layout.addWidget(stats_container)
        
        # Load total count
        QTimer.singleShot(200, self.update_total_count)
    
    def update_total_count(self):
        """Update total records count"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            if self.user_data['role'] == 'manager' and self.user_data['province']:
                cursor.execute("SELECT COUNT(*) FROM people WHERE province = ?", (self.user_data['province'],))
            else:
                cursor.execute("SELECT COUNT(*) FROM people")
            
            total = cursor.fetchone()[0]
            conn.close()
            
            self.total_stat.update_value(f"{total:,}")
        except:
            self.total_stat.update_value("Error")
    
    def create_sidebar(self, parent_layout):
        """Create animated sidebar"""
        sidebar = ModernCard("🔍 Search Filters")
        sidebar.setFixedWidth(350)
        
        # Search fields
        self.id_input = StyledLineEdit("Person ID", "🆔")
        sidebar.layout.addWidget(self.id_input)
        
        self.name_input = StyledLineEdit("Name", "👤")
        sidebar.layout.addWidget(self.name_input)
        
        self.gender_combo = StyledComboBox()
        self.gender_combo.addItems(["⚧ All Genders", "♂ Male", "♀ Female"])
        sidebar.layout.addWidget(self.gender_combo)
        
        self.age_input = StyledLineEdit("Age", "🎂")
        sidebar.layout.addWidget(self.age_input)
        
        self.province_input = StyledLineEdit("Province", "🌍")
        # Disable province field for managers - they can only see their province
        if self.user_data['role'] == 'manager' and self.user_data['province']:
            self.province_input.setText(self.user_data['province'])
            self.province_input.setEnabled(False)
            self.province_input.setStyleSheet("""
                QLineEdit {
                    border: 2px solid #FFB74D;
                    border-radius: 10px;
                    padding: 12px 18px;
                    font-size: 14px;
                    background-color: #FFF3E0;
                    color: #E65100;
                    font-weight: bold;
                }
            """)
        sidebar.layout.addWidget(self.province_input)
        
        self.district_input = StyledLineEdit("District", "📍")
        sidebar.layout.addWidget(self.district_input)
        
        self.commune_input = StyledLineEdit("Commune", "🏘️")
        sidebar.layout.addWidget(self.commune_input)
        
        self.village_input = StyledLineEdit("Village", "🏠")
        sidebar.layout.addWidget(self.village_input)
        
        # Buttons
        search_btn = AnimatedButton("Search", "🔍", "#4CAF50", "#45a049")
        search_btn.clicked.connect(self.search_people)
        sidebar.layout.addWidget(search_btn)
        
        clear_btn = AnimatedButton("Clear All", "🗑️", "#FF5722", "#E64A19")
        clear_btn.clicked.connect(self.clear_filters)
        sidebar.layout.addWidget(clear_btn)
        
        sidebar.layout.addSpacing(15)
        
        # Action buttons
        if self.user_data['role'] == 'super_admin':
            users_btn = AnimatedButton("Manage Users", "👥", "#FF9800", "#F57C00")
            users_btn.clicked.connect(self.show_users_dialog)
            sidebar.layout.addWidget(users_btn)
        
        history_btn = AnimatedButton("View History", "📜", "#9C27B0", "#7B1FA2")
        history_btn.clicked.connect(self.show_history_dialog)
        sidebar.layout.addWidget(history_btn)
        
        sidebar.layout.addStretch()
        
        # Logout
        logout_btn = AnimatedButton("Logout", "🚪", "#607D8B", "#455A64")
        logout_btn.clicked.connect(self.logout)
        sidebar.layout.addWidget(logout_btn)
        
        parent_layout.addWidget(sidebar)
    
    def create_content_area(self, parent_layout):
        """Create main content with table"""
        content = ModernCard("📊 Search Results")
        
        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(8)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Gender", "Age", "Province", "District", "Commune", "Village"
        ])
        
        self.table.setStyleSheet("""
            QTableWidget {
                border: none;
                border-radius: 10px;
                background-color: #FAFAFA;
                gridline-color: #E0E0E0;
                font-size: 13px;
            }
            QTableWidget::item {
                padding: 10px;
                border-bottom: 1px solid #F0F0F0;
            }
            QTableWidget::item:selected {
                background-color: #E3F2FD;
                color: #1976D2;
            }
            QTableWidget::item:hover {
                background-color: #F5F5F5;
            }
            QHeaderView::section {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
                padding: 14px;
                border: none;
                font-weight: bold;
                font-size: 14px;
            }
            QScrollBar:vertical {
                border: none;
                background: #F0F0F0;
                width: 12px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #CCCCCC;
                border-radius: 6px;
                min-height: 30px;
            }
            QScrollBar::handle:vertical:hover {
                background: #999999;
            }
        """)
        
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.table.verticalHeader().setVisible(False)
        
        # Column widths
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
        
        content.layout.addWidget(self.table)
        
        # Pagination
        pagination = QHBoxLayout()
        pagination.setSpacing(15)
        
        self.prev_btn = AnimatedButton("◀ Previous", "", "#2196F3", "#1976D2")
        self.prev_btn.clicked.connect(self.prev_page)
        pagination.addWidget(self.prev_btn)
        
        pagination.addStretch()
        
        self.page_label = QLabel("Page 1 / 1")
        self.page_label.setStyleSheet("""
            font-size: 16px;
            font-weight: bold;
            color: #333;
            padding: 12px 24px;
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #E3F2FD, stop:1 #F3E5F5);
            border-radius: 10px;
        """)
        pagination.addWidget(self.page_label)
        
        pagination.addStretch()
        
        self.next_btn = AnimatedButton("Next ▶", "", "#2196F3", "#1976D2")
        self.next_btn.clicked.connect(self.next_page)
        pagination.addWidget(self.next_btn)
        
        content.layout.addLayout(pagination)
        
        parent_layout.addWidget(content)

    
    def search_people(self):
        """Search with loading animation"""
        self.setCursor(Qt.CursorShape.WaitCursor)
        QApplication.processEvents()
        
        offset = (self.current_page - 1) * self.per_page
        
        # Build query
        query = "SELECT id, name, gender, age, province, district, commune, village FROM people WHERE 1=1"
        params = []
        
        # Province restriction
        if self.user_data['role'] == 'manager' and self.user_data['province']:
            query += " AND province = ?"
            params.append(self.user_data['province'])
        
        # Filters
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
        if "Male" in gender and "All" not in gender:
            query += " AND gender = ?"
            params.append("male")
        elif "Female" in gender:
            query += " AND gender = ?"
            params.append("female")
        
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
            
            # Count
            count_query = query.replace("SELECT id, name, gender, age, province, district, commune, village", "SELECT COUNT(*)")
            cursor.execute(count_query, params)
            total = cursor.fetchone()[0]
            
            # Results
            query += f" LIMIT {self.per_page} OFFSET {offset}"
            cursor.execute(query, params)
            results = cursor.fetchall()
            conn.close()
            
            # Update stats
            self.results_stat.update_value(f"{total:,}")
            self.page_stat.update_value(str(self.current_page))
            
            self.total_pages = max(1, (total + self.per_page - 1) // self.per_page)
            self.page_label.setText(f"Page {self.current_page} / {self.total_pages}")
            
            # Update table
            self.table.setRowCount(len(results))
            for row_idx, row_data in enumerate(results):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                    
                    # Color code gender
                    if col_idx == 2:
                        if value == 'male':
                            item.setForeground(QColor("#2196F3"))
                        else:
                            item.setForeground(QColor("#E91E63"))
                    
                    self.table.setItem(row_idx, col_idx, item)
            
            # Button states
            self.prev_btn.setEnabled(self.current_page > 1)
            self.next_btn.setEnabled(self.current_page < self.total_pages)
            
            self.log_action('search', details=f"Found {total} results")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Search error:\n{str(e)}")
        finally:
            self.setCursor(Qt.CursorShape.ArrowCursor)
    
    def clear_filters(self):
        """Clear all with animation"""
        self.id_input.clear()""Show login after splash"""
    login = LoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:
        global main_window
        main_window = MainWindow(login.user_data)
        main_window.show()


if __name__ == '__main__':
    main()
() == QDialog.DialogCode.Accepted:
            new_window = MainWindow(login.user_data)
            new_window.show()
            global main_window
            main_window = new_window


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    # Splash screen
    splash = SplashScreen()
    splash.show()
    
    # Simulate loading
    QTimer.singleShot(1500, splash.close)
    QTimer.singleShot(1500, lambda: show_login(app))
    
    sys.exit(app.exec())


def show_login(app):
    "essageBox.StandardButton.Yes:
            self.log_action('logout')
            
            # Fade out
            animation = QPropertyAnimation(self.opacity, b"opacity")
            animation.setDuration(300)
            animation.setStartValue(1)
            animation.setEndValue(0)
            animation.finished.connect(self.restart_login)
            animation.start()
    
    def restart_login(self):
        """Restart with login"""
        self.close()
        login = LoginWindow()
        if login.execetails, timestamp)
                VALUES (?, ?, ?, ?, ?)
            """, (self.user_data['id'], person_id, action, details, datetime.now()))
            conn.commit()
            conn.close()
        except:
            pass
    
    def logout(self):
        """Logout with confirmation"""
        reply = QMessageBox.question(self, "Logout", "Are you sure you want to logout?",
                                    QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        
        if reply == QM                history_table.setItem(row_idx, col_idx, item)
                    
        except Exception as e:
            QMessageBox.critical(dialog, "Error", f"Failed to load:\n{str(e)}")
        
        dialog.exec()
    
    def log_action(self, action, person_id=None, details=None):
        """Log action"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO edit_history (user_id, person_id, action, dexecute(query + " ORDER BY h.timestamp DESC LIMIT 100")
            
            history = cursor.fetchall()
            conn.close()
            
            history_table.setRowCount(len(history))
            for row_idx, row_data in enumerate(history):
                for col_idx, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value if value else "-"))
                    item.setTextAlignment(Qt.AlignmentFlag.AlignCenter if col_idx != 3 else Qt.AlignmentFlag.AlignLeft)
    f.db_path)
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
                cursor.story_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        history_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        header = history_table.horizontalHeader()
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        
        table_card.layout.addWidget(history_table)
        content_layout.addWidget(table_card)
        layout.addLayout(content_layout)
        
        # Load history
        try:
            conn = sqlite3.connect(sele.PointingHandCursor)
        title_layout.addWidget(close_btn)
        
        layout.addWidget(title_bar)
        
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        
        table_card = ModernCard()
        
        history_table = QTableWidget()
        history_table.setColumnCount(5)
        history_table.setHorizontalHeaderLabels(["ID", "User", "Action", "Details", "Timestamp"])
        history_table.setStyleSheet(self.table.styleSheet())
        hi0)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
        """)
        close_btn.clicked.connect(dialog.close)
        close_btn.setCursor(Qt.CursorShapdient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #9C27B0, stop:1 #7B1FA2);
        """)
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(20, 0, 20, 0)
        
        title = QLabel("📜 Action History")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background: transparent;")
        title_layout.addWidget(title)
        
        title_layout.addStretch()
        
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(40, 4ul design"""
        dialog = QDialog(self)
        dialog.setWindowTitle("Action History")
        dialog.setMinimumSize(1000, 600)
        dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        dialog.setStyleSheet("background-color: #F0F2F5;")
        
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Title bar
        title_bar = QFrame()
        title_bar.setFixedHeight(60)
        title_bar.setStyleSheet("""
            background: qlineargraesh_btn)
        
        delete_btn = AnimatedButton("Delete Selected", "🗑️", "#f44336", "#d32f2f")
        delete_btn.clicked.connect(delete_user)
        btn_layout.addWidget(delete_btn)
        
        btn_layout.addStretch()
        table_card.layout.addLayout(btn_layout)
        
        content_layout.addWidget(table_card)
        
        layout.addLayout(content_layout)
        
        refresh_users()
        dialog.exec()
    
    def show_history_dialog(self):
        """Show history with beautif,))
                    conn.commit()
                    conn.close()
                    QMessageBox.information(dialog, "Success", "✅ User deleted!")
                    refresh_users()
                except Exception as e:
                    QMessageBox.critical(dialog, "Error", f"Failed:\n{str(e)}")
        
        btn_layout = QHBoxLayout()
        refresh_btn = AnimatedButton("Refresh", "🔄", "#2196F3", "#1976D2")
        refresh_btn.clicked.connect(refresh_users)
        btn_layout.addWidget(refrlete yourself!")
                return
            
            reply = QMessageBox.question(dialog, "Confirm", f"Delete user '{username}'?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
            
            if reply == QMessageBox.StandardButton.Yes:
                try:
                    conn = sqlite3.connect(self.db_path)
                    cursor = conn.cursor()
                    cursor.execute("DELETE FROM users WHERE id = ?", (user_id        
        def delete_user():
            selected = users_table.selectedItems()
            if not selected:
                QMessageBox.warning(dialog, "Warning", "Please select a user!")
                return
            
            row = users_table.currentRow()
            user_id = int(users_table.item(row, 0).text())
            username = users_table.item(row, 1).text()
            
            if user_id == self.user_data['id']:
                QMessageBox.warning(dialog, "Error", "Cannot del_idx, value in enumerate(user):
                        display = value if value else "-"
                        if col_idx == 4 and value:
                            display = value[:16]
                        item = QTableWidgetItem(str(display))
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        users_table.setItem(row_idx, col_idx, item)
            except Exception as e:
                QMessageBox.critical(dialog, "Error", f"Failed to load:\n{str(e)}")
   table_card.layout.addWidget(users_table)
        
        def refresh_users():
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT id, username, role, province, created_at FROM users ORDER BY id")
                users = cursor.fetchall()
                conn.close()
                
                users_table.setRowCount(len(users))
                for row_idx, user in enumerate(users):
                    for cole.setHorizontalHeaderLabels(["ID", "Username", "Role", "Province", "Created"])
        users_table.setStyleSheet(self.table.styleSheet())
        users_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        users_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        
        header = users_table.horizontalHeader()
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)
        
     except Exception as e:
                QMessageBox.critical(dialog, "Error", f"Failed:\n{str(e)}")
        
        create_btn = AnimatedButton("Create User", "➕", "#4CAF50", "#45a049")
        create_btn.clicked.connect(create_user)
        form_card.layout.addWidget(create_btn)
        
        content_layout.addWidget(form_card)
        
        # Users table
        table_card = ModernCard("📋 All Users")
        
        users_table = QTableWidget()
        users_table.setColumnCount(5)
        users_tabINTO users (username, password, role, province) VALUES (?, ?, ?, ?)",
                             (username, generate_password_hash(password), role, province))
                conn.commit()
                conn.close()
                
                QMessageBox.information(dialog, "Success", "✅ User created successfully!")
                username_input.clear()
                password_input.clear()
                province_combo.setCurrentIndex(0)
                refresh_users()
                
            
                    return
                
                if role == 'manager':
                    cursor.execute("SELECT username FROM users WHERE role = 'manager' AND province = ?", (province,))
                    existing = cursor.fetchone()
                    if existing:
                        QMessageBox.warning(dialog, "Error", f"Province already has manager: {existing[0]}")
                        conn.close()
                        return
                
                cursor.execute("INSERT ager' and not province:
                QMessageBox.warning(dialog, "Error", "Province required for managers!")
                return
            
            try:
                conn = sqlite3.connect(self.db_path)
                cursor = conn.cursor()
                
                cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
                if cursor.fetchone():
                    QMessageBox.warning(dialog, "Error", "Username already exists!")
                    conn.close()      form_card.layout.addLayout(form_grid)
        
        def create_user():
            username = username_input.text().strip()
            password = password_input.text()
            role = role_combo.currentText()
            province = province_combo.currentText() if role == 'manager' else None
            
            if not username or not password:
                QMessageBox.warning(dialog, "Error", "Username and password required!")
                return
            
            if role == 'manpital", "Preah Vihear Province",
            "Prey Veng Province", "Pursat Province", "Ratanak Kiri Province",
            "Siemreap Province", "Preah Sihanouk Province", "Stung Treng Province",
            "Svay Rieng Province", "Takeo Province", "Oddar Meanchey Province",
            "Kep Province", "Pailin Province", "Tboung Khmum Province"
        ]
        province_combo.addItems(provinces)
        form_grid.addWidget(QLabel("Province:"), 1, 2)
        form_grid.addWidget(province_combo, 1, 3)
        
  ser", "manager"])
        form_grid.addWidget(QLabel("Role:"), 1, 0)
        form_grid.addWidget(role_combo, 1, 1)
        
        province_combo = StyledComboBox()
        provinces = [""] + [
            "Banteay Meanchey Province", "Battambang Province", "Kampong Cham Province",
            "Kampong Chhnang Province", "Kampong Speu Province", "Kampong Thom Province",
            "Kampot Province", "Kandal Province", "Koh Kong Province", "Kratie Province",
            "Mondul Kiri Province", "Phnom Penh Ca   form_grid.setSpacing(15)
        
        username_input = StyledLineEdit("Username", "👤")
        form_grid.addWidget(QLabel("Username:"), 0, 0)
        form_grid.addWidget(username_input, 0, 1)
        
        password_input = StyledLineEdit("Password", "🔒")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_grid.addWidget(QLabel("Password:"), 0, 2)
        form_grid.addWidget(password_input, 0, 3)
        
        role_combo = StyledComboBox()
        role_combo.addItems(["u255, 255, 255, 0.3);
            }
        """)
        close_btn.clicked.connect(dialog.close)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        title_layout.addWidget(close_btn)
        
        layout.addWidget(title_bar)
        
        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_layout.setSpacing(20)
        
        # Create form
        form_card = ModernCard("➕ Create New User")
        form_grid = QGridLayout()
     ut.addWidget(title)
        
        title_layout.addStretch()
        
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(40, 40)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.2);
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 18px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(le bar
        title_bar = QFrame()
        title_bar.setFixedHeight(60)
        title_bar.setStyleSheet("""
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop:0 #FF9800, stop:1 #F57C00);
        """)
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(20, 0, 20, 0)
        
        title = QLabel("👥 User Management")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background: transparent;")
        title_layoages:
            self.current_page += 1
            self.search_people()
    
    def show_users_dialog(self):
        """Show beautiful user management"""
        dialog = QDialog(self)
        dialog.setWindowTitle("User Management")
        dialog.setMinimumSize(1000, 650)
        dialog.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        dialog.setStyleSheet("background-color: #F0F2F5;")
        
        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Tit
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
        if self.current_page > 1:
            self.current_page -= 1
            self.search_people()
    
    def next_page(self):
        if self.current_page < self.total_p