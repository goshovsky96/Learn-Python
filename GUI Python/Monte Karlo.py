from math import*
from tkinter import*
from random import*

window = Tk()
window.title('Monte Carlo')
window.geometry('450x550')
x0,y0,xn,yn=2,2,402,402

def circle(): 
    window.geometry('450x580')
    canvas.create_rectangle(x0,y0,xn,yn,  fill = '#333')
    canvas.create_oval(x0+10,y0+10,xn-10,yn-10, outline='#aaa')
    n=int(ent.get())
    first=0
    for i in range(1,n+1):
        x=uniform(x0,xn)
        y=uniform(y0,yn)  
        if sqrt(pow(x-xn/2-5,2)+pow(y-xn/2-5,2))<xn/2-10:
                canvas.create_oval(x-2,y-2,x+2,y+2,fill='#f00')
                first+=1
        else:
                canvas.create_oval(x-2,y-2,x+2,y+2,fill='#fff')
    second=first/(n+1)
    res = second*xn*xn
    result1 = 'В колі: {}'.format(first)
    result3 = 'Точна площа: {}'.format(pi*pow(xn/2,2))
    result2 = 'Наближена площа: {}'.format(res)
    label1.configure(text=result1)
    label2.configure(text=result2)
    label3.configure(text=result3)

label=Label(window, text='Графік квaдрата та кола', font='Calibri 15')
label1=Label(window,  font='Calibri 10')
label2=Label(window,  font='Calibri 10')
label3=Label(window, font='Calibri 10')
button = Button(window, text=' + ', command = circle)
button_exit= Button(window, text=' x ', command = window.destroy)
canvas=Canvas(window, height=404, width = 404, bg='#333')

canvas.place(x=20, y=40)
canvas.create_oval(x0,y0,xn,yn, outline='#aaa') 
label.place(x=140, y=5)
Label(window,text='Кількість точок: ').place(x=70, y=475)
ent = Entry()
ent.config(fg = "silver", font = 'Courer_New 10')
ent.insert(0, '1')
ent.bind('<Return>', circle())
ent.place(x=165, y=475)
button.place(x=320, y=473)
button_exit.place(x=344, y=473)
label1.place(x=20, y=500)
label2.place(x=20, y=525)
label3.place(x=20, y=550)

window.mainloop()