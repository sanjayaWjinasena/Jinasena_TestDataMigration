# -*- coding: utf-8 -*-
{
    'name': 'Jinasena : Data : TestDataMigration',
    'version': '17.0.0.0.3',
    'summary': (
        'Runtime data migrations for test envs — one-shot patches to '
        'existing records that a source-code change cannot reach '
        '(e.g. noupdate=1 records already loaded, or DB-only Studio '
        'artefacts). Never a home for missing/wrong module data — '
        'that belongs in the respective source repo.'
    ),
    'description': """
Jinasena : Data : TestDataMigration
====================================

Only for **runtime data migrations** — one-off record fixes on
existing envs that a companion-module code change cannot apply
(e.g., ``noupdate="1"`` records that were already loaded, DB-only
Studio residue, etc.).

If a fix is "the module should have shipped X but didn't", ship X
from the module's source repo. Do NOT put it here.

Currently empty — kept as scaffolding for future real migrations.
""",
    'author': 'Jinasena Agricultural Machinery (Pvt) Ltd.',
    'category': 'Extra Tools',
    'license': 'LGPL-3',
    'depends': [
        'BugFix-Purchase',
        'BugFix-Studio-Misc',
    ],
    'data': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
