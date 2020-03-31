############################################
#
# Filter by country
# Author : MS
# Date : 16/03/2020
#
# Replace the "___" by appropriate code
#
###########################################

import urllib.request as urllib2
import csv


def download_file(url, file_name):
    '''
    Download a file from url and copy it localy with file_name as name
    '''
    try:
        # open url passed in argument
        file = urllib2.urlopen(url)
        # open file for writing in binary mode
        # https://docs.python.org/3/library/functions.html#open
        with open(file_name, 'wb') as output:
            # write in output the file read
            output.write(file.read())
        # OK : return true
        return True
    except:
        # Something is wrong : return false
        return False


def read_CSV(file):
    '''
    Read a csv file and return :
    - fields name as string in a list
    - datas dictionary  by countries in a list
    '''
    # datas is an empty list 
    datas = []
    # open the file passed in argument as csvfile
    # https://docs.python.org/3/library/csv.html#csv.reader
    with open(file) as csvfile:
        # Create a dictionnary with all datas
        reader = csv.DictReader(csvfile)
        # each row in reader is a dictionary by country
        for row in reader:
            # add row in datas list
            datas.append(row)
        # return the list of dictionaries by countries
        return datas

def data_for_country(data, state = "", country = ""):
    # for each country in data
    for pays in data:
        # if 'Province\State' key match with state given in argument
        # and if 'Country/Region' key match with country given in argument
        if pays['Country/Region'] == country and pays['Province/State'] == state:
            return pays


# here the main code
if __name__ == '__main__':

    # File name of datas
    file = "time_series_covid19_confirmed_global.csv"
    # where datas are located
    url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"

if download_file(url,file):
      print(f'Téléchargement du fichier {file} terminé avec succès')
      countries = read_CSV(file)
      print("liste des pays et régions recencés")
      print("----------------------------------")
      # for row in coutries:
      #    print(row['Province/State'], row['Country/Region'])
      france = data_for_country(countries, '', 'France')
      print(france)

else:
      print(f'Téléchargement du fichier {file} impossible')
