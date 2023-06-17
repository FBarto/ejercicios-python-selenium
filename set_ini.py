import configparser #parsea una config para luego grabarla en un archivo y darle el formato que necesitemos


configuracion=configparser.ConfigParser()
configuracion['General'] = {'chrome' : 'C:\dcrhome\chromedriver_win32\chromedriver.exe'}
configuracion['Paginas'] = {'page' : 'https://www.google.com'}

with open('configuracion.ini', 'w') as archivoconfig:
    configuracion.write(archivoconfig)

