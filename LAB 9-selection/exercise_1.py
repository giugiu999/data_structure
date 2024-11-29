import random
import time

#---------------------------------------#      
# Implement Recursive selection sort here. 
# n: size of array - index is index of starting element
def recursive_selection_sort(data, data_len, index = 0): 
    # Set the base case 
    if index >= data_len - 1:
        return
    # Find the minimum index 
    for i in range(data_len-1,-1,-1):
        smallindex = data_len - 1 - index
        for j in range(data_len - 1 - index, -1,-1):
            if data[j] < data[smallindex]:
                smallindex = j
    # Swap the data 
        temp = data[smallindex]
        data[smallindex] = data[data_len-index-1]
        data[data_len-1-index] = temp
    # Recursively calling selection sort function 
    recursive_selection_sort(data,data_len,index+1)

#---------------------------------------#
#Implement the Recursive merge sort here
  
def recursive_merge_sort(data): 
    
    # TODO-Remove pass and fill out the rest. 
    # You may use additional user_defined functions if required.
    # descending order

    # Set the base case 
    if len(data) <= 1:
        return data
    #Find the middle of the data list
    middle = len(data)//2 
    #Recursively calling merge sort function for both half of the data list
    left=recursive_merge_sort(data[:middle])
    right=recursive_merge_sort(data[middle:])
    # merge the two halves of the data list and return the data list
    result=[]
    i,j=0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(right[j])
            j+=1
        else:
            result.append(left[i])
            i+=1
    result += left[i:]
    result += right[j:]
    return result
#---------------------------------------#
if  __name__== "__main__":
    # abl=[520,521,234,6774,75,6746,77,77,565674,64]
    # recursive_selection_sort()


    # Define the list of random numbers
    random_list = [random.randint(1,1000) for i in range(500)]
    list_len = len(random_list) 
    ascending_list = sorted(random_list)
    descending_list = sorted(random_list, reverse=True)
      
    # Calculate the execution time to sort a list of random numbers #
    random_list_ = random_list.copy()  # make a copy to save the unsorted list
    start_sel = time.time()
    recursive_selection_sort(random_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(random_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of random numbers
    print('The execution time: to sort a random list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
    
    
    # Calculate the execution time to sort a list of intergers already sorted in ascending order #
    ascending_list_ = ascending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(ascending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(ascending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in ascending order 
    print('The execution time: to sort a ascending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))      
    
    
    # Calculate the execution time to sort a list of intergers already sorted in descending order #
    descending_list_ = descending_list.copy()
    start_sel = time.time()
    recursive_selection_sort(descending_list_, list_len)
    end_sel = time.time()
    
    start_merge = time.time()
    recursive_merge_sort(descending_list)
    end_merge = time.time()
    
    # Print the rsults execution time to sort a list of intergers already sorted in descending order 
    print('The execution time: to sort a descending list of integers in descending order.')
    print(' - Recursive selection sort: {}'.format(end_sel - start_sel))
    print(' - Recursive merge sort: {}'.format(end_merge - start_merge))
