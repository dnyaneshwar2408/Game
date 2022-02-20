from tkinter import *
from tkinter import messagebox
root=Tk()
root.geometry("1200x800")
root.title("coders")
root.config(bg='#000000')
bg=PhotoImage(file="raj.png")

m2=Label(root,image=bg)
m2.place(x=0,y=0,relwidth=1,relheight=1)
q1=Label(root,text="\nKeywords used in Switch case ?",fg='blue',font=('terminal','20'))
q1.pack()
def thing():
    result1=messagebox.askquestion("","Keyword Found is SWITCH. Want to save ?")
    if  result1=='no':
        print("")
    else :
        global label1
        label1=Label(root,text=" SWITCH ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
        # label1.destroy()

lbtn=PhotoImage(file='map.png')
l1=Label(image=lbtn)
mybutton = Button(root, image=lbtn , command=thing,highlightthickness=0,bd=0)
mybutton.place(x=528,y=249)
def thing1():
    result1=messagebox.askquestion("","Keyword Found is BREAK. Want to save ?")
    if  result1=='no':
        print("")
    else :

        label1=Label(root,text=" BREAK ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn1=PhotoImage(file='carpet.png')
l2=Label(image=lbtn1)
mybutton1 = Button(root, image=lbtn1 , command=thing1,highlightthickness=0,bd=0)
mybutton1.place(x=599,y=514)
def thing3():
    result2=messagebox.askquestion("Yayy","Keyword Found is FLOAT. Want to save ?")
    if  result2=='no':
        print("")
    else :
        label1=Label(root,text=" FLOAT ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn3=PhotoImage(file='books.png')
l3=Label(image=lbtn3)
mybutton3 = Button(root,image=lbtn3 ,command=thing3,highlightthickness=0,bd=0)
mybutton3.place(x=369,y=194)
def thing4():
    result3=messagebox.askquestion("Yayy","Keyword Found is DEFAULT. Want to save ?")
    if  result3=='no':
        print("")
    else :
        label1=Label(root,text=" DEFAULT ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn4=PhotoImage(file='charts.png')
l4=Label(image=lbtn4)
mybutton4 = Button(root, image=lbtn4 , command=thing4,highlightthickness=0,bd=0)
mybutton4.place(x=800,y=225)
def thing5():
    result4=messagebox.askquestion("Yayy","Keyword Found is CASE. Want to save ?")
    if  result4=='no':
        print("")
    else :
        label1=Label(root,text=" CASE ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn5=PhotoImage(file='tijori.png')
l5=Label(image=lbtn5)
mybutton5 = Button(root, image=lbtn5 , command=thing5,highlightthickness=0,bd=0)
mybutton5.place(x=755,y=422)
def thing6():
    result5=messagebox.askquestion("Yayy","Keyword Found is INT. Want to save ?")
    if  result5=='no':
        print("")
    else :
        label1=Label(root,text=" INT ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn6=PhotoImage(file='drawer.png')
l6=Label(image=lbtn6)
mybutton6 = Button(root,image=lbtn6 ,command=thing6,highlightthickness=0,bd=0)
mybutton6.place(x=435,y=469)
def thing7():
    result6=messagebox.askquestion("Yayy","Keyword Found is STRING. Want to save ?")
    if  result6=='no':
        print("")
    else :
        label1=Label(root,text=" STRING ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn7=PhotoImage(file='continent.png')
l7=Label(image=lbtn7)
mybutton7 = Button(root, image=lbtn7, command=thing7,highlightthickness=0,bd=0)
mybutton7.place(x=742,y=605)
def thing8():
    result7=messagebox.askquestion("Yayy","Keyword Found is BOOLEAN. Want to save ?")
    if  result7=='no':
        print("")
    else :
        label1=Label(root,text=" BOOLEAN ",fg='black',font=('terminal','20'))
        label1.pack(side=BOTTOM)
lbtn8=PhotoImage(file='flask.png')
l8=Label(image=lbtn8)
mybutton8 = Button(root, image=lbtn8, command=thing8,highlightthickness=0,bd=0)
mybutton8.place(x=235,y=417)

mainloop()
