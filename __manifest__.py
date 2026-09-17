# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Data : TestDataMigration',
    'version': '17.0.0.0.1',
    'summary': (
        'Cross-module data patches applied on top of the companion '
        'modules. Loads AFTER all companion modules so its records '
        'override incorrect defaults — display names, rule group '
        'scopes, action names, orphan cleanup. Test-env fixes only; '
        'never ship to production without review.'
    ),
    'description': """
Jinasena : Data : DataMigration
================================

Companion-module source repos are kept clean. Any *test-env-only* data
corrections that we discover while smoke-testing installs land here:

* model display name overrides (``<record model="ir.model">`` with new
  ``name``)
* record-rule group-scope restorations
* server-action name renames
* orphan-record deletions

Files are organised by target module in ``data/``. Each file starts
with a comment header stating (a) the model / area it touches,
(b) the reason for the patch, (c) the RPC verification it was written
against.

**Load order:** this module depends on every companion module, so
Odoo's dependency graph guarantees every record referenced here
exists before we patch it.
""",
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'BugFix-Purchase',
        'BugFix-Studio-Misc',
    ],
    'data': [
        'data/purchase_x_purchase_request.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
