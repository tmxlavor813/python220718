#DemoFile2.py

f = open("demo.txt", "wt")
f.write("첫번쩨\n두번째\n세번째\n")
f.close()

f = open("demo.txt", "rt")
result = f.read()
print(result)
print(f.tell())
f.seek(0)
lst = f.readlines()
print(lst)
for item in lst:
    print(item, end="")

f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
f.close()

with open("demo.txt", "rt") as f:
    for item in f.readlines():
        print(item, end="")

print("---첨부하는 경우---")
 #wt, a+ 다른 상황 
 f = open("demo.txt", "a+")
 f.write("다른 데이터\n")
 f.close()
