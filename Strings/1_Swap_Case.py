def swap_case(s):
    new_string=""
    for i in s:
        if i.isupper()==True:
            new_string+=i.lower()
        else:
            new_string+=i.upper()
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
