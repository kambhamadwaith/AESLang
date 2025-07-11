import argparse
from aeslang.interpreter import aeslang_to_python, python_to_aeslang

def main():
    parser = argparse.ArgumentParser(description="AESLang Interpreter")
    parser.add_argument('--from-aes', help="Run AESLang code from a .aes file")
    parser.add_argument('--to-aes', help="Convert Python code to AESLang")

    args = parser.parse_args()

    if args.from_aes:
        with open(args.from_aes, 'r') as f:
            aes_code = f.read()
        py_code = aeslang_to_python(aes_code)
        print("=== Python Code ===")
        print(py_code)
        exec(py_code, {}, {})

    elif args.to_aes:
        with open(args.to_aes, 'r') as f:
            py_code = f.read()
        aes_code = python_to_aeslang(py_code)
        print("=== AESLang Code ===")
        print(aes_code)

if __name__ == "__main__":
    main()
