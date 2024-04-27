from tkinter import *
import os

def restart():
    os.system("Shutdown -r -t 1")


def restart_time():
    os.system("Shutdown -r -t 20")



def shutdown():
    os.system("Shutdown -s -t 1")


st = Tk()


st.title("shut down app")
st.geometry("500x500")

#background colour change.
st.config(bg="black")

#restart button.
r_button = Button(st,text="Restart",font=("arial",20,"bold"),bg="red",cursor="plus",command=restart)
r_button.place(x = 150,y = 60,width=200,height=50)

#restart with time.
r_button = Button(st,text="Restart time",font=("arial",20,"bold"),bg="red",cursor="plus",command=restart_time)
r_button.place(x = 150,y = 170,width=200,height=50)

#shutdown button.
r_button = Button(st,text="shutdown",font=("arial",20,"bold"),bg="red",cursor="plus",command=shutdown)
r_button.place(x = 150,y = 270,width=200,height=50)

#closed button.
r_button = Button(st,text="close",font=("arial",20,"bold"),bg="red",cursor="plus",command=st.destroy)
r_button.place(x = 150,y = 370,width=200,height=50)


st.mainloop()