from tkinter import *
import string
import random
from datetime import datetime

hh =Tk()
hh.title("鱼王的打字练习课")
Label(hh,text='例文:').grid(row=0)
Label(hh,text='输入').grid(row=1)
Label(hh,text='成绩').grid(row=2)
v1=StringVar()
v2=StringVar()
v3=StringVar()
v1.set("点击开始按钮开始练习")

e1=Entry(hh,text=v1,state='disabled',width=40,font=('宋体',14))
e2=Entry(hh,textvariable=v2,width=40,font=('宋体',14))
e3=Entry(hh,textvariable=v3,width=40,font=('宋体',14),foreground='red')

e1.grid(row=0,column=1,padx=10,pady=20)
e2.grid(row=1,column=1,padx=10,pady=20)
e3.grid(row=2,column=1,padx=10,pady=20)

grades=Text(hh,width=80,height=7)
grades.grid(row=4,column=0,columnspan=2,pady=5)




class typing:
    
    def __init__(self):
        self.clock=[]
        self.titnum=20
        self.titstr=''
        self.check=''
        e2.bind('<Return>',self.score_copy)
    def score_copy(self,event):#因为在class中使用了故需要添加一个event参数
        self.score()#此处定义一个copy的方法执行同样的命令以完成enter键的共存绑定
    def create(self):
        grades.delete(0.0,END)
        self.titstr=''.join(random.sample(string.ascii_lowercase.split(' ')[0],self.titnum))
        v1.set(self.titstr)
        self.time_clock().__next__()#迭代器返回下一个元素
        grades.insert(END,"开始:%s \n" % str(self.clock[-1]))
        over.config(state='active')

    def time_clock(self):
        self.clock.append(datetime.now())
        yield#生成器

    def score(self):
        wrong_index=[]
        self.time_clock().__next__()
        grades.insert(END,"结束:%s\n"%str(self.clock[-1]))
        use_time=(self.clock[-1] - self.clock[-2]).seconds
        self.check =v2.get()
        if len(self.check) > self.titnum:
            v3.set("输入字符数量大于题目了！")
        else:
            right_num =0
            for i in range(len(self.check)):
                if self.check[i] == self.titstr[i]:
                    right_num += 1
                else:
                    wrong_index.append(i)
            if right_num == self.titnum:
                v3.set("完全正确，正确率%.2f%%用时:%s秒"%((right_num*1.0)/self.titnum*100,use_time))
            else:
                v3.set("正确率%.2f%%用时:%s秒"%((right_num*1.0)/self.titnum*100,use_time))
                grades.insert(END,"题目:%s\n"% self.titstr)
                tag_info= list(map(lambda x:'4.'+str(x+3),wrong_index))
                grades.insert(END,"结果:%s\n"% self.check)
                for i in range(len(tag_info)):
                    grades.tag_add("tag1",tag_info[i])
                    grades.tag_config("tag1",background='red')
                    over.config(state='disabled')
       
                    
typing = typing()


Button(hh,text="开始",width=20,command=typing.create ).grid(row=3,column=0)
over=Button(hh,text="结束",width=20,command=typing.score ,state='disable')
over.grid(row=3,column=1,sticky=E)





mainloop()
