{
    'name': "BRU - Stock",

    'summary': """ """,

    'description': """

    """,

    'author': "Eduard Ojer",
    'website': "https://www.bru.ac.th/",
    'version': '1.0',

    'depends': [
        'bru_center',
        'bru_purchase',
    ],

    'data': [
        'security/inventory_security.xml',
        'security/ir.model.access.csv',
        'views/bru_stock.xml',
        'views/bru_stock_tree.xml',
        'reports/report.xml',
        'reports/report_inventory.xml',
    ],
}