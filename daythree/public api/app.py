import click
import requests


@click.command()
def cli():
    draw_header()
    greeting()

    news_request = requests.get(
        "https://newsapi.org/v1/articles?source=the-next-web&sortBy=latest&apiKey=8ddc75bfec6b470a85fb69bccce7afbb")
    main_dict = news_request.json()
    article_list = main_dict['articles']

    for article in article_list:
        click.echo(click.style('Title: ' + article['title'], fg='green'))
        click.echo(click.style('By: ' + article['author'], fg='blue'))
        click.echo('\n')
        click.echo(click.wrap_text(article['description'], 100))
        click.echo('\n')
        click.echo('-' * 100)

def draw_header():
    click.echo('\n')
    click.echo(click.style('*' * 100, fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
	click.echo(click.style('*' + ' ' * 32 + "Welcome to Michael's news app" + ' ' * 32 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' + ' ' * 98 + '*', fg='red'))
    click.echo(click.style('*' * 100, fg='red'))
    click.echo('\n')


def greeting():
    print("This application keeps you informed with the latest news.")
   
    print('Powered by newsapi.org By Michael')
    print('-' * 100)

