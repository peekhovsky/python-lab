def replacer(s: str) -> str:
    result = ''

    for char in s:
        if char == '"':
            result += "'"
        elif char == "'":
            result += '"'
        else:
            result += char

    return result


if __name__ == '__main__':
    assert replacer('Python"is\'simple and effective!') == 'Python\'is"simple and effective!'
    assert replacer('"Python"is\'simple and effective!\'') == '\'Python\'is"simple and effective!"'
    assert replacer('\'Python"is\'simple and effective!"') == '"Python\'is"simple and effective!\''
