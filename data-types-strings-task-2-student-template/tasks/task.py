def get_longest_word(s: str) -> str:
    words = s.split()
    return max(words, key=len)


if __name__ == '__main__':
    assert get_longest_word("Python is simple and effective") == 'effective!'
    assert get_longest_word("Python is simple\nand\teffective!") == 'effective!'
