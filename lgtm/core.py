import click

@click.command()
@click.option('--message', '-m', default='LGTM',
            show_default=True, help='string-on-picture')
@click.argument('keyword')
def cli(keyword, message):
    """ comment """
    lgtm(keyword, message)
    click.echo('lgtm')

def lgtm(keyword, message):
    pass

