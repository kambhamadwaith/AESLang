# AESLang Interpreter: Pure AES version (no lowercase)

AES_SYNTAX = {
    # Keywords & Functions
    "AES": "print",
    "AESINPUT": "input",
    "AES AES": "=",
    "AES AES AES": ";",

    # Constants
    "AESNUM1": "1",
    "AESNUM5": "5",
    "AESNUM10": "10",
    "AESSTR": '"HELLO"',

    # Function defs & return
    "AESAESAES": "def",
    "AESAESAES": "return",
    "AESYIELD": "yield",
    "AESLAMBDA": "lambda",

    # Control Flow
    "AES_AES": "if",
    "AES__AES": "else",
    "AES___AES": "while",
    "AES____AES": "for",
    "AESMATCH": "match",
    "AESCASE": "case",

    # Boolean Logic
    "AES&&AES": "and",
    "AES||AES": "or",
    "!AES": "not",

    # Arithmetic Operators
    "AES+AES": "+",
    "AES-AES": "-",
    "AES*AES": "*",
    "AES/AES": "/",
    "AES%AES": "%",
    "AES**AES": "**",

    # Compound Assignment
    "AES+=AES": "+=",
    "AES-=AES": "-=",
    "AES*=AES": "*=",
    "AES/=AES": "/=",
    "AES%=AES": "%=",
    "AES**=AES": "**=",

    # Object-Oriented Programming
    "AESCLASS": "class",
    "AESSELF": "self",
    "AESINIT": "__init__",
    "AESENTER": "__enter__",
    "AESEXIT": "__exit__",

    # File Handling
    "AESOPEN": "open",
    "AESREAD": "read",
    "AESWRITE": "write",
    "AESCLOSE": "close",

    # Exception Handling
    "AESTRY": "try",
    "AESEXCEPT": "except",
    "AESFINALLY": "finally",
    "ASRAISE": "raise",

    # Importing Modules
    "AESIMPORT": "import",
    "AESFROM": "from",
    "AESAS": "as",

    # Comments & Docstrings
    "AESHASH": "#",
    "AESDOC": "\"\"\"",

    # Data Structures
    "AESLIST": "list",
    "AESDICT": "dict",
    "AESSET": "set",
    "AESTUPLE": "tuple",

    # With Statement
    "AESWITH": "with",
    "AEAS": "as",

    # Async / Await
    "AESASYNC": "async",
    "AESAWAIT": "await",

    # Typing and Annotations
    "AESINT": "int",
    "AESSTRANN": "str",
    "AESBOOL": "bool",
    "AESFLOAT": "float",
    "AESLISTT": "List",

    # Debugging / Logging
    "AESLOG": "log",
    "AESDEBUG": "debug",

    # Meta Programming
    "AESEVAL": "eval",
    "AESEXEC": "exec",

    # CLI args
    "AESSYSARGV": "sys.argv",

    # Decorators
    "AESAT": "@"
}

def aeslang_to_python(aes_code):
    lines = aes_code.strip().splitlines()
    py_lines = []
    for line in lines:
        tokens = line.strip().split()
        token_buffer = []
        i = 0
        while i < len(tokens):
            if i + 2 < len(tokens) and f"{tokens[i]} {tokens[i+1]} {tokens[i+2]}" in AES_SYNTAX:
                token_buffer.append(AES_SYNTAX[f"{tokens[i]} {tokens[i+1]} {tokens[i+2]}"])
                i += 3
            elif i + 1 < len(tokens) and f"{tokens[i]} {tokens[i+1]}" in AES_SYNTAX:
                token_buffer.append(AES_SYNTAX[f"{tokens[i]} {tokens[i+1]}"])
                i += 2
            elif tokens[i] in AES_SYNTAX:
                token_buffer.append(AES_SYNTAX[tokens[i]])
                i += 1
            else:
                token_buffer.append(tokens[i])
                i += 1
        py_line = " ".join(token_buffer).replace(';', '')
        py_lines.append(py_line)
    return "\n".join(py_lines)

def python_to_aeslang(py_code):
    reverse_map = {v: k for k, v in AES_SYNTAX.items()}
    symbols = ['(', ')', ':', ',', '=', '+', '-', '*', '/', '%', '==', '!=', '<', '>', '<=', '>=']
    for sym in symbols:
        py_code = py_code.replace(sym, f" {sym} ")
    tokens = py_code.split()
    aes_tokens = [reverse_map.get(tok, tok) for tok in tokens]
    return " ".join(aes_tokens)
