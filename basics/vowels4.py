def search_for_vowels(phrase: str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aieou')
    return vowels.intersection(set(phrase))


def search_for_letters(phrase: str, letters: str) -> set:
    """Return a set of the 'letters' foudn in 'phrase'."""
    return set(letters).intersection(set(phrase))