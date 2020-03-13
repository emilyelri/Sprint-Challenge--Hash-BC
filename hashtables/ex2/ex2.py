#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for i in range(len(tickets)):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)     # inserting each ticket to the hashtable

    prev = hash_table_retrieve(hashtable, "NONE")                                   # finding start of the chain and instantiating 'prev' variable
    
    for i in range(length):                                                         # for each value in the length of the route
        route[i] = prev                                                             # it's setting that bucket to the prev item's 'destination' (current location)
        prev = hash_table_retrieve(hashtable, route[i])                             # and then setting the prev to current value's 'source' (key)

    return route[:-1]