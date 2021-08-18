import tkinter as tk
from tkinter import ttk
import random
import string
import tkinter.messagebox as box
import os
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 28, "bold")
DEFAULT_FONT_STYLE = ("Arial", 17)
PASS_FONT = ("Arial", 35, "bold")

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"

class Generator:
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry('375x500')
        self.app.resizable(0, 0)
        self.app.title('Password Generator')
        # img = tk.PhotoImage(file='icon.ico')
        # self.app.tk.call('wm', 'iconphoto', self.app._w, img)

        self.pass_text = 'Password Generator'
        self.filed_v2 = 'V2'
        self.pass_filed= ''
        self.recommended_text = 'Recommended (12)'
        self.info_length = 'Enter The Length Of The Password'
        self.click_text = 'Click Me!!'
        self.copy_pass = 'Note: Password copy automatic'
        self.length_text = 'Length:'
        self.length_value = 'Length Of Pass:'

        self.current_value = tk.DoubleVar()
        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_labels()
        self.buttons_show = self.create_button()
        self.slider = self.create_slider()
        
    def addToClipBoard(self,text):
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)

    def Errorbox(sellf):
        box.showinfo('Error','You Are htf')

    # def update(self):
    #     self.pass_filed.config(text=self.resualte)

    def Password(self):
        try:
            length = int(self.get_current_value())
            #print(length)
            letters = string.ascii_letters
            stR = (''.join(random.choice(letters) for i in range(30)) )
            RandomWord = stR
            RandomNumber = str(random.randrange(1, 99999))
            RandomCodes = '!@#$%^&*'
            resualte = RandomWord+RandomNumber+RandomCodes
            resualte = (''.join(random.choice(resualte) for i in range(length)))
            self.pass_filed.config(text = resualte)
            self.addToClipBoard(resualte)
            #print(resualte)
            return resualte
        except:
            lengthError = int(self.get_current_value())
            if lengthError == '0':
                self.Errorbox()
        #     pass


    def create_labels(self):
        self.pass_filed = tk.Label(self.display_frame, text=self.pass_filed, anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=150, font=PASS_FONT)
        self.pass_filed.place(x=-150,y=330)
        label2 = tk.Label(self.display_frame, text=self.filed_v2, anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=24, font=LARGE_FONT_STYLE)
        label2.place(x=130, y=70)    
        label = tk.Label(self.display_frame, text=self.pass_text, anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=24, font=DIGITS_FONT_STYLE)
        label.place(x=-20, y=30)
        label3 = tk.Label(self.display_frame, text=self.info_length, anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=24, font=DEFAULT_FONT_STYLE)
        label3.place(x=-17,y=130)
        label4 = tk.Label(self.display_frame, text=self.recommended_text, anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=24, font=SMALL_FONT_STYLE)
        label4.place(x=75,y=160)
        label5 = tk.Label(self.display_frame, text=self.copy_pass, anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=24, font=SMALL_FONT_STYLE)
        label5.place(x=10,y=280)
        slider_label = ttk.Label(
            self.app,
            text=self.length_text
        )
        slider_label.place(x=80, y=201)
        slider_text = ttk.Label(
            self.app,
            text=self.length_value
        )
        slider_text.place(x=130,y=222)
        self.value_label = tk.Label(self.display_frame, text=self.get_current_value(), anchor=tk.E, bg=LIGHT_GRAY,
                         fg='black', padx=24, font=SMALL_FONT_STYLE)
        self.value_label.place(x=130,y=240)
        return label, label2


    def create_button(self):
        button2 = tk.Button(text=self.click_text, bg=LIGHT_GRAY, fg=LABEL_COLOR, font=LARGE_FONT_STYLE ,borderwidth=0,command=self.Password)
        button2.place(x=35,y=390)
        #what the fuck
        #self.update()
        #button.place(x=75,y=160)


    def create_display_frame(self):
        frame = tk.Frame(self.app, height=220, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame



    def create_slider(self):
        slider = ttk.Scale(
            self.app,
            from_=0,
            to=12,
            orient='horizontal',
            command=self.slider_changed,
            variable=self.current_value,
        )
        slider.place(x=130,y=200)
        return slider

    # def update(self):
    #     self.pass_filed = self.Password()

    def get_current_value(self):
        #return self.current_value.get()
        return '{: .0f}'.format(self.current_value.get())


    def slider_changed(self,event):
        self.value_label.configure(text=self.get_current_value())
    

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    calc = Generator()
    calc.run()
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX