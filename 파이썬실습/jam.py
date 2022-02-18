
def solution(arr):
    new_data = []
    for i in arr:
        if i not in new_data:
            new_data.append(i)
        elif i in new_data and new_data[-1] != i:
            new_data.append(i)
            answer = new_data
            return answer
        
print(solution([1,1,3,3,0,1,1]))

print(solution([4, 4, 4, 3, 3]))


# for i in [4, 4, 4, 3, 3]:
    
#     new_data = []
#     if i not in new_data:
#         new_data.append(i)
#     elif i in new_data and new_data[-1] != i:
#         new_data.append(i)
#         answer = new_data
#     print(new_data)




# for i in [1,1,3,3,0,1,1]:
    
#     new_data = []
#     if i not in new_data:
#         new_data.append(i)
#     elif i in new_data and new_data[-1] != i:
#         new_data.append(i)
#         answer = new_data
#     print(answer)







# a = [1,1,3,3,0,1,1]
# b = 1

# c = a[-1] != b

# print(c)
# print(a[-1])
