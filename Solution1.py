#1 . Write a function that takes a list of numbers as input and returns a new list
# containing only the even numbers from the input list. 
# Use list comprehension to solve this problem.
def solution(list1):
    list2=[i for i in range (list1) if(i%2==0)]
    return list2


list1=[12,21,32,4,11,10,51,8,19,8,42]
result=solution(list1)
print(result)


