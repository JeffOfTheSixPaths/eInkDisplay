from PIL import Image
import sys

def image_to_bytes(image_path):
    # Load and convert to 1-bit B/W
    img = Image.open(image_path).convert("1")
    img = img.resize((200, 200))  # Ensure size is 200x200

    pixels = img.load()
    width, height = img.size

    byte_rows = []

    for y in range(height):
        row_bytes = []
        for x in range(0, width, 8):
            byte = 0
            for i in range(8):
                if x + i < width:
                    bit = 1 if pixels[x + i, y] == 255 else 0
                    byte = (byte << 1) | bit
            row_bytes.append(byte)
        byte_rows.append(row_bytes)

    return byte_rows


data = image_to_bytes(sys.argv[1]) #or change this to filename

for row in data:
    print(", ".join(f"0x{byte:02X}" for byte in row))
    print(",")
