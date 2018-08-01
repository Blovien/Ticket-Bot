import yaml

# Load config.yml from configuration folder
data = yaml.load(open("configuration/config.yml", 'r'))

"""
Give bot's token key in config.yml
example: token: 123
"""
token = data['token']

"""
Give bot's command prefix in config.yml
"""
prefix = data['prefix']

"""
Give ticket channel in config.yml
"""
ticket_channel = data['ticket-channel']