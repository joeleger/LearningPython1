
def search4vowels(phrase: str) -> set:
    """Return the found vowels in the word phrase"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(letters: str, phrase: str = 'aeiou') -> set:
    """Return a sorted phrase from a set of letters"""
    return set(letters).intersection(set(phrase))
