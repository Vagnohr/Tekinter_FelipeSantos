from tkinter import *
i=Tk()
i.title('Programa Financeiro')
i.geometry('980x720+250+30')
lb1=Label(i,text="login",bg="red")
lb1.grid(row=1,column=1)
lb2=Label(i,text="senha",bg="yellow")
lb2.grid(row=3,column=1)
ed1=Entry(i)
ed1.grid(row=1,column=2)
ed2=Entry(i)
ed2.grid(row=3,column=2)
bt1=Button(i,text="Login")
bt1.grid(row=5,column=1)
lb3=Label(i,text="")
lb3.grid(row=0,column=1)
lb4=Label(i,text="")
lb4.grid(row=2,column=0)
lb5=Label(i,text="")
lb5.grid(row=4,column=0)
i.mainloop()