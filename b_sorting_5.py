import sys



if __name__ == '__main__':
    num = int(sys.stdin.readline())
    num_dict = {}


    for i in range(len(str(num))):
        temp = num%10
        if temp not in num_dict:
            num_dict[temp] = 1
        else:
            num_dict[temp] += 1
        num = num//10

    num_dict = sorted(num_dict.items(), key = lambda x : x[0] , reverse= True)
    for i in num_dict:
        print(str(i[0])*i[1], end='')

