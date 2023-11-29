from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Image Editor")
root.geometry("500x500")
root.configure(background = "lightblue")

label_image = Label(root, text = "Open Image ", bg = "lightblue", highlightthickness=10)
img_path = ""

def openImg():
    global img_path
    img_path = filedialog.askopenfilename(title = "Open Image File", filetypes = [("Image Files", "*.jpg *.png *.gif *.jpeg *.jfif *.jpe")])
    print(img_path)
    im = Image.open(img_path)
    img = ImageTk.PhotoImage(im)
    name = os.path.basename(img_path)
    formated_name = name.split('.')[0]
    root.title(formated_name)
    label_img["image"] = img
    img.close()
    
open_btn = Button(root, text = "Open Image", bg = "Grey", fg = "white", font = ("castellar", 15, "bold"), padx = 15, pady = 10, relief = SOLID, command = openImg)
open_btn.place(relx = 0.5, rely = 0.1, anchor = CENTER)

root.mainloop()