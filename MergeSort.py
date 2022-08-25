import random

def mergeSort(newlist):
    if len(newlist)==1:
        return newlist
    middle = len(newlist) // 2
    left_array = newlist[ :middle]
    right_array = newlist[middle: ]

    sorted_left_array = mergeSort(left_array)
    sorted_right_array = mergeSort(right_array)

    return Merge(sorted_left_array, sorted_right_array)


def Merge(left_arr , right_arr):
    arr_final = []
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] > right_arr[0]:
            arr_final.append(right_arr[0])
            right_arr.pop(0)
        else:
            arr_final.append(left_arr[0])
            left_arr.pop(0)

    while len(left_arr) > 0 :
        arr_final.append(left_arr[0])
        left_arr.pop(0)
    
    while len(right_arr) > 0:
        arr_final.append(right_arr[0])
        right_arr.pop(0)
    
    return arr_final


if __name__=="__main__":
    print("\n\n now an automatic list will be generated with random numbers:")
    howmany = int(input("Select how many numbers do you want in the list, max 100. "))
    #now i can control if the users enter correctly the number but i wont.
    newlist = [random.randint(0 , 100) for i in range(howmany)]
    print("Random list created succesfully")
    print(newlist)
    print("\nList ordered:\n")
    print(mergeSort(newlist))