import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from phones.models import Phone


class Command(BaseCommand):

    help = 'Importing data for 3 phones into the database'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            Phone(id=phone.get('id'),
                  name=phone.get('name'),
                  price=phone.get('price'),
                  image=phone.get('image'),
                  release_date=phone.get('release_date'),
                  lte_exists=phone.get('lte_exists'),
                  slug=slugify(phone.get('name'))
                  ).save()
