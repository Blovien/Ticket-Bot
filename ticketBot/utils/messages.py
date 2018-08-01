from ticketBot.utils import config_setup

message = {}

message['info'] = "Syntax:\n" \
                    "`{prefix}new ` \n" \
                    "`{prefix}close [] [reason]`\n" \
                    "`{prefix}ticket close [ticket number]; [reason]`\n" \
                    "The info can't be longer than 100 characters and not shorter than 10.\n" \
                    "A ticket can only be closed by the author or an admin.\n" \
                    "**Please __don't__ abuse tickets for normal communication or to offend.\n" \
                    "It's allowed to create one or two test tickets, " \
                    "but you have to __delete them__ after one day at the latest.**\n" \
                    "Generally, __think of closing tickets__, when the problem is solved.".replace("{prefix}", config_setup.prefix)

message['help'] = message['info']

message['not_in_channel'] = "Sorry but you can't use the command in this channel"

