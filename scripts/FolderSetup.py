from pathlib import Path 
import os 

folders = [
    "data",
    "model",
    "notebooks",
    "scripts"
]

for folder in folders:
    dir = Path("C:/Users/sanju/OneDrive/Desktop/EmotionDetection",folder)
    dir.mkdir(parents=True , exist_ok=True)
print("Folders Created Successfully....")



