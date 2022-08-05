import csv, requests, json
from slugify import slugify

with open('frama.csv', newline='') as frama:
    frama_apps_list = csv.reader(frama)
    new_frama_apps_list = []
    with open('new_frama.csv', 'w', newline='') as new_frama:
        new_frama_writer = csv.writer(new_frama)
        for app_proprio,app_libre in frama_apps_list:
            row = [app_proprio, app_libre, slugify(app_proprio, separator=''),slugify(app_libre, separator='')]
            new_frama_apps_list.append(row)
            new_frama_writer.writerow(row)