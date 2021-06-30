import os

from .models import Command
from .utils import getinstance

def command_lock(f):
    def wrapper(command,*args,**options):
        instance = getinstance(command)
        module_name = type(instance).__module__
        app, name = module_name.split('.')[-4], module_name.split('.')[-1]
        command, created = Command.objects.get_or_create({'app':app,'pid':os.getpid()},name=name)
        if command.app!=app:
            Command.objects.filter(name=name).update(app=app)
        try:
            os.kill(command.pid, 0)
            if command.is_locked:
                return
        except (OSError,ProcessLookupError):
            return f(instance,*args, **options)
    return wrapper if f else None
