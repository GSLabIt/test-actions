import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-test-ci",
    description="Meta package for test-ci addons",
    version=version,
    install_requires=[
        'odoo12-addon-l10n_it_fatturapa_in',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
