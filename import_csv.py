import csv

from django.contrib.auth.models import User
from log.models import LogEntry

desired_fields = ['text', 'event_date', 'created_at']
default_author = 'aboyle'
author = User.objects.get(username=default_author);

filename='log.csv'
with open(filename) as fh:
    reader = csv.reader(fh)
    columns = next(reader)
    print(columns)
    desired_fields_idx = list(map(desired_fields.index, desired_fields))
    print(desired_fields_idx)
    for row in reader:
        entry = {};
        for field, idx in zip(desired_fields, desired_fields_idx):
            entry[field] = row[idx]
        entry['author'] = author;
        entry['updated_at'] = entry['created_at'];
        print(entry)
        LogEntry.objects.create(**entry)

