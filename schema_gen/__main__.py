import argparse
import schema_gen

parser = argparse.ArgumentParser(
    prog='schemagen',
    description='Parse a GraphQL Schema file',
)

parser.add_argument(
    'command',
    metavar='command',
    type=str,
    help='command',
    action='store'
)

parser.add_argument(
    'payload',
    metavar='payload',
    type=str,
    help='payload',
    action='store'
)

parser.add_argument(
    '-o',
    '--output',
    metavar='output_file',
    type=str,
    help='Output file for generated code',
    action='store'
)

args = parser.parse_args()
if args.command == 'parse':
    sdl_parser = schema_gen.SDLParser(
        input_file=args.payload,
        output_file=args.output
    )
    sdl_parser()

else:
    print('invalid command!')

