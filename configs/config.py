import datetime
from configs.config_worker import ConfigReader
from parsers.headers import Headers


# Settings file
SETTINGS_JSON = r'C:\Users\OperTech\pythonProject\IvanCRM\configs\settings_parser.json'
cr = ConfigReader()
# PASSPORT PROTECTION CONFIGS
PASSPORT_FILE_TYPES = '*.doc *.pdf'
PRICE_FILE_TYPES = '*.xls *.xlsx *.csv *.xml'
PHOTO_LIST_FILE_TYPES = '*.xls *.xlsx *.csv'
STATUS_ADDED = 'Добавлен'
STATUS_PROCESSING = 'Обработка'
STATUS_READY = 'Готов'
# STATUSES
STATUS_PROCESSING_COLOR = '#FFFF00'
STATUS_READY_COLOR = '#33FF33'
STATUS_NONE_COLOR = '#FFFFFF'
STATUS_ERROR_COLOR = '#FF0000'
QLINEEDIT_STYLE_PROCESSING_COLOR = 'QLineEdit {background: ' + STATUS_PROCESSING_COLOR + ';}'
QLINEEDIT_STYLE_READY_COLOR = 'QLineEdit {background: ' + STATUS_READY_COLOR + ';}'
QLINEEDIT_STYLE_ERROR_COLOR = 'QLineEdit {background: ' + STATUS_ERROR_COLOR + ';}'
# PARSER CONFIGS
# combobox values for supplier parsing
SUPPLIERS = cr.get_supplier_names()

# Supplier names
KVT_NAME = cr.get_supplier_name('KVT_NAME')
N1_NAME = cr.get_supplier_name('N1_NAME')
P1_NAME = cr.get_supplier_name('P1_NAME')
TORG2_NAME = cr.get_supplier_name('TORG2_NAME')
TORG7_NAME = cr.get_supplier_name('TORG7_NAME')
YU1_NAME = cr.get_supplier_name('YU1_NAME')
A4_NAME = cr.get_supplier_name('A4_NAME')
VOID_NAME = cr.get_supplier_name('VOID_NAME')

# Supplier links to price-file
A4_LINK = cr.get_supplier_link(A4_NAME)
TOG7_LINK = cr.get_supplier_link(TORG7_NAME)
KVT_LINK = cr.get_supplier_link(KVT_NAME) + datetime.datetime.today().strftime('%d-%m-%y') + '.xlsx'

# Margins:
A4_MARGIN = cr.get_supplier_margin(A4_NAME)
TORG7_MARGIN = cr.get_supplier_margin(TORG7_NAME)
TORG2_MARGIN = cr.get_supplier_margin(TORG7_NAME)
YU1_MARGIN = cr.get_supplier_margin(YU1_NAME)
P1_MARGIN = cr.get_supplier_margin(P1_NAME)
N1_MARGIN = cr.get_supplier_margin(N1_NAME)

# taxes:
NDS = cr.get_taxes('NDS')

# exceptions
TORG2_EXCEPTIONS_BRANDS = cr.get_supplier_exception_brands(TORG2_NAME)

# needful products
YU1_NEEDFUL_BRANDS = cr.get_supplier_needful_brands(YU1_NAME)
P1_NEEDFUL_BRANDS = cr.get_supplier_needful_brands(P1_NAME)
N1_NEEDFUL_BRANDS = cr.get_supplier_needful_brands(N1_NAME)

# Supplier headers
KVT_HEADERS = Headers(KVT_NAME)
N1_HEADERS = Headers(N1_NAME)
P1_HEADERS = Headers(P1_NAME)
TORG2_HEADERS = Headers(TORG2_NAME)
TORG7_HEADERS = Headers(TORG7_NAME)
YU1_HEADERS = Headers(YU1_NAME)
A4_HEADERS = Headers(A4_NAME)
VOID_HEADERS = Headers(VOID_NAME)

