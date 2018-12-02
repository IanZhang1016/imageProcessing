from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.filedialog
import image_proccssing.a1 as a1
import image_proccssing.a2 as a2
import image_proccssing.a3 as a3
import image_proccssing.a4 as a4
import image_proccssing.a5 as a5
import image_proccssing.a6 as a6
import image_proccssing.a7 as a7
import image_proccssing.a8 as a8


class AppUI(object):

    def __init__(self):
        root = Tk()
        self.create_menu(root)
        self.create_content(root)
        root.title("Image Processing")
        root.update()
        curWidth = root.winfo_width()  # get current width
        curHeight = root.winfo_height()  # get current height
        scnWidth, scnHeight = root.maxsize()  # get screen width and height
        tmpcnf = '+%d+%d' % ((scnWidth - curWidth) / 2, (scnHeight - curHeight) / 2)
        root.geometry(tmpcnf)
        root.mainloop()


    def create_menu(self,root):
        menu = Menu(root)
        file_menu = Menu(menu,tearoff=0)
        file_menu.add_command(label="a1",command=self.calla1)
        file_menu.add_separator()
        file_menu.add_command(label="a2",command=self.calla2)
        file_menu.add_separator()
        file_menu.add_command(label="a3",command=self.calla3)
        file_menu.add_separator()
        file_menu.add_command(label="a4",command=self.calla4)
        file_menu.add_separator()
        file_menu.add_command(label="a5",command=self.calla5)
        file_menu.add_separator()
        file_menu.add_command(label="a6",command=self.calla6)
        file_menu.add_separator()
        file_menu.add_command(label="a7",command=self.calla7)
        file_menu.add_separator()
        file_menu.add_command(label="a8",command=self.calla8)


        about_menu = Menu(menu,tearoff=0)
        about_menu.add_command(label="Version")


        menu.add_cascade(label="Process",menu=file_menu)
        menu.add_cascade(label="About",menu=about_menu)
        root['menu'] = menu

    def create_content(self, root):
        lf = tk.LabelFrame(root, text="Result")
        lf.pack(fill=X, padx=15, pady=8)

        top_frame = Frame(lf)
        top_frame.pack(fill=X,expand=YES,side=TOP,padx=15,pady=8)

        im=Image.open("res/welcome.jpg")
        self.img=ImageTk.PhotoImage(im)
        self.imgLabel=Label(top_frame,image=self.img)
        self.imgLabel.pack()


    def open_dir(self):
        filename = tkinter.filedialog.askopenfilename()
        if filename != '':
            return filename


    def changeLabelIamge(self, filepath):
        im = Image.open(filepath)
        self.img = ImageTk.PhotoImage(im)
        self.imgLabel.configure(image=self.img)


    def calla1(self):
        self.changeLabelIamge(a1.cov_img(self.open_dir()))


    def calla2(self):
        self.changeLabelIamge(a2.a2(self.open_dir()))


    def calla3(self):
        self.changeLabelIamge(a3.a3(self.open_dir()))


    def calla4(self):
        self.changeLabelIamge(a4.resize_Image(self.open_dir()))


    def calla5(self):
        a5.a5(self.open_dir())

    def calla6(self):
        a6.a6(self.open_dir())

    def calla7(self):
        a7.find_cluster(self.open_dir(),2)

    def calla8(self):
        a8.a8(self.open_dir())


if __name__ == "__main__":
    AppUI()
