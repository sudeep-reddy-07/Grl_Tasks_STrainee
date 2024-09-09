def count_word_occurrences(n, words):
    """
    Counts the occurrences of each word and maintains the order of appearance.

    Parameters:
    n (int): The number of words.
    words (list): A list of words.

    Returns:
    tuple: (number of distinct words, list of occurrences)
    """
    word_count = {}
    word_order = []
    
    # Iterate through words and count occurrences
    for word in words:
        if word not in word_count:
            word_order.append(word)
            word_count[word] = 1
        else:
            word_count[word] += 1
    
    distinct_count = len(word_order)
    occurrences = [str(word_count[word]) for word in word_order]
    
    return distinct_count, occurrences


if __name__ == "__main__":
    # Input the number of words
    n = int(input().strip())
    words = [input().strip() for _ in range(n)]
    
    # Get the distinct word count and occurrences
    distinct_count, occurrences = count_word_occurrences(n, words)
    
    # Output the results
    print(distinct_count)
    print(" ".join(occurrences))
