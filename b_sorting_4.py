import sys



class Statistic():
    def __init__(self, number_dictionary :dict):
        self.nd = number_dictionary
        self.length = sum(number_dictionary.values())

    def mean(self):
        temp = 0
        for i in self.nd:
            temp += i*self.nd[i]
        print(round(temp/self.length))

    def median(self):
        temp = []
        for i in self.nd:
            temp += [i]*self.nd[i]
        print(temp[self.length//2])

    def most(self):
        cri = sorted(self.nd.items(), key = lambda x: x[1], reverse=True)
        temp = []

        for i in cri:
            if i[1] == cri[0][1]:
                temp.append(i[0])

        if len(temp) != 1:
            print(sorted(temp)[1])
        else:
            print(temp[0])

    def rangemm(self):

        print(max(list(self.nd.keys()))-min(list(self.nd.keys())))

if __name__ == '__main__':
    num_iter = int(sys.stdin.readline())

    num_dict = {}

    for i in range(num_iter):
        temp = int(sys.stdin.readline())
        if temp in num_dict:
            num_dict[temp] += 1

        else:
            num_dict[temp] = 1

    num_dict = dict(sorted(num_dict.items(), key=lambda x: x[0]))

    c = Statistic(num_dict)

    c.mean()
    c.median()
    c.most()
    c.rangemm()
