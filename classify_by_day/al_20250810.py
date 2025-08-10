import sys

L, R = map(int, sys.stdin.readline().split())
length = len(str(R))
answer = 0

for i in range(length):
    cur_cri = 10**(length-i-1)
    r_moc = R//cur_cri
    l_moc = L//cur_cri
    R = R%cur_cri
    L = L%cur_cri
    if r_moc != l_moc:
        break
    elif r_moc == 8 and l_moc == 8:
        answer += 1

print(answer)

explain = """
처음에는 주어진 범위 내에서 8이 아닌 수를 어떻게 가장 큰 자리 수만큼 세팅하는지를 고민하였다. 
그러나 두 수 L, R에서 각 자리가 8로 같을 때만, 8을 써야하고 그 외의 경우에는 어떻게든 8을 쓰지 않는 것이 가능하라는
성질을 기반으로 각 자리가 8로 같은 개수를 세줬다. 그리고 한번이라도 그 자리수가 8로 같지 않는 순간이 존재하면 
그 이후에는 8을 안쓰는 것이 가능하므로 for 문에서 빠줘나와 줘야 한다.(R이 L보다 크므로)
"""