# Generated from GraphQL.g4 by ANTLR 4.9
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GraphQLParser import GraphQLParser
else:
    from GraphQLParser import GraphQLParser

# This class defines a complete listener for a parse tree produced by GraphQLParser.
class GraphQLListener(ParseTreeListener):

    # Enter a parse tree produced by GraphQLParser#document.
    def enterDocument(self, ctx:GraphQLParser.DocumentContext):
        pass

    # Exit a parse tree produced by GraphQLParser#document.
    def exitDocument(self, ctx:GraphQLParser.DocumentContext):
        pass


    # Enter a parse tree produced by GraphQLParser#definition.
    def enterDefinition(self, ctx:GraphQLParser.DefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#definition.
    def exitDefinition(self, ctx:GraphQLParser.DefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#executableDefinition.
    def enterExecutableDefinition(self, ctx:GraphQLParser.ExecutableDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#executableDefinition.
    def exitExecutableDefinition(self, ctx:GraphQLParser.ExecutableDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#operationDefinition.
    def enterOperationDefinition(self, ctx:GraphQLParser.OperationDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#operationDefinition.
    def exitOperationDefinition(self, ctx:GraphQLParser.OperationDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#operationType.
    def enterOperationType(self, ctx:GraphQLParser.OperationTypeContext):
        pass

    # Exit a parse tree produced by GraphQLParser#operationType.
    def exitOperationType(self, ctx:GraphQLParser.OperationTypeContext):
        pass


    # Enter a parse tree produced by GraphQLParser#selectionSet.
    def enterSelectionSet(self, ctx:GraphQLParser.SelectionSetContext):
        pass

    # Exit a parse tree produced by GraphQLParser#selectionSet.
    def exitSelectionSet(self, ctx:GraphQLParser.SelectionSetContext):
        pass


    # Enter a parse tree produced by GraphQLParser#selection.
    def enterSelection(self, ctx:GraphQLParser.SelectionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#selection.
    def exitSelection(self, ctx:GraphQLParser.SelectionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#field.
    def enterField(self, ctx:GraphQLParser.FieldContext):
        pass

    # Exit a parse tree produced by GraphQLParser#field.
    def exitField(self, ctx:GraphQLParser.FieldContext):
        pass


    # Enter a parse tree produced by GraphQLParser#arguments.
    def enterArguments(self, ctx:GraphQLParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by GraphQLParser#arguments.
    def exitArguments(self, ctx:GraphQLParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by GraphQLParser#argument.
    def enterArgument(self, ctx:GraphQLParser.ArgumentContext):
        pass

    # Exit a parse tree produced by GraphQLParser#argument.
    def exitArgument(self, ctx:GraphQLParser.ArgumentContext):
        pass


    # Enter a parse tree produced by GraphQLParser#alias.
    def enterAlias(self, ctx:GraphQLParser.AliasContext):
        pass

    # Exit a parse tree produced by GraphQLParser#alias.
    def exitAlias(self, ctx:GraphQLParser.AliasContext):
        pass


    # Enter a parse tree produced by GraphQLParser#fragmentSpread.
    def enterFragmentSpread(self, ctx:GraphQLParser.FragmentSpreadContext):
        pass

    # Exit a parse tree produced by GraphQLParser#fragmentSpread.
    def exitFragmentSpread(self, ctx:GraphQLParser.FragmentSpreadContext):
        pass


    # Enter a parse tree produced by GraphQLParser#fragmentDefinition.
    def enterFragmentDefinition(self, ctx:GraphQLParser.FragmentDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#fragmentDefinition.
    def exitFragmentDefinition(self, ctx:GraphQLParser.FragmentDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#fragmentName.
    def enterFragmentName(self, ctx:GraphQLParser.FragmentNameContext):
        pass

    # Exit a parse tree produced by GraphQLParser#fragmentName.
    def exitFragmentName(self, ctx:GraphQLParser.FragmentNameContext):
        pass


    # Enter a parse tree produced by GraphQLParser#typeCondition.
    def enterTypeCondition(self, ctx:GraphQLParser.TypeConditionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#typeCondition.
    def exitTypeCondition(self, ctx:GraphQLParser.TypeConditionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#inlineFragment.
    def enterInlineFragment(self, ctx:GraphQLParser.InlineFragmentContext):
        pass

    # Exit a parse tree produced by GraphQLParser#inlineFragment.
    def exitInlineFragment(self, ctx:GraphQLParser.InlineFragmentContext):
        pass


    # Enter a parse tree produced by GraphQLParser#value.
    def enterValue(self, ctx:GraphQLParser.ValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#value.
    def exitValue(self, ctx:GraphQLParser.ValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#intValue.
    def enterIntValue(self, ctx:GraphQLParser.IntValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#intValue.
    def exitIntValue(self, ctx:GraphQLParser.IntValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#floatValue.
    def enterFloatValue(self, ctx:GraphQLParser.FloatValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#floatValue.
    def exitFloatValue(self, ctx:GraphQLParser.FloatValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#booleanValue.
    def enterBooleanValue(self, ctx:GraphQLParser.BooleanValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#booleanValue.
    def exitBooleanValue(self, ctx:GraphQLParser.BooleanValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#stringValue.
    def enterStringValue(self, ctx:GraphQLParser.StringValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#stringValue.
    def exitStringValue(self, ctx:GraphQLParser.StringValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#nullValue.
    def enterNullValue(self, ctx:GraphQLParser.NullValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#nullValue.
    def exitNullValue(self, ctx:GraphQLParser.NullValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#enumValue.
    def enterEnumValue(self, ctx:GraphQLParser.EnumValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#enumValue.
    def exitEnumValue(self, ctx:GraphQLParser.EnumValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#listValue.
    def enterListValue(self, ctx:GraphQLParser.ListValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#listValue.
    def exitListValue(self, ctx:GraphQLParser.ListValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#objectValue.
    def enterObjectValue(self, ctx:GraphQLParser.ObjectValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#objectValue.
    def exitObjectValue(self, ctx:GraphQLParser.ObjectValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#objectField.
    def enterObjectField(self, ctx:GraphQLParser.ObjectFieldContext):
        pass

    # Exit a parse tree produced by GraphQLParser#objectField.
    def exitObjectField(self, ctx:GraphQLParser.ObjectFieldContext):
        pass


    # Enter a parse tree produced by GraphQLParser#variable.
    def enterVariable(self, ctx:GraphQLParser.VariableContext):
        pass

    # Exit a parse tree produced by GraphQLParser#variable.
    def exitVariable(self, ctx:GraphQLParser.VariableContext):
        pass


    # Enter a parse tree produced by GraphQLParser#variableDefinitions.
    def enterVariableDefinitions(self, ctx:GraphQLParser.VariableDefinitionsContext):
        pass

    # Exit a parse tree produced by GraphQLParser#variableDefinitions.
    def exitVariableDefinitions(self, ctx:GraphQLParser.VariableDefinitionsContext):
        pass


    # Enter a parse tree produced by GraphQLParser#variableDefinition.
    def enterVariableDefinition(self, ctx:GraphQLParser.VariableDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#variableDefinition.
    def exitVariableDefinition(self, ctx:GraphQLParser.VariableDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#defaultValue.
    def enterDefaultValue(self, ctx:GraphQLParser.DefaultValueContext):
        pass

    # Exit a parse tree produced by GraphQLParser#defaultValue.
    def exitDefaultValue(self, ctx:GraphQLParser.DefaultValueContext):
        pass


    # Enter a parse tree produced by GraphQLParser#type_.
    def enterType_(self, ctx:GraphQLParser.Type_Context):
        pass

    # Exit a parse tree produced by GraphQLParser#type_.
    def exitType_(self, ctx:GraphQLParser.Type_Context):
        pass


    # Enter a parse tree produced by GraphQLParser#namedType.
    def enterNamedType(self, ctx:GraphQLParser.NamedTypeContext):
        pass

    # Exit a parse tree produced by GraphQLParser#namedType.
    def exitNamedType(self, ctx:GraphQLParser.NamedTypeContext):
        pass


    # Enter a parse tree produced by GraphQLParser#listType.
    def enterListType(self, ctx:GraphQLParser.ListTypeContext):
        pass

    # Exit a parse tree produced by GraphQLParser#listType.
    def exitListType(self, ctx:GraphQLParser.ListTypeContext):
        pass


    # Enter a parse tree produced by GraphQLParser#directives.
    def enterDirectives(self, ctx:GraphQLParser.DirectivesContext):
        pass

    # Exit a parse tree produced by GraphQLParser#directives.
    def exitDirectives(self, ctx:GraphQLParser.DirectivesContext):
        pass


    # Enter a parse tree produced by GraphQLParser#directive.
    def enterDirective(self, ctx:GraphQLParser.DirectiveContext):
        pass

    # Exit a parse tree produced by GraphQLParser#directive.
    def exitDirective(self, ctx:GraphQLParser.DirectiveContext):
        pass


    # Enter a parse tree produced by GraphQLParser#typeSystemDefinition.
    def enterTypeSystemDefinition(self, ctx:GraphQLParser.TypeSystemDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#typeSystemDefinition.
    def exitTypeSystemDefinition(self, ctx:GraphQLParser.TypeSystemDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#typeSystemExtension.
    def enterTypeSystemExtension(self, ctx:GraphQLParser.TypeSystemExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#typeSystemExtension.
    def exitTypeSystemExtension(self, ctx:GraphQLParser.TypeSystemExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#schemaDefinition.
    def enterSchemaDefinition(self, ctx:GraphQLParser.SchemaDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#schemaDefinition.
    def exitSchemaDefinition(self, ctx:GraphQLParser.SchemaDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#rootOperationTypeDefinition.
    def enterRootOperationTypeDefinition(self, ctx:GraphQLParser.RootOperationTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#rootOperationTypeDefinition.
    def exitRootOperationTypeDefinition(self, ctx:GraphQLParser.RootOperationTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#schemaExtension.
    def enterSchemaExtension(self, ctx:GraphQLParser.SchemaExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#schemaExtension.
    def exitSchemaExtension(self, ctx:GraphQLParser.SchemaExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#operationTypeDefinition.
    def enterOperationTypeDefinition(self, ctx:GraphQLParser.OperationTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#operationTypeDefinition.
    def exitOperationTypeDefinition(self, ctx:GraphQLParser.OperationTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#description.
    def enterDescription(self, ctx:GraphQLParser.DescriptionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#description.
    def exitDescription(self, ctx:GraphQLParser.DescriptionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#typeDefinition.
    def enterTypeDefinition(self, ctx:GraphQLParser.TypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#typeDefinition.
    def exitTypeDefinition(self, ctx:GraphQLParser.TypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#typeExtension.
    def enterTypeExtension(self, ctx:GraphQLParser.TypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#typeExtension.
    def exitTypeExtension(self, ctx:GraphQLParser.TypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#scalarTypeDefinition.
    def enterScalarTypeDefinition(self, ctx:GraphQLParser.ScalarTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#scalarTypeDefinition.
    def exitScalarTypeDefinition(self, ctx:GraphQLParser.ScalarTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#scalarTypeExtension.
    def enterScalarTypeExtension(self, ctx:GraphQLParser.ScalarTypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#scalarTypeExtension.
    def exitScalarTypeExtension(self, ctx:GraphQLParser.ScalarTypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#objectTypeDefinition.
    def enterObjectTypeDefinition(self, ctx:GraphQLParser.ObjectTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#objectTypeDefinition.
    def exitObjectTypeDefinition(self, ctx:GraphQLParser.ObjectTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#implementsInterfaces.
    def enterImplementsInterfaces(self, ctx:GraphQLParser.ImplementsInterfacesContext):
        pass

    # Exit a parse tree produced by GraphQLParser#implementsInterfaces.
    def exitImplementsInterfaces(self, ctx:GraphQLParser.ImplementsInterfacesContext):
        pass


    # Enter a parse tree produced by GraphQLParser#fieldsDefinition.
    def enterFieldsDefinition(self, ctx:GraphQLParser.FieldsDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#fieldsDefinition.
    def exitFieldsDefinition(self, ctx:GraphQLParser.FieldsDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#fieldDefinition.
    def enterFieldDefinition(self, ctx:GraphQLParser.FieldDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#fieldDefinition.
    def exitFieldDefinition(self, ctx:GraphQLParser.FieldDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#argumentsDefinition.
    def enterArgumentsDefinition(self, ctx:GraphQLParser.ArgumentsDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#argumentsDefinition.
    def exitArgumentsDefinition(self, ctx:GraphQLParser.ArgumentsDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#inputValueDefinition.
    def enterInputValueDefinition(self, ctx:GraphQLParser.InputValueDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#inputValueDefinition.
    def exitInputValueDefinition(self, ctx:GraphQLParser.InputValueDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#objectTypeExtension.
    def enterObjectTypeExtension(self, ctx:GraphQLParser.ObjectTypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#objectTypeExtension.
    def exitObjectTypeExtension(self, ctx:GraphQLParser.ObjectTypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#interfaceTypeDefinition.
    def enterInterfaceTypeDefinition(self, ctx:GraphQLParser.InterfaceTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#interfaceTypeDefinition.
    def exitInterfaceTypeDefinition(self, ctx:GraphQLParser.InterfaceTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#interfaceTypeExtension.
    def enterInterfaceTypeExtension(self, ctx:GraphQLParser.InterfaceTypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#interfaceTypeExtension.
    def exitInterfaceTypeExtension(self, ctx:GraphQLParser.InterfaceTypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#unionTypeDefinition.
    def enterUnionTypeDefinition(self, ctx:GraphQLParser.UnionTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#unionTypeDefinition.
    def exitUnionTypeDefinition(self, ctx:GraphQLParser.UnionTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#unionMemberTypes.
    def enterUnionMemberTypes(self, ctx:GraphQLParser.UnionMemberTypesContext):
        pass

    # Exit a parse tree produced by GraphQLParser#unionMemberTypes.
    def exitUnionMemberTypes(self, ctx:GraphQLParser.UnionMemberTypesContext):
        pass


    # Enter a parse tree produced by GraphQLParser#unionTypeExtension.
    def enterUnionTypeExtension(self, ctx:GraphQLParser.UnionTypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#unionTypeExtension.
    def exitUnionTypeExtension(self, ctx:GraphQLParser.UnionTypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#enumTypeDefinition.
    def enterEnumTypeDefinition(self, ctx:GraphQLParser.EnumTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#enumTypeDefinition.
    def exitEnumTypeDefinition(self, ctx:GraphQLParser.EnumTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#enumValuesDefinition.
    def enterEnumValuesDefinition(self, ctx:GraphQLParser.EnumValuesDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#enumValuesDefinition.
    def exitEnumValuesDefinition(self, ctx:GraphQLParser.EnumValuesDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#enumValueDefinition.
    def enterEnumValueDefinition(self, ctx:GraphQLParser.EnumValueDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#enumValueDefinition.
    def exitEnumValueDefinition(self, ctx:GraphQLParser.EnumValueDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#enumTypeExtension.
    def enterEnumTypeExtension(self, ctx:GraphQLParser.EnumTypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#enumTypeExtension.
    def exitEnumTypeExtension(self, ctx:GraphQLParser.EnumTypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#inputObjectTypeDefinition.
    def enterInputObjectTypeDefinition(self, ctx:GraphQLParser.InputObjectTypeDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#inputObjectTypeDefinition.
    def exitInputObjectTypeDefinition(self, ctx:GraphQLParser.InputObjectTypeDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#inputFieldsDefinition.
    def enterInputFieldsDefinition(self, ctx:GraphQLParser.InputFieldsDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#inputFieldsDefinition.
    def exitInputFieldsDefinition(self, ctx:GraphQLParser.InputFieldsDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#inputObjectTypeExtension.
    def enterInputObjectTypeExtension(self, ctx:GraphQLParser.InputObjectTypeExtensionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#inputObjectTypeExtension.
    def exitInputObjectTypeExtension(self, ctx:GraphQLParser.InputObjectTypeExtensionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#directiveDefinition.
    def enterDirectiveDefinition(self, ctx:GraphQLParser.DirectiveDefinitionContext):
        pass

    # Exit a parse tree produced by GraphQLParser#directiveDefinition.
    def exitDirectiveDefinition(self, ctx:GraphQLParser.DirectiveDefinitionContext):
        pass


    # Enter a parse tree produced by GraphQLParser#directiveLocations.
    def enterDirectiveLocations(self, ctx:GraphQLParser.DirectiveLocationsContext):
        pass

    # Exit a parse tree produced by GraphQLParser#directiveLocations.
    def exitDirectiveLocations(self, ctx:GraphQLParser.DirectiveLocationsContext):
        pass


    # Enter a parse tree produced by GraphQLParser#directiveLocation.
    def enterDirectiveLocation(self, ctx:GraphQLParser.DirectiveLocationContext):
        pass

    # Exit a parse tree produced by GraphQLParser#directiveLocation.
    def exitDirectiveLocation(self, ctx:GraphQLParser.DirectiveLocationContext):
        pass


    # Enter a parse tree produced by GraphQLParser#executableDirectiveLocation.
    def enterExecutableDirectiveLocation(self, ctx:GraphQLParser.ExecutableDirectiveLocationContext):
        pass

    # Exit a parse tree produced by GraphQLParser#executableDirectiveLocation.
    def exitExecutableDirectiveLocation(self, ctx:GraphQLParser.ExecutableDirectiveLocationContext):
        pass


    # Enter a parse tree produced by GraphQLParser#typeSystemDirectiveLocation.
    def enterTypeSystemDirectiveLocation(self, ctx:GraphQLParser.TypeSystemDirectiveLocationContext):
        pass

    # Exit a parse tree produced by GraphQLParser#typeSystemDirectiveLocation.
    def exitTypeSystemDirectiveLocation(self, ctx:GraphQLParser.TypeSystemDirectiveLocationContext):
        pass


    # Enter a parse tree produced by GraphQLParser#name.
    def enterName(self, ctx:GraphQLParser.NameContext):
        pass

    # Exit a parse tree produced by GraphQLParser#name.
    def exitName(self, ctx:GraphQLParser.NameContext):
        pass



del GraphQLParser