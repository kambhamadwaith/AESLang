AES_SYNTAX = {
    "AES": "print",
    "AESINPUT": "input",
    "AES AES": "=",
    "AES AES AES": ";",
    "AESNUM1": "1",
    "AESNUM5": "5",
    "AESNUM10": "10",
    "AESSTR": '"HELLO"',
    "AESAESAES": "def",
    "AES_AES": "if",
    "AES__AES": "else",
    "AES___AES": "while",
    "AES____AES": "for",
    "AES&&AES": "and",
    "AES||AES": "or",
    "!AES": "not",
    "AES+AES": "+",
    "AES-AES": "-",
    "AES*AES": "*",
    "AES/AES": "/",
    "AES%AES": "%",
    "AES**AES": "**",
    "AES+=AES": "+=",
    "AES-=AES": "-=",
    "AES*=AES": "*=",
    "AES/=AES": "/=",
    "AES%=AES": "%=",
    "AES**=AES": "**="
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
        py_lines.append(" ".join(token_buffer).replace(';', ''))
    return "\n".join(py_lines)

def python_to_aeslang(py_code):
    reverse_map = {v: k for k, v in AES_SYNTAX.items()}
    tokens = py_code.replace('(', ' ( ').replace(')', ' ) ').split()
    aes_tokens = [reverse_map.get(tok, tok) for tok in tokens]
    return " ".join(aes_tokens)
