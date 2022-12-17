import csv
import re

# columns = ['Tweet-Text', 'Tweet-ID', 'Created-At', 'From-User-Id', 'To-User-Id', 'Retweet-Count', 'PartyName', 'Score',
#           'Scoring-String', 'Negativity', 'Positivity', 'Uncovered-Tokens', 'Total-Tokens']


def is_valid_entry(column_index, entry):
    if column_index == 0:
        if entry and not isinstance(entry, int) and not isinstance(entry, float) and isinstance(entry, str):
            return True
        else:
            return False

def nullByteReader(reader):
    while True:
        try:
            yield next(reader)
        except csv.Error:
            continue
        except StopIteration:
            break

data = {}
positive = open('positive.txt', 'w')
negative = open('negative.txt', 'w')

with open('data.csv', "r", errors='ignore') as file:
    reader = nullByteReader(csv.reader(file))
    for row in reader:
        line = []
        if len(row) == 13:
            if is_valid_entry(0, row[0]):
                row[0] = re.sub(r'\s+', ' ', row[0]).strip()
                row[0] = re.sub(r'@\w+', '', row[0])
                row[0] = re.sub(r'[^\w\s]', '', row[0])
                row[0] = row[0].lower()
                line.append(row[0].split())
            if row[9] > row[10]:
                negative.write(str(line))
                negative.write('\n')
            if row[10] > row[9]:
                positive.write(str(line))
                positive.write('\n')

negative.close()
positive.close()
