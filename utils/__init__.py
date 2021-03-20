def strip_string_quotes(string: str) -> str:
    if string[0] == '"' and string[len(string) - 1] == '"':
        res = string[1:]
        res = res[:-1]
    return res


def stringify(string) -> str:
    return "'" + str(string) + "'"


def triple_stringify(string) -> str:
    return '"""' + str(string) + '"""'


def snake_case_to_camel_case(string) -> str:
    parts = string.split(sep='_')
    for i, part in enumerate(parts):
        if i != 0:
            parts[i] = part.capitalize()
    return ''.join(parts)


def camel_case_to_snake_case(string) -> str:
    parts = list(string)
    for i, part in enumerate(parts):
        if part.isupper():
            if i == 0:
                parts[i] = part.lower()
                continue
            parts[i] = '_' + part.lower()
    return ''.join(parts)


if __name__ == '__main__':
    print(camel_case_to_snake_case('CamelCaseToBeFuckingTransformed'))
