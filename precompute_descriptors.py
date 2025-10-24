# precompute_descriptors.py
# Optional: precompute face descriptors locally using face_recognition (dlib) and output descriptors.json
# Requires: pip install face_recognition numpy
# Note: face_recognition uses dlib which may require build tools. Run locally on your machine.
import face_recognition, os, json, numpy as np

IMAGES_DIR = "images"   # local folder
OUT_JSON = "descriptors.json"

entries = []
for fname in sorted(os.listdir(IMAGES_DIR)):
    if not fname.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        continue
    path = os.path.join(IMAGES_DIR, fname)
    print("Processing", path)
    img = face_recognition.load_image_file(path)
    encs = face_recognition.face_encodings(img)
    if len(encs) == 0:
        print("  no face found")
        continue
    # take first face
    enc = encs[0]
    entries.append({'url': fname, 'descriptor': enc.tolist()})

# The web app expects full URLs; edit after upload or change 'url' to full raw URLs.
with open(OUT_JSON, 'w') as f:
    json.dump(entries, f)
print("Wrote", OUT_JSON, "with", len(entries), "entries.")
