if __name__ == '__main__':
    N = int(input())
    list=[]
    for i in range(N):
        user_input=input()
        operation=user_input.split()  
        if operation[0].lower() == "insert":
            list.insert(int(operation[1]),int(operation[2]))
        elif operation[0].lower() == "print":
            print(list)
        elif operation[0].lower() == "remove":
            list.remove(int(operation[1]))
        elif operation[0].lower() == "append":
            list.append(int(operation[1]))
        elif operation[0].lower() == "sort":
            list.sort()
        elif operation[0].lower() == "pop":
            list.pop()
        elif operation[0].lower() == "reverse":
            list.reverse()
