import sys

def find_best(num_list):

    building_list = {}
    for i in range(num_list[1], 0, -1):
        building_list[i] = [1,1]

    if num_list[0] != 1:
        for i in range(2, len(num_list)):
            if num_list[i] < num_list[i-1]:
                for k in range(num_list[i-1]-num_list[i]):
                    if building_list[num_list[i]+k+1][0] <building_list[num_list[i]+k+1][1]:
                        building_list[num_list[i]+k+1][0] = building_list[num_list[i]+k+1][1]
                    building_list[num_list[i]+k+1][1] = 0
            for j in range(num_list[i], 0, -1):
                if j not in building_list:
                    building_list[j] = [1,1]
                else:
                    building_list[j][1] +=1
    final = 0

    for i in building_list:
        temp_cri = max(building_list[i][0], building_list[i][1])
        if temp_cri*i > final:
            final = temp_cri*i
    return final

if __name__ == "__main__":
    temp = list(map(int, sys.stdin.readline().split(' ')))

    while temp[0] != 0:

        print(find_best(temp))
        temp = list(map(int, sys.stdin.readline().split(' ')))

