import datetime

#   parsing links
LOCAL_PRICE_PATH = 'C:/Users/OperTech/Desktop/тест'
A4_LINK = 'http://aet-auto.ru/files/storage/price.xml'
TOG7_LINK = 'http://www.inpo.ru/documents/pricelists/pricelist.xml'
KVT_LINK = 'https://kvt.tools/price/storereports/kvt.store-status_' \
            + datetime.datetime.today().strftime('%d-%m-%y') + '.xlsx'

# margins:
A4_MARGIN = 1.4
TORG7_MARGIN = 1.35
TORG2_MARGIN = 1.5

# taxes:
NDS = 1.2



