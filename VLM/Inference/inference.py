# SolarMiner
# SolarMiner
# ├── Ablation
# │   ├── Ablation.py
# |   ├── Visualize.py
# ├── Inference
# │   ├── inference.py
# │   ├── utils.py

# This is inference.py in the Inference directory of the SolarMiner project.
# This file contains code for performing inference using the SolarMiner for the mining region
# identification and mining area calculation. The code uses the VLM (SAM) for satellite imagery segmentation

# the package used in this script is samgeo
# it should be installed before running this script
from samgeo import tms_to_geotiff
from samgeo.text_sam import LangSAM
from PIL import Image
import os
import numpy as np
import pandas as pd
from utils import *
# import the SAM model
sam = LangSAM()

# text_prompt = 'Pit' + ' from satellite'

# path of the image
image_dir = '../../Shanxi24'
type = {'All','Pit'}

# optimal text prompts and hyperparameters for segmentation
text_prompts = {
    'Overhead shot of the ' + 'Pit hole':0.26,
    'Satellite imagery, ' + 'Surface mine':0.26
}

# Image resolution and scale
ppi = 196  # pixels per inch
scale_factor = 1602  # scale factor for converting pixel area to real area

# VLM inference for the mining region identification and mining area calculation
def inference(city):
    # Dictionary to store total pixel count for each text prompt
    pixel_counts = {prompt: 0 for prompt in text_prompts}

    # Loop through each text prompt
    for text_prompt, box_threshold in text_prompts.items():
        # Loop through each image in the directory
        for filename in os.listdir(image_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                # Construct full image path
                image_path = os.path.join(image_dir, filename)

                # Load image
                image = Image.open(image_path)

                # Perform model prediction
                result = sam.predict(image, text_prompt, box_threshold=box_threshold, text_threshold=0.24)

                # Convert result to numpy array for pixel count
                mask = np.array(result['mask'])

                # Count the number of pixels in the mask
                pixel_count = np.sum(mask)

                # Add to the total pixel count for this text prompt
                pixel_counts[text_prompt] += pixel_count

    # Calculate the real area for each text prompt
    inch_per_pixel = 1 / ppi  # convert pixels to inches
    inch_to_meter = 0.0254  # convert inches to meters
    area_per_pixel = (inch_per_pixel * inch_to_meter) ** 2  # area of one pixel in square meters

    real_areas = []

    print("Real area for each text prompt (in square meters):")
    for text_prompt, pixel_count in pixel_counts.items():
        real_area = pixel_count * area_per_pixel * scale_factor
        real_areas.append(real_area)
        # print(f"{text_prompt}: {real_area:.2f} square meters")
        
    i = 1
    all_areas = 0
    results = []
    for areas in real_areas:
        if i != 2:
            all_areas = all_areas + areas
            #print(areas)
            i = i + 1
            results.extend(areas)
        else:
            areas = areas - all_areas
            #print(areas)
            results.extend(areas)
    print('The area calculation of '+city+' finish!')
    return results

def main():
    re_area = []
    for city in city_dir:
        path = province_dataloader(city)
        re_area.append(inference(path))
        re_area = np.array(re_area)
        re_area = re_area.T
    #print(installation_area)
    # save the result to installation_result.xlsx
    # add the city name to the dataframe
    df = pd.DataFrame(re_area)
    df.to_excel('area_result.xlsx', index=False)


if __name__ == '__main__':
    main()