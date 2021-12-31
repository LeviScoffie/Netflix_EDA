

names={"evis":['kithinji', 'miriti'], 'laban':['kalala', 'mutema'], 'lee':["kithingji",'yaposa']}

def count_first(names):
    a={}

    for i in list(names.keys()):
        if i[0] in a.keys():
            print(list(names.keys()))
            print(i)
            print(i[0])
            print(len(names[i]))
            
            
            a[i[0]]+=len(names[i])

        else:
            print(i)
            print(i[0])
            print(len(names[i]))
            
            
            a.update({i[0]:len(names[i])})

    return a


print(count_first(names))

print(names.items())