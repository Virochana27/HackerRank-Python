if __name__ == '__main__':
    n = int(input())
    n_integers= tuple(map(int, input().split()))
    print(hash(n_integers))
