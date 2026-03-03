def selection_sort_tuples(arr):
    n = len(arr)
    

    for i in range(len(arr)):
        min_idx = i
        

        for j in range(i+1, n):
            if arr [j][1] < arr [min_idx][1]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

    return arr


arr =[('a', 5), ('b', 2), ('c',9), ('d',1), ('e', 7), ('f', 3), ('g', 8), ('h', 4), ('i', 6),('j',0)]
sorted_arr = selection_sort_tuples(arr)
print(sorted_arr)



"""
pass 1 (i = 0)
i = 1, min_idx = 0(initially points to('a', 5))
Inner loop searches for minimum
j = 1:arr[0]='a',5 > arr[1]='b',2 ? YES min_idx = 1
j = 2:arr[1]='b',2 > arr[2]='c',9 ? NO min_idx = 1
j = 3:arr[1]='b',2 > arr[3]='d',1 ? YES min_idx = 3
j = 4:arr[3]='d',1 > arr[4]='e',7 ? NO min_idx = 3
j = 5:arr[3]='d',1 > arr[5]='f',3 ? NO  min_idx = 3
j = 6:arr[3]='d',1 > arr[6]='g',8 ? NO min_idx = 3 
j = 7:arr[3]='d',1 > arr[7]='h',4 ? NO  min_idx = 3
j = 8:arr[3]='d',1 > arr[8]='i',6 ? NO min-idx = 3
j = 9:arr[3]='d',1 > arr[9]='j',0 ? YES min_idx = 9

**Result:** Minimum is ('j', 0) at index 9

**Swap**

Before:[('a',5), ('b',2),('c',9),('d',1),('e',7),('f',3)('g',8),('h',4),('i',6),('j',0)]
i = 0
min_idx = 9


After:[('j',0),('b',2),('c',9),('d',1),('e',7),('f',3),('g',8),('h',4),('i',6),('a',5)
Sorted
pass 2
i = 1, min_idx =1 (initially points to 'b'2)
inner loop searches for minimum
j = 2:arr[1]='b',2 > arr[2]='c',9 ? NO min_idx = 1
j = 3:arr[1]='b',2 > arr[3]='d',1 ? YES min_idx = 3
j = 4:arr[3]='d',1 > arr[4]='e',7 ? NO min_idx = 3
j = 5:arr[3]='d',1 > arr[5]='f',3 ? NO min_idx = 3
j = 6:arr[3]='d',1 > arr[6]='g',8 ? NO min_idx = 3
j = 7:arr[3]='d',1 > arr[7]='h',4 ? NO min_idx = 3
j = 8:arr[3]='d',1 > arr[8]='i',6 ? NO min_idx = 3
j = 9:arr[3]='d',1 > arr[9]='a',5 ? NO min_idx = 3

**Result minimum is ('d',1) at index 3

 **Swap**
 
 Before:[('j',0),('b',2),('c',9),('d',1),('e',7),('f',3),('g',8),('h',4),('i',6),('a',5)]
Min_idx = 3
  
After:[('j',0),('d',1),('b',2),('c',9),('e',7),('f',3),('g',8),('h',4),('i',6),('a',5)]
Sorted
"""





def bubble_sort(arr):
    arr = [4,2,6,8,9,1]
    n = len(arr)

    for i in range(n-1):

        for j in range (0, n-i-1):

            if arr[j] > arr [j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    
    return arr



sorted_list = bubble_sort
print(bubble_sort(arr))

