#Registration Number :- 323586266
#Name :- D.M.T.Navoda Dissanayake
import tkinter as tk

root= tk.Tk()
root.title("Basic Calculator")
root.geometry("443x580")
root.resizable(False,False)
root.configure(bg = "#000000")

equation=" "

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation =" "
    label_result.config(text=equation)

def  calculate():
    global equation
    result =" "
    if equation != " " :
        try:
            result= eval(equation )
        except:
            result="Error"
            equation=" "
        label_result.config(text=result)



label_result= tk.Label(root,width=30,height=2,text="",font=("Franklin Gothic Book",30))
label_result.pack()

tk.Button(root,text="C",width=9,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#000000",bg="#9ABDD5",command=lambda : clear()).place(x=12,y=113)
tk.Button(root,text="/",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#000000",bg="#E6C74C",command=lambda : show("/")).place(x=228,y=113)
tk.Button(root,text="*",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#000000",bg="#E6C74C",command=lambda : show("*")).place(x=336,y=113)

tk.Button(root,text="7",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("7")).place(x=12,y=209)
tk.Button(root,text="8",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("8")).place(x=120,y=209)
tk.Button(root,text="9",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("9")).place(x=228,y=209)
tk.Button(root,text="-",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#000000",bg="#E6C74C",command=lambda : show("-")).place(x=336,y=209)

tk.Button(root,text="4",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("4")).place(x=12,y=299)
tk.Button(root,text="5",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("5")).place(x=120,y=299)
tk.Button(root,text="6",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("6")).place(x=228,y=299)
tk.Button(root,text="+",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#000000",bg="#E6C74C",command=lambda : show("+")).place(x=336,y=299)

tk.Button(root,text="1",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("1")).place(x=12,y=392)
tk.Button(root,text="2",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("2")).place(x=120,y=392)
tk.Button(root,text="3",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("3")).place(x=228,y=392)
tk.Button(root,text="0",width=9,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show("0")).place(x=11,y=486)

tk.Button(root,text=".",width=4,height=1,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#fff",bg="#263E60",command=lambda : show(".")).place(x=228,y=486)
tk.Button(root,text="=",width=4,height=3,font=("Franklin Gothic Book",30,"bold"), bd=1,fg="#000000",bg="#E6C74C",command=lambda :calculate()).place(x=336,y=392)

root.mainloop()