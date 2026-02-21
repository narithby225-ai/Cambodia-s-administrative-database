"""
CLEAN COOL GUI - People Database Management
Beautiful login without QPainter issues
"""
import sys
import sqlite3
from datetime import datetime
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from werkzeug.security import check_password_hash, generate_password_hash

# Import MainWindow from gui_pyqt6
from gui_pyqt6 import MainWindow


class CoolButton(QPushButton):
    """Beautiful button with hover effect"""
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        
        self.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
                border: none;
                border-radius: 25px;
                padding: 15px 40px;
                font-size: 16px;
                font-weight: bold;
                min-width: 200px;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #764ba2, stop:1 #667eea);
            }
            QPushButton:pressed {
                padding-top: 17px;
            }
        """)
        
        self.setCursor(Qt.CursorShape.PointingHandCursor)


class CoolLineEdit(QLineEdit):
    """Modern input field"""
    def __init__(self, placeholder="", icon="", parent=None):
        super().__init__(parent)
        
        self.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 2px solid rgba(255, 255, 255, 0.3);
                background: transparent;
                color: white;
                padding: 12px 10px;
                font-size: 16px;
                min-width: 450px;
            }
            QLineEdit:focus {
                border-bottom: 2px solid white;
            }
            QLineEdit::placeholder {
                color: rgba(255, 255, 255, 0.5);
            }
        """)
        
        self.setPlaceholderText(f"{icon} {placeholder}")
        self.setMinimumHeight(45)


class CoolLoginWindow(QDialog):
    """Clean cool login window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setFixedSize(600, 700)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.user_data = None
        self.db_path = 'instance/people.db'
        
        self.setup_ui()
        
        # Entrance animation
        self.setWindowOpacity(0)
        self.fade_in = QTimer()
        self.fade_in.timeout.connect(self.animate_entrance)
        self.opacity_value = 0
        self.fade_in.start(20)
    
    def animate_entrance(self):
        """Smooth fade in"""
        self.opacity_value += 0.05
        self.setWindowOpacity(self.opacity_value)
        if self.opacity_value >= 1:
            self.fade_in.stop()
    
    def setup_ui(self):
        """Setup beautiful UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Container
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f0c29, stop:0.5 #302b63, stop:1 #24243e);
                border-radius: 30px;
            }
        """)
        
        layout = QVBoxLayout(container)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(30)
        
        # Close button
        close_btn = QPushButton("✕")
        close_btn.setFixedSize(40, 40)
        close_btn.setStyleSheet("""
            QPushButton {
                background-color: rgba(255, 255, 255, 0.1);
                color: white;
                border: none;
                border-radius: 20px;
                font-size: 20px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: rgba(255, 100, 100, 0.8);
            }
        """)
        close_btn.clicked.connect(self.reject)
        close_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        close_btn.setParent(container)
        close_btn.move(540, 10)
        
        # Logo
        logo_container = QWidget()
        logo_layout = QVBoxLayout(logo_container)
        logo_layout.setSpacing(10)
        
        icon_label = QLabel("👥")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("font-size: 80px; background: transparent;")
        logo_layout.addWidget(icon_label)
        
        title = QLabel("People Database")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        logo_layout.addWidget(title)
        
        subtitle = QLabel("Management System")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("""
            font-size: 18px;
            color: rgba(255, 255, 255, 0.7);
            background: transparent;
            letter-spacing: 2px;
        """)
        logo_layout.addWidget(subtitle)
        
        layout.addWidget(logo_container)
        layout.addSpacing(20)
        
        # Form
        form_widget = QWidget()
        form_widget.setStyleSheet("background: transparent;")
        form_layout = QVBoxLayout(form_widget)
        form_layout.setSpacing(25)
        
        welcome = QLabel("Welcome Back!")
        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        form_layout.addWidget(welcome)
        
        # Username
        self.username_input = CoolLineEdit("Username", "👤")
        form_layout.addWidget(self.username_input)
        
        # Password
        self.password_input = CoolLineEdit("Password", "🔒")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(self.password_input)
        
        # Show password
        show_pass_container = QWidget()
        show_pass_container.setStyleSheet("background: transparent;")
        show_pass_layout = QHBoxLayout(show_pass_container)
        show_pass_layout.setContentsMargins(0, 0, 0, 0)
        
        self.show_pass_check = QCheckBox("Show password")
        self.show_pass_check.setStyleSheet("""
            QCheckBox {
                color: rgba(255, 255, 255, 0.8);
                font-size: 13px;
                background: transparent;
            }
            QCheckBox::indicator {
                width: 20px;
                height: 20px;
                border-radius: 4px;
                border: 2px solid rgba(255, 255, 255, 0.5);
                background: transparent;
            }
            QCheckBox::indicator:checked {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                border-color: #667eea;
            }
        """)
        self.show_pass_check.toggled.connect(lambda checked: 
            self.password_input.setEchoMode(
                QLineEdit.EchoMode.Normal if checked else QLineEdit.EchoMode.Password
            ))
        show_pass_layout.addWidget(self.show_pass_check)
        show_pass_layout.addStretch()
        
        form_layout.addWidget(show_pass_container)
        
        layout.addWidget(form_widget)
        layout.addSpacing(10)
        
        # Login button
        self.login_btn = CoolButton("🚀 LOGIN")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Info
        info = QLabel("💡 Default: admin / super123")
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setStyleSheet("""
            color: rgba(255, 255, 255, 0.6);
            font-size: 13px;
            background: transparent;
            padding: 10px;
        """)
        layout.addWidget(info)
        
        # Version
        version = QLabel("v2.0 • Clean Cool Edition")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version.setStyleSheet("""
            color: rgba(255, 255, 255, 0.4);
            font-size: 11px;
            background: transparent;
        """)
        layout.addWidget(version)
        
        main_layout.addWidget(container)
        
        # Connect Enter
        self.password_input.returnPressed.connect(self.login)
        self.username_input.returnPressed.connect(self.login)
        
        QTimer.singleShot(100, self.username_input.setFocus)
    
    def login(self):
        """Authenticate"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        # Check if fields are empty
        if not username or not password:
            self.shake()
            self.show_error_message("⚠️ Please fill in all fields", 
                                   "Both username and password are required!")
            # Focus on the empty field
            if not username:
                self.username_input.setFocus()
            else:
                self.password_input.setFocus()
            return
        
        self.login_btn.setText("⏳ Logging in...")
        self.login_btn.setEnabled(False)
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
                
                # Success
                self.login_btn.setText("✅ Success!")
                self.login_btn.setStyleSheet("""
                    QPushButton {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                            stop:0 #11998e, stop:1 #38ef7d);
                        color: white;
                        border: none;
                        border-radius: 25px;
                        padding: 15px 40px;
                        font-size: 16px;
                        font-weight: bold;
                    }
                """)
                QTimer.singleShot(500, self.fade_out)
            else:
                # Wrong credentials - don't close, just show message
                self.setCursor(Qt.CursorShape.ArrowCursor)
                self.login_btn.setText("🚀 LOGIN")
                self.login_btn.setEnabled(True)
                self.shake()
                
                # Show error button color temporarily
                self.login_btn.setStyleSheet("""
                    QPushButton {
                        background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                            stop:0 #eb3349, stop:1 #f45c43);
                        color: white;
                        border: none;
                        border-radius: 25px;
                        padding: 15px 40px;
                        font-size: 16px;
                        font-weight: bold;
                    }
                """)
                
                # Show error message (non-blocking)
                self.show_error_message("❌ Login Failed", 
                                       "Invalid username or password!\nPlease try again.")
                
                # Reset button color after 1 second
                QTimer.singleShot(1000, self.reset_button_style)
                
                # Clear password and focus
                self.password_input.clear()
                self.password_input.setFocus()
                
        except Exception as e:
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self.login_btn.setText("🚀 LOGIN")
            self.login_btn.setEnabled(True)
            self.show_error_message("⚠️ Database Error", 
                                   f"Could not connect to database:\n{str(e)}\n\nPlease run: python init_db.py")
            # Focus back to username for retry
            self.username_input.setFocus()
    
    def show_error_message(self, title, message):
        """Show error message without blocking"""
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.setStyleSheet("""
            QMessageBox {
                background-color: #2d2d2d;
            }
            QMessageBox QLabel {
                color: white;
                font-size: 14px;
            }
            QPushButton {
                background-color: #667eea;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 8px 20px;
                font-size: 13px;
                min-width: 80px;
            }
            QPushButton:hover {
                background-color: #764ba2;
            }
        """)
        msg.exec()
    
    def reset_button_style(self):
        """Reset button to normal style"""
        self.login_btn.setStyleSheet("""
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #667eea, stop:1 #764ba2);
                color: white;
                border: none;
                border-radius: 25px;
                padding: 15px 40px;
                font-size: 16px;
                font-weight: bold;
            }
        """)
    
    def shake(self):
        """Shake animation"""
        animation = QPropertyAnimation(self, b"pos")
        animation.setDuration(500)
        
        pos = self.pos()
        animation.setKeyValueAt(0, pos)
        animation.setKeyValueAt(0.1, pos + QPoint(-10, 0))
        animation.setKeyValueAt(0.2, pos + QPoint(10, 0))
        animation.setKeyValueAt(0.3, pos + QPoint(-10, 0))
        animation.setKeyValueAt(0.4, pos + QPoint(10, 0))
        animation.setKeyValueAt(0.5, pos)
        
        animation.start()
    
    def fade_out(self):
        """Fade out on success"""
        self.fade_out_timer = QTimer()
        self.fade_out_timer.timeout.connect(self.animate_fade_out)
        self.fade_out_timer.start(20)
    
    def animate_fade_out(self):
        """Animate fade out"""
        self.opacity_value -= 0.05
        self.setWindowOpacity(self.opacity_value)
        if self.opacity_value <= 0:
            self.fade_out_timer.stop()
            self.accept()


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    login = CoolLoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:
        # Open main application window
        main_window = MainWindow(login.user_data)
        main_window.show()
        sys.exit(app.exec())


if __name__ == '__main__':
    main()
