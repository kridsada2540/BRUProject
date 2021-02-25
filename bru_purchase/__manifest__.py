{
    'name': "BRU - Purchase",

    'summary': """ """,

    'description': """

    """,

    'author': "Eduard Ojer",
    'website': "https://www.bru.ac.th/",
    'version': '1.0',

    'depends': [
        'bru_employee',
    ],

    'data': [
        'security/purchase_security.xml',
        'security/ir.model.access.csv',
        'data/purchase_sequence.xml',
        'views/bru_purchase.xml',
        'views/purchase_request_tree.xml',
        # 'views/purchase_button.xml',

    ],
}