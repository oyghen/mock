import typer
from mocklib.core import hello

app = typer.Typer(add_completion=False)


@app.command()
def run():
    """Run CLI."""
    print("Executing mockcli's run")
    mocklib_greeting = hello()
    print(mocklib_greeting)


def main() -> None:
    app()
