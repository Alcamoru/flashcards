def last_indexof_max(numbers):
    # write the modified algorithm here
    i = 0
    for n in range(1, len(numbers)):
        if numbers[n] >= numbers[i]:
            i = n
    return i
