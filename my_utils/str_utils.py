def str_reverse(s):
    s = s[::-1]
    return s


def substr(s, x, y):
    s = s[x:y]
    return s


if __name__ == '__main__':

    print(str_reverse("123456789"))
    print(substr("123456789", 1, 7))