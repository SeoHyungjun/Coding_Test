N = input()
roma = [1, 5 ,10 ,50]
num_list = []
ca_list = []

def cal(max, cnt):
    if max == cnt:
        if(sum(ca_list) not in num_list):
            #print(ca_list)
            num_list.append(sum(ca_list))
        return
    else:
        for i in roma:
            ca_list.append(i)
            cal(N, cnt+1)
            ca_list.remove(i)
        

cal(N, 0)
#print(num_list)
print(len(num_list))