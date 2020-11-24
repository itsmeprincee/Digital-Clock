from tkinter import *
from tkinter import font
import time
#creating clock method which is used to display the Clock
def clock():
    h = str(time.strftime("%H"))
    m = str(time.strftime("%M"))
    s = str(time.strftime("%S"))
    if int(h)>12:
        h = str(int(int(h)-12))
    if int(h)>12 and int(m)>0:
        noon_number.config(text="PM")
    hours_number.config(text=h)
    minutes_number.config(text=m)
    seconds_number.config(text=s)

    hours_number.after(200,clock)




#window creation
master = Tk()
master.title("Digital Clock")
master.geometry("700x300+100+100")
master.config(bg="#2c313c")
master.resizable(False,False)
#heading for master window
main_heading=Label(master,text="Digital Clock",font =font.Font(family="Helvetica",size=20),fg="#fff",bg="#2c313c")
main_heading.pack()
#creating frame for main window
parent = Frame(master,bg='#2c313c')
parent.pack()
#creating widgets
#creating number icons for displaying time..
hours_number = Label(parent,text="12",pady=10,padx=10,fg="#fff",bg="#8d939f",font=font.Font(family="times new roman",size=50),height=2,width=3)
hours_number.grid(row =0,column=0,padx=10,pady=10)
minutes_number = Label(parent,text="00",pady=10,padx=10,bg="#599bd3",fg="#fff",font=font.Font(family="times new roman",size=50),height=2,width=3)
minutes_number.grid(row=0,column=1,padx=10,pady=10)
seconds_number = Label(parent,text="00",pady=10,padx=10,bg="#98c379",fg="#fff",font=font.Font(family="times new roman",size=50),height=2,width=3)
seconds_number.grid(row=0,column=2,padx=10,pady=10)
noon_number = Label(parent,text="AM",pady=10,padx=10,bg="#d19a66",fg="#fff",font=font.Font(family="times new roman",size=50),height=2,width=3)
noon_number.grid(row=0,column=3,padx=10,pady=10)
#creating number text for what it displays
hours_text = Label(parent,text="Hours",pady=10,padx=10,bg="#8d939f",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
hours_text.grid(row=1,column=0,padx=10,pady=10)
minutes_text = Label(parent,text ="Minutes",pady=10,padx=10,bg="#599bd3",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
minutes_text.grid(row=1,column=1,padx=10,pady=10)
seconds_text = Label(parent,text="Seconds",pady=10,padx=10,bg="#98c379",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
seconds_text.grid(row=1,column=2,padx=10,pady=10)
noon_text = Label(parent,text ="Noon",pady=10,padx=10,bg="#d19a66",fg="#fff",font=font.Font(family="times new roman",size=15),height=1,width=10)
noon_text.grid(row=1,column=3,padx=10,pady=10)
clock()
parent.mainloop()
