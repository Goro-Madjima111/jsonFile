import json
import os
from PIL import Image, ImageDraw

json_path = 'json/1.json'
output_folder = 'json_to_mask'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

with open(json_path, 'r') as f:
    data = json.load(f)

for idx, group in enumerate(data):
    image = Image.new('RGB', (900, 900), color='black')
    draw = ImageDraw.Draw(image)
    
    for annotation in group['annotations']:
        for result in annotation['result']:
            if result['type'] == 'polygonlabels':
                points = result['value']['points']
                absolute_points = [(int(point[0] * 900 / 100), int(point[1] * 900 / 100)) for point in points]
                draw.polygon(absolute_points, fill='white')
    
    output_image_path = os.path.join(output_folder, f"output_image_{idx + 1}.png")
    image.save(output_image_path)
    print(f"Processed and saved {output_image_path}")