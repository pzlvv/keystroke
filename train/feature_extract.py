from dataset import *

D, user_list = read_data('dataset')

with open("byz.data", "w+") as f:
    for i, v in enumerate(D[0]):
        if user_list[D[1][i].index(1)] == 'b00314817':
            f.write("-1 "+' '.join([str(idx+1)+":"+str(val) for idx, val in enumerate(v)])+"\n")
