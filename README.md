[![](https://img.shields.io/badge/released-2021.6.19-green.svg?longCache=True)](https://pypi.org/project/django-command-lock/)
[![](https://img.shields.io/badge/license-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)

### Installation
```bash
$ pip install django-command-lock
```

### How it works
+   multiple implementations:
    +   `LockCommand` management command class
    +   `@command_lock` decorator
+   admin interface

#### `settings.py`
```python
INSTALLED_APPS+=['django_command_lock']
```

#### `migrate`
```bash
$ python manage.py migrate
```

### Examples
`LockCommand`
```python
from django_command_lock.management.base import LockCommand

class Command(LockCommand):
    def handle(self,*args,**options):
        # your code
```

`@command_lock`
```python
from django_command_lock.decorators import command_lock

class Command(BaseCommand):
    @command_lock
    def handle(self,*args,**kwargs):
        ...
```
```python
class BaseCommand(BaseCommand):
    def execute(self,*args,**kwargs):
        return command_lock(self.handle)(self,*args,**kwargs)
```

`call_command`
```python
from django.core.management import call_command

command_lock(call_command)(name,*args,**options)
```

