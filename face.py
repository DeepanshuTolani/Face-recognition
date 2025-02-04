
import cv2

# Initialize video capture
video_cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not video_cap.isOpened():
    print("Error: Could not open camera.")
else:
    while True:
        ret, video_data = video_cap.read()

        # Check if frame is captured successfully
        if ret:
            cv2.imshow("video_live", video_data)
        else:
            print("Error: Failed to capture video frame.")

        # Break loop if 'a' is pressed
        if cv2.waitKey(10) == ord("a"):
            break

    # Release the video capture object
    video_cap.release()
    cv2.destroyAllWindows()
