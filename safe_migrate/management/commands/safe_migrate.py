from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Wraps South migrate with a lock.'

    def handle(self, *args, **options):
        locked = not cache.add('__south_lock', 1)
        if locked:
            print "Migrations are locked, don't run."
            return
        try:
            call_command('migrate')
        except:
            import traceback
            traceback.print_exc()
        finally:
            cache.delete('__south_lock')
