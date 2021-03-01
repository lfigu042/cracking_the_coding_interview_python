# Cracking the coding interview methods

# 1.1 isUnique method
def is_unique(s1):
    s2 = set(s1)
    return len(s2) == len(s1)


# 1.2 checkPermutation method
def check_perm(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1 != len2:
        return False
    sorted1 = sorted(s1)
    sorted2 = sorted(s2)
    return sorted1 == sorted2


# 1.3 URLify
def make_url(s):
    return s.strip().replace(" ", "%20")


# 1.4 check if palindrome permutation
def is_palindrome_perm(s1):
    s1 = s1.lower().replace(" ", "")
    s2 = ""

    for letter in s1:
        if letter not in s2:
            s2 = s2 + letter
        else:
            s2 = s2.replace(letter, '', 1)

    return (len(s2) == 1) or (len(s2) == 0)


if __name__ == '__main__':
    # test for 1.1 isUnique
    my_str = "abccd"
    print(is_unique(my_str))

    # test for 1.2 checkPermutation
    str1 = "hello"
    str2 = "ellho"
    print(check_perm(str1, str2))

    # test for 1.3 URLify
    s = "    bubbles are fun all time       "
    print(make_url(s))

    # test for 1.4 Palindrome Permutation
    s1 = "ba"
    print(is_palindrome_perm(s1))
