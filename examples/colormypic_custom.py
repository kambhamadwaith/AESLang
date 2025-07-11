from PIL import Image
import numpy as np
import sys

PHRASE = "AES "
ASPECT_RATIO = 0.55

def resize_image(image, new_width):
    width, height = image.size
    new_height = int(height / width * new_width * ASPECT_RATIO)
    return image.resize((new_width, new_height))

def image_to_iloveyou_ascii(image, width=120):
    image = resize_image(image, width)
    image = image.convert("RGB")
    pixels = np.array(image)

    output = ""
    phrase_index = 0
    phrase_length = len(PHRASE)

    for row in pixels:
        for pixel in row:
            r, g, b = pixel
            char = PHRASE[phrase_index % phrase_length]
            output += f"\x1b[38;2;{r};{g};{b}m{char}\x1b[0m"
            phrase_index += 1
        output += "\n"
    return output

def main(image_path, width=120):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Could not open image: {e}")
        return

    ascii_output = image_to_iloveyou_ascii(image, width=width)
    print(ascii_output)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python iloveyou_ascii.py <image_path> [width]")
        sys.exit(1)

    image_path = sys.argv[1]
    width = int(sys.argv[2]) if len(sys.argv) > 2 else 120
    main(image_path, width)
