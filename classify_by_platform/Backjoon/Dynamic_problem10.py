import sys

num_wine = int(sys.stdin.readline())

wine_box = []
for i in range(num_wine):
    wine_box.append([int(sys.stdin.readline()),[],[]])

if len(wine_box) == 1:
    print(wine_box[0][0])
    sys.exit()
elif len(wine_box) == 2:
    print(wine_box[0][0]+wine_box[1][0])
    sys.exit()

wine_box[0][1].append(wine_box[0][0])
wine_box[1][1].append(wine_box[1][0])
wine_box[1][2].append(wine_box[0][0]+wine_box[1][0])
wine_box[2][1].append(wine_box[0][0]+wine_box[2][0])


for i in range(1, num_wine-2):
    wine_box[i+1][2].append(max(wine_box[i][1])+wine_box[i+1][0])
    wine_box[i+2][1].append(max(wine_box[i][1])+wine_box[i+2][0])
    wine_box[i+2][1].append(max(wine_box[i][2])+wine_box[i+2][0])
    if i!= num_wine-3:
        wine_box[i+3][1].append(max(wine_box[i][1])+wine_box[i+3][0])
        wine_box[i+3][1].append(max(wine_box[i][2])+wine_box[i+3][0])


wine_box[num_wine-1][2].append(max(wine_box[num_wine-2][1])+wine_box[num_wine-1][0])

print(max(max(max(wine_box[-1][1]),max(wine_box[-1][2])),max(wine_box[-2][2])))

