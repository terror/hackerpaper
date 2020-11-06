import requests
import click
from request import Request
from urllib.parse import urlparse


@click.command()
# Options
@click.option(
    "--account",
    "-a",
    nargs=2,
    default=[None] * 2,
    type=click.Tuple([str, str]),
)
@click.option("--id")
@click.option(
    "--type",
    "-t",
)
@click.option(
    "--interests",
    "-i",
    multiple=True,
    default=[],
)
def cli(account, id, type, interests):
    # Authenticate instapaper credentials
    if None in account or not authenticate(account):
        click.secho("Invalid credentials!", fg="red")
        exit()

    print("[~] Fetching Data...")

    res = Request(id, type).fetch_data()
    print(res)
    add_to_instapaper(account, res, interests)
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


def add_to_instapaper(account, res, interests):
    username, password = account[0], account[1]

    if isinstance(res, list):
        posts = []

        for p in res:
            if "url" in p and "title" in p:
                posts.append(p)

        if interests:
            print("[~] Filtering posts...")
            posts = filter_posts(posts, interests)

        for p in posts:
            post(username, password, p["url"])
    else:
        if "url" in res:
            post(username, password, res["url"])


def post(username, password, url):
    print("[~] Adding URL: {} to Instapaper...\n".format(url))

    requests.post(
        "https://www.instapaper.com/api/add?username={}&password={}&url={}".format(
            username, password, url
        )
    )


def filter_posts(posts, interests):
    filtered_posts = []

    print(interests)
    for post in posts:
        subdomain = urlparse(post["url"]).hostname.split(".")[1]
        for interest in interests:
            if interest.lower() == subdomain.lower():
                filtered_posts.append(post)

    return filtered_posts


if __name__ == "__main__":
    cli()
