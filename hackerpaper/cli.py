from request import Request
import requests
import click


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
    req = Request(id, type)
    res = req.fetch_data()
    try:
        add_to_instapaper(account, res)
    except Exception as err:
        print("Error: {}".format(err))


def add_to_instapaper(account, res):
    username, password = account[0], account[1]
    click.echo("[~] Adding URLs to Instapaper")
    if isinstance(res, list):
        urls = [i["url"] for i in res]
        for i in urls:
            post(username, password, i)
    else:
        post(username, password, res["url"])
        pass


def post(username, password, url):
    try:
        requests.post(
            "https://www.instapaper.com/api/add?username={}&password={}&url={}".format(
                username, password, url
            )
        )
    except Exception as err:
        print("Error: {}".format(err))


if __name__ == "__main__":
    cli()
