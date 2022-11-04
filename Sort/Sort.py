def BubbleSort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                 temp = my_list[j]
                 my_list[j] = my_list[j+1]
                 my_list[j+1] = temp
    return my_list

def SelectionSort(my_list):
    for i in range(len(my_list)-1):
        min_index = i
        for j in range(i+1 , len(my_list)):
            if  my_list[min_index]>my_list[j]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp  
    return my_list
                   

# print(BubbleSort([5,3,2,9,8,1,3]))    
print(SelectionSort([5,3,2,9,8,1,3]))                    