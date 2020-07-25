#!/usr/bin/python3
# pip3 install pyfiglet
# pip3 install pycurl
# pip3 install colorama

import os, sys, pyfiglet
import pycurl
import io
import colorama
from colorama import Fore, Style

def check_url(url):
    headers = io.BytesIO()
    c = pycurl.Curl()
    c.setopt(c.URL, url)
    c.setopt(c.SSL_OPTIONS, c.SSLVERSION_TLSv1_2)
    c.setopt(c.SSL_VERIFYPEER, False)
    c.setopt(c.SSL_VERIFYHOST, False)
    #c.setopt(c.VERBOSE, False)
    c.setopt(c.TIMEOUT, 10)
    c.setopt(c.COOKIEFILE, "")
    c.setopt(c.USERAGENT, "")
    c.setopt(c.HEADER, False)
    c.setopt(c.NOBODY, False)
    c.setopt(c.HEADERFUNCTION, headers.write)
    c.setopt(c.WRITEFUNCTION, headers.write)
    c.perform()
    resp = c.getinfo(c.HTTP_CODE)
    c.close()
    return resp

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
    print(Fore.YELLOW+' [ '+Fore.WHITE+'REMF.COM.BR'+Fore.YELLOW+' - '+Fore.WHITE+'Find More on Domain'+Fore.YELLOW+' ]'+Style.RESET_ALL)

def ajuda():
    print(' '+Fore.CYAN)
    print(' Use:', sys.argv[0], 'dominio.com.br')
    print('     ', sys.argv[0], 'dominio.com.br lista_palavras.txt')
    print(Style.RESET_ALL+' ')

def main():
    logo()
    if len(sys.argv) == 2:
        domain = sys.argv[1]
        file_list='wordlist.txt'

        if os.path.exists(file_list):
           check_domain(domain, file_list)
        else:
            ajuda()
            print(Fore.YELLOW+' [ '+Style.BRIGHT+Fore.RED+'ERROR'+Fore.YELLOW+' ]'+Style.RESET_ALL+' Arquivo "' + file_list + '" não existe.\n')
            quit()
    elif len(sys.argv) == 3:
        domain = sys.argv[1]
        file_list=sys.argv[2]

        if os.path.exists(file_list):
           check_domain(domain, file_list)
        else:
            ajuda()
            print(Fore.YELLOW+' [ '+Style.BRIGHT+Fore.RED+'ERROR'+Fore.YELLOW+' ]'+Style.RESET_ALL+' Arquivo "' + file_list + '" não existe.\n')
            quit()
    else:
        ajuda()

if __name__== "__main__":
           main()
