import cv2
import os

# Path to the video file
video_path = r"C:\Users\Gokalp\Downloads\data2 (1).MOV"

# Create a directory to save the frames
output_dir = 'frames'
os.makedirs(output_dir, exist_ok=True)

# Open the video
video = cv2.VideoCapture(video_path)

frame_count = 0
success = True

while success:
    # Read frame-by-frame
    success, frame = video.read()

    if success:
        # Save each frame as a JPEG file
        frame_path = os.path.join(output_dir, f'frame_{frame_count:04d}.jpg')
        cv2.imwrite(frame_path, frame)
        frame_count += 1

# Release the video object
video.release()

print(f'Total frames captured: {frame_count}')
