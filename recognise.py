import cv2
from deepface import DeepFace
import time
import os

def capture_and_check_face():
    # 1. Capture a frame from the webcam
    cap = cv2.VideoCapture(0)
    
    print("Capturing image...")
    time.sleep(1)
    
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        cap.release()
        return
    
    # 2. Save the captured frame to a temporary file
    live_img_path = "_live_frame.jpg"
    cv2.imwrite(live_img_path, frame)
    
    # Release the webcam so Deepface can use it
    cap.release()
    print(f"Image captured and saved to {live_img_path}")
    
    db_path = "face_recognition_dataset/Original Images"
    
    # The first run will be slow because it needs to build the embeddings file.
    # Subsequent runs will be much faster.
    print("Verifying face... This may take a moment.")
    
    try:
        # 3. Use DeepFace.find to check against the database
        # It will automatically use the pickle file for speed after the first run.
        results_dfs = DeepFace.find(
            img_path=live_img_path,
            db_path=db_path,
            model_name="VGG-Face",
            detector_backend="mtcnn",
            enforce_detection=False,
            silent=True  # Add this to suppress verbose logging
        )
        
        # The result is a list of pandas DataFrames. We are interested in the first one.
        if results_dfs and not results_dfs[0].empty:
            df = results_dfs[0]
            
            # Sort by distance to find the best match
            df = df.sort_values(by="distance", ascending=True)
            top_match = df.iloc[0]
            
            identity = top_match['identity']
            distance = top_match["distance"]
            
            # Extract the person's name from the file path
            # e.g., "face_recognition_dataset/Original Images/Israel/israel_123.jpg" -> "Israel"
            person_name = os.path.basename(os.path.dirname(identity))
            
            print("---")
            print(f"✅ Match Found: {person_name} (Distance: {distance:.4f})")
            
            if distance < 0.40:
                print(f"Access Granted: Welcome, {person_name}!")
            else:
                print("Access Denied: Match is not confident enough.")
                
        else:
            print("---")
            print("❌ No match found in the database.")
            print("Access Denied: Person not recognized.")
            
    except Exception as e:
        # Handle cases where no face is found in the live image
        if "Face could not be detected" in str(e):
            print("---")
            print("❌ No face detected in the captured image.")
        else:
            print(f"An error occurred: {e}")
            
if __name__ == "__main__":
    capture_and_check_face()