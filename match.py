import csv, requests, json
from slugify import slugify
from time import sleep

apikey = "ddde095f-81cf-4dbe-bf8e-be0c18145d8a"
def get_first_cpe(url):
    for i in range(0, 10):
        try:
            results = requests.get(url).json()
        except:  
            print("Sleeping 10")  
            sleep(10)
            pass
    if results and results['result']['cpeCount'] > 0:
        cpe = results['result']['cpes'][0]['cpe23Uri']
        # cpe:2.3:a:nextcloud:nextcloud:1.0.0:*:*:*:*:android:*:*
        cpe = cpe.split(":")
        cpe = cpe[0:4]
        cpe = ":".concat(cpe)
        return cpe
    return False

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
        new_apps_writer.writerow(["App YnH", "Apps proprio", "CPE"])
        for ynh_app in apps_file:
            ynh_app = ynh_app.strip()

            # Match CPE
            # https://services.nvd.nist.gov/rest/json/cpes/1.0/?keyword=nextcloud&resultsPerPage=1
            cpe = get_first_cpe(f'https://services.nvd.nist.gov/rest/json/cpes/1.0/?cpeMatchString=cpe:2.3:a:{ynh_app}:{ynh_app}&resultsPerPage=1&apiKey={apikey}')
            if not cpe:
                cpe = get_first_cpe(f'https://services.nvd.nist.gov/rest/json/cpes/1.0/?keyword={ynh_app}&resultsPerPage=1&apiKey={apikey}')
            if not cpe:
                cpe = False

            # Match framathing
            corresponding_app_proprio = []
            for app_proprio, app_libre, slugified_app_proprio, slugified_app_libre in new_frama_apps_list:
                if ynh_app == slugified_app_libre:
                    corresponding_app_proprio.append(app_proprio)

            print(ynh_app+" did match "+",".join(corresponding_app_proprio)+" and CPE "+str(cpe))
            new_apps_writer.writerow([ynh_app, ",".join(corresponding_app_proprio), cpe])