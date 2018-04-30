def near_hundred(n):
    if n >= 90 and n <= 110 or n >= 190 and n <= 210:
        return True
    return False


n = input("Give me a number")
print(near_hundred(int(n)))


game_over = False



while not game_over:
    print("lol")
    is_game_over = input("is the game over? ")
    if is_game_over == "Yes":
        game_over = True