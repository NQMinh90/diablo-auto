import tkinter as tk

def test():
    root = tk.Tk()
    root.title("Test Tkinter")
    root.geometry("600x400")

    # Tạo nhãn và ô nhập
    path_label = tk.Label(root, text="Nhập đường dẫn file ảnh:", font=("Arial", 12))
    path_label.pack(pady=5)

    path_entry = tk.Entry(root, width=50, font=("Arial", 12))
    path_entry.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    test()