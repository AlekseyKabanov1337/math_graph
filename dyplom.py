from tkinter import *
from tkinter.font import BOLD
from PIL import Image as PilImage
from PIL import ImageTk
from numpy.core.numeric import Infinity 
from qual_window import QualWindow
from matplotlib.widgets import Slider
import numpy as np
import matplotlib.pyplot as plt

class Window:
    def __init__(self,width=650,height=700,title="Основное окно",resizable=(False,False)):
        self.root=Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+500+100")
        self.root.resizable(resizable[0],resizable[1])

        self.f1=Frame(self.root)
        self.label=Label(self.f1,text="Пользовательский интерфейс для визуализации и графического представления результатов",
        wraplength=600,bg="#808080",font=("times new romans", 16,"bold"),justify="center",fg="#FFFFFF",)

        self.f2=LabelFrame(self.root,text="Раздел качественного анализа")
        self.qual_text=Label(self.f2,text="После нажатия кнопки откроется окно с качественным анализом уравнения напряжений в упругом шаре",
            font=("times new romans",14),wraplength=600)
        self.button_qual_an=Button(self.f2,width=30,height=2,text="Качественный анализ", font=("times new romans",12,BOLD),
            cursor="plus",bg="#D3D3D3",activebackground="#C0C0C0",borderwidth=3,
            command=self.command_qual)

        self.f3=LabelFrame(self.root,text="Построение графиков")
        img1=PilImage.open(r"resource\grapg_img1.jpg")
        img1=img1.resize((250,42),PilImage.ANTIALIAS)
        grapg_img1=ImageTk.PhotoImage(img1)
        self.label_img1=Label(self.f3,image=grapg_img1)
        self.label_img1.image_ref=grapg_img1
        img2=PilImage.open(r"resource\grapg_img2.jpg")
        img2=img2.resize((250,120),PilImage.ANTIALIAS)
        grapg_img2=ImageTk.PhotoImage(img2)
        self.label_img2=Label(self.f3,image=grapg_img2)
        self.label_img2.image_ref=grapg_img2
        self.graph_text1=Label(self.f3,text="После нажатия кнопки выведется график по данным выше формулам",
            font=("times new romans",14),wraplength=600)
        self.graf_button=Button(self.f3,text="Построение графика",command=drawGraph,width=30,height=2, font=("times new romans",12,BOLD),
            cursor="plus",bg="#D3D3D3",activebackground="#C0C0C0",borderwidth=3,)


    def run(self):
        self.draw_widgets()
        self.root.mainloop()
    

    def draw_widgets(self):
        self.f1.pack(pady=20)
        self.label.pack(ipadx=20, ipady=10)

        self.f2.pack(ipadx=10,ipady=10)
        self.f3.pack(ipadx=10,ipady=10)
        self.label_img1.pack()
        self.label_img2.pack()
        self.qual_text.pack(padx=20, pady=10)
        self.button_qual_an.pack()
        
        self.graph_text1.pack(padx=20, pady=10)
        self.graf_button.pack()
        Button(self.root,text="Выход",font=("times new romans",14),borderwidth=3,bg="red",activebackground="#BC8F8F",cursor="cross",command=self.root.destroy).pack(side=BOTTOM,pady=20)

    def command_qual(self):
        self.child=QualWindow(self.root)


def drawGraph():
    t = np.arange(0, 250, 0.001)
    
    def f(t, thetamax):
        return (0.5*(1/np.sqrt(0.0001*t)**(1/thetamax)))

    n_min = 1
    n_max = 4
    n_init = 2  

    fig, ax = plt.subplots()
    line, = plt.plot(t, (0.5*(1/np.sqrt(0.0001*t)**(1/n_init))), 'r')
    plt.axhline(y=3.6)
    plt.grid()
    plt.xlabel('t')            
    plt.ylabel('tau')

    plt.subplots_adjust(left=0.25, bottom=0.25)


    slider_ax1 = plt.axes([0.25, 0.1, 0.65, 0.03])
    thetamax_slider = Slider(slider_ax1,'N',n_min,n_max,valinit = n_init)

    def update(val):
        line.set_ydata(f(t, thetamax_slider.val))

    thetamax_slider.on_changed(update)

    plt.show()

if __name__ == "__main__":
    window=Window() 
    window.run()
