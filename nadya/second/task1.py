"""
Заданий рядок тексту.
Вивести список, що складається с елементів-списків, де перший елемент-кожне друге слово, в другий- кількість його повторів у реченні
"""
import re
lis=[]
amount_list=[]
fin_list=[]
text="HI there, i have double-cheese in my bag"

def find_most_frequent(text):
    new_text=re.findall("\w+", text)
    print(new_text)
    for elem in new_text:
        for i in range(len(new_text)-1):#range 0-8
            if i%2==1:
                lis.append(elem)
    print(lis)
    for i in range(len(lis)-1):
        amount=re.findall(lis[i], text)
    amount_list.append(len(amount))
    print(amount_list, lis)
    for i in range(len(lis)-1):
        fin_list.append([lis[i], amount[i]])
    print(fin_list)
find_most_frequent(text)
