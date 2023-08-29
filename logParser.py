import sys
import re

'''
with open(sys.argv[1], 'rb') as logfile:
    log_string = logfile.readline()
'''

log_string = "https://www.google.com wonderful what 345.21. malicious.exe is 192.168.0.1 here https://mydomain.com innocent.exe 10.10.10.2"
log_delimiter = ' '

i = log_string.index('https://')
log_data = log_string.split(log_delimiter)
urls = []
exes = []
ips = []

for x in log_data:
    # find a url
    if (x.find('https://')) >= 0: 
        urls.append(x)
        # print(f'log string is {x}')
    
    # find exe names
    if x.find(".exe") >= 0:
        exes.append(x)

    # find ip addresses
    if re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}", x):
        ips.append(x)

    # find paths
    # find timestamps


print(f'Urls found! {urls}')
print(f'Exes found! {exes}')
print(f'IPS found! {ips}')







    


