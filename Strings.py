def string_intersection(left, right):
    strng = ''
    for ind in range(len(left)):
        if ind >= len(right): 
            break
        if left[ind] == right[ind]:            
            strng += left[ind]
    if strng != '':
        print('\n'.join(strng))

string_intersection("ZIRAFA", "KARAFA")
print("--")
string_intersection("KARATE", "KARAFA")
print("--")
string_intersection("Ahoj, jak se dneska mas?", "Mam se dneska dobre.")


print('\n')


def make_fancy(text, n):
    cnt = 0
    for cr in text:
        for i in range(cnt):
            print(end=' ')
        for i in range(n):
            print(cr, end=' ')
        print()
        cnt += 1

make_fancy("PTAKOPYSK", 3)


print('\n')


def zigzag(text):
    cik = cak = ''
    for i in range(len(text)):
        if i % 2 == 0:
            cik += text[i]
        else:
            cik += "."
    for j in range(len(text)):
        if j % 2 != 0:
            cak += text[j]
        else:
            cak += "."
    
    print(cik)
    print(cak)

zigzag("PARDUBICE")
print()
zigzag("agaga54464854ophg")


print('\n')


def alphabet(n):
    res = ""
    for i in range(65, 65 + n):
        if n == 26:
            res = res + chr(i)           
            print(res)

alphabet(26)


print('\n')


def alphabet(n):
    res = ""
    for idx in range(65, 61 + n):
        res = res + chr(idx)
    print('\n'.join(res))

alphabet(30)


print('\n')


print('function that takes two strings', '\n'
    'and returns their zipped letters', '\n'
    'from both strings on the alternating side:', '\n')

def string_zip(text1, text2):
    if not text1:
        return text2
    elif not text2:
        return text1
    else:
        return text1[0] + text2[0] + string_zip(text1[1:], text2[1:])
    return ""

print(string_zip("ovce", "koza"))
print(string_zip("Pardubice", "Brno"))
print(string_zip("prase", "velbloud"))