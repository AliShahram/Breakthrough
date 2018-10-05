def initial_state(rows, columns, prows):
    big_list = []       #The 2D array holding all the elements

    for i in range(rows - prows):
        if i <= (prows - 1):
            small_list = ["X"] * columns
            big_list.append(small_list)

        else:
            small_list = ["."] * columns
            big_list.append(small_list)

    for i in range (prows):
        small_list = ["O"] * columns
        big_list.append(small_list)

    return big_list

