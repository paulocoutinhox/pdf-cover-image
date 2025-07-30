import os

from pdf2image import convert_from_path
from PIL import Image, ImageChops


def crop_borders(img, border_color=(255, 255, 255)):
    # Convert to RGB if not already
    img = img.convert("RGB")
    bg = Image.new(img.mode, img.size, border_color)
    diff = ImageChops.difference(img, bg)
    bbox = diff.getbbox()

    if bbox:
        return img.crop(bbox)

    # Return original if no border found
    return img


input_dir = "input"
output_dir = "output"

os.makedirs(output_dir, exist_ok=True)

for fname in os.listdir(input_dir):
    if fname.lower().endswith(".pdf"):
        pdf_path = os.path.join(input_dir, fname)
        try:
            # Extract first page as image (cover)
            pages = convert_from_path(pdf_path, dpi=300, first_page=1, last_page=1)

            if pages:
                img = pages[0]
                img_cropped = crop_borders(img)

                # Save cropped image (PNG to avoid quality loss)
                base = os.path.splitext(fname)[0]
                output_path = os.path.join(output_dir, f"{base}_cover.png")
                img_cropped.save(output_path)

                print(f"Cover exported: {output_path}")
        except Exception as e:
            print(f"Error processing {fname}: {e}")
