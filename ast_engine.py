# ast_engine.py

class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value  # Optional: For operand nodes (e.g., >, <, ==)
        self.left = left  # Left child (another Node)
        self.right = right  # Right child (for operators)

def create_rule(rule_string):
    # Implement logic to parse string and build AST
    pass

def combine_rules(rules):
    combined_root = Node('operator', 'AND')
    for rule in rules:
        rule_ast = create_rule(rule)
        if combined_root.left is None:
            combined_root.left = rule_ast
        else:
            combined_root.right = rule_ast
    return combined_root

def evaluate_rule(ast, data):
    if ast.type == 'operand':
        return eval(ast.value.format(**data))
    elif ast.type == 'operator':
        left_eval = evaluate_rule(ast.left, data)
        right_eval = evaluate_rule(ast.right, data)
        if ast.value == 'AND':
            return left_eval and right_eval
        elif ast.value == 'OR':
            return left_eval or right_eval
