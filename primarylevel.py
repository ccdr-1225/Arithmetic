import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox,tkinter.filedialog,tkinter.font
#我们在刚开始上课的时候介绍过一�?小�?�四则运算自动生成程序的例子，�?�实现它，�?�求�?
# ①　能�?�自动生成四则运算练习�??
# ②　�?以定制�?�目数量
# �?　用户�?以选择运算�?
# ④　用户设置最大数（�?�十以内、百以内等）
# ⑤　用户选择�?否有�?号、是否有小数
# ⑥　用户选择输出方式（�?�输出到文件、打印机等）
# ⑦　最好能提供图形用户界面（根�?�?己能力选做，以完成上述功能为主�?
#maininterface
window=tk.Tk() 
window.geometry('1000x600+200+200')
window.title('Primary Arithmetic')




#frame_1 tittle&Preview
mathquestion=("This is Preview")
lable_main=tk.Label(window,text='  Math Practice',width="1000",height="2",font=("幼圆",50,"bold"),fg="#83DAFF",bg="#F6FFC0")
lable_main.pack()
# lable_display=tk.Label(frame_1,text='This is Preview',width="100",height="2",font=("幼圆",10,"bold"),fg="#83DAFF",bg="#F6FFC0")
# lable_display.pack()
stext = tk.scrolledtext.ScrolledText(window,width=20,height=3,font=("幼圆", 16,),fg='black',bg="#F4FFB7")#创建下拉�?
stext.pack()#设置下拉框位�?
stext.insert('end',mathquestion)


#frame_2 settings

lable_main=tk.Label(window,text='Settings',width="30",height="2")
lable_main.pack()

label_qnumber=tk.Label(window, text='Question num :',height=2,font=("幼圆", 12),anchor='center')
label_qnumber.place(x=200, y=245)
numenter=tk.Entry(window,width="10")
numenter.place(x=340,y=253)

label_level=tk.Label(window, text='Question level :',height=2,font=("幼圆", 12),anchor='center')
label_level.place(x=530, y=245)
level_enter=tk.Entry(window,width="10")
level_enter.place(x=690,y=253)

label_level=tk.Label(window, text='Formula :',height=2,font=("幼圆", 12),anchor='center')
label_level.place(x=200, y=310)
label_level=tk.Label(window, text='More Settings :',height=2,font=("幼圆", 12),anchor='center')
label_level.place(x=200, y=383)
var_dafult=tk.IntVar()
var_dafult.set(1)
sybutton=tk.Radiobutton(window,text=" ＋ ", value=1,variable=var_dafult,font=("幼圆", 25))
sybutton.place(x=340,y=308)
sybutton=tk.Radiobutton(window,text=" ─ ",value=2,variable=var_dafult,font=("幼圆", 25))
sybutton.place(x=440,y=308)
sybutton=tk.Radiobutton(window,text=" × ",value=3,variable=var_dafult,font=("幼圆", 20))
sybutton.place(x=550,y=313)
sybutton=tk.Radiobutton(window,text=" ÷ ",value=4,variable=var_dafult,font=("幼圆", 20))
sybutton.place(x=630,y=313)

b_button=tk.Checkbutton(window,text=" () ",font=("幼圆", 10))
b_button.place(x=340,y=383)
bbutton=tk.Checkbutton(window,text=" Print to File ",font=("幼圆", 10))
bbutton.place(x=340,y=420)
bbutton=tk.Checkbutton(window,text=" Print to Mechine ",font=("幼圆", 10))
bbutton.place(x=650,y=420)

create_button=tk.Button(window,text="Create",height=2,font=("幼圆", 12),bg='#FF4081',fg='white',width=20)
create_button.place(x=300,y=475)
reset_button=tk.Button(window,text="Reset",height=2,font=("幼圆", 12),bg='#22C9C9',fg='white',width=20)
reset_button.place(x=600,y=475)


window.mainloop()