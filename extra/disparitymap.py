import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load left and right images (grayscale)
left_img = cv2.imread("screenshots/left_eye.png", cv2.IMREAD_GRAYSCALE)
right_img = cv2.imread("screenshots/right_eye.png", cv2.IMREAD_GRAYSCALE)

# Create StereoBM object
stereo = cv2.StereoBM_create(
    numDisparities=64, blockSize=15
)  # Adjust parameters as needed

# Compute disparity map
disparity = stereo.compute(left_img, right_img)

# Normalize for visualization
disparity = cv2.normalize(disparity, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
disparity = np.uint8(disparity)

# Define thresholds for depth segmentation
min_disp = disparity.min()
max_disp = disparity.max()
fg_thresh = min_disp + (max_disp - min_disp) * 0.7  # Foreground threshold
mg_thresh = min_disp + (max_disp - min_disp) * 0.4  # Midground threshold

# Classify depth into foreground, midground, and background
depth_map = np.zeros_like(disparity)

depth_map[disparity >= fg_thresh] = 255  # Foreground (White)
depth_map[(disparity < fg_thresh) & (disparity >= mg_thresh)] = 150  # Midground (Gray)
depth_map[disparity < mg_thresh] = 50  # Background (Dark)

# Display results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("Disparity Map")
plt.imshow(disparity, cmap="gray")

plt.subplot(1, 2, 2)
plt.title("Depth Segmentation")
plt.imshow(depth_map, cmap="gray")

plt.show()
