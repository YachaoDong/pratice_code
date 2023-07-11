# -*- coding: utf-8 -*-
'''
@Time    : 7/10/2023 5:13 PM
@Author  : dong.yachao
'''


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
        1.判空，其中一个链表为空，则返回另外一个链表
        2. 新建空链表用于存储排序后的链表
        3. 循环两个链表，比较较小值，并添加至结果链表中，然后next
        4. 比较完后，如果两个链表其中一个为空，则直接添加剩下的部分
'''
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge(pHead1, pHead2):
    if not pHead1:
        return pHead2
    if not pHead2:
        return pHead1
    res = ListNode(0)
    cur = res
    while pHead1 and pHead2:
        if pHead1.val < pHead2.val:
            cur.next = pHead1
            pHead1 = pHead1.next
        else:
            cur.next = pHead2
            pHead2 = pHead2.next
        # 重点
        cur = cur.next
    if pHead1:
        cur.next = pHead1
    if pHead2:
        cur.next = pHead2
    return res

'''
链表中倒数最后K个结点：
    思路：
        快慢双指针，间隔K遍历
        1) 第一个循环，fast先走K步
        2) 第二个循环，slow和fast循环next，直到fast走完
'''
def find_kth_to_tail(pHead, k):
    if not pHead:
        return None
    fast = pHead
    for i in range(k):
        if fast.next:
            fast = fast.next
        else:
            return None
    slow = pHead
    while fast:
        slow = slow.next
        fast = fast.nextu
    return slow

'''
复杂链表的复制：一个链表有next值，还有一个random值
    思路：
        1)遍历，clone每个值到next中
        2)遍历，clone每个random值
        3)遍历，双指针，分离ori和clone
'''
def clone(pHead):
    pass


'''
删除链表中的重复结点：重复结点不保留，比如1->2->3->3->4->4->5，删除后变为1->2->5
    思路：
        1）循环。判断cur-next.val 和 cur.next.next.val值是否相等，
        2）内部循环。后续的next.val的值是否与当前重复的值相等，如果相等则next
'''
def deleteDuplication(pHead):
    pass

'''
删除链表中的节点：给定一个结点，删除该结点
    思路：循环遍历链表，判断val是否与给定的x值相等，相等则删除即跳过该值连接后续部分
'''
def deleteNode(pHead, x):
    pass

'''
两个链表的第一个公共节点：输入两个无环单向链表，找出他们的第一个公共节点，如果没有则返回空。
    思路：使用双指针，N1节点遍历完链表1后，遍历链表2；N2节点遍历完链表2后，遍历链表1；
          则N1节点和N2节点走的路程均为N1+N2，终点即为相遇点即公共节点
'''
def find_first_common_node(pHead1, pHead2):
    pass

'''
链表中环的入口结点：给一个长度为n的链表，找出环的入口结点返回，否则换回空。
    思路：
        快慢双指针；
        1）判断是否有环: 使用快慢双指针，如果相遇则说明有环；
        2）相遇后，fast返回头结点，slow不动，然后按照相同步幅next，再次相遇则为环的入口点
        hash表；
        将遍历的值记录到hash表中，如果遇到重复，则为环的入口结点。 
'''
def entry_node_loop(pHead):
    pass























>>>>>>> 16aa4c845eadf2fdc56a5ed2be58da8e4c44ef1c
