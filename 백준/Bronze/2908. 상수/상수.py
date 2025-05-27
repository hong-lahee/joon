i = input().split(' ')
s = [x[::-1] for x in i]

if int(s[0]) > int(s[1]):
    print(s[0])
else:
    print(s[1])
    
 