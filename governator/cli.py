import click

@click.group()
def cli():
    """Governator: Manage your data access policies as code."""
    pass

@click.command()
def sync():
    """Synchronize your data access policies across systems."""
    click.echo("Synchronizing data access policies...")

@click.command()
def check():
    """Check the current state of data access policies."""
    click.echo("Checking data access policies...")

cli.add_command(sync)
cli.add_command(check)

if __name__ == '__main__':
    cli()
