from tkinter import*
root=Tk()
root["bg"]="grey"
c=Label(root, text="CALCULATOR",bg="grey",fg="blue").pack()
l=Label(root,text="ENTER THE FIRST VALUE",bg="white",fg="cyan")
l.place(x=50, y=150)
var1=DoubleVar()
k=Entry(root,textvariable=var1)
k.place(x=450,y=150, width=220)

l2=Label(root,text="ENTER THE SECOND VALUE",bg="white",fg="cyan")
l2.place(x=50, y=200)
var2=DoubleVar()
k2=Entry(root,textvariable=var2)
k2.place(x=450,y=200, width=220)


def ts():
	total=float(k.get())+float(k2.get())
	f=Label(root,text=f"Total = {total}"). place(x=300,y=255)
	
def tp():
	total1=float(k.get())-float(k2.get())
	f1=Label(root,text=f"Total  = {total1}"). place (x=300,y=355)
	
def tm():
    total2= float(k.get())*float(k2.get())
    F2=Label(root,text=f"Total = {total2}"). place (x=300,y=455)
def td()    :
    total3	= float(k.get())/float(k2.get())
    F3=Label(root,text=f"Total = {total3}"). place (x=300,y=555)
def clear():
    k.delete(0,END)	
    k2.delete(0,END)
       
b=Button(root,text="Add",command=ts,bg="white", fg="yellow").place(x=100,y=250)

b1=Button(root,text="Sub",command=tp,bg="white",fg="yellow"). place (x=100,y=350)

b2=Button(root,text="multiple",command=tm,bg="white",fg="yellow").place(x=100, y=450)

b3=Button(root,text="division",command=td,bg="white",fg="yellow"). place(x=100, y=550)

clear=Button(root, text="CLEAR", command=clear,bg="white",fg="cyan"). place (x=100,y=700)
Exit =Button(root,text="EXIT", command=root.destroy,bg="white",fg="cyan"). place (x=300,y=700)
root.mainloop()
