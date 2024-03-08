from tkinter import *
win = Tk()
win.title("Calculator") #title of windows
win.geometry('380x380') #size of windows
win.resizable(0,0) #disable resize the window


def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)




#function to clear input faild
def bt_clear():
    global expression
    expression = ""
    input_text.set("")


#function to equale button
def btn_equal():
    global expression
    result = str(eval(expression))
    input_text.set(result)
    expression= ""





expression = ""
input_text = StringVar()

#input faield frame
input_frame = Frame(win, width=350, height=100, border=5)
input_frame.pack(side=TOP)

input_faild = Entry(input_frame,font=('arial',18,'bold'), width=50, justify=RIGHT, textvariable= input_text)
input_faild.grid(row=0,column=0)

#increase the height of input faield
input_faild.pack(ipady=5)

#button frame
btns_frame = Frame(win,width=310,height=270,border=1)
btns_frame.pack()

clear = Button(btns_frame, text='C',width=38, height=3, command=lambda: bt_clear()).grid(row=0, column=0, columnspan=3, padx=1,pady=1)
divide = Button(btns_frame,text='/',width=10, height=3, command=lambda: btn_click('/')).grid(row=0, column=3, padx=1, pady=1)

#button secund row
sevin = Button(btns_frame, text='7', width=10, height=3, command=lambda: btn_click(7)).grid(row=1, column=0,padx=1,pady=1)
eight = Button(btns_frame, text='8', width=10, height=3, command=lambda: btn_click(8)).grid(row=1, column=1,padx=1,pady=1)
nign = Button(btns_frame, text='9', width=10, height=3, command=lambda: btn_click(9)).grid(row=1, column=2,padx=1,pady=1)
mutiply = Button(btns_frame, text='*', width=10, height=3, command=lambda: btn_click("*")).grid(row=1, column=3,padx=1,pady=1)

#button third row
four = Button(btns_frame, text='4', width=10, height=3, command=lambda: btn_click(4)).grid(row=2, column=0,padx=1,pady=1)
five = Button(btns_frame, text='5', width=10, height=3, command=lambda: btn_click(5)).grid(row=2, column=1,padx=1,pady=1)
six = Button(btns_frame, text='6', width=10, height=3, command=lambda: btn_click(6)).grid(row=2, column=2,padx=1,pady=1)
nigatev = Button(btns_frame, text='-', width=10, height=3, command=lambda: btn_click('-')).grid(row=2, column=3,padx=1,pady=1)

#button fourth row
one = Button(btns_frame, text='1', width=10, height=3, command=lambda: btn_click(1)).grid(row=3, column=0,padx=1,pady=1)
two = Button(btns_frame, text='2', width=10, height=3, command=lambda: btn_click(2)).grid(row=3, column=1,padx=1,pady=1)
three = Button(btns_frame, text='3', width=10, height=3, command=lambda: btn_click(3)).grid(row=3, column=2,padx=1,pady=1)
plus = Button(btns_frame, text='+', width=10, height=3, command=lambda: btn_click('+')).grid(row=3, column=3,padx=1,pady=1)

##button fifth row
zero = Button(btns_frame, text='0', width=10, height=3, command=lambda: btn_click(0)).grid(row=4, column=0,padx=1,pady=1)
point = Button(btns_frame, text='.', width=10, height=3, command=lambda: btn_click('.')).grid(row=4, column=1,padx=1,pady=1)
equal = Button(btns_frame, text='=', width=25,height=3, command=lambda: btn_equal()).grid(row=4,column=2, columnspan=2,padx=1,pady=1)

win.mainloop() #view window