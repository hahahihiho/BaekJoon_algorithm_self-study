import numpy as np

ESM = input().split(' ')
ESM = list(map(int,ESM))

while not (ESM[0]==ESM[1] and ESM[1]==ESM[2]):
    index_min = np.argmin(ESM)
    if index_min==0:
        ESM[0] += 15
    elif index_min==1:
        ESM[1] += 28
    else:
        ESM[2] += 19

print(ESM[0])