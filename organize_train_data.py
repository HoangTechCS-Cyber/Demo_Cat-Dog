# organize_train_data.py

import os
import shutil

def create_class_directories(train_dir):
    """
    Tạo các thư mục con 'cats' và 'dogs' trong thư mục train nếu chưa tồn tại.
    """
    classes = ['cats', 'dogs']
    for cls in classes:
        cls_dir = os.path.join(train_dir, cls)
        os.makedirs(cls_dir, exist_ok=True)
        print(f"Đã tạo hoặc xác nhận tồn tại thư mục: {cls_dir}")

def organize_files(train_dir):
    """
    Di chuyển các tệp ảnh vào thư mục tương ứng dựa trên tiền tố tên tệp.
    """
    classes = {'cats': 'cat.', 'dogs': 'dog.'}  # Từ điển ánh xạ lớp với tiền tố tên tệp
    for filename in os.listdir(train_dir):
        file_path = os.path.join(train_dir, filename)
        
        # Bỏ qua nếu là thư mục
        if os.path.isdir(file_path):
            continue
        
        # Phân loại dựa trên tiền tố tên tệp
        moved = False  # Biến kiểm tra xem tệp đã được di chuyển chưa
        for cls, prefix in classes.items():
            if filename.startswith(prefix):
                destination = os.path.join(train_dir, cls, filename)
                shutil.move(file_path, destination)
                print(f"Đã di chuyển {filename} vào thư mục {cls}.")
                moved = True
                break  # Thoát khỏi vòng lặp nếu đã di chuyển
        
        if not moved:
            print(f"Không xác định được loại cho {filename}. Bỏ qua.")

if __name__ == "__main__":
    # Đường dẫn đến thư mục train
    train_directory = os.path.join('data', 'train')
    
    print("Bắt đầu tạo các thư mục con 'cats' và 'dogs'...")
    create_class_directories(train_directory)
    
    print("\nBắt đầu phân loại và di chuyển các tệp ảnh...")
    organize_files(train_directory)
    
    print("\nHoàn thành việc phân loại dữ liệu trong thư mục train.")
