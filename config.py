from beancount.ingest.importers import ofx

CONFIG = [
    ofx.Importer(r"78126\-6", "Assets:Bancos:BB", balance_type=ofx.BalanceType.NONE),
]
