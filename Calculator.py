# GUI Development using Tkinter
import tkinter as t

app = t.Tk()
app.title('Calculator')
app.geometry('350x400')

result = t.Variable(app)
val =t.Variable(app)
box = t.Entry(app, textvariable = val,width=25,bg = 'beige',highlightthickness=2,font=('Timesroman',16,'normal'))
box.place(x = 20,y =10,height=50)

# highlightbackground and highlightcolor for the border color
box.config(highlightbackground = "grey", highlightcolor= "grey")
input_v = ""

def operate(e):
    global input_v
    input_v += str(e)
    val.set(input_v)

def clear():
    global input_v
    box.delete(0,'end')
    input_v = ''
 
def output(s):
    global input_v
    val.set(eval(input_v))
    input = ""
    
    
t.Button(app, text = '1',bd ='3',font ="calibri",fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('1')).place(x =20,y=140)
t.Button(app, text = '2',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('2')).place(x =100,y=140)
t.Button(app, text = '3',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('3')).place(x =180,y=140)
t.Button(app, text = '+',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('+')).place(x =260,y=140)
t.Button(app, text = '4',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('4')).place(x =20,y=200)
t.Button(app, text = '5',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('5')).place(x =100,y=200)
t.Button(app, text = '6',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('6')).place(x =180,y=200)
t.Button(app, text = '-',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('-')).place(x =260,y=200)
t.Button(app, text = '7',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('7')).place(x =20,y=260)
t.Button(app, text = '8',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('8')).place(x=100,y=260)
t.Button(app, text = '9',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('9')).place(x =180,y=260)
t.Button(app, text = 'x',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('*')).place(x =260,y=260)
t.Button(app, text = '.',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('.')).place(x =20,y=320)
t.Button(app, text = '0',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('0')).place(x =100,y=320)
t.Button(app, text = '=',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :output('=')).place(x =180,y=320)
t.Button(app, text = '/',bd ='3',font ='calibri',fg ='black',bg ='grey',relief ="groove",highlightcolor="grey",width =7,height = 1,command =lambda :operate('/')).place(x=260,y=320)
t.Button(app, text = 'clear',bd ='3',font ='calibri',fg ='red',bg ='grey',relief ="groove",highlightcolor="purple",width =7,height = 1,command =lambda:clear()).place(x=260,y=80)

##    
##t.Button(app, text='+', width = 2, command=plus).place(x=50,y=70)
##t.Button(app, text='-', width = 2, command=minus).place(x=100,y=70)
##t.Button(app, text='x', width = 2, command=lambda:operate('*')).place(x=160,y=70)
##t.Button(app, text='/', width = 2, command=lambda:operate('/')).place(x=210,y=70)
##
##

app.mainloop()


##t.Label(app, text = 'Hello').pack()
##t.Label(app, text = 'Bye').pack()
##t.Label(app, text = 'Hi').pack()

##t.Label(app, text = 'Hello').grid(row=0,column=0)
##t.Label(app, text = 'Bye').grid(row=1,column=1)
##t.Label(app, text = 'Hi').grid(row=2,column=1)

##t.Label(app, text = 'Hello').place(x=100, y=20)
##t.Label(app, text = 'Bye').place(x=130, y=80)
##t.Label(app, text = 'Hi').place(x=200, y=120)

##
##class Abc():
##    a=10
##    def fun(self,v):
##        print(self.a)
##        print('hello')
##
