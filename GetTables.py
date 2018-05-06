# encoding: utf-8
import re
import sys
import os
# 获取桌面test文件夹里作业的源表,写到result并在控制台打印
def listfiles(filepath):
    constr = '\n'
    # 每次清空result文本
    fclean=open('E:\\DongLinyong\\MyFiles\\Desktop\\result.txt','w')
    fclean.truncate()
    fclean.close()
    for root,pathname,filename in os.walk(filepath): # 遍历文件夹
        for fn in filename:
            path=os.path.join(root,fn)
            fr=open(path)
            str=fr.read()
            reg = r'((?i)(from)|(join))\s+[^(tmp)][a-zA-Z0-9\_]+\.\s*([a-zA-Z0-9\_]+)'
            rsl=re.findall(reg,str)
            tableset = set()
            for m in rsl:
                tableset.add('job_'+m[3].lower())  # dwd_data.
            str1=constr.join(tableset)
            fw=open('E:\\DongLinyong\\MyFiles\\Desktop\\result.txt','a') # 结果存放处
            (x,y)=os.path.splitext(fn)
            wstr =x+'\n'+str1
            print wstr+'\n'
            fw.write(wstr+'\n')
            fw.close()
            fr.close()
    print 'bingo'

filepath='E:\\DongLinyong\\MyFiles\\Desktop\\test' # 目标文件路径
listfiles(filepath) # 调用函数

sys.exit()
