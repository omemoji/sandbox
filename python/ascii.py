import sys
from PIL import Image

def generate_ascii_art(image_path, width=100):
    # Open the image
    image = Image.open(image_path)

    # Resize the image while maintaining aspect ratio
    aspect_ratio = image.width * 2 / image.height
    height = int(width / aspect_ratio)
    image = image.resize((width, height))

    # Convert the image to grayscale
    image = image.convert('L')

    # Define the ASCII characters to use for the art
    ascii_chars = '@%#*+=-:. '

    # Generate the ASCII art
    ascii_art = ''
    for y in range(height):
        for x in range(width):
            pixel = image.getpixel((x, y))
            ascii_art += ascii_chars[pixel // 32]
        ascii_art += '\n'
    return ascii_art

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ascii.py <image_path> [width]")
        sys.exit(1)
    
    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 100
    ascii_art = generate_ascii_art(image_path, width)
    with open('out/ascii_python.txt', 'w') as file:
        file.write(ascii_art)