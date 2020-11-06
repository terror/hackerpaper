import click

static_type = "item"

live_types = [
    "askstories",
    "livestories",
    "jobstories",
    "newstories",
    "topstories",
    "beststories",
]


def static_data(id, type):
    """Returns url for a static data request (single article)

    :param id: id of hacker news article
    :param type: type of hacker news article (item)
    :return: url for static data request
    """
    if type.lower() != static_type:
        display_error()

    return "https://hacker-news.firebaseio.com/v0/{}/{}.json?print=pretty".format(
        type.lower(), id
    )


def live_data(type):
    """Returns url for a live data request

    :param type: type of hacker news articles
    :return: url for live data request
    """
    if type.lower() not in live_types:
        display_error()

    return "https://hacker-news.firebaseio.com/v0/{}.json?print=pretty".format(
        type.lower()
    )


def display_error():
    """Display's error message"""
    click.secho("Invalid type!", fg="red")
    exit()
