from tkinter import *
def bt_click():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1=int(ed1.get())
        num2=int(ed2.get())
        #Se valores não forem númericos imprime a mensagem abaixo:
        lb["text"]=num1+num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores são invalidos"
        lb["bg"]="red"
def bt_clicked():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1=int(ed1.get())
        num2=int(ed2.get())
        #Se valores não forem númericos imprime a mensagem abaixo:
        lb["text"]=num1-num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores são invalidos"
        lb["bg"]="red"
def bt_clacked():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1=int(ed1.get())
        num2=int(ed2.get())
        #Se valores não forem númericos imprime a mensagem abaixo:
        lb["text"]=num1*num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores são invalidos"
        lb["bg"]="red"
def bt_cracked():
    if(str(ed1.get()).isnumeric()and str(ed2.get()).isnumeric()):
        num1=int(ed1.get())
        num2=int(ed2.get())
        #Se valores não forem númericos imprime a mensagem abaixo:
        lb["text"]=num1/num2
        lb["bg"]="#00FA9A"
    else:
        lb["text"]="Valores são invalidos"
        lb["bg"]="red"
i=Tk()
i.title('Programa Financeiro')
i.geometry('980x720+250+30')
lb=Label(i, text="0")
lb.place(x=230,y=200)
bt=Button(i,width="20",text="Soma",command=bt_click)
bt.place(x=230,y=230)
bt2=Button(i,width="20",text="Subtração",command=bt_clicked)
bt2.place(x=400,y=230)
bt3=Button(i,width="20",text="Multiplicação",command=bt_clacked)
bt3.place(x=570,y=230)
bt4=Button(i,width="20",text="Divisão",command=bt_cracked)
bt4.place(x=740,y=230)
ed1=Entry(i)
ed1.place(x=230,y=150)
ed2=Entry(i)
ed2.place(x=230,y=180)
lb2=Label(i,text="Felipe Bortoluzzi dos Santos")
lb2.place(x=230,y=270)
i.mainloop()