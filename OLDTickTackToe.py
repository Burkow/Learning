

def winning_condition(a, b, c, d, e, f, g, h, i):
   
    # horizontal 
    if a == "o" and b == "o" and c == "o":
        return True
    elif d == "o" and e == "o" and f == "o":
        return True
    elif g == "o" and h == "o" and i == "o":
        return True

    # diagonals o
    elif a == "o" and e == "o" and i == "o":
        return True
    elif g == "o" and e == "o" and c == "o":
        return True

    # verticals o 
    elif a == "o" and d == "o" and g == "o":
        return True
    elif b == "o" and e == "o" and h == "o":
        return True
    elif c == "o" and f == "o" and i == "o":
        return True

    # horizontal x 
    elif a == "x" and b == "x" and c == "x":
        return True
    elif d == "x" and e == "x" and f == "x":
        return True
    elif g == "x" and h == "x" and i == "x":
        return True
    elif a == "x" and e == "x" and i == "x":

    # diagonals x
        return True
    elif g == "x" and e == "x" and c == "x":
        return True

    # verticals x 
    elif a == "x" and d == "x" and g == "x":
        return True
    elif b == "x" and e == "x" and h == "x":
        return Tru
    elif c == "x" and f == "x" and i == "x":
        return True

    else:
        return False




def placement_of_symbol_x(placement_x, a, b, c, d, e, f, g, h, i):
    if placement_x == "1" and a != "o" and a != "x":
        a = "x"
        return (a, b, c, d, e, f, g, h, i) 
    if placement_x == "2" and b != "o" and b != "x":
        b = "x"
        return (a, b, c, d, e, f, g, h, i)
    if placement_x == "3" and c != "o" and c != "x":
        c = "x"
        return (a, b, c, d, e, f, g, h, i)
    if placement_x == "4" and d != "o" and d != "x":
        d = "x"
        return (a, b, c, d, e, f, g, h, i)
    if placement_x == "5" and e != "o" and e != "x":
        e = "x"
        return (a, b, c, d, e, f, g, h, i)
    if placement_x == "6" and f != "o" and f != "x":
        f = "x"
        return (a, b, c, d, e,f ,g, h, i)
    if placement_x == "7" and g != "o" and g != "x":
        g = "x"
        return (a, b, c, d, e, f, g, h, i)
    if placement_x == "8" and h != "o" and h != "x":
        h = "x"
        return (a, b, c, d, e, f, g, h, i)
    if placement_x == "9" and i != "o" and i != "x":
        i = "x"
        return (a, b, c, d, e, f, g, h, i)
    return (a, b, c, d, e, f, g, h, i)


def placement_of_symbol_o(placement_o, a, b, c, d, e, f, g, h, i):
    if placement_o == "1" and a != "o" and a != "x":
        a = "o"
        return (a, b, c, d, e, f, g, h, i) 
    if placement_o == "2" and b != "o" and b != "x":
        b = "o"
        return (a, b, c, d, e, f, g, h, i)
    if placement_o == "3" and c != "o" and c != "x":
        c = "o"
        return (a, b, c, d, e, f, g, h, i)
    if placement_o == "4" and d != "o" and d != "x":
        d = "o"
        return (a, b, c, d, e, f, g, h, i)
    if placement_o == "5" and e != "o" and e != "x":
        e = "o"
        return (a, b, c, d, e, f, g, h, i)
    if placement_o == "6" and f != "o" and f != "x":
        f = "o"
        return (a, b, c, d, e,f ,g, h, i)
    if placement_o == "7" and g != "o" and g != "x":
        g = "o"
        return (a, b, c, d, e, f, g, h, i)
    if placement_o == "8" and h != "o" and h != "x":
        h = "o"
        return (a, b, c, d, e, f, g, h, i)
    if placement_o == "9" and i != "o" and i != "x":
        i = "o"
        return (a, b, c, d, e, f, g, h, i)
    return (a, b, c, d, e, f, g, h, i)

def print_board_state (a, b, c, d, e, f, g, h, i):
    print("[" + a + "] [" + b + "] [" + c + "]")
    print("[" + d + "] [" + e + "] [" + f + "]")
    print("[" + g + "] [" + h + "] [" + i + "]")


print("[ 1 ] [ 2 ] [ 3 ]")
print("[ 4 ] [ 5 ] [ 6 ]")
print("[ 7 ] [ 8 ] [ 9 ]")



a = " "
b = " "
c = " "
d = " "
e = " "
f = " "
g = " "
h = " "
i = " "

while True:

    placement_x = input ("Player 1\nType the number where you want to place your symbol\n")
    (a, b, c, d, e, f, g, h, i) = placement_of_symbol_x (placement_x, a, b, c, d, e, f, g, h, i)
    print_board_state (a, b, c, d, e, f, g, h, i)
    if winning_condition(a, b, c, d, e, f, g, h, i) == True:
        break
        
    if a in ("x", "o") and b in ("x", "o") and c in ("x", "o") and d in ("x", "o") and e in ("x", "o") and f in ("x", "o") and g in ("x", "o") and h in ("x", "o") and i in ("x", "o"):
        print("Draw")
        break
    
    placement_o = input ("player 2\nType the number where you want to place your symbol\n")
    (a, b, c, d, e, f, g, h, i) = placement_of_symbol_o (placement_o, a, b, c, d, e, f, g, h, i)
    print_board_state (a, b, c, d, e, f, g, h, i)
    if winning_condition(a, b, c, d, e, f, g, h, i) == True:
        break

    if a in ("x", "o") and b in ("x", "o") and c in ("x", "o") and d in ("x", "o") and e in ("x", "o") and f in ("x", "o") and g in ("x", "o") and h in ("x", "o") and i in ("x", "o"):
        print("Draw")
        break

print("I want to thank my teacher and mentor Aleksander")