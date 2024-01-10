import os
from PIL import Image, ImageOps

# Get the current working directory where the Python script is located
directory = os.getcwd()

# Loop through each file in the directory
for file_name in os.listdir(directory):
    # Check if the file is an image (JPEG or PNG)
    if file_name.endswith(".jpg") or file_name.endswith(".jpeg") or file_name.endswith(".png"):
        # Open the image
        image = Image.open(os.path.join(directory, file_name))

        # Invert the colors of the image
        negative_image = ImageOps.invert(image.convert('RGB'))

        # Save the negative image, replacing the original file
        negative_image.save(os.path.join(directory, file_name))
