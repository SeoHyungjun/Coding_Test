# 2021-03-09 15:48 -> 17:16

import sys
sys.setrecursionlimit(10**6)

class node:
    def __init__(self, input_data):
        self.data = max(input_data, key = lambda x : x[1])

        left = list(filter(lambda x: x[0] < self.data[0], input_data))
        right = list(filter(lambda x: x[0] > self.data[0], input_data))
        
        if left != []:
            self.left = node(left)
        else:
            self.left = None

        if right != []:
            self.right = node(right)
        else:
            self.right = None
        

def preorder(tree, pre_list):
    #print(tree.data, end = ' ')
    pre_list.append(tree.data[2])
    if tree.left != None:
        preorder(tree.left, pre_list)
    if tree.right != None:
        preorder(tree.right, pre_list)

def postorder(tree, post_list):
    if tree.left is not None:
        postorder(tree.left, post_list)
    if tree.right is not None:
        postorder(tree.right, post_list)
    #print(tree.data, end = ' ')
    post_list.append(tree.data[2])

def solution(nodeinfo):
    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)

    tree = node(nodeinfo)

    preorder_list = []
    preorder(tree, preorder_list)
    postorder_list = []
    postorder(tree, postorder_list)

    return [preorder_list, postorder_list]


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))