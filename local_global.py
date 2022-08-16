import sys

g_v = 30
g_list = [1,2,3]
def test(n):
    global g_v
    g_v = n+ g_v
    g_list.append(n)
    return 0
test(20)
print(g_v)
print(g_list)


class Bank():
    def __init__(self):
        self.acc_num = 0
        self.whole_acc = {}

    def make_accou1nt(self, acc_num, per_name, money):
        assert acc_num not in self.whole_acc, "오류: 계좌번호가 중복됩니다"
        self.whole_acc[acc_num] = []
        self.whole_acc[acc_num].append(per_name)
        self.whole_acc[acc_num].append(money)
        return 0

    def deposit(self, acc_num, money):
        assert acc_num in self.whole_acc, "오류: 해당 계좌번호가 존재하지 않습니다"
        self.whole_acc[acc_num][1] += money
        return 0

    def withdrawl(self, acc_num, money):
        assert acc_num in self.whole_acc, "오류: 해당 계좌번호가 존재하지 않습니다"
        self.whole_acc[acc_num][1] -= money
        return 0

    def print_whole(self):
        for i in self.whole_acc:
            print(f'계좌ID: {i}')
            print(f'이름: {self.whole_acc[i][0]}')
            print(f'잔액: {self.whole_acc[i][1]}')


b = Bank()
b.make_accou1nt(70, '양성민', 30000)
b.print_whole()
b.deposit(70, 1000000)
b.print_whole()