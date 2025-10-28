import sys 

K = int(sys.stdin.readline())
for _ in range(K):
    cur_num = list(map(int, sys.stdin.readline().split()))
    g1, g2 = cur_num[:4], cur_num[4:]
    target = {
        (g1[1], g1[2], g1[3]): True,
        (g1[2], g1[3], g1[1]): True,
        (g1[3], g1[1], g1[2]): True
        }
    bot = g1[0]
    flag = False
    
    if bot in g2:
        index_l = []
        for idx, v in enumerate(g2):
            if v == bot:
                index_l.append(idx)
        
        for idx in index_l:
            if idx == 0:
                g2_iter = tuple(g2[1:])
            
            elif idx == 1:
                g2_iter = (g2[0], g2[3], g2[2])
            
            elif idx == 2:
                g2_iter = (g2[0], g2[1], g2[3])
                
            elif idx == 3:
                g2_iter = (g2[0], g2[2], g2[1])
                
            
            if g2_iter in target:
                flag = True
                break
    if flag:
        print(1)
    else:
        print(0)

explain = """
첫번째 정사면체의 밑면을 타겟 색으로 잡고 두번째 정사면체에서 해당 색의 인덱스를 구한 후, 
해당 색의 인덱스가 0, 1, 2, 3일 때를 나누어서 가능한 색배열을 구한다. 그 후 그 색배열이
첫번째 정사면체에서 나올 수 있는 색 배열이면 1을 출력하는 것이 알고리즘의 골자이다.
주의해야 할점은 첫번째 정사면체의 밑몉 색이 두번째 정사면체에 여러개 존재할 수 있어 그 경우를 
모두 고려해야 한다.
"""