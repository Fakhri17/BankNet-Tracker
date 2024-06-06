import dns.resolver

def get_a_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_aaaa_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_cname_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'CNAME')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_mx_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'MX')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_ns_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'NS')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_srv_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'SRV')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_soa_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'SOA')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)

def get_txt_record(domain):
    try:
        answers = dns.resolver.resolve(domain, 'TXT')
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return str(e)