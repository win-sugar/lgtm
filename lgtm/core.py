import click

@click.command()
def cli():
    """ comment """
    lgtm()
    click.echo('lgtm')

def lgtm():
    pass

