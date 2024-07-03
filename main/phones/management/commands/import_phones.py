import csv

from django.template.defaultfilters import slugify
from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        '''Для загрузки данных из csv в БД'''
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        for phone_ in phones:
            phone = Phone(name=phone_['name'],
                          price=phone_['price'],
                          image=phone_['image'],
                          release_date=phone_['release_date'],
                          lte_exists=phone_['lte_exists'],
                          slug=slugify(phone_['name'])
                          )
            phone.save()
