from beancount.ingest.importers import ofx

CONFIG = [
    # ofx.Importer(r"78126\-6", "Assets:Bancos:BB", balance_type=ofx.BalanceType.NONE), # tive que alterar aqui para considerar os arquivos ofx que estava baixando do app do BB
    ofx.Importer(r"^78126$", "Assets:Bancos:BB", balance_type=ofx.BalanceType.NONE),
]
