import os
import ast

def find_print_statements(base_dir='.'):
    for root, _, files in os.walk(base_dir):
        for f in files:
            if f.endswith('.py'):
                path = os.path.join(root, f)
                with open(path, encoding='utf-8') as file:
                    try:
                        tree = ast.parse(file.read(), filename=path)
                    except SyntaxError:
                        continue
                for node in ast.walk(tree):
                    if isinstance(node, ast.Call) and getattr(node.func, 'id', '') == 'print':
                        print(f"🔍 Print statement found in {path}:{node.lineno}")

if __name__ == "__main__":
    find_print_statements()
