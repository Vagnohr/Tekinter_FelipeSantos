#comando abaixo importa tudo da biblioteca que é necessaria
#para a criação de telas. (ASTERISCO significa tudo)
from tkinter import *
#i (instanciar) recebe o objeto Tk
i=Tk()
#gerar titulo da jenela
i.title('Programa Financeiro')
#propriedade que altera o tamanho da janela (980x720) e distancia da direita e topo a tela (250x30)
i.geometry('980x720+250+30')
#propriedades graficas cor de fundo da tela (bg) ou (background)
#não pode passar o i com ponto! DEVE SER i[]
i["bg"]="dark red"
#cria o icone na jenela, voce deve ter a imagem no mesmo local do codigo.
#i.wm_icontbitmap('icone.ico')
#cria um label e posiciona (place) ele em relação a tela
lb=Label(i,text='Nome do usuario')
lb.place(x=100, y=100)
#cria um botão e posiciona (place) ele em relação a label
bt=Button(i,width='20',text='OK')
bt.place(x=230,y=100)
#gera a janela grafica
i.mainloop()