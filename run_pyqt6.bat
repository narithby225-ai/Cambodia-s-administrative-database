@echo off
echo ========================================
echo  People Database Management System
echo  Modern PyQt6 GUI Version
echo ========================================
echo.
echo Starting application...
echo.
python gui_pyqt6.py
if errorlevel 1 (
    echo.
    echo Error: Failed to start application
    echo.
    echo Make sure PyQt6 is installed:
    echo pip install PyQt6
    echo.
)
pause
