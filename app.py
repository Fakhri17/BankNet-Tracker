from flask import Flask, render_template
import socket

app = Flask(__name__)

banks = [
    {"bankName": "Bank Aceh", "linkBank": "www.bankaceh.co.id", "slug": "bank-aceh"},
    {"bankName": "Bank BPD Bali", "linkBank": "www.bpdbali.co.id", "slug": "bank-bpd-bali"},
    {"bankName": "Bank Bengkulu", "linkBank": "www.bankbengkulu.co.id", "slug": "bank-bengkulu"},
    {"bankName": "Bank DKI (Jakarta)", "linkBank": "www.bankdki.co.id", "slug": "bank-dki-jakarta"},
    {"bankName": "Bank Jambi", "linkBank": "www.bankjambi.co.id", "slug": "bank-jambi"},
    {"bankName": "Bank Banten", "linkBank": "www.bankbanten.co.id", "slug": "bank-banten"},
    {"bankName": "Bank Jateng (Central Java)", "linkBank": "www.bankjateng.co.id", "slug": "bank-jateng-central-java"},
    {"bankName": "Bank BJB (West Java and Banten)", "linkBank": "www.bankbjb.co.id", "slug": "bank-bjb-west-java-and-banten"},
    {"bankName": "Bank Jatim (East Java)", "linkBank": "www.bankjatim.co.id", "slug": "bank-jatim-east-java"},
    {"bankName": "Bank Kaltimtara (East Kalimantan and North Kalimantan)", "linkBank": "www.bankaltimtara.co.id", "slug": "bank-kaltimtara-east-kalimantan-and-north-kalimantan"},
    {"bankName": "Bank Kalteng (Central Kalimantan)", "linkBank": "www.bankkalteng.co.id", "slug": "bank-kalteng-central-kalimantan"},
    {"bankName": "Bank Kalbar (West Kalimantan)", "linkBank": "www.bankkalbar.co.id", "slug": "bank-kalbar-west-kalimantan"},
    {"bankName": "Bank Kalsel (South Kalimantan)", "linkBank": "www.bankkalsel.co.id", "slug": "bank-kalsel-south-kalimantan"},
    {"bankName": "Bank Lampung", "linkBank": "www.banklampung.co.id", "slug": "bank-lampung"},
    {"bankName": "Bank Maluku Malut (Maluku and North Maluku)", "linkBank": "www.bankmaluku.co.id", "slug": "bank-maluku-malut-maluku-and-north-maluku"},
    {"bankName": "Bank NTB (West Nusa Tenggara)", "linkBank": "www.bankntb.co.id", "slug": "bank-ntb-west-nusa-tenggara"},
    {"bankName": "Bank NTT (East Nusa Tenggara)", "linkBank": "www.bankntt.co.id", "slug": "bank-ntt-east-nusa-tenggara"},
    {"bankName": "Bank Papua", "linkBank": "www.bankpapua.co.id", "slug": "bank-papua"},
    {"bankName": "Bank Riau Kepri (Riau and Riau Islands)", "linkBank": "www.bankriaukepri.co.id", "slug": "bank-riau-kepri-riau-and-riau-islands"},
    {"bankName": "Bank Sultra (Southeast Sulawesi)", "linkBank": "www.banksultra.co.id", "slug": "bank-sultra-southeast-sulawesi"},
    {"bankName": "Bank Sulteng (Central Sulawesi)", "linkBank": "www.banksulteng.co.id", "slug": "bank-sulteng-central-sulawesi"},
    {"bankName": "Bank Sulselbar (South and West Sulawesi)", "linkBank": "www.banksulselbar.co.id", "slug": "bank-sulselbar-south-and-west-sulawesi"},
    {"bankName": "Bank Sulut (North Sulawesi and Gorontalo)", "linkBank": "www.bankbsg.co.id", "slug": "bank-sulut-north-sulawesi-and-gorontalo"},
    {"bankName": "Bank Nagari (West Sumatra)", "linkBank": "www.banknagari.co.id", "slug": "bank-nagari-west-sumatra"},
    {"bankName": "Bank Sumsel Babel (South Sumatra and Bangka Belitung Islands)", "linkBank": "www.bank.sumselbabel.co.id", "slug": "bank-sumsel-babel-south-sumatra-and-bangka-belitung-islands"},
    {"bankName": "Bank Sumut (North Sumatra)", "linkBank": "www.banksumut.co.id", "slug": "bank-sumut-north-sumatra"},
    {"bankName": "Bank BPD DIY (Yogyakarta)", "linkBank": "www.bpddiy.co.id", "slug": "bank-bpd-diy-yogyakarta"}
]

@app.route('/')
def index():
    return render_template('index.html', banks=banks)

@app.route('/<slugBank>')
def detail(slugBank):
    mapBank = {}
    for bank in banks:
        if bank['slug'] == slugBank:
            mapBank = bank
            break
    bankLink = mapBank['linkBank']
    # get ip4 from bankLink

    def get_ipv4():
        try:
            return socket.gethostbyname(bankLink)
        except:
            return 'Error'
        
    return render_template('_bank.html', bank=mapBank, ip4=get_ipv4())


if __name__ == '__main__':
    app.run(debug=True)