{
    'name': "BRU - Employee",

    'summary': """ """,

    'description': """

    """,

    'author': "Eduard Ojer",
    'website': "https://www.bru.ac.th/",
    'version': '1.0',

    'depends': [
        'bru_center'
    ],

    'data': [
        'security/employee_security.xml',
        # 'security/ir.model.access.csv',
        'views/bru_employee.xml',
    ],
}