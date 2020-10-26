# hn api endpoints for static and live data

static_types = ["item", "user"]
live_types = ["askstories", "livestories", "jobstories", "newstories", "topstories"]


def static_data(id, type):
    if type.lower() not in static_types:
        return "Invalid type"
    return "https://hacker-news.firebaseio.com/v0/{}/{}.json?print=pretty".format(
        type.lower(), id
    )


def live_data(type):
    if type.lower() not in live_types:
        return "Invalid type"
    return "https://hacker-news.firebaseio.com/v0/{}.json?print=pretty".format(
        type.lower()
    )
