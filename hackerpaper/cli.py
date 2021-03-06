import requests
import click
from urllib.parse import urlparse
from request import Request


@click.command()
@click.option(
    "--account",
    "-a",
    required=True,
    nargs=2,
    default=[None] * 2,
    help="Instapaper account information",
    type=click.Tuple([str, str]),
)
@click.option(
    "--id",
    "-id",
    help="HackerNews article ID",
    required=False
)
@click.option(
    "--type",
    "-t",
    help="HackerNews article type",
    required=True
)
@click.option(
    "--limit",
    "-l",
    help="A cap on how many articles to add",
    type=int,
    required=False
)
@click.option(
    "--interests",
    "-i",
    help="Subdomains of the HackerNews articles",
    multiple=True,
    default=[],
)
def cli(account, id, type, limit, interests):
    """Entry point for the cli

    :param account: user's Instapaper account information
    :param id: hackernews article id
    :param type: type of hackernews articles
    :param interests: array of subdomains user is interested in
    """
    if None in account or not authenticate(account):
        click.secho("Invalid credentials!", fg="red")
        exit()

    print("[~] Fetching Data...")

    res = Request(id, type).fetch_data()
    try:
        add_to_instapaper(account, res, limit, interests)
        click.secho("Process complete!", fg="green")
    except Exception as error:
        print("Error: {}", error)


def authenticate(account):
    """Authenticate's users Instapaper credentials

    :param account: user's Instapaper account information
    :rtype: boolean
    """
    username, password = account[0], account[1]

    res = requests.get(
        "https://www.instapaper.com/api/authenticate?username={}&password={}".format(
            username, password
        )
    )

    if res.status_code == 200:
        return True
    return False


def add_to_instapaper(account, res, limit, interests):
    """Processes and calls post on array of hackernews post objects

    :param account: user's Instapaper account information
    :param res: array of hackernews post objects
    :param interests: array of subdomain's user is interested in
    """
    username, password = account[0], account[1]

    if isinstance(res, list):
        posts = []

        for p in res:
            if "url" in p and "title" in p:
                posts.append(p)

        if interests:
            print("[~] Filtering posts...")
            posts = filter_posts(posts, interests)

        if limit is not None:
            added = 0
            for p in posts:
                added += post(username, password, p["url"])
                if added == limit:
                    break
        else:
            for p in posts:
                post(username, password, p["url"])
    else:
        if "url" in res:
            post(username, password, res["url"])


def post(username, password, url):
    """Posts url to users Instapaper account

    :param username: username or email to user's Instapaper account
    :param password: password to user's Instapaper account
    """
    print("[~] Adding URL: {} to Instapaper...\n".format(url))

    try:
        requests.post(
            "https://www.instapaper.com/api/add?username={}&password={}&url={}".format(
                username, password, url
            )
        )
    except Exception as error:
        click.secho(
            "Error adding URL to Instapaper: {}".format(error), fg="red")
        exit()

    return 1


def filter_posts(posts, interests):
    """Filters hacker news post objects based on user interests

    :param posts: array of hacker news post objects
    :param interests: array of subdomains user is interested in
    :return: array of filtered hacker news post objects
    """
    filtered_posts = []

    for post in posts:
        subdomain = urlparse(post["url"]).hostname.split(".")[1]
        if subdomain in interests:
            filtered_posts.append(post)

    return filtered_posts


if __name__ == "__main__":
    cli()
