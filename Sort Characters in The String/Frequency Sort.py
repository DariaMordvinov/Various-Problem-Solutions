from heapq import *


def sort_character_by_frequency(str):
    # Creates hashmap for storing frequency of each character in the string
    charFrequencyMap = {}
    for char in str:
        if char not in charFrequencyMap:
            charFrequencyMap[char] = 0
        charFrequencyMap[char] += 1

    # Creates max heap for storing frequencies
    heap = []
    for char, frequency in charFrequencyMap.items():
        heappush(heap, [-frequency, char])

    # Constructs the answer by getting from the heap character by character
    # in decreasing order based on their frequency
    answer = ""
    while heap:
        char_freq = heappop(heap)
        answer += char_freq[1] * (-char_freq[0])

    return answer


def main():

    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " +
        sort_character_by_frequency("abcbab"))


main()
