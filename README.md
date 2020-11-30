## hackerpaper

Hacker News Articles to your Instapaper.

### Usage

Simply install hackerpaper using pip

```bash
$ pip install hackerpaper
```

### Options

```
Usage: cli.py [OPTIONS]

  Entry point for the cli

  :param account: user's Instapaper account information :param id:
  hackernews article id :param type: type of hackernews articles :param
  interests: array of subdomains user is interested in

Options:
  -a, --account <TEXT TEXT>...  Instapaper account information  [required]
  -id, --id TEXT                HackerNews article ID
  -t, --type TEXT               HackerNews article type  [required]
  -l, --limit INTEGER           A cap on how many articles to add
  -i, --interests TEXT          Subdomains of the HackerNews articles
  --help                        Show this message and exit.

```

### Example

```bash
$ hackerpaper -a <email> <pass> -t newstories -i github
```

The above example will add all HackerNews articles under the `newstories` type that have the subdomain `github`
to your Instapaper account.
