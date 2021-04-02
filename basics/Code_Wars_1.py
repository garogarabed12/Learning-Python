def comp(array1, array2):
    """
    A function that checks whether the two arrays have the "same" elements, with the same multiplicities.
    "Same" means, here, that the elements in b are the elements in a squared, regardless of the order.
    """
    return sorted([i * i for i in array1]) == sorted(array2)


def sum_array(arr):
    """
    Sum all the numbers of the array (in F# and Haskell you get a list) except the highest and the lowest
    element (the value, not the index!).
    (The highest/lowest element is respectively only one element at each edge, even if there are more than one
    with the same value!)
    """
    if arr is None:
        return 0
    else:
        arr = sorted(arr)
        return sum([i for i in arr[1:len(arr) - 1: 1]])  # OR:   return 0 if arr == None else sum(sorted(arr)[1:-1])


def points(games):
    """
Our football team finished the championship. The result of each match look like "x:y". Results of all matches
    are recorded in the collection.
For example: ["3:1", "2:2", "0:1", ...]
Write a function that takes such collection and counts the points of our team in the championship. Rules for
counting points for each match:
    if x>y - 3 points
    if x<y - 0 point
    if x=y - 1 point
    """
    points = 0
    for game in games:
        scores = game.split(':')
        if scores[0] > scores[1]:
            points += 3
        elif scores[0] == scores[1]:
            points += 1
    return points


def reverse(string):
    """Reverse a given string"""
    return string[::-1]
