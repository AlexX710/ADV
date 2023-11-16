def chapter_2():
    print("All of sudden you find yourself in a hedge maze")
    choice = input("You are presented with 3 paths. Do you want to go left, right, or forward?").lower()
    if choice == "Right":
        print("Dead end, go back")
        return True
    else:
        print("Choose a path")
        return False
