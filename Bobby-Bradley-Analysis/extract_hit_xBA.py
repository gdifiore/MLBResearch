'''
import csv

f = open('savant_data.csv')
csv_f = csv.reader(f)

for row in csv_f:
  print(row)
'''
import csv

username = input()

with open('savant_data.csv', 'rt') as f:
     reader = csv.reader(f, delimiter=',') # good point by @paco
     for row in reader:
          for field in row:
              if field == username:
                  print(row)
