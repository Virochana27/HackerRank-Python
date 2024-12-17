def split_and_join(line):
    Split_Line=line.split()
    new_line="-".join(Split_Line)
    return new_line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
