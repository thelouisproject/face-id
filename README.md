# Face Recognition Security System 🔐

A complete face recognition system that can identify people from a webcam feed and log their check-ins. This system includes a web interface for easy use and an onboarding system to add new people.

## 📋 What This System Does

- **Onboard New People**: Capture photos of new people and add them to the system
- **Real-time Face Recognition**: Identify people using your webcam
- **Web Interface**: Easy-to-use web application for face recognition
- **Logging**: Keep track of who was recognized and when

## 🛠️ Setup Instructions (Step-by-Step)

### Step 1: Install Python and Conda

First, you need to install Python and Conda on your computer.

#### For Windows:
1. Go to https://docs.conda.io/en/latest/miniconda.html
2. Download "Miniconda3 Windows 64-bit" installer
3. Run the installer and follow the instructions
4. **Important**: Check the box "Add Miniconda3 to my PATH environment variable" during installation

#### For Mac:
1. Go to https://docs.conda.io/en/latest/miniconda.html
2. Download "Miniconda3 macOS Intel x86 64-bit pkg" (or Apple M1 if you have a newer Mac)
3. Run the installer and follow the instructions

#### For Linux:
1. Go to https://docs.conda.io/en/latest/miniconda.html
2. Download "Miniconda3 Linux 64-bit" installer
3. Open terminal and run: `bash Miniconda3-latest-Linux-x86_64.sh`

### Step 2: Open Terminal/Command Prompt

#### Windows:
- Press `Windows key + R`
- Type `cmd` and press Enter
- OR search for "Anaconda Prompt" in the Start menu

#### Mac:
- Press `Cmd + Space`
- Type "Terminal" and press Enter

#### Linux:
- Press `Ctrl + Alt + T`

### Step 3: Navigate to the Project Folder

In the terminal, you need to go to where you saved this project folder. Use the `cd` command:

```bash
# Replace "path/to/Face_Recognition" with the actual path to your project folder
# Example for Windows: cd C:\Users\YourName\Desktop\Face_Recognition
# Example for Mac: cd /Users/YourName/Desktop/Face_Recognition
# Example for Linux: cd /home/YourName/Desktop/Face_Recognition

cd path/to/Face_Recognition
```

**Tip**: You can often drag and drop the folder into the terminal to get the correct path!

### Step 4: Create the Conda Environment

Copy and paste this command into your terminal and press Enter:

```bash
conda create -n face-rec python=3.10 -y
```

This creates a new isolated environment called "face-rec" with Python 3.10.

### Step 5: Activate the Environment

```bash
conda activate face-rec
```

You should see `(face-rec)` appear at the beginning of your terminal prompt. This means you're now working in the face-rec environment.

### Step 6: Install Required Packages

Now install all the necessary packages by running:

```bash
pip install -r requirements.txt
```

**Note**: This might take 5-10 minutes as it downloads and installs several packages including TensorFlow and OpenCV.

### Step 7: Test Your Webcam

Make sure your webcam is working and not being used by other applications (like Zoom, Skype, etc.).

## 🚀 How to Use the System

### Option 1: Using the Web Interface (Recommended for Beginners)

1. **Start the web application**:
   ```bash
   streamlit run app.py
   ```

2. **Open your web browser**: 
   - The terminal will show a URL like `http://localhost:8501`
   - Click on it or copy-paste it into your web browser

3. **Use the interface**:
   - The web page will load with options for face recognition
   - Follow the on-screen instructions

### Option 2: Using Individual Scripts

#### To Add New People to the System:

1. **Run the onboarding script**:
   ```bash
   python onboard.py
   ```

2. **Follow the prompts**:
   - Type the person's name when asked
   - A webcam window will open
   - Press 'c' to capture each photo (you need 5 photos total)
   - Press 'q' when done

#### To Test Face Recognition:

1. **Run the recognition script**:
   ```bash
   python recognise.py
   ```

2. **The system will**:
   - Capture your photo automatically
   - Try to match it against known faces
   - Show the results in the terminal

## 📁 Project Structure

```
Face_Recognition/
├── app.py                          # Main web application
├── onboard.py                      # Script to add new people
├── recognise.py                    # Script to test face recognition
├── requirements.txt                # List of required packages
├── README.md                       # This file
├── check_in_log.csv               # Log of recognitions (created automatically)
└── face_recognition_dataset/       # Database folder
    ├── Dataset.csv                # Dataset information
    ├── Faces/                     # Processed face data
    └── Original Images/           # Photos of people
        ├── Person1/               # Folder for each person
        ├── Person2/
        └── ...
```

## 🔧 Troubleshooting

### Common Issues and Solutions

#### 1. "conda: command not found" or "python: command not found"
**Solution**: Restart your terminal after installing Miniconda, or add Conda to your PATH.

#### 2. Webcam not working
**Solutions**:
- Make sure no other applications are using your webcam
- Check if your webcam privacy settings allow the application to access it
- Try unplugging and reconnecting external webcams

#### 3. "ModuleNotFoundError" when running scripts
**Solution**: Make sure you activated the conda environment:
```bash
conda activate face-rec
```

#### 4. Installation takes too long or fails
**Solutions**:
- Check your internet connection
- Try installing packages one by one if the batch installation fails:
  ```bash
  pip install streamlit
  pip install pandas
  pip install opencv-python
  pip install deepface
  ```

#### 5. Web application won't start
**Solution**: 
- Make sure no other application is using port 8501
- Try running: `streamlit run app.py --server.port 8502`

### Getting Help

If you encounter issues:

1. **Check the terminal output** - error messages often contain helpful information
2. **Make sure you're in the right folder** - use `pwd` (Mac/Linux) or `cd` (Windows) to check
3. **Verify the environment is activated** - you should see `(face-rec)` in your terminal prompt
4. **Restart everything** - sometimes a fresh start helps:
   ```bash
   conda deactivate
   conda activate face-rec
   ```

## 📝 Usage Tips

1. **For best recognition results**:
   - Ensure good lighting when taking photos
   - Take photos from different angles during onboarding
   - Look directly at the camera

2. **Managing the system**:
   - The system automatically saves logs in `check_in_log.csv`
   - You can view/edit this file with Excel or any text editor
   - To remove someone, delete their folder from `face_recognition_dataset/Original Images/`

3. **Performance**:
   - The first recognition might be slow (building face embeddings)
   - Subsequent recognitions will be much faster
   - Close other applications if the system runs slowly

## 🔒 Privacy and Security

- All face data is stored locally on your computer
- No data is sent to external servers
- You can delete anyone's data by removing their folder from the `Original Images` directory

## 📞 Support

If you have questions or need help:
1. Check the troubleshooting section above
2. Make sure you followed all steps in order
3. Contact the person who shared this project with you

---

**Note**: This system requires a working webcam and good lighting conditions for optimal performance.