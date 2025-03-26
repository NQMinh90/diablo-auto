import os
import cv2
import numpy as np
import pyautogui
import tkinter as tk
from tkinter import messagebox


def find_health_bar():
    # Chụp màn hình
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)

    # Chuyển đổi sang không gian màu HSV
    hsv = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

    # Định nghĩa dải màu (tùy chỉnh theo thanh máu của bạn)
    lower_color = np.array([0, 0, 0])  # Màu tối (đen hoặc đỏ sẫm)
    upper_color = np.array([180, 255, 50])  # Màu tối (đen hoặc đỏ sẫm)

    # Tạo mask để lọc màu
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Tìm các contours trong mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # Lấy tọa độ và kích thước của vùng tìm được
        x, y, w, h = cv2.boundingRect(contour)

        # Lọc các vùng có kích thước phù hợp với thanh máu
        if w > 100 and h < 20:  # Thanh máu thường dài và mỏng
            return f"Thanh máu được tìm thấy tại: x={x}, y={y}, w={w}, h={h}"

    return "Không tìm thấy thanh máu."


def on_find_health_bar():
    # Gọi hàm tìm thanh máu và hiển thị kết quả
    result = find_health_bar()
    messagebox.showinfo("Kết quả", result)

def convert_image():
    # Lấy đường dẫn từ ô nhập
    image_path = path_entry.get()

    # Kiểm tra xem file có tồn tại không
    if not os.path.isfile(image_path):
        messagebox.showerror("Lỗi", "File không tồn tại. Vui lòng kiểm tra đường dẫn.")
        return

    # Đọc ảnh từ đường dẫn
    image = cv2.imread(image_path)

    if image is None:
        messagebox.showerror("Lỗi", "Không thể đọc file ảnh. Vui lòng kiểm tra định dạng.")
        return

    # Chuyển đổi sang không gian màu HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Lưu ảnh HSV
    output_path = "converted_image_hsv.png"
    cv2.imwrite(output_path, hsv_image)

    # Thông báo thành công
    messagebox.showinfo("Thành công", f"Ảnh đã được chuyển đổi và lưu tại: {output_path}")

def main():
    # Tạo cửa sổ chính
    root = tk.Tk()
    root.title("Diablo Auto")

    # Tạo nhãn tiêu đề
    label = tk.Label(root, text="Welcome to Diablo Auto!", font=("Arial", 16))
    label.pack(pady=10)

    # Tạo nút để tìm thanh máu
    find_button = tk.Button(root, text="Tìm Thanh Máu", command=on_find_health_bar, font=("Arial", 12))
    find_button.pack(pady=10)

    # Tạo nhãn và ô nhập đường dẫn file ảnh
    path_label = tk.Label(root, text="Nhập đường dẫn file ảnh:", font=("Arial", 12))
    path_label.pack(pady=5)

    global path_entry
    path_entry = tk.Entry(root, width=50, font=("Arial", 12))
    path_entry.pack(pady=5)

    # Tạo nút để chuyển đổi ảnh
    convert_button = tk.Button(root, text="Convert Image", command=convert_image, font=("Arial", 12))
    convert_button.pack(pady=10)

    # Chạy vòng lặp giao diện
    root.mainloop()


if __name__ == "__main__":
    main()