# python3

def bwt(string):
    l = len(string)
    bwt_list = []
    for i in range(l):
        new_string = ''
        for j in range(i, i+l):
            if j >= l:
                j -= l
            new_string += string[j]
        bwt_list.append(new_string)
    bwt_list.sort()
    result = ''
    for s in bwt_list:
        result += s[-1]
    return result

if __name__ == "__main__":
    print(bwt(input()))
