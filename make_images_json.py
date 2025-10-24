# make_images_json.py
# Usage: put your images in a local 'images' folder, set BASE_URL to the raw hosting URL (e.g. GitHub raw URL),
# then run: python3 make_images_json.py
import os, json
BASE_URL = "https://raw.githubusercontent.com/vishalguleria/Wedding-Photos/main/images/"  # <-- EDIT
LOCAL_IMAGES_DIR = "images"

images = []
if not os.path.isdir(LOCAL_IMAGES_DIR):
    print("Create a folder named 'images' and put all photos there, then run this script.")
else:
    for fname in sorted(os.listdir(LOCAL_IMAGES_DIR)):
        if fname.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
            images.append(BASE_URL + fname)
    with open('images.json','w') as f:
        json.dump(images, f, indent=2)
    print(f"Written images.json with {len(images)} entries.")
