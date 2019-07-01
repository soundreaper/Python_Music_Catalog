class List:
    def __init__(self, lst, size, cap):
        self.lst = lst
        self.size = size
        self.cap = cap
    def __eq__(self, other):
        return ((type(other) == List)
          and self.lst == other.lst
          and self.size == other.size
          and self.cap == other.cap
        )
    def __repr__(self):
        return ("List({!r}, {!r}, {!r})".format(self.lst, self.size, self.cap))

# list -> int
# returns the size of the list
# def size(lst):
#   pass
def length(lst):
    return lst.size

# None -> list
# returns an empty list
# def empty_list():
#   pass
def empty_list():
    return List([None, None], 0, 2)

#lst -> lst
#helper function for add that increases lst capacity by 2
def enlarge(array_list):
    return List(array_list.lst+[None]*2,array_list.size,array_list.cap+2)

# list, index, value -> list
# Takes in list, puts value into desired index, returns new list with changes
# def add(lst, index, value):
#   pass
def add(lst, index, value):
    if index < 0 or index > lst.size:
        raise IndexError()
    else:
        if lst.size == lst.cap:
            return add(enlarge(lst), index, value)
        else:
            temp = lst.lst[index]
            for i in range(lst.size, index-1,-1):
                lst.lst[i] = lst.lst[i-1]
            lst.lst[index] = value
            lst.size += 1
            return lst

# list, index -> value
# returns the value at a certain index
# def get(lst, index):
#   pass
def get(lst, index):
    if index < 0 or index >= lst.size:
        raise IndexError()
    return lst.lst[index]

# list, index, value -> list
# returns a list with the value at the index if appropriate
# def set(lst, index, value):
#   pass
def set(lst, index, value):
    if index < 0 or index >= lst.size:
        raise IndexError()
    else:
        lst.lst[index] = value
        return lst

# list, index -> list
# returns list with removed value
# def remove_lst(lst, index):
#   pass
def remove(lst,index):
    if index < 0 or index > lst.size-1:
        raise IndexError()
    else:
        temp = lst.lst[index]
        for i in range(index, lst.size-1):
            lst.lst[i] = lst.lst[i+1]
        lst.lst[lst.size-1] = None
        lst.size -= 1
        return temp, lst

# list, function -> None
# returns None (applies Function)
# def forreach(lst, function):
#   pass
def foreach(lst, function):
    for i in range(length(lst)):
        function(lst.lst[i])

# list, function -> Sorted List
# returns Sorted List
# def sort(lst, function):
#   pass
def sort(lst, function):
    largest = 0
    swap_index = length(lst) - 1

    while swap_index != 0:
        for idx in range(swap_index + 1):
            if function(lst.lst[largest], lst.lst[idx]):
                largest = idx
        lst.lst[swap_index], lst.lst[largest] = lst.lst[largest], lst.lst[swap_index]
        swap_index -= 1
        largest = 0
    return lst