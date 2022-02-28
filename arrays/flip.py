def flip(A):
    max_1 = 0
    max_start_index = -1
    max_last_index = -1
    temp_1 = 0
    temp_start_index = 0
    temp_last_index = 0
    start_flag = 0
    for i in range(len(A)):
        if start_flag == 0:
            temp_start_index = i
            start_flag = 1
        if A[i] == '0':
            temp_1 += 1
        else:
            temp_1 -= 1
        if temp_1 < 0:
            temp_1 = 0
            temp_start_index = 0
            start_flag = 0
            continue
        temp_last_index = i
        
        if max_1 < temp_1: #or (max_1 == temp_1 and (temp_start_index < max_start_index or temp_start_index == max_start_index and temp_last_index < max_last_index)):
            max_1 = temp_1
            max_start_index = temp_start_index
            max_last_index = temp_last_index
    
    if max_start_index == -1 or max_last_index == -1:
        return []
    return [max_start_index+1,max_last_index+1]

print(flip("010"))