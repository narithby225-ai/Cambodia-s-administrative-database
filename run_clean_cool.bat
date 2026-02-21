@echo off
cls
echo.
echo ========================================
echo   CLEAN COOL LOGIN - NO ERRORS!
echo   Beautiful and Bug-Free
echo ========================================
echo.
echo Starting the perfect login...
echo.
python gui_clean_cool.py
if errorlevel 1 (
    echo.
    echo Error occurred!
    echo.
) else (
    echo.
    echo Closed successfully!
)
pause
