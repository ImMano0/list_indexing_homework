def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    d=[list1[0]]*len(list1)
    b=(d==list1)
    
    return b

print(main(list1=['x','y',0,0]))