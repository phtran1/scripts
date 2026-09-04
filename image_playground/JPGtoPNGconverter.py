import sys
import os
from pathlib import Path
from PIL import Image

images = sys.argv[1]
output = sys.argv[2]
# print(images)
# print(output)

if not os.path.exists(output):
    os.makedirs(output)

dir_path = Path(images)
# print(dir_path)

for file in dir_path.iterdir():
    img = Image.open(file)
    # print(file.stem)
    img.save(f'{output}{file.stem}.png', 'png')

