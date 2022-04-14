from PIL import Image
import os

path = "car_data/train"

for root, dirs, files in os.walk(path):
    for name in files:
        img = Image.open(root + "/" + name)

        resized = img.resize((640, 480), Image.BILINEAR)
        # BILINEAR, BICUBIC BRZO-KVALITETA--
        # LANCZOS SPORO-KVALITETA++

        resized.save(root + "/" + name, quality=95)
        # quality=100, subsampling=0 NAJKVALITETNIJE

        print(root + "/" + name)
