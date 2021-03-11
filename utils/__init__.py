def strip_string_quotes(string: str) -> str:
    res = string[1:]
    res = res[:-1]
    return res


def stringify(string) -> str:
    return "'" + str(string) + "'"
