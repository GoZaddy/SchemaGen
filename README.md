# SchemaGen
Schema Gen is a simple CLI tool that generates Python GraphQL implementations(using Graphene) from a Graphql Schema file.

# Installation
```shell
pip install schemagen
```

# Usage
As a CLI tool:
```shell
schemagen parse test.graphql -o test.py
```
As a Python Package:
```python
from schema_gen import SDLParser

sdl_parser = SDLParser(
    input_file='test.graphql',
    output_file='test.py'
)

# parse input file
sdl_parser()
```

# Notes
SchemaGen is currently in its first version so there are some things you need to know:
* GraphQL type declarations in your schema file **must be ordered**. 
  
  Because of the way Python and SchemaGen works, you cannot use a GraphQL type
  before declaring it. For example, the following graphql schema definition would be invalid because we are using the **Url** scalar in our **User** type before declaring it:
  ```graphql
    type User {
        id: ID!
        username: String
        avatar_url: Url
    }
  
    scalar Url    
  ```
  The correct version of the above code is:
    ```graphql
    scalar Url 
     
    type User {
        id: ID!
        username: String
        avatar_url: Url
    }
  ```

* Using a GraphQL SDL keyword as an object field name in your schema will throw an error.

  For example, doing this:
  ```graphql
  enum UserType {
    Example
  }
  
  type User{
    name: String
    type: UserType
  }
  ```
  will throw an error.
  
  Do this instead:
  ```graphql
  enum UserType {
    Example
  }
  
  type User{
    name: String
    user_type: UserType
  }
  ```
  
We plan to fix these issues in the future. Pull requests are welcome!
  


