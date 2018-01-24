from celery import chain
from celery.task import Task
from django.core.management import BaseCommand
from cel.tasks import AddTask


class Command(BaseCommand):

    def handle(self, *args, **options):
        c = chain(AddTask().si(1, 2))()
        print(c.get())
