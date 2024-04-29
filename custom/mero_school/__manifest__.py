{
    'name': 'School management',
    'author':'Mohit Basnet',
    'website': 'www.meroschool.com',
    'summary':'This is our school management system',
    'depends':['mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'views/teacher.xml',
        'views/menu.xml',
        'views/student.xml',
       
    ],
    'application':True,
    'installable':True,
}