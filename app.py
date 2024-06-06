import os
from flask import Flask, render_template, abort
from helpers.ipaddress import get_ip_addresses, get_hostname
from helpers.whoisdomain import whois_domain
from helpers.dnslookup import get_a_record, get_aaaa_record, get_cname_record, get_mx_record, get_ns_record, get_srv_record, get_soa_record, get_txt_record
TEMPLATE_DIR = os.path.abspath('./templates')
STATIC_DIR = os.path.abspath('./static')


app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

banks = [
    {"bankName": "Bank Aceh", "linkBank": "bankaceh.co.id", "slug": "bank-aceh"},
    {"bankName": "Bank BPD Bali", "linkBank": "bpdbali.co.id", "slug": "bank-bpd-bali"},
    {"bankName": "Bank Bengkulu", "linkBank": "bankbengkulu.co.id", "slug": "bank-bengkulu"},
    {"bankName": "Bank DKI (Jakarta)", "linkBank": "bankdki.co.id", "slug": "bank-dki-jakarta"},
    {"bankName": "Bank Jambi", "linkBank": "bankjambi.co.id", "slug": "bank-jambi"},
    {"bankName": "Bank Banten", "linkBank": "bankbanten.co.id", "slug": "bank-banten"},
    {"bankName": "Bank Jateng (Central Java)", "linkBank": "bankjateng.co.id", "slug": "bank-jateng-central-java"},
    {"bankName": "Bank BJB (West Java and Banten)", "linkBank": "bankbjb.co.id", "slug": "bank-bjb-west-java-and-banten"},
    {"bankName": "Bank Jatim (East Java)", "linkBank": "bankjatim.co.id", "slug": "bank-jatim-east-java"},
    {"bankName": "Bank Kaltimtara (East Kalimantan and North Kalimantan)", "linkBank": "bankaltimtara.co.id", "slug": "bank-kaltimtara-east-kalimantan-and-north-kalimantan"},
    {"bankName": "Bank Kalteng (Central Kalimantan)", "linkBank": "bankkalteng.co.id", "slug": "bank-kalteng-central-kalimantan"},
    {"bankName": "Bank Kalbar (West Kalimantan)", "linkBank": "bankkalbar.co.id", "slug": "bank-kalbar-west-kalimantan"},
    {"bankName": "Bank Kalsel (South Kalimantan)", "linkBank": "bankkalsel.co.id", "slug": "bank-kalsel-south-kalimantan"},
    {"bankName": "Bank Lampung", "linkBank": "banklampung.co.id", "slug": "bank-lampung"},
    {"bankName": "Bank Maluku Malut (Maluku and North Maluku)", "linkBank": "bankmaluku.co.id", "slug": "bank-maluku-malut-maluku-and-north-maluku"},
    {"bankName": "Bank NTB (West Nusa Tenggara)", "linkBank": "bankntb.co.id", "slug": "bank-ntb-west-nusa-tenggara"},
    {"bankName": "Bank NTT (East Nusa Tenggara)", "linkBank": "bankntt.co.id", "slug": "bank-ntt-east-nusa-tenggara"},
    {"bankName": "Bank Papua", "linkBank": "bankpapua.co.id", "slug": "bank-papua"},
    {"bankName": "Bank Riau Kepri (Riau and Riau Islands)", "linkBank": "bankriaukepri.co.id", "slug": "bank-riau-kepri-riau-and-riau-islands"},
    {"bankName": "Bank Sultra (Southeast Sulawesi)", "linkBank": "banksultra.co.id", "slug": "bank-sultra-southeast-sulawesi"},
    {"bankName": "Bank Sulteng (Central Sulawesi)", "linkBank": "banksulteng.co.id", "slug": "bank-sulteng-central-sulawesi"},
    {"bankName": "Bank Sulselbar (South and West Sulawesi)", "linkBank": "banksulselbar.co.id", "slug": "bank-sulselbar-south-and-west-sulawesi"},
    {"bankName": "Bank Sulut (North Sulawesi and Gorontalo)", "linkBank": "bankbsg.co.id", "slug": "bank-sulut-north-sulawesi-and-gorontalo"},
    {"bankName": "Bank Nagari (West Sumatra)", "linkBank": "banknagari.co.id", "slug": "bank-nagari-west-sumatra"},
    {"bankName": "Bank Sumsel Babel (South Sumatra and Bangka Belitung Islands)", "linkBank": "bank.sumselbabel.co.id", "slug": "bank-sumsel-babel-south-sumatra-and-bangka-belitung-islands"},
    {"bankName": "Bank Sumut (North Sumatra)", "linkBank": "banksumut.co.id", "slug": "bank-sumut-north-sumatra"},
    {"bankName": "Bank BPD DIY (Yogyakarta)", "linkBank": "bpddiy.co.id", "slug": "bank-bpd-diy-yogyakarta"}
]



@app.route('/')
def index():
    return render_template('index.html', banks=banks)

@app.route('/<slugBank>')
def detail(slugBank):
    mapBank = next((bank for bank in banks if bank['slug'] == slugBank), None)
    if not mapBank:
        abort(404, description="Bank not found")
    
    domain = mapBank['linkBank']
    hostname = get_hostname(domain)
    ipv4, ipv6 = get_ip_addresses(hostname)
    ipInfo = {
        'ipv4': ipv4,
        'ipv6': ipv6
    }

    whoisDomain = whois_domain(domain)
    a_record = get_a_record(domain)
    return render_template('_bank.html', bank=mapBank, hostname=hostname, ipInfo=ipInfo, whoisDomain=whoisDomain, a_record=a_record)

if __name__ == '__main__':
    app.run(port=11003, debug=True)
