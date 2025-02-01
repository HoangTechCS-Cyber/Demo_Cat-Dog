# create_validation_set.py

import os
import shutil
from sklearn.model_selection import train_test_split

def create_validation_split(train_dir, validation_dir, split_ratio=0.2):
    """
    Chia tập train thành train và validation dựa trên split_ratio.
    """
    classes = ['cats', 'dogs']
    for cls in classes:
        cls_train_dir = os.path.join(train_dir, cls)
        cls_validation_dir = os.path.join(validation_dir, cls)
        os.makedirs(cls_validation_dir, exist_ok=True)
        
        images = os.listdir(cls_train_dir)
        train_images, val_images = train_test_split(images, test_size=split_ratio, random_state=42)
        
        for img in val_images:
            src = os.path.join(cls_train_dir, img)
            dst = os.path.join(cls_validation_dir, img)
            shutil.move(src, dst)
            print(f"Đã di chuyển {img} từ {cls_train_dir} vào {cls_validation_dir}")

if __name__ == "__main__":
    train_directory = os.path.join('data', 'train')
    validation_directory = os.path.join('data', 'validation')
    
    print("Bắt đầu chia tập validation...")
    create_validation_split(train_directory, validation_directory, split_ratio=0.2)
    print("Hoàn thành việc chia tập validation.")
