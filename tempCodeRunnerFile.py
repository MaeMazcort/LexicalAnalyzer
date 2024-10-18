import re
import pandas as pd

# Define a set of regular expressions for tokenizing
TOKENS = {
    'NUMBER': r'\d+',
    'PLUS': r'\+',
    'MINUS': r'-',
    'MULTIPLY': r'\*',
    'DIVIDE': r'/',
    'LPAREN': r'\(',
    'RPAREN': r'\)',
    'IF': r'\bif\b',
    'THEN': r'\bthen\b',
    'ELSE': r'\belse\b',
    'ID': r'\b[a-zA-Z_]\w*\b',  # Identifier pattern
    'NUM': r'\d+',  # Number pattern
    'MEN': r'<',
    'MEI': r'<=',
    'IGU': r'=',
    'DIF': r'<>',
    'MAY': r'>',
    'MAI': r'>='
}

# Tokenizer function
def tokenize(code):
    tokens = []
    while code:
        match = None
        # Skip whitespace
        code = code.lstrip()
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
        if token_type in ['IF', 'THEN', 'ELSE']:
            rows.append([token_value, token_type.lower(), '-'])
        elif token_type == 'ID':
            rows.append([token_value, 'id', 'apuntador a la entrada en la tabla'])
        elif token_type == 'NUM':
            rows.append([token_value, 'num', 'apuntador a la entrada en la tabla'])
        elif token_type in ['MEN', 'MEI', 'IGU', 'DIF', 'MAY', 'MAI']:
            rows.append([token_value, 'oprel', token_type])

    # Create a DataFrame to simulate the table
    df = pd.DataFrame(rows, columns=headers)
    
    # Print the DataFrame or save it to a file
    print(df)  # This will display the table in the console
    
    # Optionally, save the DataFrame to a CSV file
    df.to_csv('lexical_components_table.csv', index=False)


# Example usage:
code = "if x <= 10 then y = 5 else z > 10"
tokens = tokenize(code)
simulate_dfa(tokens)
