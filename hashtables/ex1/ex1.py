#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for i in range(length):                                         # add weights to hashtable
        hash_table_insert(ht, weights[i], i)                        # weight as key so we can find weights in table by key after. i is kinda useless here

    for i in range(length):                                         # loop thru again for comparisons
        seeking = limit - weights[i]                                # calculate the value that would add to weight to equal limit
        found = hash_table_retrieve(ht, seeking)                    # check if seeking is a key in the table
                                                                    # FUNCTION NEEDS TO RETURN INDICES (values) --- NOT WEIGHTS (keys)
        if found:                                                   # if retrieve returns a value that matches
            if found > i:                                           # compare the returned index (found) to the index of the initial weight (i)
                 return (found, i)                                  # order by larger first and return as a tuple
            return (i, found)           
    return None                                                     # otherwise return [None]

def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
