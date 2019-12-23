"""
задан рядок
вивести кількість чисел у рядку
"""
text="ghkdlh5673bjhdvfl"
count=0
for i in text:
    if i.isdigit():
        count=count+1
print(count)