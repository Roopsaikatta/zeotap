# api.py

from flask import Flask, request, jsonify
from ast_engine import create_rule, combine_rules, evaluate_rule

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_route():
    rule_string = request.json['rule']
    ast = create_rule(rule_string)
    return jsonify({"ast": str(ast)})  # Convert AST to string for simplicity

@app.route('/combine_rules', methods=['POST'])
def combine_rules_route():
    rules = request.json['rules']
    combined_ast = combine_rules(rules)
    return jsonify({"combined_ast": str(combined_ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_route():
    ast = request.json['ast']
    data = request.json['data']
    result = evaluate_rule(ast, data)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
