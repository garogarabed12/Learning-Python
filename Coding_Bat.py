def not_string(str):
    """
    Given a string, return a new string where "not " has been added to the front. However, if the string already
    begins with "not", return the string unchanged.

    Examples:
    not_string('candy') → 'not candy'
    not_string('x') → 'not x'
    not_string('not bad') → 'not bad'
    """
    str = str.lower()
    if str[0:3] != "not":
        return "".join("not " + str)
    else:
        return str


def missing_char(str, n):
    """
    Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value
    of nwill be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

    Examples:
    missing_char('kitten', 1) → 'ktten
    missing_char('kitten', 0) → 'itten
    missing_char('kitten', 4) → 'kittn'
    """
    return str[:n] + str[n + 1:]


def front_back(str):
    """
    Given a string, return a new string where the first and last chars have been exchanged.

    Examples:
    front_back('code') → 'eod
    front_back('a') → '
    front_back('ab') → 'ba'
    """
    if len(str) <= 1:
        return str
    body = str[1:-1]
    return str[-1] + body + str[0]


def front3(str):
    """
    Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3, the
    front is whatever is there. Return a new string which is 3 copies of the front.

    Examples
    front3('Java') → 'JavJavJ
    front3('Chocolate') → 'ChoChoC
    front3('abc') → 'abcabcabc'
    """
    return str[:3] * 3


def string_splosion(str):
    """
    Given a non-empty string like "Code" return a string like "CCoCodCode".
    Examples
    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
    """
    res = ""
    for i in range(len(str) + 1):
        res = res + str[:i]
    return res
