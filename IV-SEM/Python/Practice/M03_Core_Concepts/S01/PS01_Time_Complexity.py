def Linear_Search(element, target):

    for i in range(len(element)):
        if element[i] == target:
            return i
    return -1

element = list(map(int, input("Enter List: ").split()))
target = int(input("Enter target value: "))
print("Index Value: ", Linear_Search(element, target)) 

print(Linear_Search([12, 21, 20, 5, 4], 12)) #Found at 1st idx --> Best Case O(1)
print(Linear_Search([12, 21, 20, 5, 4], 20)) #Found at 3rd idx --> Average Case O(n)
print(Linear_Search([12, 21, 20, 5, 4], 4)) #Found at 5th idx --> Worst Case O(n)

