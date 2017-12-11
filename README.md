# RCForb Report Builder
Small application build csv reports from [RCForb Server](http://www.remotehams.com/index.php)
remote radio logs written in Python.

## Dependencies

- pyyaml

## Installation
It's recommended that the application be installed in a virtual environment:

```bash
$ python -m venv venv
$ source venv/bin/activate
```

Install dependencies:

```bash
$ python setup.py install
```
## Getting Started

Set the path to your sqlite dababase 'Database.db' of your RCForb server 
installation in 'conf.yml' under `database_path`
Creating reports:
```bash
$ ./report-builder.py <conf.yml>
```

Reports can be found in the `reports` folder.

## Adding reports

New reports can be added to [conf.yml](./conf.yml) by giving them a name (filename) and a valid
sqlite query.

