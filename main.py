# -*- coding: utf-8 -*-
"""
Created on Thu May 26 11:46:34 2022

@author: Lenovo
"""



import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Plant Leaf Disease Detection System")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('sample.jpg')
image2 = image2.resize((1500, 800), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Plant Leaf Disease Detection System",font=("Times New Roman", 30, 'bold'),
                    background="#C70039", fg="white", width=60, height=2)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])

def plant():
    from subprocess import call
    call(["python","GUI_Master_plant.py"])


  
def window():
  root.destroy()


button1 = tk.Button(root, text="Plant Detection", command=plant, width=20, height=1,font=('times', 20, ' bold '), bg="maroon", fg="white")
button1.place(x=500, y=160)



button3 = tk.Button(root, text="Exit",command=window,width=20, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=500, y=230)

root.mainloop()
