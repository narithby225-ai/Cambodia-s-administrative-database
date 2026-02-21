"""
Build standalone executable for the GUI application
Requires: pip install pyinstaller
"""
import os
import subprocess

def build_executable():
    """Build standalone .exe file"""
    
    print("Building standalone executable...")
    print("This may take a few minutes...\n")
    
    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--onefile',  # Single executable file
        '--windowed',  # No console window
        '--name=PeopleDatabaseManager',
        '--icon=NONE',  # Add icon file path if you have one
        '--add-data=instance;instance',  # Include database folder
        'gui_app.py'
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print("\n✅ Build complete!")
        print("📁 Executable location: dist/PeopleDatabaseManager.exe")
        print("\nTo distribute:")
        print("1. Copy dist/PeopleDatabaseManager.exe")
        print("2. Copy instance/ folder (with database)")
        print("3. Users can run the .exe directly without Python installed")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Build failed: {e}")
        print("\nMake sure PyInstaller is installed:")
        print("pip install pyinstaller")
    except FileNotFoundError:
        print("\n❌ PyInstaller not found!")
        print("\nInstall it with:")
        print("pip install pyinstaller")

if __name__ == '__main__':
    build_executable()
