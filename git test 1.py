def single_insert_or_delete (s1,s2):
    s1, s2 = s1.lower(), s2.lower()
    c=0
    if s1==s2 :
        c=0
    elif abs(len(s1)-len(s2))==1 :
        if len(s1)>len(s2):
            if s1.find(s2)!=-1 :
                c=1
        elif len(s2)>len(s1):
            if s2.find(s1)!=-1 :
                c=1
        if len(s1)>len(s2):
            for char in s1 :
                if s1.find(char)!=s2.find(char):
                    c=1
        elif len(s2)>len(s1):
            for char in s2 :
                if s2.find(char)!=s1.find(char):
                    c=1
    else :
        c=2
    return c
str1=input()
str2=input()
print(single_insert_or_delete(str1,str2))