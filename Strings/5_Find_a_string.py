def count_substring(string, sub_string):
    new_string=string
    count=0
    while len(new_string)>len(sub_string):
        if sub_string in new_string:
            count+=1
            index=new_string.find(sub_string)
            new_string=new_string[index+1:]
        else:
            break
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
