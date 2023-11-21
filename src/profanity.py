from better_profanity import profanity
import asyncio
from datetime import timedelta
import discord
import db

profanity.load_censor_words()
custom_words = []
###########################
# Function: check_profanity
# Description: Uses better_profanity to check profanity in a message
# Inputs:
#      - msg: message from user
###########################
def check_profanity(msg):
    ''' check if message contains profanity through profanity module '''
    if msg in custom_words:
        return True

    return profanity.contains_profanity(msg)

###########################
# Function: censor_profanity
# Description: censor the message per better_profanity
# Inputs:
#      - msg: message from user
###########################
def censor_profanity(msg):
    ''' take action on the profanity by censoring it '''
    if msg in custom_words:
        msg = '****'
    return profanity.censor(msg)

BOT = None
###########################
# Function: set
# Description: prompts the instructor to set the profanity settings
# Inputs:
#      - ctx: the context of the channel we are on
###########################
async def set(ctx):
    if ctx.channel.name == 'instructor-commands':
        # only run in the instructor command channel
        await ctx.send('How many messages should a user be able to send before they are muted due '
                       'usage of profanity?')
        try:
            msg = (await BOT.wait_for('message', timeout=60.0, check=lambda x: x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content
            msg = int(msg)
            msg_warn_num = msg
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        await ctx.send('How many messages containing profanity should a user be able to send before they are put in '
                       'timeout?')
        try:
            msg_timeout_num = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content)
        except:
            await ctx.send('Invalid entry. Try again...')
            return
        await ctx.send('How long should a user be placed in timeout when caught spamming? '
                        'Format: min,hours,days Example: 5,0,0 is 5 minutes')
        try:
            msg_timeout_time = (await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content
            timeout_time = msg_timeout_time.split(',')
            minutes = int(timeout_time[0])
            hours = int(timeout_time[1])
            days = int(timeout_time[2])
            timedelta(seconds=0, minutes=minutes, hours=hours, days=days)
        except:
            await ctx.send('Invalid entry. Try again...')
            return
        
        await ctx.send('How many messages containing profanity should a user be able to send before they are'
                       'kicked out?')
        try:
            msg_kicked_num = int((await BOT.wait_for('message', timeout=60.0, check=lambda x:
            x.channel.name ==
                'instructor-commands' and x.author.id != BOT.user.id)).content)
        except:
            await ctx.send('Invalid entry. Try again...')
            return

        db.mutation_query(
            'UPDATE profanity_settings SET warning_num = ?, timeout_num = ?, timeout_min = ?, '
            'timeout_hour = ?, timeout_day = ?, time_between_clears = ?',
            [msg_warn_num, msg_timeout_num, int(timeout_time[0]), int(timeout_time[1]),
             int(timeout_time[2]), msg_kicked_num]
        )
        await ctx.send('Profanity Settings successfully updated!')
    else:
        await ctx.author.send('`!set_profanity_settings` can only be used in the `instructor-commands` '
                              'channel')
        await ctx.message.delete()
