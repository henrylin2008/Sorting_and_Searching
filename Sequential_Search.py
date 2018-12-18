# Sequential Search
# Check out the video lecture for a full breakdown, in this Notebook all we do is implement Sequential Search for an Unordered List and an Ordered List.


#Sequential Search
def seq_search(arr,ele):
    """
    General Sequential Search. Works on Unordered lists.
    """
    
    # Start at position 0
    pos = 0
    # Target becomes true if ele is in the list
    found = False
    
    # go until end of list
    while pos < len(arr) and not found:
        
        # If match
        if arr[pos] == ele:
            found = True
            
        # Else move one down
        else:
            pos  = pos+1
    
    return found



# In [18]:
# arr = [1,9,2,8,3,4,7,5,6]
# In [6]:
# print seq_search(arr,1)
# True
# In [7]:
# print seq_search(arr,10)
# False