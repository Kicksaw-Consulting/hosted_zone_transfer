### Business Requirements

We have to move a handful of hosted zones from one account to another. The process is tedious and we'd like a tool that handles the json parsing process that otherwise is done by hand.

### Part 1: CLI Script

Your script will be specifically automating the json transformation required in step 4 of [this document](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html#hosted-zones-migrating-edit-records)

This script will consume a json file created by the aws cli `list-resource-record-sets` command print out json suitable for consumption by the aws cli `change-resource-record-sets` command. It should be noted that you will NOT be calling those commmands. But they are the foundation of this script, so I'm pointing this out.

A sample of the output from `list-resource-record-sets` lives at `example_zone.json`.

Your solution will use the [click](https://click.palletsprojects.com/en/7.x/) framework to define input and will output the json to standard out. A poetry toml file is included for your requirements. A sample json file (`import.py`) has been provided with the basics of Click already set up.

Your solution will work in Python 3.8 or greater.

### Part 2: Django App

Take the library you made in the previous step and create a one-page Django website to receive input and display the output. The page should have a form with which you'll submit the untransformed JSON, and after submitting it should show the transformed results.

### Supporting files

The `import.py` file has been included to jumpstart your process. The click arguments have been pre-defined for you.

The `example_zone.json` is a zone file you can use for practice input.

### Submission

To submit this assessment, do the following:

1. fork this project as a private repo
2. complete your work
3. invite these users as contributors: [tsabat](https://github.com/tsabat) and [brno32](https://github.com/brno32)
4. profit
