import argparse
from aeslang.interpreter import aeslang_to_python

def main():
    parser = argparse.ArgumentParser(description="AESLang CLI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--from-aes', help="Run AESLang file")
    group.add_argument('--to-aes', help="Convert Python file to AESLang")
    args = parser.parse_args()

    if args.from_aes:
        with open(args.from_aes) as f:
            aes_code = f.read()
        py_code = aeslang_to_python(aes_code)
        print("=== Python Code ===\n", py_code)
        exec(py_code, {}, {})
    elif args.to_aes:
        with open(args.to_aes) as f:
            py_code = f.read()
        print("=== AESLang (reverse conversion not implemented) ===")
        print(py_code)

if __name__ == '__main__':
    main()