import time
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    current_weight = []
    current_where = []
    
    #while (not current_weight) and (not truck_weights) or (answer != 0):
    while True:
        if answer > 0 and (not current_weight) and (not truck_weights):
            break

        if current_where and current_where[0] >= bridge_length:
            current_weight.pop(0)
            current_where.pop(0)

        if truck_weights and sum(current_weight) + truck_weights[0] <= weight:
            current_weight.append(truck_weights[0])
            current_where.append(0)
            truck_weights.pop(0)

        for i in range(len(current_where)):
            current_where[i] += 1
        #print(answer, current_weight, current_where, truck_weights)
        answer += 1
        #time.sleep(0.1)

    return answer

print("start")
#print(solution(2, 10, [7,4,5,6]))
print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))