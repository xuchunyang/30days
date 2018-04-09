from configparser import ConfigParser

CONFIGFILE = "foo.ini"

config = ConfigParser()
config.read(CONFIGFILE)

print(config["user"]["username"])
print(config["user"]["email"])
print(config["database"]["path"])
