def solve(h, l):
    """c == h - r
    c == l / 2 - 2 * r"""
    r = ((l // 2) - h)
    c = h - r
    print("chikens:", c, "rubbits:", r)

heads, legs = 35, 94
print(solve(heads, legs))
#done