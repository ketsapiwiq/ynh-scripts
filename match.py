import csv
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

# new_apps_list = []

with open('apps.txt', newline='') as apps_file:
    with open('new_apps.csv', 'w', newline='') as new_apps:
        new_apps_writer = csv.writer(new_apps)
        for ynh_app in apps_file:
            ynh_app = ynh_app.strip()
            for app_proprio, app_libre, slugified_app_proprio, slugified_app_libre in new_frama_apps_list:
                if ynh_app == slugified_app_libre:
                    # new_apps_list.append([ynh_app, app_proprio])
                    new_apps_writer.writerow([ynh_app, app_proprio])
                    print(ynh_app+" did match "+slugified_app_libre)
                # else:
                #     print(ynh_app+" did not match "+slugified_app_libre)
