import re
import pandas as pd

# Define a set of regular expressions for tokenizing
TOKENS = {
    # Numbers
    'FLOAT': r'\d+\.\d+',  # Floating-point number pattern
    'NUMBER': r'\d+',  # Integer pattern
    
    # Operators (Order matters: prioritize compound operators first)
    'LESSEQUAL': r'<=',  # Must be checked before '<'
    'GREATEREQUAL': r'>=',  # Must be checked before '>'
    'NOTEQUAL': r'!=',  # Must be checked before '='
    'EQUAL': r'==',  # Must be checked before '='
    'LESSTHAN': r'<',
    'GREATERTHAN': r'>',
    'ASSIGN': r'=',
    'PLUS': r'\+',
    'MINUS': r'-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    
    # Delimiters
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'LBRACE': r'\{',
    'RBRACE': r'\}',
    'SEMICOLON': r';',
    
    # Keywords
    'IF': r'\bif\b',
    'ELSE': r'\belse\b',
    'WHILE': r'\bwhile\b',
    'RETURN': r'\breturn\b',
    
    # Identifiers
    'ID': r'\b[a-zA-Z_]\w*\b',  # Identifier pattern
}

# Tokenizer function with comment handling and correct order of operators
def tokenize(code):
    tokens = []
    
    while code:
        code = code.lstrip()  # Skip any leading whitespace
        if not code:  # If code is empty after stripping whitespace, break the loop
            break

        # Ignore single-line comments starting with '#'
        if code.startswith('#'):
            code = code.split('\n', 1)[-1]
            continue

        match = None
        for token_type, pattern in TOKENS.items():
            regex = re.compile(pattern)
            match = regex.match(code)
            if match:
                token_value = match.group(0)
                tokens.append((token_type, token_value))
                code = code[len(token_value):]
                break

        if not match:
            raise SyntaxError(f'Unexpected character: {code[0]}')
    
    return tokens


# DFA simulation function
def simulate_dfa(tokens):
    # Define the table headers
    headers = ['Expresión Regular', 'Componente Léxico', 'Valor del Atributo']
    
    # Create rows based on tokens
    rows = []
    for token_type, token_value in tokens:
        # Based on the token type, classify the component lexically and provide attributes
        if token_type in ['IF', 'THEN', 'ELSE', 'WHILE', 'RETURN']:
            rows.append([token_value, token_type.lower(), '-'])
        elif token_type == 'ID':
            rows.append([token_value, 'id', 'apuntador a la entrada en la tabla'])
        elif token_type == 'NUMBER':
            rows.append([token_value, 'num', 'apuntador a la entrada en la tabla'])
        elif token_type == 'FLOAT':
            rows.append([token_value, 'float', 'apuntador a la entrada en la tabla'])
        elif token_type in ['PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'EQUAL', 'ASSIGN', 'NOTEQUAL', 'LESSTHAN', 'LESSEQUAL', 'GREATERTHAN', 'GREATEREQUAL']:
            rows.append([token_value, 'oprel', token_type])
        elif token_type in ['LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMICOLON']:
            rows.append([token_value, 'delimiter', token_type])

    # Create a DataFrame to simulate the table
    df = pd.DataFrame(rows, columns=headers)
    
    # Print the DataFrame or save it to a file
    print(df)  # This will display the table in the console
    
    # Optionally, save the DataFrame to a CSV file
    df.to_csv('lexical_components_table.csv', index=False)

# Read the input code from a file
def read_code_from_file(filename):
    with open(filename, 'r') as file:
        code = file.read()
        print(f"Code read from file:\n{code}")  # Debugging: Print the content of the file
        return code

# Example usage:
input_file = 'input_code.txt'  # Replace with your file path
code = read_code_from_file(input_file)
tokens = tokenize(code)
simulate_dfa(tokens)
