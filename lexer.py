import math


class Lexer:
    def __init__(self, expression):
        self.expression = expression
        self.tokens = self.tokenize()

    def tokenize(self):
        if self.expression.count("(") != self.expression.count(")"):
            return None

        operators = {
            "(": "LPAR",
            ")": "RPAR",
            "^": "EXP",
            "*": "MUL",
            "/": "DIV",
            "+": "ADD",
            "-": "SUB",
            "sin": "SIN",
            "cos": "COS",
            "tan": "TAN",
        }
        tokens = []
        i = 0
        length = len(self.expression)
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]
        prev = "#"
        while i < length:
            curr = self.expression[i]
            trig = ""
            if i < length - 2:
                trig = self.expression[i : i + 3].lower()
            pi = ""
            if i < length - 1:
                pi = self.expression[i : i + 2].lower()
            if curr in operators:
                if (prev in operators or i == 0) and curr == "-":
                    tokens.append(("NEG", curr))
                else:
                    tokens.append((operators[curr], curr))
            elif trig in operators:
                tokens.append((operators[trig], trig))
                i += 2
            elif pi == "pi":
                tokens.append(("NUM", math.pi))
                i += 1
            elif curr in digits:
                while i + 1 < length and self.expression[i + 1] in digits:
                    i += 1
                    curr += self.expression[i]
                tokens.append(("NUM", curr))
            i += 1
            prev = curr
        return tokens
