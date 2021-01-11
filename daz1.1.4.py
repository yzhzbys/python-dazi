from tkinter import *
import string
import random
import time
import tkinter
import re
from datetime import datetime

hh =Tk()
hh.rowconfigure(1, weight=1)
hh.columnconfigure(0, weight=1)

tit1=Text(hh,fg='#78a2a1',wrap='none',bg='#68312e',state='disabled',width=77,height=1,font=('楷体',11,'bold'))
tit2=Text(hh,fg='#ccc',state='disabled',width=77,height=1,font=('楷体',11,'bold'))




hh.title("鱼王的打字练习课")
Label(hh,text='例文:',justify='right',font=('黑体',12),width=5).grid(row=0,column=0)
Label(hh,text='输入',justify='right',font=('黑体',12),width=5).grid(row=1,column=0)
Label(hh,text='下一行',justify='right',font=('黑体',12),width=5).grid(row=2,column=0)
Label(hh,text='成绩').grid(row=3,column=3)
v2=StringVar()  
v3=StringVar()
v4=StringVar()
v5=StringVar()
v6=StringVar()
tit1.insert(END,"点击开始按钮开始练习")




class typing:
    
    def __init__(self):

        self.i=0
        self.a=''#第一段例文字数
        self.b=''
        self.c=''#直到当前的例文
        self.d=''#当输入超过当前例文时的前部分
        self.e=''#当输入超过当前例文时的后部分
        self.clock=[]   
        self.string_all=open('文章.txt','r')#读取文章
        self.titnum=50#此处设置字数
        self.b_all=self.strQ2B(self.string_all.read())#将输入文章字符变更为半角
        self.all=''.join(self.b_all.splitlines())#read返回字符串 .splitlines()去除换行
        self.all_num=len(self.all)
        self.a=self.all[:self.titnum]
        self.b=self.all[self.titnum:self.titnum*2]
        print(self.b)
        self.string_tit=self.a
        self.check_a=''#全篇判断
        self.check_b=''#单行判断
        self.check_tt=''#速度提示
        self.tips=''#提示
        self.all_spd=0#当前速度
        self.wrong_index=[]#错误索引
        v2.trace('w',self.text_trace)
    def strQ2B(self,ustring):
        #全角转半角
        rstring = ""
        for uchar in ustring:
            inside_code=ord(uchar)
            if inside_code == 12288:                              #全角空格直接转换            
                inside_code = 32 
            elif (inside_code >= 65281 and inside_code <= 65374): #全角字符（除空格）根据关系转化
                inside_code -= 65248

            rstring += chr(inside_code)
        return rstring
    def strB2Q(self,ustring):
        #半角转全角
        rstring = ""
        for uchar in ustring:
            print(uchar)
            inside_code=ord(uchar)
            if inside_code == 32:                                 #半角空格直接转化                  
                inside_code = 12288
            elif inside_code >= 32 and inside_code <= 126:        #半角字符（除空格）根据关系转化
                inside_code += 65248

            rstring += chr(inside_code)
        return rstring
       

    def tit_change(self):#变更例文
        self.i+=1
        print(self.i)
        tit1.config(state='normal')
        tit2.config(state='normal')
        tit1.delete(1.0,END)
        tit2.delete(1.0,END)
        self.a=self.all[self.titnum*self.i:self.titnum*(self.i+1)]
        self.b=self.all[self.titnum*(self.i+1):self.titnum*(self.i+2)]
        tit1.insert(0.0,self.a)
        tit2.insert(0.0,self.b)
        tit1.config(state='disable')
        tit2.config(state='disable')
        if len(self.b)==0:#最后一页
            over.config(state='active')
        if len(self.a)==0:#完成页
            v2.set("本篇文章已完成")
            e2.config(state='disable')
            self.score()
            v6.set('恭喜你完成本篇章')
            over.config(state='disable')

            

    def text_trace(self, var, mode, event):#此为v2(输入栏)的跟踪项
        a=v2.get()
        c=self.strQ2B(a)
        print(c)#此处显示的是我想让他显示在输入栏的值（半角字符）
        v2.set(c)
        tag1_index=[]
        tit1.tag_delete('tag1')
        tag1_index.append(len(a))
        print(tag1_index)
        tag1_info= list(map(lambda x:'1.'+str(x),tag1_index))
        b=tit1.get(0.0,END)[:-1]#text控件最后有一个换行符
        self.tips=''.join("还需要输入%d个字呀\n"%(len(b)-len(a)))
        v6.set(self.tips)
        if len(a) <len(b):#此处添加判断目的是优化指示tag
            tit1.tag_add('tag1',tag1_info)
            tit1.tag_config('tag1',background='#ccc')



            
    def enter(self,event):#回车触发事件 因为在class中使用了故需要添加一个event参数
        #self.score()#此处定义一个copy的方法执行同样的命令以完成enter键的共存绑定
        a=v2.get()
        print(len(a))
        b=tit1.get(0.0,END)[:-1]
        print(len(b))
        if len(a)>=len(b):#判断输入栏内的字符数量
            self.d = a[:len(b)]
            self.e = a[len(b):]
            self.c=self.all[:self.titnum*(self.i+1)]
            self.check_al()
            self.tit_change()#变更例文
            e2.delete(0,END)
            e2.insert(0,self.e)
        else:
            self.tips=''.join("还需要输入%d个字呀\n"%(len(b)-len(a)))
            v6.set(self.tips)

        
       
    def create(self):#开始
        print(self.all)
        cutout.config(state='active')
        tit1.config(state='normal')
        tit2.config(state='normal')
        tit1.delete(0.0,END)
        grades.delete(0.0,END)
        tit1.insert(END,self.a)
        tit2.insert(END,self.b)
        self.time_clock().__next__()#迭代器返回下一个元素
        tit1.config(state='disable')
        tit2.config(state='disable')
        grades.config(state='normal')
        grades.insert(END,"开始:%s \n" % str(self.clock[-1]))
        start.config(state='disable')
        a=datetime.now()
        e2.config(state='normal')
       
        grades.config(state='disable')
        

    def restart(self):#重置
        restart.config(state='disable')
        cutout.config(state='active')
        e2.config(state='normal')
        grades.config(state='normal')
        self.check_tt=''.join("前次速度:%d字/分"%(self.all_spd))
        v5.set(self.check_tt)
        v4.set('本次速度:--字/分')
        grades.delete(0.0,END)
        self.i=-1
        self.check_b=''#重置时清除输入内容
        self.tit_change()
        e2.delete(0,END)
        self.clock.clear()
        self.time_clock().__next__()#迭代器返回下一个元素
        grades.insert(END,"开始:%s \n" % str(self.clock[-1]))
        grades.config(state='disable')

    def check_al(self):     #验证输入完成的内容   
        
        right_num = 0 #正确率
        
        self.time_clock().__next__()
        use_time=(self.clock[-1] - self.clock[0]).seconds
        self.check_a=self.d
        self.check_b=self.check_b+self.check_a
        self.check_num=len(self.check_b)
        print("当前输入:",self.check_a)
        print("已输入:",self.check_b)
        print("当前例文:",self.a)
        print('已完成例文:',self.c)
        e3.config(state='normal')
        for i in range(len(self.check_b)):
            if self.check_b[i] == self.c[i]:
                right_num += 1
            else:
                self.wrong_index.append(i)
            if right_num == len(self.all):
                v3.set("完全正确，正确率%.2f%%用时:%s秒"%((right_num*1.0)/self.check_num*100,use_time))
            else:
                v3.set("正确率%.2f%%用时:%s秒"%((right_num*1.0)/self.check_num*100,use_time))
        e3.config(state='disable')
    def time_clock(self):#计时器
        self.clock.append(datetime.now())
        yield#生成器


    def score(self):#结束
        grades.config(state='normal')
        a=v2.get()
        print(len(a))
        b=tit1.get(0.0,END)[:-1]
        if len(a) >= len(b):#输入完成，待改进
            over.config(state='active')
            self.d = a[:len(b)]
            self.e = a[len(b):]
            self.c=self.all[:self.titnum*(self.i+1)]
            self.check_al()
            grades.insert(END,"结束:%s\n"%str(self.clock[-1]))
            all_time=(self.clock[-1] - self.clock[0]).seconds#最后一次时间和第一次计时
            
            self.all_spd=len(self.check_b)*60/(all_time)
            self.check_tt=''.join("本次速度:%d字/分"%(self.all_spd))
            v4.set(self.check_tt)
            grades.insert(END,"题目:%s\n"% self.c)
            tag_info= list(map(lambda x:'4.'+str(x+3),self.wrong_index))
            print(tag_info)
            grades.insert(END,"结果:%s\n"% self.check_b)
            for i in range(len(tag_info)):
                grades.tag_add("tag2",tag_info[i])
                grades.tag_config("tag2",background='red')
        
            restart.config(state='active')
            grades.config(state='disable')
            e2.config(state='disable')
            v6.set('恭喜你完成本篇章')
            over.config(state='disable')
            cutout.config(state='disable')
            
        elif len(a)<len(b):
            self.tips=''.join("还需要输入%d个字呀\n"%(len(b)-len(a)))
            v6.set(self.tips)

    def cut(self):#还未完成但希望终止测试
        grades.config(state='normal')
        a=v2.get()
        print(len(a))
        b=tit1.get(0.0,END)[:-1]
        
        self.d = a[:len(b)]
        self.e = a[len(b):]
        self.c=self.all[:self.titnum*(self.i+1)]
        self.check_al()
        grades.insert(END,"结束:%s\n"%str(self.clock[-1]))
        all_time=(self.clock[-1] - self.clock[0]).seconds#最后一次时间和第一次计时
        
        self.all_spd=len(self.check_b)*60/(all_time)
        self.check_tt=''.join("本次速度:%d字/分"%(self.all_spd))
        v4.set(self.check_tt)
        grades.insert(END,"题目:%s\n"% self.c)
        tag_info= list(map(lambda x:'4.'+str(x+3),self.wrong_index))
        print(tag_info)
        grades.insert(END,"结果:%s\n"% self.check_b)
        for i in range(len(tag_info)):
            grades.tag_add("tag2",tag_info[i])
            grades.tag_config("tag2",background='red')
    
        over.config(state='disabled')
        restart.config(state='active')
        e2.config(state='disabled')
        grades.config(state='disable')

            

        
if __name__=='__main__':                    
    tp = typing()
    tp.string_all.close()

  
e2=Entry(hh,textvariable=v2,state='disabled',width=77,font=('楷体',11,'bold'))
e2.bind('<Return>',tp.enter) 
e3=Entry(hh,textvariable=v3,state='disabled',width=30,font=('宋体',8),foreground='red')
l1=Label(hh,textvariable=v4,width=20,foreground='red')
l2=Label(hh,textvariable=v5,width=20,foreground='red')

tit1.grid(row=0,column=1,columnspan=3,ipadx=80,ipady=1,padx=10,pady=1)
e2.grid(row=1,column=1,columnspan=3,ipadx=80,ipady=1,padx=10,pady=1)
tit2.grid(row=2,column=1,columnspan=3,ipadx=80,ipady=1,padx=10,pady=1)
e3.grid(row=4,column=3,padx=10,pady=1)
l1.grid(row=5,column=3,padx=10,pady=1,)
l2.grid(row=6,column=3,padx=10,pady=1)

grades=Text(hh,width=90,height=7,font=('宋体',10),state='disable')
grades.grid(row=3,column=1,columnspan=1,rowspan=3,pady=1,padx=10)
scroll=tkinter.Scrollbar(width=20,command=grades.yview)
grades.config(yscrollcommand = scroll.set)
scroll.grid(row=3,column=2,rowspan=3,sticky=S  + N+E,padx=1)

tips=Label(hh,textvariable=v6,width=40,height=1,pady=5)
tips.grid(row=6,column=1,columnspan=1,rowspan=1)


start=Button(hh,text="开始",width=20,command=tp.create )
start.grid(row=3,column=0)
over=Button(hh,text="结束",width=20,command=tp.score ,state='disable')
over.grid(row=5,column=0)
restart=Button(hh,text="再来一次",width=20,command=tp.restart,state='disable')
restart.grid(row=4,column=0)
cutout=Button(hh,text="终止",width=20,command=tp.cut,state='disable')
cutout.grid(row=6,column=0)






mainloop()
