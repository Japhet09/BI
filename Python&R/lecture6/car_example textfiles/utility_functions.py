def clean_list(l):

    nam_lst = l
    
    # cleaning the list from \n at the end on
    # each line being read by using the rstrip-method
    # to remove \n from each element
    index = 0
    while index < len(nam_lst):
        
        nam_lst[index] = nam_lst[index].rstrip("\n").lower()
        index += 1

    return nam_lst
