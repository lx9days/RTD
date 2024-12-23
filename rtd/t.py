import numpy as np

# 读取同文件夹下的 'tmp_sp.txt' 文件
filename = 'tmp_sp.txt'

# 使用 numpy.loadtxt 读取文件，假设数据以空格或制表符分隔
distance_matrix = np.loadtxt(filename)

# 打印读取的距离矩阵
print(distance_matrix)