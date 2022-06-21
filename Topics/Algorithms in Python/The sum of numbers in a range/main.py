def range_sum(numbers, start, end):
    sum_numbers = 0
    for number in numbers:
        if int(start) <= int(number) <= int(end):
            sum_numbers += int(number)
    return sum_numbers


input_numbers = list(input().split())
a, b = input().split()
print(range_sum(input_numbers, a, b))