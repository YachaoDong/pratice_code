
'''
从尾巴到头打印链表
    思路1：python使用逆序 [::-1]
    思路2：链表逆序
    思路3：使用栈
'''
def printListFromTailToHead(listNone):
    # 使用栈，先进后出
    res = []

    # 添加链表的值
    val_list = []
    while listNone:
        val_list.append(listNone.val)
        listNone = listNone.next

    while val_list:
        res.append(val_list[-1])
        val_list.pop()
    return res

'''
反转链表
    思路：定义辅助结点pre；先临时值tmp存储；然后断开链表；最后连接；next循环
'''
def reverse_list(listNode):
    if not listNode:
        return []
    pre = None
    cur = listNode
    while cur:
        tmp = cur.next
        cur.next = pre
        pre = cur
        cur = tmp
    return pre

'''
合并两个排序的链表
    思路：
'''





















