def check_if_combination_is_valid(param1, param2, param3):
    if param1 == param2 == param3 :
        return 1
    if param1 != param2 and param1 != param3 and param2 != param3:
        return 1
    else :
        return 0

print("LLL =", check_if_combination_is_valid("L","L","L"), "we want 1")
print("ROL =", check_if_combination_is_valid("R","0","L"), "we want 1")
print("RRL =", check_if_combination_is_valid("R","R","L"), "we want 0")
print("LOO =", check_if_combination_is_valid("L","O","O"), "we want 0")
print("RLR =", check_if_combination_is_valid("R","L","R"), "we want 0")