from antlr4 import *
from antlr import GraphQLParser, GraphQLLexer, GraphQLListener
from codegen import CodegenTool, Class, String, ClassInstance
import re
from math import floor
from datetime import datetime
from utils import strip_string_quotes

GraphQLParser = GraphQLParser.GraphQLParser

graphene = 'graphene'

sdl_type_to_graphene_type = {
    'ID': '',
    'String': ''
}


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
            if isinstance(child, GraphQLParser.ObjectTypeDefinitionContext) or isinstance(child, GraphQLParser.InterfaceTypeDefinitionContext):
                is_object_type = isinstance(child, GraphQLParser.ObjectTypeDefinitionContext)
                is_interface = isinstance(child, GraphQLParser.InterfaceTypeDefinitionContext)

                if is_object_type:
                    type_class = Class(name=child.name().getText(), base_class="ObjectType", add_init_method=False)
                elif is_interface:
                    type_class = Class(name=child.name().getText(), base_class="Interface", add_init_method=False)
                meta_class = Class(name='meta')

                # get type description
                desc = child.description()
                if desc:
                    meta_class.add_class_variable('description', String(strip_string_quotes(desc.getText())))

                # get implemented interfaces
                if is_object_type:
                    interfaces = child.implementsInterfaces().getText().split(sep='implements')
                    interfaces = interfaces[1].split(sep='&')
                    interface_string = ''
                    for i in interfaces:
                        interface_string = interface_string+i+','
                    meta_class.add_class_variable('interfaces', f"({interface_string})")

                # get fields of the ObjectType
                fields = child.fieldsDefinition().fields
                for field in fields:
                    # get field name and type
                    var_name = field.name().getText()
                    var_value = field.type_().getText()

                    # get field description
                    field_desc = field.description()
                    if field_desc is not None:
                        field_desc = String(strip_string_quotes(field_desc.getText()))
                    else:
                        field_desc = ''

                    # if field is a required field
                    if var_value[len(var_value) - 1] == '!':
                        field_code = ClassInstance('Field', var_value[:-1], required=True)
                    else:
                        field_code = ClassInstance('Field', var_value)

                    # if field is a list type
                    if field.type_().listType() is not None:
                        list_type_named_type = field.type_().listType().type_().getText()
                        if list_type_named_type[len(list_type_named_type) - 1] == '!':
                            field_code = ClassInstance('List', str(ClassInstance('NonNull', list_type_named_type[:-1])))
                        else:
                            field_code = ClassInstance('List', list_type_named_type)

                    if field_desc != '':
                        field_code.add_kwarg(key='description', value=field_desc)

                    type_class.class_variables[var_name] = str(field_code)
                if type_class.name == 'Query':
                    for var in type_class.class_variables:
                        type_class.add_method(method_name='resolve_' + var, arguments_names=['info'])

                if len(meta_class.class_variables) != 0:
                    type_class.add_sub_class(meta_class)

                self.codegen.write_class(type_class)


            else:
                pass

    def __call__(self):
        self.codegen.import_package(package=graphene, mode=2, object='*')
        input_stream = FileStream(self.input_file)
        lexer = GraphQLLexer.GraphQLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = GraphQLParser(stream)
        tree = parser.document()
        walker = ParseTreeWalker()
        walker.walk(self, tree)
        print(tree.toStringTree(recog=parser))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parser = SDLParser('test.graphql', 'test.py')
    parser()
