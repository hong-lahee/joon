i = input().strip().upper()
a ={}
for s in i:
    if s in a:
        a[s] += 1
    else:
        a[s] = 1
        
m = max(a.values())
l = [t for t,w in a.items() if w==m]
if len(l)> 1:
    print('?')
else:
    print(l[0])
        
