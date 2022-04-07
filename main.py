import random
import time
import os
 
def pdhs(pd):#定义函数，用于判断是否进行游戏
    if pd == '1':
        with open('ck.txt') as f:
            dic=[]
            for line in f.readlines():
                    line = line.strip('\n')
                    b = line.split(',')
                    dic.append(b)
            dicta = dict(dic)
        with open('da.txt') as d: #打开储存答案的文件
            dic1=[] #定义一个空的列表
            for line1 in d.readlines():
                line1 = line1.strip('\n')
                h = line1.split(',')
                dic1.append(h)
        dictb = dict(dic1)
        dictc = {} 
        for k in random.sample(dicta.keys(), 1):
            v = dicta[k]
            dictc.update(dict({k:v}))
            points = 0 #初始化答对的题目数量
            
        print("请说出'",v,"'的下一句：")
        ans = input("在这里输入：")
        print('---------------------------------------')
        if ans == dictb[k]:
            os.system('clear')
            print("回答正确，很赞哦  (๑•̀ㅂ•́)و✧")
            print('---------------------------------------')
            points = points+1
            time.sleep(1)
            print('要继续吗？，\n如果是请输入：1\n退出游戏请输入：0\n在答题过程中随时可以输入：0来退出游戏')
            xz = input('在这里输入:')
            print('---------------------------------------')
        elif ans == '0':
            os.system('clear')
            print(f'您本次答对了{points}.题，加油，下次你可以做的更好的!(~^o^~)!')
        elif ans != dictb[k]:
            os.system('clear')
            print('回答错误，下次继续努力')
            print('---------------------------------------')
            time.sleep(1)
            print('要继续吗？，\n如果是请输入：1\n退出游戏请输入：0\n在答题过程中随时可以输入：0来退出游戏')
            xz = input('在这里输入:')
            print('---------------------------------------')
        s = 0 #定义一个变量
        while xz == '1':  #判断是否继续游戏
            os.system('clear')
            with open('ck.txt') as f:
                dic=[]
                for line in f.readlines():
                    line = line.strip('\n')
                    b = line.split(',')
                    dic.append(b)
                    dicta = dict(dic)
            with open('da.txt') as d:
                dic1=[]
                for line1 in d.readlines():
                    line1 = line1.strip('\n')
                    h = line1.split(',')
                    dic1.append(h)
            dictb = dict(dic1)
            dictc = {}

            for k in random.sample(dicta.keys(), 1):
                    v = dicta[k]
                    l = dicta[k]
                    dictc.update(dict({k:v}))

            s1 = s+1 #判断数据加1
            
            while l == v and s1 > 1: #符合条件循环，此循环体为了解决题目重复问题
                with open('ck.txt') as f:
                    dic=[]
                    for line in f.readlines():
                        line = line.strip('\n')
                        b = line.split(',')
                        dic.append(b)
                    dicta = dict(dic)
                with open('da.txt') as d:
                    dic1=[]
                    for line1 in d.readlines():
                        line1 = line1.strip('\n')
                        h = line1.split(',')
                        dic1.append(h)
                dictb = dict(dic1)
                dictc = {}

                for k in random.sample(dicta.keys(), 1):
                    v = dicta[k]
                    l = dicta[k] #记录上一道题的值
                    dictc.update(dict({k:v}))
            #上述循环体是为了解决新题目小概率与旧题目重复的问题
                    
                    
            print("请说出'",v,"'的下一句：")
            ans = input("在这里输入：")
            print('---------------------------------------')
            if ans == '0':
                os.system('clear')
                print('我们下次再见吧')
            elif ans == dictb[k]:
                os.system('clear')
                print("回答正确，很赞哦 (๑•̀ㅂ•́)و✧")
                print('---------------------------------------')
                points = points+1 #回答正确累计答题数目加1
            else:
                os.system('clear')
                print("很抱歉，您回答错误，继续努力:(")
                print('---------------------------------------')
            time.sleep(1)
            print('要继续吗？，\n如果是请输入：1\n退出游戏请输入：任意数字或者直接回车\n在答题过程中随时可以输入：0来退出游戏')
            xz = input('在这里输入:')
            print('---------------------------------------')
        print('我们下次再见吧')
        print(f'您本次答对了{points}.题，加油，下次你可以做的更好的!(~^o^~)!')
    elif pd == '0':
        os.system('clear')    
        print('我们只能下次再见了ヾ(￣▽￣)Bye~Bye~')
    else:
        print('无效命令，你确定你输入的正确吗，再来输入一次吧')
        time.sleep(1)
        print('---------------------------------------\n\n这次输入一定要看清楚哦！\n')
        print('-----------------飞花令-----------------')
        print('\n欢迎来到飞花令游戏\n要开始游戏请输入：1,退出游戏请按：0\nPS:在游戏内诺想要退出可以在答题阶段输入：0 ')
        pd2 = input('在这里输入：')
        print('---------------------------------------')
        pdhs(pd2)#返回函数值
print('-----------------飞花令-----------------')
print('\n欢迎来到飞花令游戏\n要开始游戏请输入：1,退出游戏请按：0\nPS:在游戏内诺想要退出可以在答题阶段输入：0 ')
pd2 = input('在这里输入：')
print('---------------------------------------')
pdhs(pd2)#返回函数值
