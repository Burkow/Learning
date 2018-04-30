def winning_condition(a, b, c, d, e, f, g, h, i):
    # horizontal 
    if a == b == c and a != " ":
        return True
    elif d == e == f and d != " ":
        return True
    elif g == h == i and g != " ":
        return True
    # diagonals
    elif a == e == i and a != " ":
        return True
    elif g == e == c and g != " ":
        return True
    # verticals 
    elif a == d == g and a != " ":
        return True
    elif b == e == h and b != " ":
        return True
    elif c == f == i and c != " ":
        return True
    else:
        return False


def placement_of_symbol(n, placement, a, b, c, d, e, f, g, h, i):
    if placement == "1":
        a = n
    elif placement == "2":
        b = n
    elif placement == "3":
        c = n
    elif placement == "4":
        d = n
    elif placement == "5":
        e = n
    elif placement == "6":
        f = n
    elif placement == "7":
        g = n
    elif placement == "8":
        h = n 
    elif placement == "9":
        i = n
        
    return (a, b, c, d, e, f, g, h, i)


def print_board_state (a, b, c, d, e, f, g, h, i):
    print("[" + a + "] [" + b + "] [" + c + "]")
    print("[" + d + "] [" + e + "] [" + f + "]")
    print("[" + g + "] [" + h + "] [" + i + "]")


def input_placement():
    while True:
        placement = input ()
        if placement == "1" and a == " ":
            return placement
        if placement == "2" and b == " ":
            return placement
        if placement == "3" and c == " ":
            return placement
        if placement == "4" and d == " ":
            return placement
        if placement == "5" and e == " ":
            return placement
        if placement == "6" and f == " ":
            return placement
        if placement == "7" and g == " ":
            return placement
        if placement == "8" and h == " ":
            return placement
        if placement == "9" and i == " ":
            return placement
    


print("[ 1 ] [ 2 ] [ 3 ]")
print("[ 4 ] [ 5 ] [ 6 ]")
print("[ 7 ] [ 8 ] [ 9 ]")


a = b = c = d = e = f = g = h = i= " "

while True:
    print("Player 1\nType the number where you want to place your symbol\n")
    placement_x = input_placement()
    (a, b, c, d, e, f, g, h, i) = placement_of_symbol("x", placement_x, a, b, c, d, e, f, g, h, i)
    print_board_state (a, b, c, d, e, f, g, h, i)
    if winning_condition(a, b, c, d, e, f, g, h, i):
        print("\nPlayer 1 won!")
        break
        
    if a in ("x", "o") and b in ("x", "o") and c in ("x", "o") and d in ("x", "o") and e in ("x", "o") and f in ("x", "o") and g in ("x", "o") and h in ("x", "o") and i in ("x", "o"):
        print("Draw")
        break
        
    print("player 2\nType the number where you want to place your symbol\n")
    placement_o = input_placement()
    (a, b, c, d, e, f, g, h, i) = placement_of_symbol("o", placement_o, a, b, c, d, e, f, g, h, i)
    print_board_state (a, b, c, d, e, f, g, h, i)
    if winning_condition(a, b, c, d, e, f, g, h, i):
        print("\nPlayer 2 won!")
        break

    if a in ("x", "o") and b in ("x", "o") and c in ("x", "o") and d in ("x", "o") and e in ("x", "o") and f in ("x", "o") and g in ("x", "o") and h in ("x", "o") and i in ("x", "o"):
        print("Draw")
        break

print("\nNow go do something productive!\n\n")