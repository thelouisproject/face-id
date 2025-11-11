#!/bin/bash

# Face Recognition System - Easy Setup Script
# This script will set up everything automatically

echo "🔐 Face Recognition System - Setup Script"
echo "========================================="
echo ""

# Check if conda is installed
if ! command -v conda &> /dev/null; then
    echo "❌ Conda is not installed or not in PATH."
    echo "Please install Miniconda first from: https://docs.conda.io/en/latest/miniconda.html"
    exit 1
fi

echo "✅ Conda found!"

# Create the environment
echo "📦 Creating conda environment 'face-rec' with Python 3.10..."
conda create -n face-rec python=3.10 -y

if [ $? -ne 0 ]; then
    echo "❌ Failed to create conda environment"
    exit 1
fi

echo "✅ Environment created successfully!"

# Activate the environment
echo "🔧 Activating environment..."
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate face-rec

if [ $? -ne 0 ]; then
    echo "❌ Failed to activate environment"
    exit 1
fi

echo "✅ Environment activated!"

# Install requirements
echo "📥 Installing required packages... (this may take 5-10 minutes)"
pip install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Failed to install requirements"
    exit 1
fi

echo "✅ All packages installed successfully!"
echo ""
echo "🎉 Setup completed!"
echo ""
echo "To use the system:"
echo "1. Run: conda activate face-rec"
echo "2. Then run: streamlit run app.py"
echo ""
echo "For more detailed instructions, see README.md"