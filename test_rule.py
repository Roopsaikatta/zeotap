# tests/test_rules.py

import unittest
from ast_engine import create_rule, combine_rules, evaluate_rule

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule = "age > 30 AND department == 'Sales'"
        ast = create_rule(rule)
        self.assertIsNotNone(ast)  # Ensure AST is created

    def test_combine_rules(self):
        rule1 = "age > 30 AND department == 'Sales'"
        rule2 = "salary > 50000 OR experience > 5"
        combined_ast = combine_rules([rule1, rule2])
        self.assertIsNotNone(combined_ast)

    def test_evaluate_rule(self):
        data = {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}
        rule = "age > 30 AND department == 'Sales'"
        ast = create_rule(rule)
        result = evaluate_rule(ast, data)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
