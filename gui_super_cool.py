"""
SUPER COOL GUI - People Database Management
The Most Amazing Login Screen Ever!
"""
import sys
import sqlite3
import random
from datetime import datetime
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from werkzeug.security import check_password_hash, generate_password_hash

# Ensure pyqtProperty is available
try:
    from PyQt6.QtCore import pyqtProperty
except ImportError:
    from PyQt6.QtCore import Property as pyqtProperty


class GlowingButton(QPushButton):
    """Button with glowing effect"""
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
        
        # Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setColor(QColor(102, 126, 234, 150))
        shadow.setOffset(0, 5)
        self.setGraphicsEffect(shadow)


class ModernLineEdit(QLineEdit):
    """Modern input with floating label"""
    def __init__(self, placeholder="", icon="", parent=None):
        super().__init__(parent)
        self.placeholder_text = placeholder
        self.icon_text = icon
        
        self.setStyleSheet("""
            QLineEdit {
                border: none;
                border-bottom: 2px solid rgba(255, 255, 255, 0.3);
                background: transparent;
                color: white;
                padding: 12px 5px;
                font-size: 15px;
            }
            QLineEdit:focus {
                border-bottom: 2px solid white;
            }
        """)
        
        self.setPlaceholderText(f"{icon} {placeholder}")
        
        # Animation for focus
        self.focus_animation = QPropertyAnimation(self, b"geometry")
        self.focus_animation.setDuration(200)
    
    def focusInEvent(self, event):
        """Animate on focus"""
        super().focusInEvent(event)
        # Add subtle scale effect
        
    def focusOutEvent(self, event):
        """Animate on blur"""
        super().focusOutEvent(event)


class CoolLoginWindow(QDialog):
    """Super cool animated login window"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Login")
        self.setFixedSize(600, 750)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        self.user_data = None
        self.db_path = 'instance/people.db'
        
        self.setup_ui()
        
        # Entrance animation
        self.opacity = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self.opacity)
        
        self.fade_in = QPropertyAnimation(self.opacity, b"opacity")
        self.fade_in.setDuration(800)
        self.fade_in.setStartValue(0)
        self.fade_in.setEndValue(1)
        self.fade_in.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.fade_in.start()
        
        # Scale animation
        self.scale_animation = QPropertyAnimation(self, b"geometry")
        self.scale_animation.setDuration(800)
        start_rect = QRect(150, 175, 300, 400)
        end_rect = QRect(0, 0, 600, 750)
        self.scale_animation.setStartValue(start_rect)
        self.scale_animation.setEndValue(end_rect)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
    
    def setup_ui(self):
        """Setup the amazing UI"""
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Background container
        container = QFrame()
        container.setStyleSheet("""
            QFrame {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #0f0c29, stop:0.5 #302b63, stop:1 #24243e);
                border-radius: 30px;
            }
        """)
        
        # Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(40)
        shadow.setColor(QColor(0, 0, 0, 180))
        shadow.setOffset(0, 10)
        container.setGraphicsEffect(shadow)
        
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
        
        # Position close button
        close_btn.setParent(container)
        close_btn.move(540, 10)
        
        # Animated logo
        logo_container = QWidget()
        logo_layout = QVBoxLayout(logo_container)
        logo_layout.setSpacing(10)
        
        # Icon with glow
        icon_label = QLabel("👥")
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("""
            font-size: 80px;
            background: transparent;
        """)
        
        # Glow effect for icon
        icon_glow = QGraphicsDropShadowEffect()
        icon_glow.setBlurRadius(30)
        icon_glow.setColor(QColor(102, 126, 234, 200))
        icon_glow.setOffset(0, 0)
        icon_label.setGraphicsEffect(icon_glow)
        
        logo_layout.addWidget(icon_label)
        
        # Title with gradient
        title = QLabel("People Database")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("""
            font-size: 36px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        logo_layout.addWidget(title)
        
        # Subtitle
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
        
        # Login form
        form_widget = QWidget()
        form_widget.setStyleSheet("background: transparent;")
        form_layout = QVBoxLayout(form_widget)
        form_layout.setSpacing(25)
        
        # Welcome text
        welcome = QLabel("Welcome Back!")
        welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: white;
            background: transparent;
        """)
        form_layout.addWidget(welcome)
        
        # Username input
        self.username_input = ModernLineEdit("Username", "👤")
        form_layout.addWidget(self.username_input)
        
        # Password input
        self.password_input = ModernLineEdit("Password", "🔒")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        form_layout.addWidget(self.password_input)
        
        # Show password toggle
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
        self.login_btn = GlowingButton("🚀 LOGIN")
        self.login_btn.clicked.connect(self.login)
        layout.addWidget(self.login_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Info text
        info = QLabel("💡 Default: admin / admin123")
        info.setAlignment(Qt.AlignmentFlag.AlignCenter)
        info.setStyleSheet("""
            color: rgba(255, 255, 255, 0.6);
            font-size: 13px;
            background: transparent;
            padding: 10px;
        """)
        layout.addWidget(info)
        
        # Version
        version = QLabel("v2.0 • Super Cool Edition")
        version.setAlignment(Qt.AlignmentFlag.AlignCenter)
        version.setStyleSheet("""
            color: rgba(255, 255, 255, 0.4);
            font-size: 11px;
            background: transparent;
        """)
        layout.addWidget(version)
        
        main_layout.addWidget(container)
        
        # Connect Enter key
        self.password_input.returnPressed.connect(self.login)
        self.username_input.returnPressed.connect(self.login)
        
        # Focus
        QTimer.singleShot(100, self.username_input.setFocus)
    
    def login(self):
        """Authenticate with cool animations"""
        username = self.username_input.text().strip()
        password = self.password_input.text()
        
        if not username or not password:
            self.shake_animation()
            QMessageBox.warning(self, "Error", "Please enter username and password")
            return
        
        # Show loading
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
                
                # Success animation
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
                self.setCursor(Qt.CursorShape.ArrowCursor)
                self.login_btn.setText("🚀 LOGIN")
                self.login_btn.setEnabled(True)
                self.shake_animation()
                
                # Error animation
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
                QTimer.singleShot(1000, lambda: self.login_btn.setStyleSheet("""
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
                """))
                
                QMessageBox.critical(self, "Login Failed", "❌ Invalid username or password")
                self.password_input.clear()
                self.password_input.setFocus()
        except Exception as e:
            self.setCursor(Qt.CursorShape.ArrowCursor)
            self.login_btn.setText("🚀 LOGIN")
            self.login_btn.setEnabled(True)
            QMessageBox.critical(self, "Database Error", f"Error:\n{str(e)}")
    
    def shake_animation(self):
        """Shake animation for error"""
        animation = QPropertyAnimation(self, b"pos")
        animation.setDuration(500)
        animation.setLoopCount(2)
        
        pos = self.pos()
        animation.setKeyValueAt(0, pos)
        animation.setKeyValueAt(0.09, pos + QPoint(-15, 0))
        animation.setKeyValueAt(0.18, pos + QPoint(15, 0))
        animation.setKeyValueAt(0.27, pos + QPoint(-15, 0))
        animation.setKeyValueAt(0.36, pos + QPoint(15, 0))
        animation.setKeyValueAt(0.45, pos)
        
        animation.start()
    
    def fade_out(self):
        """Fade out on success"""
        animation = QPropertyAnimation(self.opacity, b"opacity")
        animation.setDuration(400)
        animation.setStartValue(1)
        animation.setEndValue(0)
        animation.setEasingCurve(QEasingCurve.Type.InCubic)
        animation.finished.connect(self.accept)
        animation.start()


# Rest of the application code from gui_pyqt6.py would go here
# For now, let's create a simple test

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    login = CoolLoginWindow()
    if login.exec() == QDialog.DialogCode.Accepted:
        # Here you would launch the main window
        QMessageBox.information(None, "Success", f"Logged in as: {login.user_data['username']}")
    
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
