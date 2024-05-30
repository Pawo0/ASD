def anagram(a,b,k):
    T = [0] * k
    for i in a:
        T[ord(i)-ord(a)] += 1
    for i in b:
        T[ord(i)-ord(a)] -= 1
    for i in T:
        if i != 0:
            return False
    return True


