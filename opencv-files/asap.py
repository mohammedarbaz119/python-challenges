# def listnew(l: list, p: int):
#     a = 0
#     l.sort()
#     s = []
#     c = float('inf')
#     for i in range(int(len(l)/2)):
#         for x in range(i, len(l)):
#             if(len(s) == p):
#                 break
#             s.append(l[x])
#         a = max(s)-min(s)
#         if(a < c):
#             c = a
#         s.clear()
#     return c


# print(listnew(l=[1, 234, 45, 5, 4, 6, 3, 56, 4], p=3))
# def find_Min_Difference(l, p):
#     a = 0
#     l.sort()
#     s = []
#     c = float('inf')
#     for i in range(int(len(l)/2)):
#         for x in range(i, len(l)):
#             if(len(s) == p):
#                 break
#             s.append(l[x])
#         a = max(s)-min(s)
#         if(a < c):
#             c = a
#         s.clear()
#     return c


# L = list(map(int, input().strip().split()))
# P = int(input())
# # print(find_Min_Difference(L, P))
# # print(type(L))
# # print(type(P))
# # print(find_Min_Difference(L, P))
# b = L.sort()
# print(b)

def Find_Min_Difference(l, p):
    a = 0
    l.sort()
    po = p-1
    c = float('inf')
    for i in range(int(len(l)/2)):
        a = l[po]-l[i]
        po += 1
        if(a < c):
            c = a

    return c


def Find_Min_Difference(b, p):
    b.sort()
    c = False
    a, e, i = 0, 0, 0
    while(c == False):
        print(f"e = {e}")
        if(i == 0):
            a = b[p-1]-b[0]
            i += 1
            e = i+(p-1)
        if(i > len(b)-p):
            c = True

        if(e > len(b)-1):
            i += 1
            e = i+(p-1)
            break
        if(b[e]-b[i] < a):
            a = b[e]-b[i]
            e += 1
        else:
            e += 1
    return a


g = [3, 4, 1, 9, 56, 7, 9, 12, 13]
print(Find_Min_Difference(g, 5))
