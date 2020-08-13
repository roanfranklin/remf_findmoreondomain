#!/usr/bin/python3
# pip3 install pyfiglet
# pip3 install colorama

import os, sys, pyfiglet
import requests
import io
import colorama
from colorama import Fore, Style
from urllib.parse import urlparse

def is_url(url):
  try:
    result = urlparse(url)
    return all([result.scheme, result.netloc])
  except ValueError:
    return False

def check_url(url):
   try:
      resp = requests.get(url,timeout=3)
      return int(resp.status_code)
   except requests.exceptions.RequestException as err:
      # OOps: Something Else
      return 0
   except requests.exceptions.HTTPError as errh:
      # Http Error
      return 0
   except requests.exceptions.ConnectionError as errc:
      # Error Connecting
      return 0
   except requests.exceptions.Timeout as errt:
      # Timeout Error
      return 404

def check_domain(domain, flist):
    file1 = open(flist, 'r')
    Lines = file1.readlines()
    
    for line in Lines:
        url_test = domain + '/' + line.strip() + '/'
        if check_url(url_test) == 200:
            print('Domínio encontrado:',url_test)
        
        url_test = domain + '/' + line.strip()
        if check_url(url_test) == 200:
            print('Arquivo encontrado:',url_test)

        url_test = domain + '/.' + line.strip() + '/'
        if check_url(url_test) == 200:
            print('Domínio oculto encontrado:',url_test)

        url_test = domain + '/.' + line.strip() 
        if check_url(url_test) == 200:
            print('Arquivo oculto encontrado:',url_test)

    print(' ')


def logo():
    os.system("clear")
    ascii_banner = pyfiglet.figlet_format("REMF - FMD")
    print(Style.BRIGHT+Fore.BLUE+ascii_banner)
    print(Fore.YELLOW+' [ '+Fore.WHITE+'REMF.COM.BR'+Fore.YELLOW+' - '+Fore.WHITE+'Find More on Domain'+Fore.YELLOW+' ]'+Style.RESET_ALL+'\n')

def ajuda():
    print(' '+Fore.CYAN)
    print(' Use:', sys.argv[0], 'dominio.com.br')
    print('     ', sys.argv[0], 'dominio.com.br lista_palavras.txt')
    print(Style.RESET_ALL+' \n')

def print_error(txt):
    print(Fore.YELLOW+' [ '+Style.BRIGHT+Fore.RED+'ERROR'+Fore.YELLOW+' ]'+Style.RESET_ALL + txt + '\n')

def print_ok(txt):
    print(Fore.YELLOW+' [ '+Fore.BLUE+'OK'+Fore.YELLOW+' ] '+Style.RESET_ALL + txt + '\n')

def print_check(txt):
    print(Fore.YELLOW+' [ '+Style.BRIGHT+Fore.YELLOW+'CHECK'+Fore.YELLOW+' ] '+Style.RESET_ALL + txt + '\n')

def main():
    logo()
    if len(sys.argv) == 2:
        domain = sys.argv[1]
        file_list='wordlist.txt'

        if os.path.exists(file_list):
           if is_url(domain):
              print_check(domain)
              check_domain(domain, file_list)
           else:
              if is_url('http://'+domain):
                 print_check('http://'+domain)
                 check_domain('http://'+domain, file_list)
              else:		
                 print_error(' http://'+domain+' não é domínio.')
        else:
            ajuda()
            print_error(' Arquivo "' + file_list + '" não existe.')
            quit()
    elif len(sys.argv) == 3:
        domain = sys.argv[1]
        file_list=sys.argv[2]

        if os.path.exists(file_list):
            if is_url(domain):
               print_check(domain)
               check_domain(domain, file_list)
            else:
               if is_url('http://'+domain):
                  print_check('http://'+domain)
                  check_domain('http://'+domain, file_list)
               else:             
                  print_error(' http://'+domain + ' não é domínio.')
        else:
            ajuda()
            print_error(' Arquivo "' + file_list + '" não existe.')
            quit()
    else:
        ajuda()

if __name__== "__main__":
           main()
