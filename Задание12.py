def holes_in_word(word) -> int:
    """
    Calculate the number of holes in a word.
    :param word: str
    :return: int
    """
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    count = 0
    for letter in word:
        if letter in holes_letters:
            count += 1
    return count


def count_letters(text) -> int:
    """
    Calculate the number of letters in a text
    with holes and without holes.
    :param text: str
    :return: int
    """
    holes_letters = {'a', 'b', 'd', 'e', 'g', 'o', 'p', 'q'}
    holes = 0
    no_holes = 0

    for let in text:
        if let.isalpha():
            if let in holes_letters:
                holes += 1
            else:
                no_holes += 1
    return holes, no_holes


def words_with_two_or_more_holes(text) -> list[str]:
    """
    Return a list of words with two or more holes.
    :param text:
    :type text: str
    :return: result
    :rtype: list[str]
    """
    words = text.split()
    result = []
    for word in words:
        if holes_in_word(word) >= 2:
            result.append(word)
    return result


text = input()

# Calculate amount of letters with holes and without holes.
holes, no_holes = count_letters(text)
print(holes, no_holes)

# List of words with two or more holes.
words_with_holes = words_with_two_or_more_holes(text)
print(words_with_holes)
