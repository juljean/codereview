"""
дано рядок тексту
вивести кожне друге слово з кінця
"""
text="Just always and always look around and act wisely"
newlist=list(text.split(" "))
rang=len(newlist)
for i in range(rang-2, -1, -2):
    print(newlist[i])