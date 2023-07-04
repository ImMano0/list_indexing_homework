def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    if list1[0] == 1:
        list1[0] = False
    
    if list1[1] == 1:
        list1[1] = False
    
    if list1[2] == 1:
        list1[2] = False
    
    if list1[3] == 1:
        list1[3] = False
    
    if list1[4] == 1:
        list1[4] = False

    if list1[5] == 1:
        list1[5] = False    

    return list1

print(main([1,2,3,4,5,6]))