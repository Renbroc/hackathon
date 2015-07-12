# Renaissance Broccoli

Renaissance Broccoli will make you want to eat your vegetables first. 

[http://google.com/](URL Example-Google)

- List item 1

- List item 2


## Sub head

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
