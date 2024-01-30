#!/usr/bin/python3

def text_indentation(text):
    """
    function that prints a text with 2 lines
    after each of these chars: ., ? and :
    Args:
        text: text to be fed(string)
    Notes:
        checks if input text is string or not
    """
    try:
        if not isinstance(text, str):
            raise TypeError("text must be a string")

        seprs = ['.', '?', ':']
        check_seprs = False

        for c in text:
            if c in seprs:
                print(c + '\n')
                check_seprs = True
            elif (c == ' ' and check_seprs):
                continue
            else:
                print(c, end='')
                check_seprs = False
    except TypeError as TE:
        print(TE)


if (__name__ == "__main__"):
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
