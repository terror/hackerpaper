## hackerpaper 
Hacker News Articles to your Instapaper.

### Usage
Simply install hackerpaper using pip

```bash
$ pip install hackerpaper
```

### Arguments
`--account, -a`: required, email and password to your instapaper account.  

`--id, -id`: optional, HackerNews article id to add.  

`--type, -t`: required, type of HackerNews article, if id is blank, will scrape posts with given type,
see [here](https://github.com/terror/hackerpaper/blob/master/types.txt) for the full list of valid types.  

`--interests, -i`: optional, subdomains of the HackerNews articles

### Example

```bash
$ hackerpaper -a <email> <pass> -t newstories -i github
```

The above example will add all HackerNews articles under the `newstories` type that have the subdomain `github`
to your Instapaper account.
