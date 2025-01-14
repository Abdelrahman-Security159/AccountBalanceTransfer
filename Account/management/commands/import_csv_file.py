import csv
from django.core.management.base import BaseCommand
from Account.models import Account

class Command(BaseCommand):
    help = 'Import accounts from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        try:
            with open(csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if not row.get('ID'):
                        self.stdout.write(self.style.WARNING(f'Skipping invalid row: {row}, reason: No ID Found'))
                        continue

                    if not row.get('Balance'):
                        self.stdout.write(self.style.WARNING(f'Skipping invalid row: {row}, reason: No Balance Found'))
                        continue

                    if not row.get('Name'):
                        self.stdout.write(self.style.WARNING(f'Skipping invalid row: {row}, reason: No Name Found'))
                        continue

                    if Account.objects.filter(account_id=row['ID']).exists():
                        self.stdout.write(self.style.WARNING(f'Duplicate account ID: {row["ID"]}'))
                        continue

                    Account.objects.create(
                        account_id=row['ID'],
                        balance=row['Balance']
                    )
                    
            self.stdout.write(self.style.SUCCESS('Accounts imported successfully!'))
        except Exception as e:
            print(repr(e))
            self.stdout.write(self.style.ERROR('''
[!] Error importing accounts

Debugging!!

0) Check from migrating -> python manage.py migrate                                                    
1) Try to check from the file path
2) Check if the CSV file is in the correct format
3) Write this command "python manage.py import_csv_file path\\to\\accounts.csv"
'''))