# coding: utf-8
"""
01背包问题最优解
"""
import math

def __get_dividend(weights):
    """
    获取最大公约数
    :param weights:
    :return:
    """
    dividend = 1
    step = 1024
    flag = True
    while True:
        for weight in weights:
            if weight < 1024:
                flag = False
                break
        if not flag:
            break
        dividend = dividend * step
        weights = [weight/step for weight in weights]
    return dividend


def divided(weights, ssd_size):
    """
    分治法，计算最佳分配组合。
    时间复杂度为 len(weights) * ssd_size。
    因此，尽量减小ssd_size的大小，办法是将ssd_size和weights里的各个值转换成以M为单位的数字
    :param weights: 待分配的db磁盘大小列表
    :param ssd_size: SSD磁盘大小
    :return: 被选择的db下标数组。（倒序排列）
    """
    if ssd_size < min(weights):
        return []
    dividend = __get_dividend(weights)
    weights = [weight/dividend for weight in weights]
    ssd_size = int(math.floor(ssd_size/dividend))
    # 在数组起始位置添加一个0，为了方便判断边界条件。
    weights = [0] + weights
    db_num = len(weights)
    results = [[0 for tmp_i in range(ssd_size + 1)] for tmp_j in range(db_num)]
    for n in range(0, db_num):
        for w in range(0, ssd_size + 1):
            # n = 0, 说明是检测第一个物品是否要选择的情况， 这种情况下，只要
            # 剩余空间 w > n的weight，即选中该物品
            if n == 0:
                if w >= weights[n]:
                    results[n][w] = weights[n]
            # n>0,说明是第二个物品，可以根据第一个物品推出来。
            else:
                # 可以装入，需要判断大小
                if w >= weights[n]:
                    tmp1 = results[n - 1][w]
                    tmp2 = results[n - 1][w - weights[n]] + weights[n]
                    results[n][w] = max(tmp1, tmp2)
                # 不可装入，选择上一个最大值。
                else:
                    results[n][w] = results[n - 1][w]
    # 计算被选中的weight
    index = db_num - 1
    w = ssd_size
    selected = []
    while index > 0:
        if results[index][w] != results[index - 1][w]:
            # 选中了该值, 真实下标为：index-1， 因为weights在计算的时候，首位添加了个0.
            selected.append(index - 1)
            w = w - weights[index]
            index -= 1
        else:
            index -= 1
    return selected

weights = [40,40,40,40,80,80,80,80,120,120,120,120,
        40,40,40,40,80,80,80,80,120,120,120,120,
        40,40,40,40,80,80,80,80,120,120,120,120]

weights = [weight * 1024 * 1024 * 1024 for weight in weights]
ssd_size = 1.2 * 1024 * 1024 * 1024 * 1024

import time
start = time.time()
results = divided(weights, ssd_size)
end = time.time()
selected = []
for result in results:
    selected.append(weights[result])
print "期望最佳：", ssd_size
print "实际最佳：", sum(selected)/1024/1024/1024/1024.0
print "选中列表：", selected
print "选中下标：", results
print "耗时：", end - start