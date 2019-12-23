# See LICENSE file for full copyright and licensing details.
{
    "name": "Mass Label Reporting",
    "version": "12.0.1.0.0",
    "category": "Tools",
    "license": "AGPL-3",
    "summary": "Generate customised labels of any document",
    "author": 'NDS4IT-Ali Elgarhi',
    "website": "http://www.nds4it.com",
    "maintainer": 'Ali Elgarhi',
    'depends': ['base'],
    'data': [
        'data/report_paperformat.xml',
        'security/label.brand.csv',
        'security/label.config.csv',
        'security/ir.model.access.csv',
        'views/label_config_view.xml',
        'views/label_print_view.xml',
        'views/label_size_data.xml',
        'wizard/label_print_wizard_view.xml',
        'views/label_report.xml',
        'report/dynamic_label.xml'
    ],
    'uninstall_hook': 'uninstall_hook',
    'images': ['static/description/logo.png'],
    'installable': True,
    'auto_install': False,
}
