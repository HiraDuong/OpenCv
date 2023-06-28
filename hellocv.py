import tkinter as tk
import numpy as np
from tkinter import filedialog, Button, Tk
from PIL import Image, ImageTk
import cv2

def increase_brightness(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    
    v = cv2.add(v, value)
    
    v = np.where(v > 255, 255, v)
    
    hsv = cv2.merge((h, s, v))
    brightened_image = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    
    return brightened_image

def Browser_Img():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        brightened_image = increase_brightness(image, 250)  
        
        cv2.imshow("Original Image", image)
        cv2.imshow("Brightened Image", brightened_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

window = tk.Tk()
window.title("Tăng cường độ sáng ảnh")
window.geometry("800x600")

browser_button = tk.Button(window, text="Browser", command=Browser_Img)
browser_button.pack(pady=20)

window.mainloop()
