from PIL import Image

# Load the image and resizes just in case
img = Image.open("your_image.png").convert("1")  # Convert to 1-bit pixels (black and white)
img = img.resize((200, 200))

pixels = img.load()
width, height = img.size

# Convert to 2D list of 0s and 1s
pixel_matrix = [[1 if pixels[x, y] else 0 for x in range(width)] for y in range(height)]

for row in pixel_matrix:
    print("".join(str(val) for val in row)) # prints the values to copy and paste
