from numpy import array

def to_sequences(dataset, seq_size=1):
    x = []
    y = []

    for i in range(len(dataset)-seq_size-1):
        # print(dataset[i], dataset[i+seq_size, -1])
        window = dataset[i:(i+seq_size), :-1]
        x.append(window)
        y.append(dataset[i+seq_size, -1])

    return array(x), array(y)