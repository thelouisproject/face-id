import cv2
import os
import time

def onboard_new_person():
    # 1. Get the person's name
    person_name = input("Enter the name of the person: ")
    if not person_name:
        print("Name cannot be empty.")
        return

    # 2. Create the directory path
    base_dir = "face_recognition_dataset/Original Images"
    person_dir = os.path.join(base_dir, person_name)
    
    # Create the base directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"Created base directory: {base_dir}")

    # Create the person's directory
    if not os.path.exists(person_dir):
        os.makedirs(person_dir)
        print(f"Created directory for {person_name}: {person_dir}")
    else:
        print(f"Directory for {person_name} already exists. Adding new images.")

    # 3. Capture 5 images from the webcam
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    print("\nGet ready to capture 5 images.")
    print("A new window will open. Press 'c' to capture an image.")

    img_count = 0
    while img_count < 5:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Display the resulting frame
        cv2.imshow('Webcam - Press "c" to capture, "q" to quit', frame)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            img_count += 1
            # Create a unique filename
            img_name = f"{person_name}_{int(time.time())}_{img_count}.jpg"
            img_path = os.path.join(person_dir, img_name)
            
            # Save the captured frame
            cv2.imwrite(img_path, frame)
            print(f"Image {img_count}/5 saved to {img_path}")
            
            # Give user feedback
            if img_count < 5:
                print("Great! Get ready for the next one...")
                time.sleep(1)

        elif key == ord('q'):
            print("Quitting capture.")
            break
    
    # 4. Release everything
    print("\nOnboarding complete!")
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    onboard_new_person()
