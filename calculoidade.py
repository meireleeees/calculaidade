from tkinter import *
from tkinter import ttk

#-----importando tkcalendar
from tkcalendar import Calendar, DateEntry


#--- importando dateutil
from dateutil.relativedelta import relativedelta

#------importando datetime --
from datetime import date




janela= Tk()
janela.title("Calculadora de idade")
janela.geometry('310x400')

#cores
cor1= "#3b3b3b" #preto leve
cor2= "#333333" #preto pesado
cor3= "#ffffff" #branco
cor4 = "#fcc058" #laranja


#--------criando frames
frame_cima = Frame(janela, width=310, height =140, pady=0, padx=0, relief=FLAT, bg=cor2)
frame_cima.grid(row=0, column=0)
frame_baixo = Frame(janela, width=310, height =300, pady=0, padx=0, relief=FLAT, bg=cor1)
frame_baixo.grid(row=1, column=0)

#-------criando função

def calcular():
    inicio= cal_1.get()
    terminio= cal_2.get()

    anos = relativedelta(inicio, terminio).years
    
#------separando os valores

dia_1, mes_1, ano_1 = [int(f) for f in inicio.split('/')]

#convertendo em formato datetime

data_inicial = date(ano_1, mes_1, dia_1)

    
#------separando os valores

dia_2, mes_2, ano_2 = [int(f) for f in terminio.split('/')]
data_nascimento = date(ano_2, mes_2, dia_2)

anos = relativedelta(data_inicial, data_nascimento).years
meses = relativedelta(data_inicial, data_nascimento).years
dias = relativedelta(data_inicial, data_nascimento).years

l_app_anos['text'] = dias
l_app_meses['text'] = meses
l_app_dias['text'] = dias



#--------criando label para frame

calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief=FLAT, anchor=CENTER, font=('Ivi 15 bold'), bg=cor2,fg=cor3)
calculadora.place(x=0, y=30)
idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief=FLAT, anchor=CENTER, font=('Arial 35 bold'), bg=cor2,fg=cor4)
idade.place(x=0, y=70)

#--------criando label para frame baixo

data_inicial = Label(frame_baixo, text="Data Inicial", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivi 11'), bg=cor1,fg=cor3)
data_inicial.place(x=40, y=30)

data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivi 11'), bg=cor1,fg=cor3)
data_nascimento.place(x=40, y=70)

#---criando o calendário
cal_1 = DateEntry(frame_baixo, width=13, background="darkblue", fg=cor3, borderwidht=2, data_pattern= 'dd/mm/y', y=2025)
cal_1.place(x=170, y=30)

data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief=FLAT, anchor=NW, font=('Ivi 11'), bg=cor1,fg=cor3)
data_nascimento.place(x=50, y=70)
cal_2 = DateEntry(frame_baixo, width=13, background="darkblue", fg=cor3, borderwidht=2, data_pattern= 'dd/mm/y', y=2025)
cal_2.place(x=10, y=70)


#--------criando label para frame baixo
l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Ivi 25 bold'), bg=cor1,fg=cor3)
l_app_anos.place(x=60, y=135)
l_app_anos_nome = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Ivi 11 bold'), bg=cor1,fg=cor3)
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Ivi 25 bold'), bg=cor1,fg=cor3)
l_app_meses.place(x=140, y=135)
l_app_meses_nome = Label(frame_baixo, text="27", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Ivi 11 bold'), bg=cor1,fg=cor3)
l_app_meses_nome.place(x=140, y=175)


l_app_dias = Label(frame_baixo, text="27", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Ivi 25 bold'), bg=cor1,fg=cor3)
l_app_dias.place(x=220, y=135)
l_app_dias_nome = Label(frame_baixo, text="27", height=1, padx=0, pady=0, relief=FLAT, anchor=CENTER, font=('Ivi 11 bold'), bg=cor1,fg=cor3)
l_app_dias_nome.place(x=220, y=175)


#--------criando botão calcular
b_calcular = Label(frame_baixo, command=calcular ,width=20, text="Calcular idade", height=1, padx=0, pady=0, relief=RAISED,overrelier= "ridge", font=('Ivi 10 bold'), bg=cor1,fg=cor3)
b_calcular.place(x=70, y=225)


janela.mainloop()

