## hackerpaper 
Hacker News Articles to your Instapaper.

### Usage
Simply install hackerpaper using pip

```bash
$ pip install hackerpaper
```

### Arguments
`--account`: required, email and password to your instapaper account  
`--id`: optional, HackerNews Article ID to add  
`--type`: required, type of HackerNews Article, if ID is blank, will scrape posts with given type

### Example

```bash
$ hackerpaper --account <email> <pass>
HackerNews Article ID []: 12345
Type of HackerNews Articles (item, askstories, newstories, jobstories, beststories, showstories): item
```
