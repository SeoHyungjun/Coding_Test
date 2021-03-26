import copy

answer = []

class tree:
    def __init__(self, id, name, p_id):
        self.id = id
        self.name = name
        self.p_id = p_id
        
        self.child = []
        
def search(root, id):
    if root.id == id:
        return root

    if root.child:
        for ch in root.child:
            if ch.id == id:
                return ch
            else:
                search(ch, id)

    else:
        return False

def search_leaf_and_include(tr, word, name_stack):
    name_stack.append(tr.name)

    # 리프라면
    if not tr.child:
        # 이름안에 word포함되는지 확인
        index = 0
        check = 0
        first = ''
        while index + len(word) <= len(tr.name):
            if word in tr.name[index:index+len(word)+1]:
                #first.append(index)
                first += str(index)
                index += len(word)
                check += 1
                answer.append((copy.deepcopy(name_stack), len(tr.name) - len(word), check, tr.id, first))
            else:
                index += 1
    
    else:
        for ch in tr.child:
            search_leaf_and_include(ch, word, name_stack)
    
    name_stack.pop()

def dif(li):
    pass


def solution(data, word):
    global answer
    tree_list = []

    for d in data:
        id, name, p_id = d.split()
        print(id, name, p_id)
        id, p_id = int(id), int(p_id)
        if p_id == 0:
            # 루트이므로 tree_list에 추가
            tree_list.append(tree(id, name, p_id))

        # p_id가 0이 아니므로 이미 있는 트리에서 찾기
        else:
            for tr in tree_list:
                par = search(tr, p_id)
                if par:
                    par.child.append(tree(id, name, p_id))

    # 리프노드에서 찾기
    stack = []
    for tr in tree_list:
        search_leaf_and_include(tr, word, stack)

    #print(answer)
    #answer = sorted(answer, key=lambda x : (x[1], -1*x[2], x[3]))
    answer = sorted(answer, key=lambda x : (x[1], -1*x[2], int(x[4]), x[3]))
    re_answer = []
    for a in answer:
        re_answer.append('/'.join(a[0]))

    if re_answer:
        return re_answer
    else:
        return "Your search for {} didn't return any results".format(word)


data = ["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"]
word = 'BROWN'
#word = 'SALLY'
#["Your search for (SALLY) didn't return any results"]
print(solution(data, word))