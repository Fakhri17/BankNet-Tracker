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

#get CNAME
def get_cname_record(domain):
    try:
        cname_record = dns.resolver.resolve(domain, 'CNAME')
        return cname_record
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

#get MX record
def get_mx_record(domain):
    try:
        mx_record = dns.resolver.resolve(domain, 'MX')
        return mx_record
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

#get NS record
def get_ns_record(domain):
    try:
        ns_record = dns.resolver.resolve(domain, 'NS')
        return ns_record
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
