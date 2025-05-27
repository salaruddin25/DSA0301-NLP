import re

# Define token types
TOKEN_SPEC = [
    ('QUANTIFIER', r'∀|∃'),
    ('IDENTIFIER', r'[A-Z][a-zA-Z_]*'),
    ('VARIABLE', r'[a-z][a-zA-Z_]*'),
    ('LPAREN', r'\('),
    ('RPAREN', r'\)'),
    ('COMMA', r','),
    ('AND', r'∧'),
    ('OR', r'∨'),
    ('IMPLIES', r'→'),
    ('NOT', r'¬'),
    ('WS', r'\s+'),
]

TOKEN_REGEX = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in TOKEN_SPEC)

# Tokenizer
def tokenize(expression):
    for match in re.finditer(TOKEN_REGEX, expression):
        kind = match.lastgroup
        value = match.group()
        if kind != 'WS':
            yield (kind, value)

# Basic parser (very simplified and rule-based)
def parse(tokens):
    tokens = list(tokens)
    pos = 0

    def peek():
        return tokens[pos] if pos < len(tokens) else (None, None)

    def consume(expected=None):
        nonlocal pos
        tok = tokens[pos] if pos < len(tokens) else (None, None)
        if expected and tok[0] != expected:
            raise SyntaxError(f"Expected {expected} but got {tok}")
        pos += 1
        return tok

    def parse_expression():
        tok_type, tok_val = peek()
        if tok_type == 'QUANTIFIER':
            return parse_quantified()
        elif tok_type == 'IDENTIFIER':
            return parse_predicate()
        else:
            raise SyntaxError(f"Unexpected token {tok_type}")

    def parse_quantified():
        quant = consume('QUANTIFIER')[1]
        var = consume('VARIABLE')[1]
        expr = parse_expression()
        return {'type': 'quantifier', 'quantifier': quant, 'variable': var, 'expression': expr}

    def parse_predicate():
        name = consume('IDENTIFIER')[1]
        args = []
        if peek()[0] == 'LPAREN':
            consume('LPAREN')
            while True:
                tok_type, tok_val = peek()
                if tok_type == 'VARIABLE' or tok_type == 'IDENTIFIER':
                    args.append(consume()[1])
                    if peek()[0] == 'COMMA':
                        consume('COMMA')
                    elif peek()[0] == 'RPAREN':
                        break
                else:
                    raise SyntaxError("Expected argument")
            consume('RPAREN')
        return {'type': 'predicate', 'name': name, 'args': args}

    return parse_expression()

# Main
if __name__ == "__main__":
    print("Enter a basic FOPC expression (e.g., ∀x Loves(John,x)):")
    expr = input("> ")
    try:
        tokens = tokenize(expr)
        tree = parse(tokens)
        print("\nParsed Structure:")
        print(tree)
    except SyntaxError as e:
        print("Syntax Error:", e)
