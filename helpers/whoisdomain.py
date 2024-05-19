import whois

def whois_domain(domain):
    try:
        return dict(whois.whois(domain))
    except Exception as e:
        return str(e)
# Path: helpers/ipaddress.py
