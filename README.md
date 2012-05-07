# Let's prevent [South](http://south.aeracode.org/) from running two migrations at the same time!

## The problem
A common situation in continuous integration/deployment scenarios is having production code pushed to a number of servers at once without any type of "master" controller. All servers are treated equally. In this case when mixed with South, migrations can get crazy. Only one migration instance can run at one time. This lets you do that.

## Installation
`$ pip install django-locking-south`

Add `locking_south` to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = (
    #...
    'south',
    'locking_south',
)
```

_Cache must be configured inside your Django app and be accessible by all servers for locking to actually work._


## Usage
`$ ./manage.py safe_migrate`

_Note_: All options and args for South are passed through and valid for `safe_migrate`.
