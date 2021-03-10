from antlr4 import *
from antlr import GraphQLParser, GraphQLLexer, GraphQLListener


def generate_code(input_file, output_file):
    input_stream = FileStream(input_file)
    lexer = GraphQLLexer.GraphQLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GraphQLParser.GraphQLParser(stream)
    tree = parser.document()
    walker = ParseTreeWalker()
    listener = GraphQLListener.GraphQLListener()
    walker.walk(listener, tree)
    print(tree.toStringTree(recog=parser))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_code('test.graphql', '')
