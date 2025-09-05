import kaggle
import kagglehub
import os
import shutil

# Download latest version
path = kagglehub.dataset_download("msambare/fer2013")

print("Path to dataset files:", path)

# Path where KaggleHub stored it
source_dir = path   

# Destination in your project
dest_dir = "data"

for split in ["train", "test"]:
    src_path = os.path.join(source_dir, split)
    dest_path = os.path.join(dest_dir, split)

    if not os.path.exists(dest_path):
        shutil.move(src_path, dest_path)
        print(f"Moved {split} → {dest_path}")
    else:
        print(f"{split} already exists in {dest_dir}, skipping...")