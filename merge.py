"""
merge module
"""
def merge ( list1, list2) :

    # set everything to zero.
    i = j = k = 0
    list3 = [ ]
    '''
        The below method merges two lists in sorted order, returns sorted new list.
        Prerequisite: all argument lists should eb sorted.
    '''
    while True:
        if len ( list1 )  == i :
           list3.extend ( list2[ j: ] )
           break
        elif len(list2)  == j :
            list3.extend(list1[i:])
            break
        if list1[i] < list2[j] :
            list3.append(list1[i])
            i += 1
            k += 1
        else:
            list3.append(list2[j])
            j += 1
            k += 1
    return list3
