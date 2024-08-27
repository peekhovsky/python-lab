def check_str(s: str):
    str_len = len(s)

    i = 0
    j = str_len - 1

    while i < j:
        char1 = s[i]
        char2 = s[j]

        if not char1.isalpha() and not char1.isdigit():
            i += 1
            continue
        elif not char2.isalpha() and not char2.isdigit():
            j -= 1
            continue
        elif s[i].lower() != s[j].lower():
            return False
        else:
            i += 1
            j -= 1

    return True


if __name__ == '__main__':
    assert check_str("LoL") is True
    assert check_str("LoLoL") is True
    assert check_str("LoggoL") is True
    assert check_str("32635745") is False
    assert check_str("tip spot!") is False
    assert check_str("LoL racecar LoL") is True
    assert check_str("LoL racedffcar LoL") is False

    assert check_str("A man, a plan, a canal - Panama") is True
    assert check_str("No 'x' in Nixon") is True
    assert check_str("top spot") is True
