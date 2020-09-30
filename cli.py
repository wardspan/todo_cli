import click

@click.group()
def main():
    """simple cli to greet me"""
    pass

@main.command()
@click.argument('name')
def greet(name):
    """greet me back with your name"""
    click.echo("Hello, " + name)

if __name__ == "__main__":
    main()