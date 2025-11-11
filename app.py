import streamlit as st
import pandas as pd
import os
import time
from datetime import datetime
import cv2
from deepface import DeepFace

# --- Page Configuration ---
st.set_page_config(
    page_title="Facial Recognition Security",
    page_icon="🔐",
    layout="wide"
)

# --- Constants and Setup ---
DB_PATH = "face_recognition_dataset/Original Images"
LOG_FILE = "check_in_log.csv"

# --- Helper Functions ---
def initialize_log_file():
    """Creates the log file if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=["Timestamp", "Name", "Status", "Distance"])
        df.to_csv(LOG_FILE, index=False)

def add_log_entry(name, status, distance):
    """Adds a new entry to the log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_entry = pd.DataFrame([[timestamp, name, status, distance]], columns=["Timestamp", "Name", "Status", "Distance"])
    log_df = pd.read_csv(LOG_FILE)
    log_df = pd.concat([log_df, new_entry], ignore_index=True)
    log_df.to_csv(LOG_FILE, index=False)

def capture_and_check_face(placeholder):
    """Captures an image from the webcam and checks for a match."""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Error: Could not open webcam.")
        return

    st.info("Capturing image... Please look at the camera.")
    time.sleep(1)
    ret, frame = cap.read()
    cap.release()

    if not ret:
        st.error("Failed to grab frame from webcam.")
        return

    live_img_path = "_live_frame.jpg"
    cv2.imwrite(live_img_path, frame)
    
    placeholder.image(frame, channels="BGR", caption="Captured Image")

    try:
        st.info("Verifying face... This may take a moment.")
        results_dfs = DeepFace.find(
            img_path=live_img_path,
            db_path=DB_PATH,
            model_name="VGG-Face",
            enforce_detection=False,
            silent=True
        )

        if results_dfs and not results_dfs[0].empty:
            df = results_dfs[0]
            df = df.sort_values(by="distance", ascending=True)
            top_match = df.iloc[0]
            
            identity = top_match['identity']
            distance = top_match["distance"]
            person_name = os.path.basename(os.path.dirname(identity))

            if distance < 0.40:
                status = "Access Granted"
                st.success(f"Welcome, {person_name}! (Distance: {distance:.4f})")
            else:
                status = "Access Denied"
                st.warning(f"Match found for {person_name}, but confidence is too low. (Distance: {distance:.4f})")
            
            add_log_entry(person_name, status, f"{distance:.4f}")
        else:
            st.error("No match found in the database. Access Denied.")
            add_log_entry("Unknown", "Access Denied", "N/A")

    except Exception as e:
        st.error(f"An error occurred during face verification: {e}")
    finally:
        if os.path.exists(live_img_path):
            os.remove(live_img_path)

def onboard_new_person(person_name, uploaded_files):
    """Onboards a new person using uploaded images."""
    if not person_name:
        st.error("Please enter a name for the person.")
        return
    if not uploaded_files:
        st.error("Please upload at least one image.")
        return

    person_dir = os.path.join(DB_PATH, person_name)
    os.makedirs(person_dir, exist_ok=True)

    for i, uploaded_file in enumerate(uploaded_files):
        file_path = os.path.join(person_dir, f"{person_name}_{i+1}.jpg")
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
    
    st.success(f"Successfully onboarded {person_name} with {len(uploaded_files)} images.")
    # Force a re-scan of the directory on the next check-in
    pickle_file = os.path.join(DB_PATH, "representations_vgg_face.pkl")
    if os.path.exists(pickle_file):
        os.remove(pickle_file)
        st.info("Embeddings cache cleared. The next check-in will rebuild it.")

# --- Streamlit UI ---
st.title("🔐 Facial Recognition Door Lock System")

# Initialize log file
initialize_log_file()

# --- Main Layout ---
col1, col2 = st.columns([2, 1])

with col1:
    st.header("Live Security Feed")
    
    if st.button("Activate Door Camera & Check-In"):
        image_placeholder = st.empty()
        capture_and_check_face(image_placeholder)

    st.header("Check-In Log")
    log_df = pd.read_csv(LOG_FILE)
    st.dataframe(log_df.sort_values(by="Timestamp", ascending=False), use_container_width=True)
    
    if st.button("Refresh Log"):
        st.rerun()

with col2:
    st.header("System Management")
    with st.expander("Onboard New Person", expanded=False):
        with st.form("onboard_form", clear_on_submit=True):
            new_person_name = st.text_input("Person's Name")
            uploaded_images = st.file_uploader(
                "Upload Images (5 recommended)", 
                accept_multiple_files=True, 
                type=['jpg', 'jpeg', 'png']
            )
            submitted = st.form_submit_button("Onboard Person")

            if submitted:
                onboard_new_person(new_person_name, uploaded_images)
