import click
import json
from pathlib import Path


@click.command()
@click.option(
    "--path", prompt="Input file path", help="The person to greet.", type=Path
)
def transform(path: Path):
    """Transforms zone intput to zone output"""
    print(path.name)

    with open(path, "r") as file:
        file_input = json.loads(file.read())

    print(file_input)


if __name__ == "__main__":
    transform()
