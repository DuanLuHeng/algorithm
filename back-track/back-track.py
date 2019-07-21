# coding: utf-8
import sys
import copy
out = sys.stdout.write
# 使用回溯法搜索最佳匹配
# 待搜索序列
strs = [7, 8, 9]
# strs.sort(reverse=False)
# 希望得到的目标最佳
dest_result = 15
# 记录当前选择情况下的值
# 记录当前选择情况
now_result=0
now_choise = [0] * len(strs)
# 记录当前最佳选择情况
best_result = 0
best_choise=[0] * len(strs)
# 搜索叶子节点个数
total = 0
# 替换最佳匹配次数
best_total = 0
# 记录是否要终止搜索
finded = False


def back_track(index):
    global dest_result
    global now_result
    global now_choise
    global best_result
    global best_choise
    global total, best_total
    global finded
    if finded:
        print "已经找到组价组合，当前组合为：", now_choise
        return
    # 判断是否是最后一个数字
    if index == len(strs):
        print now_choise
        total += 1
        # 保留最优值
        if now_result > best_result:
            best_total += 1
            best_result = now_result
            best_choise = copy.deepcopy(now_choise)
        # 如果能够完全匹配，则不用再往下寻找。设置标记，终止迭代
        if best_result == dest_result:
            finded = True
        return
    # 根据贪心算法，只要当前值加上now_result不大于dest_result，即选中它
    # 尝试选中
    for i in [0, 1]:
        # 左子树，代表不选择，即，不影响之前的选择结果，只需迭代下一层即可
        if i == 0:
            back_track(index + 1)
        # 右子树代表选择，需要判断是否已经超出，如果超出，则不进行下一层，否则继续往下搜索。
        if i == 1:
            # 如果选中后大于目标值，则直接返回，不在往下进行。
            if now_result + strs[index] > dest_result:
                print "如果选中该节点，将会超过最佳值，减掉，不在往下进行。当前选择为:", now_choise
                return
            # 如果选中后，不大于，则选中，并往下进行
            else:
                now_choise[index] = 1
                now_result += strs[index]
                back_track(index + 1)
                # 回溯，还原本节点对全局结果的影响。
                now_choise[index] = 0
                now_result -= strs[index]

back_track(0)
print "输入：", strs
print "期望最佳和：", dest_result
print "最佳组合：", best_choise
buffer_out = []
for index, chooise in enumerate(best_choise):
    if chooise:
        buffer_out.append(strs[index])
print "最佳值分别是：", buffer_out
print "最佳和：", best_result
print "叶子节点总数：", 2**len(strs)
print "遍历过的叶子节点:", total
print "更新最佳选择次数:", best_total