if __name__ == '__main__':
    s = input()
    alnum=False
    alpha=False
    digit=False
    lower=False
    upper=False
    for i in s:
        if i.isalpha():
            alpha=True
        if i.isdigit():
            digit=True
        if i.islower():
            lower=True
        if i.isupper():
            upper=True
    print(alpha or digit)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
    
