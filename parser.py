from node import Node


class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.length = len(tokens)
        self.index = 0
        self.ast = self.parse()

    def parse(self):
        return self.add_sub()

    def add_sub(self):
        node = self.mul_div()

        while self.index < self.length and self.tokens[self.index][0] in [
            'ADD', 'SUB'
        ]:
            if self.tokens[self.index][0] == 'ADD':
                self.index += 1
                node = Node('ADD', left=node, right=self.mul_div())
            elif self.tokens[self.index][0] == 'SUB':
                self.index += 1
                node = Node('SUB', left=node, right=self.mul_div())

        return node

    def mul_div(self):
        node = self.exp()

        while self.index < self.length and self.tokens[self.index][0] in [
            'MUL', 'DIV'
        ]:
            if self.tokens[self.index][0] == 'MUL':
                self.index += 1
                node = Node('MUL', left=node, right=self.exp())
            elif self.tokens[self.index][0] == 'DIV':
                self.index += 1
                node = Node('DIV', left=node, right=self.exp())

        return node

    def exp(self):
        node = self.factor()

        while self.index < self.length and self.tokens[self.index][0] == 'EXP':
            self.index += 1
            node = Node('EXP', left=node, right=self.factor())

        return node

    def factor(self):

        token_type, token_value = self.tokens[self.index]
        if token_type == 'NEG':
            self.index += 1
            return Node(token_type, down=self.factor())
        elif token_type in ['SIN', 'COS', 'TAN']:
            self.index += 1
            return Node(token_type, down=self.factor())
        elif token_type == 'LPAR':
            self.index += 1
            node = self.parse()
            if self.index < self.length and self.tokens[self.index][0] == 'RPAR':
                self.index += 1
                return node
        elif token_type == 'NUM':
            self.index += 1
            return Node(token_type, value=float(token_value))
