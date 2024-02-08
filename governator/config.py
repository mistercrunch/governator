from os import environ

config_defaults = {
    "GOVERNATOR_FOLDER": "/tmp/allstars",
    "GOVERNATOR_SQLA_CONN": "mysql://",
    "GOVERNATOR_PROJECT": "jaffleshop",
}

conf = {}

for k in config_defaults.keys():
    if k in environ and environ.get(k):
        conf[k] = environ.get(k)
    else:
        conf[k] = config_defaults[k]
