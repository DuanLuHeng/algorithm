# coding: utf-8
# 01背包问题

weights = [0,40,40,40,40,80,80,80,80,120,120,120,120,
        40,40,40,40,80,80,80,80,120,120,120,120,
        40,40,40,40,80,80,80,80,120,120,120,120]
# weights = [0,5,2,3,4,6] # 物品重量
N = len(weights) # 物品总数
package = 40 # 背包总容量
W = package  # 背包总容量

results = [[0 for tmp_i in range(W+1)] for tmp_j in range(N)]
import time
start = time.time()
total = 0
# 循环判断每个物品是否要放入背包 注意要遍历到每个物品：[1,N]
for n in range(0, N):
    # 循环判断该物品在背包容量为w时的最佳价值, 要判断所有价值区间[1,W]
    for w in range(0, W+1):
        total += 1
        # 判断边界
        # n = 0, 说明是检测第一个物品是否要选择的情况， 这种情况下，只要
        # 剩余空间 w > n的weight，即选中该物品
        # 如果计算过了，则直接跳过。
        # if results[n][w] != 0:
        #     continue
        if n == 0:
            if w >= weights[n]:
                results[n][w] = weights[n]
        else: # n>0,说明是第二个物品，可以根据第一个物品推出来。
            # 可以装入，需要判断大小
            if w >= weights[n]:
                tmp1 = results[n-1][w]
                tmp2 = results[n-1][w - weights[n]] + weights[n]
                results[n][w] = max(tmp1, tmp2)
            # 保留上一个最大值
            else:
                results[n][w] = results[n-1][w]
end = time.time()
# print N, W
# for index, result in enumerate(results):
#     print index, weights[index], result
print "输入值：", weights
print "输入总和：", sum(weights)
print "期望值：", package
print "耗时：", end - start
print "最佳值：", results[N-1][W]
print "选中的值："
index = N-1
w = W
selected = []
selected_index = []
while index >0:
    if results[index][w] != results[index-1][w]:
        # 选中了该值
        selected.append(weights[index])
        selected_index.append(index)
        w = w-weights[index]
        index -= 1
    else:
        index -= 1
print selected
print "sum(selected)", sum(selected)
print selected_index
print "循环次数：", total
for index, res in enumerate(results):
    print weights[index], res