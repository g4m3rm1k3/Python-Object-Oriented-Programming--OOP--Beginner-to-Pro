# Get all digits as str
import random
user_input = "20 19 18 17 16 15 14 13 12 11 10 9 8 6 5 4 3 2 1"  # input()
# user_input = "30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 6 5 4 3 2 1"  # input()
# user_input = "40 39 38 37 36 35 34 33 32 31 30 29 28 27 26 25 24 23 22 21 20 19 18 17 16 15 14 13 12 11 10 9 8 6 5 4 3 2 1"  # input()


def generate_unique_random_list(size, min_value=0, max_value=100):
    """
    Generates a random list of unique numbers.

    Parameters:
    - size: The number of elements in the list.
    - min_value: The minimum value of the random numbers.
    - max_value: The maximum value of the random numbers.

    Returns:
    - A list of unique random numbers.

    Raises:
    - ValueError: If size is greater than the range of unique values.
    """
    if size > (max_value - min_value + 1):
        raise ValueError(
            "Size is greater than the number of unique values in the range.")

    return random.sample(range(min_value, max_value + 1), size)



# cast as int
digits = [int(i) for i in user_input.split(" ") if int(i) > 0]
# print(digits)
# sort in place double pointer
digits = [i for i in range(10, 0, -1)]
# print(digits)
digits = generate_unique_random_list(size=10, min_value=1, max_value=50)

def first_loop(digits):
    swaps = 0
    compares = 0
    for i in range(len(digits)-1):
        swap = False
        for j in range(i, len(digits)-1):
            curr, next = digits[j], digits[j+1]
            compares += 1
            if curr > next:
                digits[j], digits[j+1] = next, curr
                swap = True
                swaps += 1
            if digits[j] < digits[i]:
                digits[i], digits[j] = digits[j], digits[i]
                swap = True
                swaps += 1
        if not swap:
            break
    return f'Swaps: {swaps}, Compares: {compares}'


def second_loop(digits):
    swaps = 0
    compares = 0
    for i in range(len(digits)-1):
        swap = False
        for j in range(i, len(digits)-(i+1)):
            last, prev = digits[-(i+1)], digits[-(i+2)]
            if prev > last:
                digits[-(i+1)], digits[-(i+2)] = prev, last
                prev, last = last, prev
            first, last = digits[i],  digits[-(i+1)]
            if first > last:
                digits[i], digits[-(i+1)] = last, first
            before, after = digits[-(i+2)], digits[-(i+3)]
            if after > before:
                digits[-(i+2)], digits[-(i+3)], =  after, before
                after, before = before, after
            curr, next = digits[j], digits[j+1]
            compares += 1
            if curr > next:
                digits[j], digits[j+1] = next, curr
                swap = True
                swaps += 1
            if digits[j] < digits[i]:
                digits[i], digits[j] = digits[j], digits[i]
                swap = True
                swaps += 1
        if not swap:
            break
    return f'Swaps: {swaps}, Compares: {compares}'





def third_loop(digits):
    swaps = 0
    compares = 0
    for i in range(len(digits)//2):
        swap = False
        for j in range(i, len(digits)//2):
            compares += 1
            first, last = digits[i], digits[-i+-1]
            next = digits[j]
            if next > last:
                digits[j], digits[-i+-1] = last, next
                swap = True
                swaps += 1
            if first > next:
                digits[i], digits[j] = next, first
                swap = True
                swaps += 1
        if not swap:
            break
    return f'Swaps: {swaps}, Compares: {compares} ,list size: {len(digits)}'


def fourth_loop(digits):
    swaps = 0
    swap = False
    compares = 0
    i = 0
    j = 0
    k = -1
    while i < len(digits)//2:
        compares += 1
        next = j
        last = k
        first = i
        if digits[next] > digits[last]:
            digits[last], digits[next] = digits[next], digits[last]
            swaps += 1
            swap = True
        if digits[next] < digits[first]:
            digits[first], digits[next] = digits[next], digits[first]
            swaps += 1
            swap = True
        if j == len(digits)//2:
            if not swap:
                break
            i += 1
            j = i
            k -= 1
        j += 1
    return f'Swaps: {swaps}, Compares: {compares} ,list size: {len(digits)}'







def fifth_loop(digits):
    compares = 0
    swaps = 0
    start = 0
    end = -1
    next = 1
    prev = -2
    i = 0
    while i < len(digits):
        compares += 1
        first = start
        last = end
        if digits[first] < digits[last]:
            digits[first], digits[last] = digits[last], digits[first]
            swaps += 1
        if digits[first] > digits[next]:
            digits[first], digits[next] = digits[next], digits[first]
            swaps += 1
        if digits[last] < digits[prev]:
            digits[last], digits[prev] = digits[prev], digits[last]
            swaps += 1
        if i == len(digits)//2:
            first -= 1
            last += 1
            next -= 1
            prev += 1
        else:
            first += 1
            last -= 1
            next += 1
            prev -= 1
        i += 1
    return f'Swaps: {swaps}, Compares: {compares} ,list size: {len(digits)}'


# filter list cast generator as list join as str
# digits = " ".join([str(i) for i in digits])
# print(digits, end=" ")
print()
# print(first_loop(digits))
# print(second_loop(digits))
# print(third_loop(digits))
# print(digits)
print(fourth_loop(digits))
# print(fifth_loop(digits))
print(digits)
