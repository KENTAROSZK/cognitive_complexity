import os
import ast

class CognitiveComplexityCalculator(ast.NodeVisitor):
    def __init__(self):
        self.complexity = 0
        self.depth = 0
    
    def visit_If(self, node):
        self._increase_complexity()
        self.generic_visit(node)
    
    def visit_For(self, node):
        self._increase_complexity()
        self.generic_visit(node)
    
    def visit_While(self, node):
        self._increase_complexity()
        self.generic_visit(node)
    
    def visit_Try(self, node):
        self._increase_complexity()
        self.generic_visit(node)
    
    def visit_FunctionDef(self, node):
        # Reset depth when entering a new function
        previous_depth = self.depth
        self.depth = 0
        self.generic_visit(node)
        self.depth = previous_depth
    
    def visit_And(self, node):
        self._increase_complexity()
        self.generic_visit(node)
    
    def visit_Or(self, node):
        self._increase_complexity()
        self.generic_visit(node)
    
    def _increase_complexity(self):
        # Every time a new control structure is encountered, we add complexity
        self.complexity += 1
        if self.depth > 0:
            self.complexity += self.depth
        self.depth += 1

    def calculate(self, code):
        tree = ast.parse(code)
        self.visit(tree)
        return self.complexity


if __name__ == "__main__":
    
    file_path = "./target_func.py"

    # ファイルが存在するとき
    # そのファイルの複雑度を判定させたいので
    # .pyスクリプトを文字列として読み込む
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            code = file.read()
    else:
        code = '''
def example_function(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                while i < 10:
                    print(i)
                    i += 1
    else:
        try:
            x = int(x)
        except ValueError:
            print("Invalid input")
    return x
        '''
    
    calculator = CognitiveComplexityCalculator()
    complexity = calculator.calculate(code)
    print(f"Cognitive Complexity: {complexity}")