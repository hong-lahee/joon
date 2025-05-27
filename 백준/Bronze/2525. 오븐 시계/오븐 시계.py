h, m = map(int,input().split())
t = int(input())

m += t
h += m//60
m = m % 60

if h > 23:
    h = h%24
    
print(h,m)
    