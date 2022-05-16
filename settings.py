from os import environ

SESSION_CONFIGS = [
    dict(
        name='pooled_all',
        display_name="Pooled - All Apps",
        num_demo_participants=4,
        app_sequence=['pooled_contest'],
        tickets_per_point_A=20,
        tickets_per_point_B=10,
        exchange_rate=10,
        endowment=100,
    ),
    dict(
        name='pooled_homo',
        display_name="Pooled - Homo",
        num_demo_participants=4,
        app_sequence=['pooled_homo'],
        tickets_per_point_A=10,
        tickets_per_point_B=10,
        exchange_rate=10,
        endowment=100,
    ),
    dict(
        name='prodem_contest',
        display_name="Prodem - All Apps",
        num_demo_participants=4,
        app_sequence=['prodem_contest'],
        tickets_per_point_A=20,
        tickets_per_point_B=10,
        exchange_rate=10,
        endowment=100,
    ),
    dict(
        name='prodem_homo',
        display_name="Prodem - Homo",
        num_demo_participants=4,
        app_sequence=['prodem_homo'],
        tickets_per_point_A=10,
        tickets_per_point_B=10,
        exchange_rate=10,
        endowment=100,
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = 'iq*wislsw2@1inesa@d2f3f*#^zpl*bwizx$$@vkz-weq&l@0#'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
