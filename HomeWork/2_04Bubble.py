data = [16, 25, 39, 27, 12, 8, 45, 63]
print('Bubble sort\'s origin data is:')
for i in range (len(data)):
    print('%3d' %data[i], end='')
print()

for i in range(len(data)-1, -1, -1):
    for j in range (i):
        if data[j] > data[j+1]:
            data[j],data[j+1] = data[j+1], data[j]

    print('Result after %d times sort:' %(len(data)-i), end='')
    
    for j in range (8):
        print('%3d' %data[j], end='')
    print()

print('The final result is:')
for j in range(len(data)):
    print('%3d' %data[j], end='')
print()