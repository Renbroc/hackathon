# Renaissance Broccoli

Renaissance Broccoli will make you want to eat your vegetables first. 

## Project Info
OUR GOAL is to serve up high-quality but low-attention content to audiences who would otherwise have missed it.

### THE PROBLEM

Journalists and their publishers want you to read their work. You want to read good work. But existing recommendation engines and trending topic tallies have a few key gaps.

1. The "Ren": Information bubbles and becoming well-rounded. Modern news consumption is generally balkanizing: echo chambers abound and we curate our social feeds and news aggregators in such a way that we are likely to see lots of information relating to our key interests… but not so much about anything else. Lots of other work -- potentially important, high-quality, or meaningful -- stories just might not float across our streams. To become a true renaissance (wo)man, you need to know what it is you don't know and fill in your areas of weakness, not just reinforce your strengths.

2. The "Broc": Stories that tend to trend the most quickly or the most virally aren't necessarily the important, in-depth, investigative, or uncomfortable stories that really need to be heard. Research-heavy, "unsexy" work by both major news outlets as well as by advocacy-heavy nonprofits is critical but rarely travels as well as stories about entertainment, arts, and the like.

In short, your media diet can't just be tasty junk food. You need your broccoli, too.

Stories about major regulatory, political, international, and social issues might be interesting and high-quality, with solid reporting and compelling writing -- but if they don't first come across your path their quality doesn't matter, because you aren't reading them. So we want to draw your attention to them.

### THE SOLUTION

We compare interactions -- comments and social interactions -- against page views to find stories that have heavily engaged the audience that has read them, but that haven't spread very far, and have low view counts. We then recommend these stories to users, giving them an interface to find some broccoli to add to their media diet, and a way to see what they have read and how well-rounded their diet really is.

[Project presentation](https://docs.google.com/presentation/d/1XemqiDHPRvLryLiI268vzJQzPt3kbOxX39OQMKc9Qds/edit?usp=sharing)


## Development

Install Python requirements:

    pip install -r requirements.txt

Pull the git repository 'postgress' and do the following:


To run, you will first need to set the evironment variables for config.py:

    export EXAMPLE="value"


Run the web server

    python runserver.py

Update database:

    drop database renbroc;
    create database renbroc;
    use renbroc;
    source /full/path/to/renbroc.sql

Update Urls

    use renbroc;
    drop table urls;
    source /full/path/to/renbroc_urls.sql



Import the database (using command line):
- create database renbroc;
- grant all privileges on renbroc.* to ren_user@localhost identified by 'ren_pass';
- use renbroc;
- source /full/path/to/renbroc.sql


## Pay Attention To:
- [http://flask.pocoo.org/docs/0.10/]Flack Documentation!
- views.py : This will hold URL information, and what templates to pull in
- templates/ : Directory with template files. [http://jinja.pocoo.org/docs/dev/](Tempalte Docs)
- static/ : Directory with static files: js, css, images
- models.py : Blank currently, will have model info as we create
- [http://flask.pocoo.org/docs/0.10/patterns/packages/](More information) about project directory setup

Example of config:
- app.config['CONFIG_VAR_NAME']



## Future

Need to do:
- example 1
- example 2
- example 3
