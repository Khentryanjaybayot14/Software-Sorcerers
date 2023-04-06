from tkinter import *
import webbrowser

window = Tk()
window.minsize(1200 ,700)
window.maxsize(1200 ,700)

window.configure(bg="dark green")

heading = Label(window, text="Software Scorcerers", bg="dark green", fg="yellow", font=("algerian", 30))
heading.pack()
#insert image
image1 = PhotoImage(file="D:/ppt bg.gif")

leader_pic = Label(window, image=image1)
leader_pic.place(x=536, y=120)

l1 = Label(window, image=image1)
l1.place(x=50, y=450)
l2 = Label(window, image=image1)
l2.place(x=283, y=450)
l3 = Label(window, image=image1)
l3.place(x=535, y=450)
l4 = Label(window, image=image1)
l4.place(x=780, y=450)
l5 = Label(window, image=image1)
l5.place(x=1010, y=450)

def callback(url):
    webbrowser.open_new_tab(url)
#label of names
leader = Label(window, text="Bayot KRJ,", bg="dark green", fg="white", font=("calibry body", 12) )
leader.place(x=537, y=230)

l_name1 = Label(window, text="Aribal C,", bg="dark green", fg="white", font=("calibry body", 12) )
l_name1.place(x=50, y=560)
aribal_link = Label(window, text="https://www.facebook.com/", fg="light blue", bg="dark blue", font=("bold", 10))
aribal_link.place(x=50,y=583)
aribal_link.bind("<Button>", lambda e: callback("https://www.facebook.com/"))

l_name2 = Label(window, text="Apostol BJ,", bg="dark green", fg="white", font=("calibry body", 12) )
l_name2.place(x=284, y=560)
apostol_link = Label(window, text="https://www.facebook.com/", fg="light blue", bg="dark blue", font=("bold", 10))
apostol_link.place(x=285,y=583)
apostol_link.bind("<Button>", lambda e: callback("https://www.facebook.com/"))

l_name3 = Label(window, text="Balusada MG,", bg="dark green", fg="white", font=("calibry body", 12) )
l_name3.place(x=536, y=560)

l_name4 = Label(window, text="Baslan CM,", bg="dark green", fg="white", font=("calibry body", 12) )
l_name4.place(x=780, y=560)

l_name5 = Label(window, text="Monsuller D,", bg="dark green", fg="white", font=("calibry body", 12) )
l_name5.place(x=1010, y=560)

#links in fb profile


window.mainloop()