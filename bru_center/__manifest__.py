{
    'name': "BRU - Center",

    'summary': """ """,

    'description': """

    """,

    'author': "Eduard Ojer",
    'website': "https://www.bru.ac.th/",
    'version': '1.0',

    'depends': [
        'base',
        'purchase',
        'hr',
        'stock',
        'sale',
    ],

    'data': [
        'security/bru_center_security.xml',
        'security/ir.model.access.csv',
        'views/bru_base.xml',
        'views/bru_branch.xml',
        'views/bru_budget.xml',
        'views/type_product.xml',
        # 'views/faculty_branch.xml',
    ],
}