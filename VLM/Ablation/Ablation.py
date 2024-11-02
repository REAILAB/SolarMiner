# SolarMiner
# ├── Ablation
# │   ├── Ablation.py
# |   ├── Visualize.py
# ├── Inference
# │   ├── inference.py
# │   ├── utils.py

# The VLM utilized in SolarMiner is Segment Anything Model (SAM) 
# This is a python script to run the SAM model with a text prompt
# for the ablation study of the SAM model with different text prompts and box thresholds

# The package used in this script is samgeo
# It should be installed before running this script
# from samgeo import tms_to_geotiff
from samgeo.text_sam import LangSAM
import numpy as np
import cv2  # OpenCV for loading images
import pandas as pd  # Import pandas for saving results to Excel
#from TP import *

# Import the SAM model
sam = LangSAM()

# Define mining area terms
mining_area = ['Mining area', 'Surface mine', 'Pit', 'Pit hole']

# Path of the image and labels
Path = '../../subset/'
PathLabel = '../../subset_label/'

# Function to load ground truth mask
def load_ground_truth_mask(label_path):
    mask = cv2.imread(label_path, cv2.IMREAD_GRAYSCALE)
    return mask / 255  # Normalize to binary mask (0 or 1)

# Dataframes to store results
iou_results = []
pa_results = []

# Loop through each mining area term and text prompt combination for IoU
for mining_term in mining_area:
    for i in range(1, 5):
        if i == 1:
            text_prompt = mining_term
        elif i == 2:
            text_prompt = mining_term + ' from satellite'
        elif i == 3:
            text_prompt = 'Satellite imagery, ' + mining_term 
        elif i == 4:
            text_prompt = 'Overhead shot of the ' + mining_term

        iou_scores = []
        for figure in range(1, 101):
            image_path = Path + str(figure) + '.jpg'
            label_path = PathLabel + str(figure) + '.png'
            
            # Model prediction
            sam.predict(image_path, text_prompt, box_threshold=0.24, text_threshold=0.24)
            predicted_mask = sam.shown_anns()

            # Load ground truth label
            ground_truth_mask = load_ground_truth_mask(label_path)

            # Calculate IoU
            intersection = np.logical_and(predicted_mask, ground_truth_mask)
            union = np.logical_or(predicted_mask, ground_truth_mask)
            iou_score = np.sum(intersection) / np.sum(union)
            iou_scores.append(iou_score)

        # Calculate average IoU for this text prompt
        avg_iou = np.mean(iou_scores)
        iou_results.append([mining_term, text_prompt, avg_iou])

# Convert IoU results to DataFrame and save to Excel
iou_df = pd.DataFrame(iou_results, columns=['MiningTerm', 'TextPrompt', 'IoU'])
iou_df_pivot = iou_df.pivot(index='MiningTerm', columns='TextPrompt', values='IoU')
iou_df_pivot.to_excel('IoU_results.xlsx')

# mIoU calculation
# the mIoU is calculated by averaging the average IoU of the text prompt group
# 8x8 matrix is created to store the average IoU of the text prompt group
# saved in mIoU_results.xlsx
mIoU_results = []
ioufirst8 = iou_results[:8]
ioulast8 = iou_results[8:]

for i in range(8):
    mIoU_res = []
    for j in range(8):
        mIoU = (ioufirst8[i][2] + ioulast8[j][2]) / 2
        mIoU_res.append(mIoU)
    mIoU_results.append(mIoU_res)

mIoU_df = pd.DataFrame(mIoU_results)
mIoU_df.to_excel('mIoU_results.xlsx')


best_TP_Pit = 'Satellite imagery, ' + 'Surface mine'
best_TP_All = 'Overhead shot of the ' + 'Pit hole'
# Find the best box threshold with PA metric
# For Pit
for i in range(11, 40):
    box_threshold = i / 100
    pa_scores = []
    for figure in range(1, 101):
        image_path = Path + str(figure) + '.jpg'
        label_path = PathLabel + str(figure) + '.png'
        
        # Model prediction
        sam.predict(image_path, best_TP_Pit, box_threshold=box_threshold, text_threshold=0.24)
        predicted_mask = sam.shown_anns()

        # Load ground truth label
        ground_truth_mask = load_ground_truth_mask(label_path)

        # Calculate PA
        correct = np.sum(predicted_mask == ground_truth_mask)
        total = ground_truth_mask.size
        accuracy = correct / total
        pa_scores.append(accuracy)

    # Calculate average PA for this box threshold
    pa = np.mean(pa_scores)
    pa_results.append([box_threshold, pa])

# Convert PA results to DataFrame and save to Excel
pa_df = pd.DataFrame(pa_results, columns=['BoxThreshold', 'PA'])
pa_df_pivot = pa_df.pivot(columns='BoxThreshold', values='PA')
pa_df_pivot.to_excel('Pit_pa_results.xlsx')

# For all the mining regions
for i in range(11, 40):
    box_threshold = i / 100
    pa_scores = []
    for figure in range(1, 101):
        image_path = Path + str(figure) + '.jpg'
        label_path = PathLabel + str(figure) + '.png'
        
        # Model prediction
        sam.predict(image_path, best_TP_All, box_threshold=box_threshold, text_threshold=0.24)
        predicted_mask = sam.shown_anns()

        # Load ground truth label
        ground_truth_mask = load_ground_truth_mask(label_path)

        # Calculate PA
        correct = np.sum(predicted_mask == ground_truth_mask)
        total = ground_truth_mask.size
        accuracy = correct / total
        pa_scores.append(accuracy)

    # Calculate average PA for this box threshold
    pa = np.mean(pa_scores)
    pa_results.append([box_threshold, pa])

# Convert PA results to DataFrame and save to Excel
pa_df = pd.DataFrame(pa_results, columns=['BoxThreshold', 'PA'])
pa_df_pivot = pa_df.pivot(columns='BoxThreshold', values='PA')
pa_df_pivot.to_excel('All_pa_results.xlsx')

print("Ablation study completed!")