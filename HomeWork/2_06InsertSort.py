def showdata (data):
    for i in range (SIZE):
        print('%3d' %data[i], end='')
    print()

def insert (data):
    for i in range(1,SIZE):
        tmp = data[i]
        no = i - 1
        while no >= 0 and tmp < data[no]:
            data[no+1] = data[no]
            no -= 1
            data[no+1] = tmp

def dataLen(data):
    return len(data)

def main():
    global dataSet
    dataSet = [16, 25, 39, 27, 12, 8, 45, 63]
    global SIZE
    SIZE = dataLen(dataSet)
    print('Orign data:')
    showdata(dataSet)

    insert(dataSet)

    print('Result:')
    showdata(dataSet)

main()