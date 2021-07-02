from tkinter import *
from tkinter.font import BOLD 
from PIL import Image as PilImage
from PIL import ImageTk
import numpy as np
import matplotlib.pyplot as plt

class QualWindow:
    def __init__(self,parent,width=650,height=570,title="Окно качественного анализа",resizable=(False,False)):
        self.root=Toplevel(parent)
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+600+150")
        self.root.resizable(resizable[0],resizable[1])

        

        self.label2=Label(self.root,text="Ниже представленна формула напряжённого состояния упругого шара, её качественный анализ производиться буз учёта температурных изменений. \nФазовый портрет открывается при нажатии на кнопку.",
            wraplength=600, font=("times new romans",14),justify=CENTER)
        

        img1=PilImage.open(r"resource\formula_qual.jpg")
        img1=img1.resize((600,90),PilImage.ANTIALIAS)
        formula_img=ImageTk.PhotoImage(img1)
        self.label1=Label(self.root,image=formula_img)
        self.label1.image_ref=formula_img
        self.label3=Label(self.root,text="Данное уравнение преобразуется в систему:",wraplength=600, font=("times new romans",14),justify=CENTER)
        img2=PilImage.open(r"resource\qual_system.jpg")
        img2=img2.resize((300,120),PilImage.ANTIALIAS)
        system_img=ImageTk.PhotoImage(img2)
        self.label4=Label(self.root,image=system_img)
        self.label4.image_ref=system_img
        self.button_qual=Button(self.root,text="Фазовый портрет", font=("times new romans",16,BOLD),justify=CENTER,borderwidth=5,
            cursor="plus",bg="#D3D3D3",activebackground="#C0C0C0",command=drawPhasePortrait)
        self.button_exit=Button(self.root,text="Закрыть окно",justify=CENTER,borderwidth=3,cursor="cross",bg="red",
            activebackground="#BC8F8F",font=("times new romans",14),command=self.root.destroy)
        

        self.label2.pack(padx=20,pady=20)
        self.label1.pack(fill="both")
        self.label3.pack(pady=20)
        self.label4.pack()
        self.button_qual.pack(pady=20)
        self.button_exit.pack()

        self.grab_focus()

    def grab_focus(self):
        self.root.grab_set()
        self.root.focus_set()
        self.root.wait_window()


def drawPhasePortrait():
    
    figure, axes = plt.subplots()

    r=1
    k=0.5

    Y, X = np.mgrid[-1.5*np.pi:1.5*np.pi:20j,
                    -1.5*np.pi:1.5*np.pi:20j]
  
    U = Y
    V = k-(2/r)*Y + (2/r**2)*X
    
    axes.streamplot(X, Y, U, V, 
                color = 'b')
       
    axes.quiver(X, Y, U, V)    

    figure.set_figwidth(5)     
    figure.set_figheight(5)    

    plt.xlabel('u')            
    plt.ylabel('du/dr')        

    plt.show()                 

#создание окна с графиком
#создание многомерной сетки
#задание функций векторов
#построение потока векторов:
#построение векторного поля поверх потока (стрелок)
#определение ширины графика
#определение высоты графика
#название горизонтальной оси
#название вертикальной оси
#вывод графика