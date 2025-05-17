# SolarMiner
### Assessing Mine-site Photovoltaic (PV) and Floating PV Potential Using Vision Large Model

This is the official website of SolarMiner.

The official rep of Assessing Mine-site Photovoltaic (PV) and Floating PV Potential Using Vision Large Model

The source code of utilizing VLM (Vision Large Model) for the mine-site solar energy potential assessment has been published there.

Also, the referenced datas for the PV (Photovoltiac) simulation model construction, environmental and economical analysis were displayed here.

So, let us go step by step to know How the SolarMiner works...

## 1. What is SolarMiner?
### 1.1 Background
Installing PV systems in post-mining areas offers numerous advantages. However, there is currently a lack of algorithms capable of assessing the PV potential of mining areas on a large scale. Furthermore, the development of Float PV (FPV) technology has made it possible to install FPV systems in these areas. Therefore, we propose a model capable of conducting a wide-ranging assessment of the extensive potential of mining areas. This model, incorporating computer vision techniques, enables the calculation of potential installation areas for both FPV and traditional PV systems.
![image](https://github.com/user-attachments/assets/a995d81a-3239-4a71-992d-26fe384376de)


### 1.2 VLM
The architecture of the VLM was shown in this figure

![image](https://github.com/user-attachments/assets/6b62f87b-c928-4798-989e-8060b1df3213)

For more detials, please visit [Github-SAM](https://github.com/facebookresearch/segment-anything)

The code can also be used:
```shell
git clone https://github.com/pvlib/pvlib-python.git
```
### 1.3 PV Models
Pvlib for python, an open sourced package for PV simulation and power generation calculation.
![image](https://github.com/user-attachments/assets/7232f3b8-5769-495b-96eb-173d927a132d)

For detail, please visit [PVlib](https://github.com/pvlib/pvlib-python)

Your can also use the source code, by pasting the following code in bash
```shell
git clone https://github.com/pvlib/pvlib-python.git
```

## 2. Folders introduction
### 2.1 VLM
The source code of using VLM for the mining area segmentation and calculation was sorted in this folder

In this paper, the VLM is Segment Anything Model (SAM) which is open-source with both the model structure and the model weight by Meta AI, reader and developer can download the model from https://github.com/facebookresearch/segment-anything.git, or
```shell
git clone https://github.com/facebookresearch/segment-anything.git
```

### 2.2 Data
The data source which is referenced for the comprehensive analysis in the paper can be obtained here
### 2.3 Analysis
The calculation of economic or environmental analysis can be obtained here
### 2.4 Results
The results of ablation process and final calculation results which was sorted in .xlsx can be obtained here
### To use these code, please paste the following code in bash
```shell
git clone https://github.com/REAILAB/SolarMiner.git
```
## 3. Citition
If you are interested in SolarMiner, for more information, you can read our paper:

Pre-print:

DOI:

If your use the model, the results or get ideas from the paper, please cite it.

And your can also send email to me for more information (Please using English or Chinese).

## 4. [REAILAB (REAILab)](https://github.com/REAILAB) and series works
REAI is AI for Renewable Energy
![image](https://github.com/user-attachments/assets/0c9bf286-5eae-4ecc-ae80-b584ca80f3c3)

REAILAB is a non-profit, enthusiast-driven organization dedicated to exploring the applications of artificial intelligence and pattern recognition technologies in EE and energy.

### Previous work
### SolarSAM
Published in Elsevier Renewable Energy [Click here to read](https://doi.org/10.1016/j.renene.2024.121560)

For the code, please click: [Code on Github](https://github.com/REAILAB/SolarSAM.git)
