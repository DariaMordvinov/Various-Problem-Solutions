from collections import deque


def backspace_compare(str1, str2):
    str1_d = deque()
    str2_d = deque()

    # Iterates through first string
    for pointer1 in range(len(str1)):
        if str1[pointer1] != "#":
            str1_d.append(str1[pointer1])
        else:
            if len(str1_d) > 0:
                # Pop character from the deque if encounter #
                str1_d.pop()

    # Iterates through second string
    for pointer2 in range(len(str2)):
        if str2[pointer2] != "#":
            str2_d.append(str2[pointer2])
        else:
            if len(str2_d) > 0:
                # Pop character from the deque if encounter #
                str2_d.pop()

    if str1_d == str2_d:
        return True
    return False
