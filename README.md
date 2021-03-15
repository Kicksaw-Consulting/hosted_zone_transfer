### Business Requirements

We have to move a handful of hosted zones from one account to another. The process is tedious and we'd like a tool that handles the json parsing process that otherwise is done by hand.

### Technical Requirements

Your script will be specifically automating the json transformation required in step 4 of [this document](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html#hosted-zones-migrating-edit-records)

This script will consume a json file created by the aws cli `list-resource-record-sets` command print out json suitable for consumption by the aws cli `change-resource-record-sets` command. It should be noted that you will NOT be calling those commmands. But they are the foundation of this script, so I'm pointing this out.

A sample of the output from `list-resource-record-sets` lives at `example_zone.json`.

Your solution will use the [click](https://click.palletsprojects.com/en/7.x/) framework to define input and will output the json to standard out. A poetry toml file is included for your requirements. A sample json file (`import.py`) has been provided with the basics of Click already set up.

Your solution will work in Python 3.8 or greater.

### Supporting files

The `import.py` file has been included to jumpstart your process. The click arguments have been pre-defined for you.

The `example_zone.json` is a zone file you can use for practice input.
