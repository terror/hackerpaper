import requests
import click
from .request import Request


@click.command()
@click.option(
    "--account",
    nargs=2,
    default=[None] * 2,
    type=click.Tuple([str, str]),
)
@click.option("--id", default="", prompt="HackerNews Article ID")
@click.option(
    "--type",
    type=click.Choice(
        [
            "item",
            "askstories",
            "newstories",
            "jobstories",
            "beststories",
            "showstories",
        ],
        case_sensitive=False,
    ),
    prompt="Type of HackerNews Articles",
)
def cli(account, id, type):
    if None in account or not authenticate(account):
        click.secho("Invalid credentials!", fg="red")
        exit()
    click.echo("[~] Fetching Data...")

    res = Request(id, type).fetch_data()
    add_to_instapaper(account, res)
    click.secho("Process complete!", fg="green")


def authenticate(account):
    username, password = account[0], account[1]
    res = requests.get(
        "https://www.instapaper.com/api/authenticate?username={}&password={}".format(
            username, password
        )
    )
    if res.status_code == 200:
        return True
    return False


def add_to_instapaper(account, res):
    username, password = account[0], account[1]
    click.echo("[~] Adding URLs to Instapaper...")
    if isinstance(res, list):
        urls = []
        for i in res:
            if "url" in i:
                urls.append(i["url"])
        for i in urls:
            post(username, password, i)
    else:
        if "url" in res:
            post(username, password, res["url"])


def post(username, password, url):
    requests.post(
        "https://www.instapaper.com/api/add?username={}&password={}&url={}".format(
            username, password, url
        )
    )


if __name__ == "__main__":
    cli()
