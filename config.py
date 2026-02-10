from beancount.ingest.importers import ofx

CONFIG = [
    ofx.Importer(r"^78126$", "Assets:Bancos:BB", balance_type=ofx.BalanceType.NONE), # Há versões que no arquivo ofx do app do BB está com o dígito 6: "78126\-6"
]
