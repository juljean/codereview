"""
задан список з різними типами даних
вивести кількість елементів типу float
"""
newlist=["k",6.8,99,345,True,"66"]
count=0
for i in newlist:
    if isinstance(i,float):
        count=count+1
print(count)