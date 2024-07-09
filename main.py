import coding
import cv2
import numpy as np
import os

encode_session = coding.CodingInstance()

encode_session.Encode('test_file2.txt', 8, (1920, 1080), 1)


"""
def create_block_image(img_dim, block_size, colors):

    num_blocks_vertical = img_dim[0] // block_size[0]
    num_blocks_horizontal = img_dim[1] // block_size[1]

    # Initialize the image with zeros (black image)
    image = np.zeros((img_dim[0], img_dim[1], 3), dtype=np.uint8)

    # Assign colors to blocks
    color_index = 0
    for i in range(num_blocks_vertical):
        for j in range(num_blocks_horizontal):
            vertical_start = i * block_size[0]
            vertical_end = vertical_start + block_size[0]
            horizontal_start = j * block_size[1]
            horizontal_end = horizontal_start + block_size[1]

            # Set the color of the block
            image[vertical_start:vertical_end, horizontal_start:horizontal_end] = colors[color_index]
            color_index = (color_index + 1) % len(colors)

    return image


# Define image and block dimensions
img_dimension = (240, 240)  # 240x240 pixels
block_dimension = (40, 40)  # Each block is 40x40 pixels

# Define block colors (BGR format)
block_colors = [
    (255, 0, 0),  # Red
    (0, 255, 0),  # Green
    (0, 0, 255),  # Blue
    (0, 255, 255),  # Cyan
    (255, 0, 255),  # Magenta
    (255, 255, 0),  # Yellow
    (192, 192, 192)  # Light gray
]

# Create the block image
block_image = create_block_image(img_dimension, block_dimension, block_colors)

# Save the image
cv2.imwrite('block_image.png', block_image)

# If you want to view the image within a Python script
cv2.imshow('Block Image', block_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

