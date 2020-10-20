from discord.ext import commands
from utils.methods import Cooldown, BasicValidation, Playing
from services.xp import Xp
from utils.vars import activities_blacklists

# Class to verify events to give a member Xp
class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Verify when a member send a message (bot and commands not included)
    @commands.Cog.listener()
    async def on_message(self, message):
        if not Cooldown.check_cooldown(message.author.id) and BasicValidation.check_message(message):
            Cooldown.add_cooldown(message.author.id)
            await Xp.add_random_xp(message.author)

    # Verify when a member has a voice state update (like mute, unmute, join channel, etc) (bot not included)
    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if not Cooldown.check_cooldown(member.id) and not BasicValidation.check_bot(member):
            Cooldown.add_cooldown(member.id)
            await Xp.add_random_xp(member)

    # Verify when a member started or stoped an activitie (like play a game) (bot not included)
    @commands.Cog.listener()
    async def on_member_update(self, old_member, new_member):
        if not BasicValidation.check_bot(old_member):
            if Playing.check_playing(old_member.id):
                if str(old_member.status) == "online" and str(old_member.status) != str(new_member.status):
                    minutes_played = Playing.stop_playing(new_member.id)
                    await Xp.add_play_xp(new_member, minutes_played)
                elif old_member.activities and not new_member.activities:
                    minutes_played = Playing.stop_playing(new_member.id)
                    await Xp.add_play_xp(new_member, minutes_played)
            else:
                if new_member.activities:
                    if str(new_member.activities[0].type) != "ActivityType.custom" and not new_member.activities[0].name in activities_blacklists:
                        print(f"\n--> {new_member.name} começou a jogar: {new_member.activities[0].name}")
                        Playing.add_playing(new_member.id)
                else:
                    if str(new_member.status) == "online" and str(old_member.status) != str(new_member.status):
                        if not Cooldown.check_cooldown(new_member.id) and not BasicValidation.check_bot(new_member):
                            Cooldown.add_cooldown(new_member.id)
                            await Xp.add_random_xp(new_member)


def setup(client):
    client.add_cog(Basic(client))
