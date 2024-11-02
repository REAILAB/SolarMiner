# The utils module contains utility functions for SolarMiner.
# SolarMiner
# ├── Ablation
# │   ├── Ablation.py
# |   ├── Visualize.py
# ├── Inference
# │   ├── inference.py
# │   ├── utils.py

# dirctory
city_dir = {
    "Taiyuan",
    "Datong",
    "Yangquan",
    "Changzhi",
    "Jincheng",
    "Shuozhou",
    "Jinzhong",
    "Yuncheng",
    "Xinzhou",
    "Linfen",
    "Lvliang"
}

# dataloader
# return path of the image
# ../../Shanxi24/[province]/shanxi1.jpg
def province_dataloader(province):
    """
    11 city-level administrative regions in Shanxi Province
    Taiyuan
    Datong
    Yangquan
    Changzhi
    Jincheng
    Shuozhou
    Jinzhong
    Yuncheng
    Xinzhou
    Linfen
    Lvliang
    """ 
    return '../../Shanxi24/' + province
