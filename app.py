import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk

root = tk.Tk()

canvas =tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=3)

# Logo
logo = Image.open('')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.label(image.logo)
logo_label.grid(column=1, row=0)

root.mainloop()