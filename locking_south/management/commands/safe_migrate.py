import sys
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.cache import cache

from south.management.commands.migrate import Command as MigrateCommand


class Command(BaseCommand):
    # Inherit options and args from South directly to be passed through
    option_list = MigrateCommand.option_list
    args = MigrateCommand.args

    help = '%s [with locking]' % MigrateCommand.help

    def handle(self, *args, **options):
        locked = not cache.add('__south_lock', 1)
        if locked:
            print 'Migrations are locked, don\'t run.'
            # Explicity end cleanly. Just because it was locked,
            # doesn't mean a failure.
            sys.exit(0)
        try:
            call_command('migrate', *args, **options)
        except:
            import traceback
            traceback.print_exc()
            sys.exit(1)
        finally:
            cache.delete('__south_lock')
