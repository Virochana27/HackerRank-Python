if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    max=-101
    runnerUp=-101
    sum=0
    for i in arr:
        if i>max:
            runnerUp=max
            max=i
        if i>runnerUp and i<max:
            runnerUp=i
    print(runnerUp)
