@echo off
cls
echo.
echo ========================================
echo   ULTIMATE People Database Manager
echo   The Most Beautiful Version!
echo ========================================
echo.
echo Starting the ultimate GUI...
echo.
python gui_ultimate.py
if errorlevel 1 (
    echo.
    echo Error starting application!
    echo.
    echo Make sure PyQt6 is installed:
    echo pip install PyQt6
    echo.
)
pause
