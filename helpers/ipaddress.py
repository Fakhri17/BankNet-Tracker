import socket
import requests

def get_responseurl(url):
    try:
       response = requests.head(url, allow_redirects=True)
       return response.headers
    except requests.exceptions.RequestException:
        return None
    

def get_hostname(url):
    return url.split('//')[-1].split('/')[0].split('?')[0].split(':')[0]

def get_ip_addresses(hostname):
    try:
        ipv4 = socket.gethostbyname(hostname)
    except socket.gaierror:
        ipv4 = 'No IPv4 Address Found'
    try:
        ipv6 = socket.getaddrinfo(hostname, None, socket.AF_INET6)[0][4][0]
    except socket.gaierror:
        ipv6 = 'No IPv6 Address Found'
    return ipv4, ipv6