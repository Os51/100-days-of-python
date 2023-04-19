# Notes about Syntax

## Functions
- Defining a "test" function.
    - Functions can be defined using "def (name of function)"
- Anything indented after the definition is considered to be part of the function

```python
def test():
    print("test")
    print("test2")
```

- Anything not indented is *not* part of the function:

```python
def test():
    print("test")
    print("test2")

string = "string"
number = 10
```

- Functions must be called to be processed by the interpreter
```python
test()
```

## Variables
- Variables can be assigned string, int, float or bool data types
- Mathematical operations can also be assigned to variables.
```python
x = 1 + 2 + 3
print(x)
```
- The result of the operation is what is printed to the console

## Indentation
- Python works on indentation.
- If code is improperly or unexpectedly indented, you will receive a "Indentation Error"

```python
    print('hello world')
  
  File "<stdin>", line 1
    print('hello world')
IndentationError: unexpected indent
```

- Generally the indentation is at the beginning of the line. If you were to indent in the middle of a operation, this is technically valid, but may not be standard practice and could make your code more confusing to read
- Though the below is non-standard styling, it is valid syntax:
```python
y = 1    +   1
print(      y   )
```

## Help Pages
- Documentation: https://docs.python.org
- Python also has a built in help page available in the interpreter

```python
help <function>
```

- You can also use dir(function_name) to print out a list of attirbutes or defined symbols for the function
```python
dir(print)
```

- Most scripts should follow recommendations listed in the PEP Style Guide, but it is not mandatory: https://peps.python.org/pep-0008/
