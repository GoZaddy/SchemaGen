def strip_string_quotes(string: str) -> str:
    if string[0] == '"' and string[len(string) - 1] == '"':
        res = string[1:]
        res = res[:-1]
    else:
        return string
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


def is_a_builtin(word) -> bool:
    """
    Returns True if a word is a builtin python object
    Args:
        word: word to check

    Returns: True if word is builtin python object

    """
    import builtins
    return str(word) in dir(builtins)


def process_input_value_definition(ivd) -> dict:
    """
    This function process an inputValueDefintionContext and returns the needed results
    Args:
        ivd: the inputValueDefinitionContext

    Returns:
        a dict containing the results

    """

    from schema_gen import codegen
    ClassInstance = codegen.ClassInstance

    arg_type = ivd.type_().getText()
    arg_required = False
    if arg_type[len(arg_type) - 1] == '!':
        arg_required = True
        arg_type = arg_type[:-1]

    # this represents the graphene implementation of this IVD (InputValueDefinition)
    arg_impl = ClassInstance(arg_type, required=arg_required)

    # if any of the argument types is a list type:
    if ivd.type_().listType() is not None:
        list_type_named_type = ivd.type_().listType().type_().getText()
        if list_type_named_type[len(list_type_named_type) - 1] == '!':
            arg_impl = ClassInstance('List', str(
                ClassInstance('NonNull', list_type_named_type[:-1])), required=arg_required)
        else:
            arg_impl = ClassInstance('List', list_type_named_type, required=arg_required)

    # get argument description
    if ivd.description() is not None:
        arg_desc = ivd.description().getText()
        arg_impl.add_kwarg('description', arg_desc)

    # get argument default value
    if ivd.defaultValue() is not None:
        arg_impl.add_kwarg('default_value', ivd.defaultValue().value().getText())

    return {
        'name': ivd.name().getText(),
        'arg_impl': arg_impl
    }


if __name__ == '__main__':
    print(camel_case_to_snake_case('CamelCaseToBeFuckingTransformed'))
