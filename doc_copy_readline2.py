import re 

f=open('/Users/iyun-il/Desktop/work/PV3.txt','rt',encoding='utf-8')
g=open('/Users/iyun-il/Desktop/work/PV3_copy.txt','wt',encoding='utf-8')

#많은 라인의 파일이면 
#한번에 한줄씩 읽어서 처리한다.  
#파일의 EOF(End Of File)이 아니면 계속 읽도록 한다. 
line = f.readline()
while (line != ''):
    if (re.search("\d{4}", line)):
        g.write(line + "\n")
    line = f.readline()

f.close() 
g.close()







