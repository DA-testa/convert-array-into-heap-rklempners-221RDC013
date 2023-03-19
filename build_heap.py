# python3


def build_heap(data):
    swaps = []
    size = len(data)
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for i in range((size // 2) - 1, -1, -1):
        index_1 = i 

        left_child = 2 * i + 1
        if left_child < size and data[left_child] < data[index_1]:
            index_1 = left_child
        
        right_child = 2 * i + 2
        if right_child < size and data[right_child] < data[index_1]:
            index_1 = right_child

        if i != index_1:
            swaps.append((i, index_1))
            data[i], data[index_1] = data[index_1], data[i]

            while index_1 * 2 + 1 < size:
                left_child = index_1 * 2 + 1
                right_child = index_1 * 2 + 2 if index_1 * 2 + 2 < size else left_child

                if data[left_child] < data[right_child]:
                    child = left_child
                else:
                    child = right_child

                if data[index_1] > data[child]:
                    swaps.append((index_1, child))
                    data[index_1], data[child] = data[child], data[index_1]
                    index_1 = child
                else:
                    break        

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    choice = input()

    # input from keyboard
    if choice == "I":
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        swaps = build_heap(data)
        assert len(swaps) < 4*n
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    
    # input from file
    if choice == "F":
        file = str(input())
        file = "tests/" + str(file)
        with open(file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
        assert len(data) == n
        swaps = build_heap(data)
        assert len(swaps) < 4*n
        print(len(swaps))
        for i, j in swaps:
            print(i, j)
    # checks if lenght of data is the same as the said lenght
    #assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    #swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    #assert len(swaps) < 4*n

    # output all swaps
    print(len(swaps))
    #for i, j in swaps:
        #print(i, j)


if __name__ == "__main__":
    main()
