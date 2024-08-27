def get_fractions(a_b: str, c_b: str) -> str:
    fraction1_split = a_b.split('/')

    numerator1 = fraction1_split[0]
    numerator2 = c_b.split('/')[0]
    denominator = fraction1_split[1]

    result_numerator = int(numerator1) + int(numerator2)
    return f"{a_b} + {c_b} = {result_numerator}/{denominator}"


if __name__ == '__main__':
    assert get_fractions('1/3', '5/3') == '1/3 + 5/3 = 6/3'
    assert get_fractions('55/8', '3/8') == '55/8 + 3/8 = 58/8'
