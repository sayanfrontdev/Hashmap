def remove_and_split(string, word):
    newStr=string.replace(word,"")
    return newStr.strip()

this="      Sayan is a good        "
n=remove_and_split(this,"Sayan")
print(n)