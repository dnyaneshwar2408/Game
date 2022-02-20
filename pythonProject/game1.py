from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
root=Tk()
root.geometry("1200x800")
bs=PhotoImage(file="raj.png")
# bs=Image.open("full.png")
# bs=bs.res
m2=Label(root,image=bs)
m2.place(x=0,y=0,relwidth=1,relheight=1)
# def things():
#     messagebox.askquestion("Yayy","Keyword Found is INT. Want to save ?")
# lbtn=PhotoImage(file='cap.png')
# l1=Label(image=lbtn)
# mybutton = Button(root, image=lbtn ,command=things,highlightthickness=0,bd=0)
# mybutton.place(x=512,y=430)
# def things1():
#     messagebox.askquestion("Yayy","Keyword Found is FLOAT. Want to save ?")
# lbtn1=PhotoImage(file='fish.png')
# l2=Label(image=lbtn1)
# mybutton1 = Button(root, image=lbtn1 , command=things1,highlightthickness=0,bd=0)
# mybutton1.place(x=600,y=348)
# def things2():
#     messagebox.askquestion("Yayy","Keyword Found is FLOAT. Want to save ?")
# lbtn2=PhotoImage(file='gun.png')
# mybutton2 = Button(root, image=lbtn2 , command=things2,highlightthickness=0,bd=0)
# mybutton2.place(x=450,y=538)
# def things3():
#     messagebox.askquestion("Yayy","Keyword Found is FLOAT. Want to save ?")
# lbtn3=PhotoImage(file='mirror.png')
# l3=Label(image=lbtn2)
# l4=Label(image=lbtn3)
# mybutton3 = Button(root, image=lbtn3 , command=things3,highlightthickness=0,bd=0)
# mybutton3.place(x=718,y=290)
# def things4():
#     messagebox.askquestion("Yayy","Keyword Found is FLOAT. Want to save ?")
# lbtn4=PhotoImage(file='paint.png')
# l5=Label(image=lbtn4)
# mybutton4 = Button(root, image=lbtn4 , command=things4,highlightthickness=0,bd=0)
# mybutton4.place(x=438,y=315)
# def things5():
#     messagebox.askquestion("Yayy","Keyword Found is FLOAT. Want to save ?")
# lbtn5=PhotoImage(file='turtle.png')
# l6=Label(image=lbtn5)
# mybutton5 = Button(root, image=lbtn5 , command=things5,highlightthickness=0,bd=0)
# mybutton5.place(x=631,y=522)

mainloop()