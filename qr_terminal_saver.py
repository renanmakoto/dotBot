import pyqrcode
import tkinter as tk
from tkinter import filedialog
from time import sleep
def generate_qr():
    data = input("\nEnter text or URL to generate QR Code: ")
    qr = pyqrcode.create(data)
    root = tk.Tk()
    root.withdraw()
    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All Files", "*.*")],
        title="Save QR Code As"
    )
    if save_path:
        qr.png(save_path, scale=8)
        sleep(0.5)
        print(f"\nQR Code successfully saved as '{save_path}'")
    else:
        sleep(0.5)
        print("\nQR Code saving cancelled.")
if __name__ == "__main__":
    generate_qr()
