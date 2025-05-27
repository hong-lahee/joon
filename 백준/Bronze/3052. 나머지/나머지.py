#for s in range(10):
#    num = int(input())
#b = [] 
#for i in num:
#    a = i % 42
#    if a not in b:
#        b.append(a)
        
    
print(len({int(input()) % 42 for a in range(10)}))