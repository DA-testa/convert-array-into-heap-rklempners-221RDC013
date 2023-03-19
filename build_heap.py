# python3


def build_heap(data):
    swaps = []
    size = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range(size // 2, -1, -1):
        j = i
        while True:
            k = 2 * j + 1
            if k >= size:
                break
            if k + 1 < size and data[k + 1] < data[k]:
                k = k + 1
            if data[j] <= data[k]:
                break
            swaps.append((j,k))
            data[j], data[k] = data[k], data[j]
            j = k    

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    choice = input()

    # input from keyboard
    if "I" in choice:
        n = int(input())
        data = list(map(int, input().split()))
    # input from file
    elif "F" in choice:
        file = input()
        if "a" not in file:
            path = "./tests/" + file
            with open(path, 'r', encoding = 'utf-8') as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
    
    # checks if lenght of data is the same as the said lenght
    assert data is not None and len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
