We have to move a handful of hosted zones from one account to another. The process is tedious and we'd like a tool that handles the json parsing process that otherwise is done by hand.

Your script will be specifically automating the json transformation required in step 4 of [this document](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-migrating.html#hosted-zones-migrating-edit-records)

This script will consume a json file created by the aws cli list-resource-record-sets command and create another json file suitable for consumption by the aws cli change-resource-record-sets command.

Your solution will use the [click](https://click.palletsprojects.com/en/7.x/) framework to define input and will output the json to standard out. A poetry toml file is included for your requirements.

Your solution will work in Python 3.8 or greater.
