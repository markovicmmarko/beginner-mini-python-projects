def love_score(name1, name2):
    mixed_name = name1 + name2
    true = ["T","R","U","E"]
    love = ["L","O","V","E"]
    count_true = [0,0,0,0]
    count_love = [0,0,0,0]

    for idx,i in enumerate(true):
        for j in mixed_name:
            if i.lower() == j:
                count_true[idx] += 1

    for idx,i in enumerate(love):
        for j in mixed_name:
            if i.lower() == j:
                count_love[idx] += 1

    total_true = str(sum(count_true))
    total_love = str(sum(count_love))

    for letter,times in zip(true, count_true):
        if times == 1:
            print(f"Letter {letter} occurs 1 time.")
        else:
            print(f"Letter {letter} occurs {times} times.")
    print(f"Total = {total_true}")

    for letter,times in zip(love, count_love):
        if times == 1:
            print(f"Letter {letter} occurs 1 time.")
        else:
            print(f"Letter {letter} occurs {times} times.")
    print(f"Total = {total_love}")

    print(f"Love Score = {total_true+total_love}")


love_score(name1="", name2="")






