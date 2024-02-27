from PIL import Image
import os
import numpy as np

def convert_to_bw_with_transparency(input_path, output_path):
  # Open the image file
  image = Image.open(input_path)

  # Convert the image to RGBA (to handle transparency)
  rgba_image = image.convert('RGBA')

  # Create a new image with a transparent background
  transparent_image = Image.new('RGBA', rgba_image.size, (255, 255, 255, 0))

  # Paste the original image onto the new image, using the alpha channel as a mask
  transparent_image.paste(rgba_image, (0, 0), rgba_image)

  # Convert to a binary image (black and white) with no background
  bw_image = transparent_image.convert('1')

  # Get pixel data as a flattened array
  pixel_data = np.array(bw_image.getdata())

  # Reshape the data into a 2D array based on image size
  width, height = bw_image.size
  bw_array = pixel_data.reshape(height, width)

  # Optional: Save the final image for verification (unchanged)
  bw_image.save(output_path)

  # Return the 2D array representing the black and white image
  return bw_array

if __name__ == "__main__":
  # Replace 'input.png' and 'output.png' with your file names
  input_image_path = 'brian.png'
  output_image_path = 'output1.png'

  # Call the function and get the 2D array
  bw_array = convert_to_bw_with_transparency(input_image_path, output_image_path)

  # Print the 2D array (example)
  print(bw_array)