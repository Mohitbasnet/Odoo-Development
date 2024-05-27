{
    "name": "Real Estate Ads",
    "version": "1.0",
    "website": "https://www.mohitbasnet.com",
    "author": "Mohit",
    "description": "Nothing to say",
    "license": "LGPL-3",
    "category": "Sales",
    "application": True,
    "installable": True,
    "depends": ['base','mail'],
    "data": [
        "security/ir.model.access.csv",
        "security/res_groups.xml",
        "security/model_access.xml",
        
        "views/property_type.xml",
        
        "views/property_tag.xml",
        "views/property_view.xml",
        "views/property_offer_view.xml",
         "views/menu_items.xml",
         "report/property_report.xml",
         "report/report_template.xml",

        
        # "data/property_type.xml",
        "data/estate.property.type.csv"
    ],
     'assets': {
        'web.assets_backend': [
            'real_estate_ads/static/src/js/my_custom_tag.js',
            'real_estate_ads/static/src/xml/my_custom_tag.xml',
        ]
    },
    "demo": [
        "demo/property_tag.xml"
    ],


}
