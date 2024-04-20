'''
在Python中，and、or和not是逻辑运算符，用于组合条件或对条件进行取反操作。
and：当两个条件都为True时，整个表达式的结果才为True。如果任何一个条件为False，那么整个表达式的结果就为False。
or：当至少有一个条件为True时，整个表达式的结果就为True。只有当所有条件都为False时，表达式的结果才为False。
not：用来取反一个布尔值。如果条件为True，not运算符会使其变为False；如果条件为False，则变为True。
以下是这些逻辑运算符的一些示例：
# 使用 and
    if condition1 and condition2:
    # 当 condition1 和 condition2 都为 True 时执行
    pass
# 使用 or
if condition1 or condition2:
    # 当 condition1 或 condition2 为 True 时执行
    pass
# 使用 not
if not condition:
    # 当 condition 为 False 时执行
    pass
逻辑运算符通常用于控制程序流程，例如在if语句中判断多个条件。在使用时，它们遵循短路求值原则：
对于and运算符，如果第一个条件为False，则不会评估第二个条件，因为无论第二个条件是什么值，整个表达式结果都是False。
对于or运算符，如果第一个条件为True，则不会评估第二个条件，因为第一个条件已经保证了整个表达式结果为True。
'''
