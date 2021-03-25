from antlr4 import *
from schema_gen.antlr import GraphQLLexer, GraphQLListener, GraphQLParser
from schema_gen.codegen import CodegenTool, Class, String, ClassInstance, IfElse, If, Method, Expr, Variable
import re
from math import floor
from datetime import datetime
from schema_gen.utils import strip_string_quotes, camel_case_to_snake_case, process_input_value_definition
from schema_gen.errors import ParsingError

GraphQLParser = GraphQLParser.GraphQLParser

graphene = 'graphene'
built_in_scalars = [
    'Int',
    'Float',
    'String',
    'Boolean',
    'ID',
    'Date',
    'Datetime',
    'Time'
    'Decimal',
    'JSONString',
    'Base64',
]


class SDLParser(GraphQLListener.GraphQLListener):
    def __init__(self, input_file, output_file=None):
        if output_file is None:
            output_file = input_file.split(sep='.')[0] + '_' + str(floor(datetime.now().timestamp())) + '.py'

        is_valid_file_name = re.match("\w+.py$", output_file)
        if is_valid_file_name is None:
            raise Exception('File is not a python file')
        self.output_file = output_file
        self.input_file = input_file
        self.codegen = CodegenTool(output_file=self.output_file)
        super().__init__()

    def enterTypeDefinition(self, ctx: GraphQLParser.TypeDefinitionContext):

        for child in ctx.children:
            # type definition is for an Object Type Definition
            if isinstance(child, GraphQLParser.ObjectTypeDefinitionContext) or isinstance(child,
                                                                                          GraphQLParser.InterfaceTypeDefinitionContext):
                # print(child.name().getText())
                # if ":" in child.name().getText():
                #     child.exitRule(self)
                is_object_type = isinstance(child, GraphQLParser.ObjectTypeDefinitionContext)
                is_interface = isinstance(child, GraphQLParser.InterfaceTypeDefinitionContext)

                type_class = Class(name=child.name().getText(), add_init_method=False)
                if is_object_type:
                    type_class.base_class = "ObjectType"
                elif is_interface:
                    type_class.base_class = "Interface"

                is_mutation = False
                if type_class.name == 'Mutation':
                    is_mutation = True
                    is_object_type = False

                meta_class = Class(name='meta')

                # create map for methods to be resolved
                methods_to_be_resolved = {}

                # get type description
                desc = child.description()
                if desc:
                    meta_class.add_class_variable('description', String(strip_string_quotes(desc.getText())))

                # get implemented interfaces
                if is_object_type or is_mutation:
                    if child.implementsInterfaces() is not None:
                        interfaces = child.implementsInterfaces().getText().split(sep='implements')
                        interfaces = interfaces[1].split(sep='&')
                        interface_string = ''
                        for i in interfaces:
                            interface_string = interface_string + i + ','
                        meta_class.add_class_variable('interfaces', f"({interface_string})")

                # get fields of the ObjectType or Interface

                if child.fieldsDefinition():
                    fields = child.fieldsDefinition().fields
                    if not is_mutation:
                        for field in fields:
                            # get field name and type
                            field_name = camel_case_to_snake_case(field.name().getText())
                            field_type = field.type_().getText()
                            field_required = False

                            # get field description
                            field_desc = field.description()
                            if field_desc is not None:
                                field_desc = String(strip_string_quotes(field_desc.getText()))
                            else:
                                field_desc = ''

                            if is_interface:
                                if field_type.lower() == type_class.name.lower():
                                    field_type = 'lambda: ' + field_type

                            # if field is a required field
                            if field_type[len(field_type) - 1] == '!':
                                field_required = True
                                field_code = ClassInstance('Field', field_type[:-1], required=True)
                            else:
                                field_code = ClassInstance('Field', field_type)

                            # if field is a list type
                            if field.type_().listType() is not None:
                                list_type_named_type = field.type_().listType().type_().getText()

                                if is_interface:
                                    if list_type_named_type.lower() == type_class.name.lower():
                                        list_type_named_type = 'lambda: ' + list_type_named_type

                                if list_type_named_type[len(list_type_named_type) - 1] == '!':
                                    field_code = ClassInstance('List',
                                                               str(ClassInstance('NonNull', list_type_named_type[:-1])),
                                                               required=field_required)
                                else:
                                    field_code = ClassInstance('List', list_type_named_type, required=field_required)

                            # get field arguments
                            if is_object_type:
                                args = field.argumentsDefinition()
                                args_string = []
                                if args is not None:
                                    args = args.args
                                    for arg in args:
                                        # add info to method_to_be_resolved map
                                        if field_name not in methods_to_be_resolved:
                                            methods_to_be_resolved[field_name] = [arg.name().getText()]
                                        else:
                                            methods_to_be_resolved[field_name].append(arg.name().getText())
                                        processed_arg = process_input_value_definition(arg)
                                        args_string.append(
                                            f"{String(processed_arg['name'])}: {str(processed_arg['arg_impl'])}")

                                    field_code.add_kwarg('args', "{" + ', '.join(args_string) + "}")

                            if field_desc != '':
                                field_code.add_kwarg(key='description', value=field_desc)
                            type_class.class_variables[field_name] = str(field_code)
                    else:
                        for field in fields:
                            # get field name and type
                            field_name = camel_case_to_snake_case(field.name().getText())
                            field_type = field.type_().getText()
                            field_required = False

                            field_class = Class(field.name().getText(), add_init_method=False, base_class='Mutation')
                            argument_class = Class(name='arguments')

                            # get field description
                            field_desc = field.description()
                            if field_desc is not None:
                                field_desc = String(strip_string_quotes(field_desc.getText()))
                            else:
                                field_desc = ''

                            # if field is a required field
                            if field_type[len(field_type) - 1] == '!':
                                field_required = True
                                field_code = ClassInstance('Field', field_type[:-1], required=True)
                            else:
                                field_code = ClassInstance('Field', field_type)

                            # if field is a list type
                            if field.type_().listType() is not None:
                                list_type_named_type = field.type_().listType().type_().getText()

                                if list_type_named_type[len(list_type_named_type) - 1] == '!':
                                    field_code = ClassInstance('List',
                                                               str(ClassInstance('NonNull', list_type_named_type[:-1])),
                                                               required=field_required)
                                else:
                                    field_code = ClassInstance('List', list_type_named_type, required=field_required)

                            # get field arguments
                            args = field.argumentsDefinition()
                            arg_list = []
                            if args is not None:
                                args = args.args
                                for arg in args:
                                    processed_arg = process_input_value_definition(arg)
                                    argument_class.add_class_variable(processed_arg['name'],
                                                                      str(processed_arg['arg_impl']))
                                    arg_list.append(processed_arg['name'])

                            field_class.add_sub_class(argument_class)
                            field_class.add_method(
                                method=Method(
                                    name='mutate',
                                    arguments=['root', 'info'] + arg_list
                                )
                            )

                            if field_desc != '':
                                field_code.add_kwarg(key='description', value=field_desc)

                            # write mutation classes for the mutation's fields
                            self.codegen.write_class(field_class)
                            type_class.class_variables[field_name] = str(field_code)

                # add resolver methods
                if not is_mutation:
                    for method in methods_to_be_resolved:
                        type_class.add_method(method_name='resolve_' + method,
                                              arguments_names=['info'] + methods_to_be_resolved[method])

                if type_class.name == 'Query':
                    for var in type_class.class_variables:
                        if var not in methods_to_be_resolved:
                            type_class.add_method(method_name='resolve_' + var, arguments_names=['info'])

                if len(meta_class.class_variables) != 0:
                    type_class.add_sub_class(meta_class)

                self.codegen.write_class(type_class)

            # type definition is for an EnumTypeDefinition
            elif isinstance(child, GraphQLParser.EnumTypeDefinitionContext):
                enum_class = Class(name=child.name().getText(), base_class="Enum", add_init_method=False)
                meta_class = Class(name='meta')

                # get enum description
                desc = child.description()
                if desc:
                    meta_class.add_class_variable('description', String(strip_string_quotes(desc.getText())))

                # get fields of the Enum
                fields = child.enumValuesDefinition().fields
                fields_and_desc = {}
                for field in fields:
                    # get field name and type
                    enum_value = field.enumValue().getText()

                    # get enum description
                    field_desc = field.description()
                    if field_desc is not None:
                        field_desc = String(strip_string_quotes(field_desc.getText()))
                    else:
                        field_desc = ''

                    if field_desc != '':
                        # do something
                        fields_and_desc[enum_value] = field_desc

                    # add enums as class variables to main class
                    enum_class.add_class_variable(enum_value, String(enum_value))

                # add enums description
                method = Method(
                    name='description',
                    decorators=['@property'],
                    arguments=[]
                )

                if_else = IfElse(
                    indent_level=method.get_indent_level() + 1,
                    else_action=[Expr("pass")],
                )

                for i in fields_and_desc:
                    if_else.add_elif(If(
                        expr=Expr(f"self == {enum_class.name}.{i}"),
                        action=[Expr(f"return {fields_and_desc[i]}")]
                    ))

                method.set_body([if_else])

                enum_class.add_method(method=method)

                if len(meta_class.class_variables) != 0:
                    enum_class.add_sub_class(meta_class)

                self.codegen.write_class(enum_class)

            # type definition is for an EnumTypeDefinition
            elif isinstance(child, GraphQLParser.ScalarTypeDefinitionContext):
                if child.name().getText().capitalize() in built_in_scalars:
                    continue
                scalar_class = Class(name=child.name().getText(), base_class="Scalar", add_init_method=False)
                desc = child.description()

                if desc is not None:
                    scalar_class.description = strip_string_quotes(desc.getText())

                serialize_method = Method(
                    name='serialize',
                    arguments=['val'],
                    decorators=['@staticmethod'],
                    body=[Expr('# write method body'), Expr('pass')],
                    is_static=True
                )
                parse_literal_method = Method(
                    name='parse_literal',
                    arguments=['node'],
                    decorators=['@staticmethod'],
                    body=[Expr('# write method body'), Expr('pass')],
                    is_static=True
                )

                parse_value_method = Method(
                    name='parse_value',
                    arguments=['value'],
                    decorators=['@staticmethod'],
                    body=[Expr('# write method body'), Expr('pass')],
                    is_static=True
                )

                scalar_class.add_method(method=serialize_method)
                scalar_class.add_method(method=parse_literal_method)
                scalar_class.add_method(method=parse_value_method)

                self.codegen.write_class(scalar_class)

            elif isinstance(child, GraphQLParser.UnionTypeDefinitionContext):
                union_class = Class(name=child.name().getText(), base_class='Union')
                meta_class = Class(name='Meta')

                unions = child.unionMemberTypes().getText()

                if unions[0] == '=':
                    unions = unions[1:]

                unions = ', '.join(unions.split(sep='|'))

                meta_class.add_class_variable(variable_name='types', variable_value=f"({unions})")

                desc = child.description()

                if desc is not None:
                    meta_class.add_class_variable(variable_name='description',
                                                  variable_value=String(strip_string_quotes(desc.getText())))

                union_class.add_sub_class(meta_class)
                self.codegen.write_class(union_class)
                print(unions)

            elif isinstance(child, GraphQLParser.InputObjectTypeDefinitionContext):
                type_class = Class(name=child.name().getText(), base_class="InputObjectType", add_init_method=False)
                meta_class = Class(name='meta')

                # get type description
                desc = child.description()
                if desc:
                    meta_class.add_class_variable('description', String(strip_string_quotes(desc.getText())))

                # get fields
                if child.inputFieldsDefinition():
                    fields = child.inputFieldsDefinition().fields
                    for field in fields:
                        processed_ivd = process_input_value_definition(field)
                        type_class.add_class_variable(processed_ivd['name'], str(processed_ivd['arg_impl']))

                if len(meta_class.class_variables) != 0:
                    type_class.add_sub_class(meta_class)

                self.codegen.write_class(type_class)
            else:
                print(type(child))

    def enterSchemaDefinition(self, ctx: GraphQLParser.SchemaDefinitionContext):

        schema_obj = ClassInstance('Schema')

        fields = ctx.fields
        for field in fields:
            schema_obj.add_kwarg(strip_string_quotes(field.operationType().getText()),
                                 strip_string_quotes(field.namedType().getText()))

        var = Variable(
            name='schema',
            value=schema_obj
        )
        self.codegen.write_variable(var)

    def __call__(self):
        try:
            self.codegen.import_package(package=graphene, mode=2, object='*')
            input_stream = FileStream(self.input_file)
            lexer = GraphQLLexer.GraphQLLexer(input_stream)
            stream = CommonTokenStream(lexer)
            parser = GraphQLParser(stream)
            tree = parser.document()
            walker = ParseTreeWalker()
            walker.walk(self, tree)
        except Exception as err:
            raise ParsingError(str(err))



# TODO: Fix issue with parser reading type in fields
# TODO: Write documentation
# TODO: Publish app
