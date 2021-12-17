from collections import deque


def generate_generalized_abbreviation(word):
    result = []
    queue = deque()
    queue.append("_")

    # Generate permutations of the word, where each character either stays the same or is replaced with "_"
    for letter in word:
        n = len(queue)
        for _ in range(n):
            string = queue.popleft()
            queue.append(string + "_")
            queue.append(string + letter)

    # Goes through every permutation in the queue
    while queue:
        # Gets the string and gets rid of its first character, which is always "_"
        string = queue.popleft()[1:]
        count = 0
        new_string = ""
        # Goes through each character of the string and counts "_" character
        for i in range(len(string)):
            if string[i] == "_":
                if i == len(string) - 1:
                    new_string += str(count + 1)
                else:
                    count += 1
            else:
                if count > 0:
                    new_string += str(count)
                    count = 0
                new_string += string[i]
        result.append(new_string)

    return result
