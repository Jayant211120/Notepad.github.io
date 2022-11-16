import tkinter as gui
from tkinter import messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
import tkinter.ttk as ttk
from tkinter import X,BOTH,TOP,Y

# Screen Properties
screen = gui.Tk()
screen.title("Jayant Notepad")
screen.minsize(700,700)
logo=gui.PhotoImage(file='notes.png')
screen.iconphoto(False,logo)

# Function for appling logic
def new_file():
    global file
    screen.title("Untitled - Notepad")
    file = None
    text.delete(1.0, gui.END)

def open_file():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        screen.title(os.path.basename(file)+"-Notepad")
        text.delete(1.0, gui.END)
        f = open(file, "r")
        text.insert(1.0, f.read())


def open_folder():
    pass


def saveas():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[
                                 ("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, gui.END))
            f.close()
            screen.title(os.path.basename(file)+"-Notepad")
    else:
        f = open(file, "w")
        f.write(text.get(1.0, gui.END))
        f.close()
        screen.title(os.path.basename(file)+"-Notepad")


def save():
    pass


def print():
    pass


def exit():
    quit()


def cut():
    text.event_generate(("<<Cut>>"))


def copy():
    text.event_generate(("<<Copy>>"))


def paste():
    text.event_generate(("<<Paste>>"))


def font():
    pass

# Colors Functions
def red():
    text.config(background='red')

def red_text():
    text.config(foreground='red')

def yellow():
    text.config(background='#dee052')

def yellow_text():
    text.config(foreground='#dee052')

def darkgreen():
    text.config(background='#11b61f')

def darkgreen_text():
    text.config(foreground='#11b61f')

def lightgreen():
    text.config(background='#7ce285')

def lightgreen_text():
    text.config(foreground='#7ce285')

def pink():
    text.config(background='`#d77ce2`')

def pink_text():
    text.config(foreground='#d77ce2')

def white():
    text.config(background='#f6f3f6')

def white_text():
    text.config(foreground='#f6f3f6')

def black():
    text.config(background='#1c121c')

def black_text():
    text.config(foreground='#1c121c')

def orange():
    text.config(background='#f2851e')

def orange_text():
    text.config(foreground='#f2851e')

def grey():
    text.config(background='#87817b')

def grey_text():
    text.config(foreground='#87817b')

def message():
    messagebox.showinfo('ThankYou','ThankYou For Using This Notepad')
    
def developer():
    messagebox.showinfo('Develper',"Developer:Jayant Verma")
 
#Start MainFunction 
if __name__ == '__main__':
    # For Text window
    text = gui.Text(screen, font="Lucida 20")
    file = None
    text.pack(fill='both',expand=True)
    
    # For Menu Bars
    main_menu = gui.Menu(screen)
    sub_menu = gui.Menu(main_menu, tearoff=0)
    # Images
    image1 = gui.PhotoImage(file='crossright.png')
    image2 = gui.PhotoImage(file='newfile.png')
    save_image = gui.PhotoImage(file='save.png')
    open_file_image = gui.PhotoImage(file='openfile.png')
    
    sub_menu.add_command(label='New File', command=new_file,
                         image=image2, compound=gui.LEFT, accelerator='Ctrl+N')
    sub_menu.add_command(label='OpenFile', command=open_file,
                         image=open_file_image, compound=gui.LEFT, accelerator='Ctrl+O')
    sub_menu.add_command(label='Open Folder', state="disabled")
    sub_menu.add_command(label='Save As', command=saveas, image=save_image,
                         compound=gui.LEFT, accelerator='Ctrl+S')
    sub_menu.add_command(label='Save As', state="disabled")
    sub_menu.add_command(label='Print', state="disabled")
    sub_menu.add_command(label='Exit', command=exit,
                         image=image1, compound=gui.LEFT, accelerator="Ctrl+Q")
    main_menu.add_cascade(menu=sub_menu, label="File")
    screen.config(menu=main_menu)
    
    # second Menu
    sub_menu2 = gui.Menu(main_menu, tearoff=0)
    
    image_cut = gui.PhotoImage(file='cut.png')
    image_paste = gui.PhotoImage(file='paste (2).png')
    copy_image = gui.PhotoImage(file='copy.png')
    
    sub_menu2.add_command(label='Copy', image=copy_image,command=copy,compound=gui.LEFT,accelerator='Ctrl+C')
    sub_menu2.add_command(label='Cut', image=image_cut,command=cut, compound=gui.LEFT,accelerator='Ctrl+X')
    sub_menu2.add_command(label='Paste', image=image_paste,command=paste,compound=gui.LEFT,accelerator='Ctrl+V')
    sub_menu2.add_command(label='Font', state="disabled")
    main_menu.add_cascade(menu=sub_menu2, label="Edit")
    screen.config(menu=main_menu)

    # Third Menu
    sub_menu3 = gui.Menu(main_menu, tearoff=False)
    
    orange_color=gui.PhotoImage(file='orange.png')
    grey_color=gui.PhotoImage(file='grey.png')
    black_color=gui.PhotoImage(file='black.png')
    pink_color=gui.PhotoImage(file='pink.png')
    yellow_color=gui.PhotoImage(file='yellow.png')
    white_color=gui.PhotoImage(file='white.png')
    dark_green_color=gui.PhotoImage(file='darkgreen.png')
    light_green_color=gui.PhotoImage(file='light_green.png')
    red_color=gui.PhotoImage(file='red_color.png')
    
    sub_menu3.add_command(label='Red', command=red, image=red_color, compound=gui.LEFT)
    sub_menu3.add_command(label='yellow', command=yellow, image=yellow_color, compound=gui.LEFT)
    sub_menu3.add_command(label='grey', command=grey, image=grey_color, compound=gui.LEFT)
    sub_menu3.add_command(label='pink', command=pink, image=pink_color, compound=gui.LEFT)
    sub_menu3.add_command(label='white', command=white, image=white_color, compound=gui.LEFT)
    sub_menu3.add_command(label='black', command=black, image=black_color, compound=gui.LEFT)
    sub_menu3.add_command(label='orange', command=orange, image=orange_color, compound=gui.LEFT)
    sub_menu3.add_command(label='green', command=lightgreen, image=light_green_color, compound=gui.LEFT)
    sub_menu3.add_command(label='orange', command=darkgreen, image=dark_green_color, compound=gui.LEFT)
    main_menu.add_cascade(menu=sub_menu3, label="Background Color")
    screen.config(menu=main_menu)
    
    # Fourth Menu
    sub_menu4 = gui.Menu(main_menu, tearoff=False)
    sub_menu4.add_command(label='Red', command=red_text, image=red_color, compound=gui.LEFT)
    sub_menu4.add_command(label='yellow', command=yellow_text, image=yellow_color, compound=gui.LEFT)
    sub_menu4.add_command(label='grey', command=grey_text, image=grey_color, compound=gui.LEFT)
    sub_menu4.add_command(label='pink', command=pink_text, image=pink_color, compound=gui.LEFT)
    sub_menu4.add_command(label='white', command=white_text, image=white_color, compound=gui.LEFT)
    sub_menu4.add_command(label='black', command=black_text, image=black_color, compound=gui.LEFT)
    sub_menu4.add_command(label='orange', command=orange_text, image=orange_color, compound=gui.LEFT)
    sub_menu4.add_command(label='green', command=lightgreen_text, image=light_green_color, compound=gui.LEFT)
    sub_menu4.add_command(label='orange', command=darkgreen_text, image=dark_green_color, compound=gui.LEFT)
    main_menu.add_cascade(menu=sub_menu4, label="Text Color")
    screen.config(menu=main_menu)
    
    # Fifth Menu
    sub_menu5=gui.Menu(screen,tearoff=0)
    sub_menu5.add_command(label="About",command=message)
    sub_menu5.add_command(label='Developer',command=developer)
    main_menu.add_cascade(menu=sub_menu5,label='Message')
    screen.config(menu=main_menu)
    screen.bind('<Control-n>',lambda n:new_file())
    screen.bind('<Control-o>',lambda o:open_file())
    screen.bind('<Control-s>',lambda s:saveas())
    screen.bind('<Control-q>',lambda e:exit())
    screen.bind('<Control-x>',lambda c:cut())
    screen.bind('<Control-c>',lambda cpt:copy())
    screen.bind('<Control-v>',lambda p:paste())
# Mainloop is used for permanent show screen
screen.mainloop()
