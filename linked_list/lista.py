from random import randrange


class Node:
    """basic linked list, only val and next"""
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return self.print_list()

    def print_list(self):
        """printing list lol"""
        p = self
        res = ""
        while p is not None:
            res = f"{res}{p.val} -> "
            p = p.next
        res = res + " END"
        return res


# directly print
def print_list(p):
    """printing list lol"""
    while p is not None:
        print(p.val, end=" -> ")
        p = p.next
    print("END")


# creating linked lists
def init_natural(n=10):
    """Create linked list with natural numbers to n"""
    a = Node(n)
    for i in range(n-1,-1,-1):
        a = Node(i,a)
    return a


def init_rand(n=10,x=1,y=100):
    """Create linked list with n random numbers i range (x,y)"""
    a = Node(randrange(x,y))
    for i in range(n-1,-1,-1):
        a = Node(randrange(x,y),a)
    return a


def init_number(n):
    a = Node(n%10)
    n //= 10
    while n != 0:
        digit = n%10
        a = Node(digit,a)
        n //= 10
    return a

def linked_to_int(p:Node):
    p = Node(None,p) if p.val is not None else p # guard
    res = 0
    while p.next is not None:
        digit = p.next.val % 10
        res = res*10 + digit
        p = p.next
    return res


def int_to_linked(n:int):
    s = Node(n%10)
    n //= 10
    while n != 0:
        s = Node(n%10,s)
        n //= 10
    return s


def tab_to_linked(t:list):
    n = len(t)
    s = Node(t[n-1])
    for i in range(n-2,-1,-1):
        tmp = Node(t[i],s)
        s = tmp
    return s


# standard operations
def add_to_end_list(p,what):
    p = Node(None,p) # guard
    start = p.next
    while p.next is not None:
        p = p.next
    p.next = Node(what)
    return start


def remove_element(p,what):
    p = Node(None,p) # guard
    start = p.next
    while p.next is not None:
        if p.next.val == what:
            p.next = p.next.next
            return start
        p = p.next
    return start


# cycles stuff
def is_cycle(p:Node) -> bool:
    w = p
    z = p
    while w.next is not None and w.next.next is not None:
        w = w.next.next
        z = z.next
        if w == z:
            return True
    return False


def print_list_cycle(p,n=20):
    if is_cycle(p):
        for i in range(n):
            print(p.val, end=" -> ")
            p = p.next
        print("END")
    else:
        print("This is not a cycle")
        print("-"*10)
        print_list(p)
        print("-"*10)


if __name__ == "__main__":
    print("Hello world!")
