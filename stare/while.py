x = 5
y = 6

for a in range(x):
    for b in range(y):
        if a == 4 or b ==3:
            continue
        print(a*b)

        
a,b = 0,0

while a < x:
    a += 1
    while b < y:
        b += 1
        print(a*b)
        
