def solution(Directories, Cmd):
    cur = Directories[0]
    folder_list = []
    cri = Directories[0].strip().split('\\')[0]
    for i in Directories:
        if '.' in i:
            temp = i.strip().split('\\')[:-1]
            tt = ''
            for j in range(len(temp)):
                if j ==0:
                    tt = temp[j]
                else:
                    tt = tt + '\\' + temp[j]
            if tt not in folder_list:
                folder_list.append(tt)
        else:
            folder_list.append(i)
    print(folder_list)
    for i in Cmd:

        if i[0] == 'CD':

            if i[1] in folder_list:

                cur = i[1]

            else:

                if cur+f'\{i[1]}' in folder_list:
                    cur = cur+f'\{i[1]}'

                else:

                    continue
        elif i[0] == "mkdir":
            if cri in i[1]:
                if i[1] not in folder_list:
                    folder_list.append(i[1])
            else:
                t_cur = cur + '\\' + i[1]
                if t_cur not in folder_list:
                    folder_list.append(t_cur)

    answer = cur
    for i in folder_list:
        print(i)
    return answer, folder_list

print(solution([r"C:\root\folder1", r"C:\root\folder2\file1.txt", r"C:\root\folder2\file2.txt"], [['mkdir', r'C:\root\folder3'],['CD', r"C:\root\folder3"]]))


