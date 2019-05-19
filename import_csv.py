import csv

from django.contrib.auth.models import User
from log.models import LogEntry

desired_fields = ['text', 'event_date', 'created_at', 'updated_at', 'author']

filename='captains_log.csv'
with open(filename) as fh:
    reader = csv.reader(fh)
    columns = next(reader)
    print(columns)
    desired_fields_idx = list(map(columns.index, desired_fields))
    print(desired_fields_idx)
    for row in reader:
        entry = {};
        for field, idx in zip(desired_fields, desired_fields_idx):
            entry[field] = row[idx]

        author = User.objects.get(username=entry['author']);
        entry['author'] = author;
        print(entry)
        LogEntry.objects.create(**entry)
