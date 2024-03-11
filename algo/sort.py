def SortH(p,k):
    def merge_list(a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.val <= b.val:
            result = a
            result.next = merge_list(a.next, b)
        else:
            result = b
            result.next = merge_list(a, b.next)
        return result

    def sort_by_split_list(p):
        if p is None or p.next is None:
            return p
        head = p
        middle = get_middle(p)
        last = middle
        first = middle.next
        last.next = None

        left = sort_by_split_list(head)
        right = sort_by_split_list(first)

        res = merge_list(left, right)
        return res

    def get_middle(p):
        slow = p
        fast = p
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    g = Node()
    g.next = p
    res = sort_by_split_list(p)
    return res

# Merge


def sort_merge(p):

    def merge_list(a, b):
        if a is None:
            return b
        if b is None:
            return a

        if a.val <= b.val:
            result = a
            result.next = merge_list(a.next, b)
        else:
            result = b
            result.next = merge_list(a, b.next)
        return result

    def sort_by_split_list(p):
        if p is None or p.next is None:
            return p
        head = p
        middle = get_middle(p)
        last = middle
        first = middle.next
        last.next = None

        left = sort_by_split_list(head)
        right = sort_by_split_list(first)

        res = merge_list(left, right)
        return res

    def get_middle(p):
        slow = p
        fast = p
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    res = sort_by_split_list(p)
    return res