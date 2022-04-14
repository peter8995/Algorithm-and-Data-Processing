def showdata (data):
    for i in range (SIZE):
        print('%3d' %data[i], end='')
    print()

def select (data):
    for i in range(SIZE-1):
        for j in range(i+1,SIZE):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    print()

data = [16, 25, 39, 27, 12, 8, 45, 63]
SIZE = len(data)

print('Orign data:')
showdata(data)

select(data)

print('Result:')
showdata(data)