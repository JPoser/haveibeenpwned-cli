import click, api_interface

api = api_interface.api_interface()

@click.command()
@click.option('--json', is_flag=True, help='output as json')
@click.argument('email')
def search(json, email):
    if json == True:
        click.echo(api.check_pwned('{}'.format(email)))
    else:
        click.echo(api.list_pwned(api.check_pwned('{}'.format(email))))

if __name__ == '__main__':
    search()
