@echo off
REM Face Recognition System - Easy Setup Script for Windows
REM This script will set up everything automatically

echo 🔐 Face Recognition System - Setup Script
echo =========================================
echo.

REM Check if conda is installed
conda --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Conda is not installed or not in PATH.
    echo Please install Miniconda first from: https://docs.conda.io/en/latest/miniconda.html
    pause
    exit /b 1
)

echo ✅ Conda found!

REM Create the environment
echo 📦 Creating conda environment 'face-rec' with Python 3.10...
conda create -n face-rec python=3.10 -y

if errorlevel 1 (
    echo ❌ Failed to create conda environment
    pause
    exit /b 1
)

echo ✅ Environment created successfully!

REM Activate the environment
echo 🔧 Activating environment...
call conda activate face-rec

if errorlevel 1 (
    echo ❌ Failed to activate environment
    pause
    exit /b 1
)

echo ✅ Environment activated!

REM Install requirements
echo 📥 Installing required packages... (this may take 5-10 minutes)
pip install -r requirements.txt

if errorlevel 1 (
    echo ❌ Failed to install requirements
    pause
    exit /b 1
)

echo ✅ All packages installed successfully!
echo.
echo 🎉 Setup completed!
echo.
echo To use the system:
echo 1. Open Anaconda Prompt or Command Prompt
echo 2. Run: conda activate face-rec
echo 3. Navigate to this folder: cd path\to\Face_Recognition
echo 4. Then run: streamlit run app.py
echo.
echo For more detailed instructions, see README.md
pause