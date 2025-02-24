from tkinter import *
#criando uma fução para clique no botão
def bt_click():
    #o label que usa propriedade TEXT recebera a mensagem "Trocou o texto"
    lb["text"]="Troucou o texto"
    #esse print abaixo exibe o texto na tela do console.
    print("O botão foi clicado!")
def bt_clickar():
    #esse print exibe o testo digitaod na caixa de texto e exibe na label da tela
    print(ed.get())
    lb['text']=ed.get()
#i (instanciar) recebe o objeto Tk
i=Tk()
#gerar titulo na janela
i.title('Programa financeiro')
i.geometry('980X720+250+30')
i["bg"]='dark red'
#i.wm._iconbitmap('icone.ico')
lb=Label(i,text='Nome do Usuario')
lb.place(x=100,y=100)
bt=Button(i,width="20",text='OK',command=bt_click)
bt.place(x=230,y=100)
#o condigo abaixo cria um botão que posiciona abaixo do botão OK
bt=Button(i,width="20",text='Capturar',command=bt_click)
bt.place(x=230,y=190)
#cria a caixa de texo para digitar algo dentro
ed=Entry(i)
ed.place(x=230,y=150)
i.mainloop()