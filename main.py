from flask import Flask, render_template, request
from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/evaluate", methods=["POST"])
def evaluate():
    expression = request.form["expression"]

    try:
        lexer = Lexer(expression)
        tokens = lexer.tokens

        parser = Parser(tokens)
        ast = parser.ast

        evaluator = Evaluator(ast)
        ans = evaluator.ans
        traversal = evaluator.traversal

        graph = ast.to_graphviz()
        graph_svg = graph.pipe(format="svg").decode("utf-8")

        return render_template(
            "result.html",
            expression=expression,
            result=ans,
            traversal=traversal,
            graph_svg=graph_svg,
        )
    except Exception as e:
        error_message = f"Error: {e}"
        return render_template("index.html", error=error_message)


if __name__ == "__main__":
    app.run()
