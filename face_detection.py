import cv2
import os
import time

# Relative path to the Haar Cascade file
cascade_path = "haarcascade_frontalface_default.xml"

# Debug: Verify if the file exists
if not os.path.exists(cascade_path):
    print(f"Error: File not found at {cascade_path}. Ensure the file is in the same folder as the script.")
    exit()

# Load the cascade classifier
face_cap = cv2.CascadeClassifier(cascade_path)

if face_cap.empty():
    print("Error: Failed to load the cascade file. Check the file integrity!")
    exit()

# Welcome message
print("Welcome to Face Detection!")
print("Starting camera... Please wait.")

# Initialize video capture
video_cap = cv2.VideoCapture(0)

if not video_cap.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Countdown before starting
for i in range(3, 0, -1):
    print(f"Starting in {i} seconds...")
    time.sleep(1)

print("Press 'a' to exit the program.")

# Main loop
while True:
    ret, video_data = video_cap.read()
    if not ret:
        print("Error: Failed to capture video frame.")
        break

    # Convert frame to grayscale
    col = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        # Alternate rectangle color
        color = (0, 255, 0) if len(faces) % 2 == 0 else (255, 0, 0)
        cv2.rectangle(video_data, (x, y), (x + w, y + h), color, 2)
  # Add heading at the top of the frame
    cv2.putText(video_data, "Face Detection by Deepanshu Tolani", (50, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display message if no faces are detected
    if len(faces) == 0:
        cv2.putText(video_data, "No faces detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Add instructions to the video feed
    cv2.putText(video_data, "Press 'a' to exit", (10, video_data.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Show the video with detected faces
    cv2.imshow("Face Detection", video_data)

    # Exit the loop if 'a' is pressed
    if cv2.waitKey(10) == ord("a"):
        print("Exiting the program. Goodbye!")
        break

# Release resources
video_cap.release()
cv2.destroyAllWindows()


# cd C:\Users\Dell\Desktop\detection\git
# python face_detection.py
