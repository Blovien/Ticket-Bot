from ticketBot.utils import config_setup

message = {}

message['info'] = "Syntax:\n" \
                  "`{prefix}new [message]` \n" \
                  "`{prefix}close [reason]`\n" \
                  "The info can't be longer than 100 characters and not shorter than 10.\n" \
                  "A ticket can only be closed by the author or an admin.\n" \
                  "**Please __don't__ abuse tickets for normal communication or to offend.\n" \
                  "Generally, __think of closing tickets__, when the problem is solved." \
    .replace("{prefix}", config_setup.prefix)

message['help'] = message['info']

message['not_in_channel'] = "Sorry but you can't use the command in this channel"

message['status_1'] = "Create a ticket with {prefix}new".replace("{prefix}", config_setup.prefix)
message['status_2'] = "Type {prefix}new for help".replace("{prefix}", config_setup.prefix)
message['status_3'] = "Bot by Blovien#3637"
