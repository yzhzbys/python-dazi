from tkinter import *
import string
import random
import time
from datetime import datetime

hh =Tk()
hh.title("鱼王的打字练习课")
string.all=(string.ascii_lowercase+string.ascii_letters + string.digits+ string.punctuation)
Label(hh,text='例文:').grid(row=0)
Label(hh,text='输入').grid(row=1)
Label(hh,text='成绩').grid(row=2)
v1=StringVar()
v2=StringVar()
v3=StringVar()
v4=StringVar()
v5=StringVar()
v1.set("点击开始按钮开始练习")

e1=Entry(hh,text=v1,state='disabled',width=40,font=('宋体',14))
e2=Entry(hh,textvariable=v2,width=40,font=('宋体',14))
e3=Entry(hh,textvariable=v3,state='disabled',width=40,font=('宋体',14),foreground='red')
l1=Label(hh,textvariable=v4,width=20,foreground='red')
l2=Label(hh,textvariable=v5,width=20,foreground='red')

e1.grid(row=0,column=1,padx=10,pady=20)
e2.grid(row=1,column=1,padx=10,pady=20)
e3.grid(row=2,column=1,padx=10,pady=20)
l1.grid(row=4,column=1,padx=10,pady=20)
l2.grid(row=4,column=2,padx=10,pady=20)

grades=Text(hh,width=80,height=7)
grades.grid(row=5,column=0,columnspan=2,pady=5)




class typing:
    
    def __init__(self):
        self.clock=[]
        self.titnum=80#此处设置字数
        self.titstr=''
        self.check=''
        self.check_tt=''
        self.all_spd=0#当前速度
        e2.bind('<Return>',self.score_copy)
    def score_copy(self,event):#因为在class中使用了故需要添加一个event参数
        self.score()#此处定义一个copy的方法执行同样的命令以完成enter键的共存绑定
    def create(self):
        grades.delete(0.0,END)
        self.titstr=''.join(random.sample(string.all.split('/\b/g')[0],self.titnum))
        v1.set(self.titstr)
        self.time_clock().__next__()#迭代器返回下一个元素
        grades.insert(END,"开始:%s \n" % str(self.clock[-1]))
        over.config(state='active')
        start.config(state='disable')
        a=datetime.now()
        '''
        #速度
        self.time_clock().__next__()#迭代器返回下一个元素
        all_time=(self.clock[-1] - self.clock[0]).seconds#最后一次时间和第一次计时
        self.check =v2.get()
        enter_num =0
        for i in range(len(self.check)):
            enter_num += 1
        self.check_tt=''.join("速度:%d字/分"%(enter_num*60/(all_time+0.01)))
        v4.set(self.check_tt)
        '''

    def restart(self):#重置
        self.check_tt=''.join("前次速度:%d字/分"%(self.all_spd))
        v5.set(self.check_tt)
        grades.delete(0.0,END)
        self.titstr=''.join(random.sample(string.all.split(' ')[0],self.titnum))
        v1.set(self.titstr)
        
        self.clock.clear()
        self.time_clock().__next__()#迭代器返回下一个元素
        grades.insert(END,"开始:%s \n" % str(self.clock[-1]))
        over.config(state='active')
        restart.config(state='disable')
        e2.config(state='normal')
        e2.delete(0,END)

            

    def time_clock(self):
        self.clock.append(datetime.now())
        yield#生成器

    def score(self):#结束
        wrong_index=[]
        self.time_clock().__next__()
        grades.insert(END,"结束:%s\n"%str(self.clock[-1]))
        use_time=(self.clock[-1] - self.clock[-2]).seconds
        all_time=(self.clock[-1] - self.clock[0]).seconds#最后一次时间和第一次计时
        self.check =v2.get()
        if len(self.check) > self.titnum:
            v3.set("输入字符数量大于题目了！")
        else:
            enter_num =0#速度
            for i in range(len(self.check)):
                enter_num += 1
            self.all_spd=enter_num*60/(all_time)
            self.check_tt=''.join("当前速度:%d字/分"%(self.all_spd))
            v4.set(self.check_tt)
            
            right_num =0#正确率
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
        restart.config(state='active')
        e2.config(state='disabled')

        
if __name__=='__main__':                    
    tp = typing()

start=Button(hh,text="开始",width=20,command=tp.create )
start.grid(row=3,column=0)
over=Button(hh,text="结束",width=20,command=tp.score ,state='disable')
over.grid(row=3,column=2,sticky=E)
restart=Button(hh,text="再来一次",width=20,command=tp.restart,state='disable')
restart.grid(row=3,column=1)





mainloop()
