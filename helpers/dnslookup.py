# get A records
import dns.resolver

def get_a_record(domain):
    try:
        a_record = dns.resolver.resolve(domain, 'A')
        return a_record
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        return None
    except dns.resolver.NoNameservers:
        return None
    except dns.resolver.Timeout:
        return None
    except dns.resolver.NoRootSOA:
        return None
    except dns.exception.DNSException:
        return None
    except Exception as e:
        return None
# get hostname
def get_aaaa_record(domain):
    try:
        aaaa_record = dns.resolver.resolve(domain, 'AAAA')
        return aaaa_record
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        return None
    except dns.resolver.NoNameservers:
        return None
    except dns.resolver.Timeout:
        return None
    except dns.resolver.NoRootSOA:
        return None
    except dns.exception.DNSException:
        return None
    except Exception as e:
        return None
    
def get_soa_record(domain):
    try:
        soa_record = dns.resolver.resolve(domain, 'SOA')
        return soa_record
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        return None
    except dns.resolver.NoNameservers:
        return None
    except dns.resolver.Timeout:
        return None
    except dns.resolver.NoRootSOA:
        return None
    except dns.exception.DNSException:
        return None
    except Exception as e:
        return None