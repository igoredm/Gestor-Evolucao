from dao.xp import XpDao
import random
from app import discord
from app import client


class Xp():
    # add random xp to member in action 
    async def add_random_xp(member):
        id = member.id
        member_data = UtilsXp.get_member_data(id)

        add = int(random.random() * 15) + 10

        await UtilsXp.give_member_xp(member_data, add, member)
    
    # add minute played * 0.5 xp to member  
    async def add_play_xp(member, minutes_played):
        id = member.id
        member_data = UtilsXp.get_member_data(id)

        add = int(0.5 * minutes_played)
        print(f"--> {member.name} parou de jogar, tempo jogado: {minutes_played}, XP: {add} \n")

        await UtilsXp.give_member_xp(member_data, add, member)

# Utils methods for class Xp
class UtilsXp():
    def get_member_data(id):
        data = XpDao.find_by_member_id(str(id))
        if data:
            del data['_id']
            data['member_id'] = int(data['member_id']) 
            return data
        else:
            XpDao.create_member_register(str(id))
            return {'member_id': id, 'xp': 0, 'level': 0}

    async def give_member_xp(member_data, add, member):

        boost_role = discord.utils.get(
            member.guild.roles, id=659128728323883030)

        if boost_role in member.roles:
            old_add = add
            add *= 2
            print("Membro é booster, então xp foi de: " +
                  old_add + "para: " + add)

        member_data['xp'] += add

        n = member_data['level'] + 1
        next_level_xp = int(5 * (n ** 2) + 50 * n + 100)

        if member_data['xp'] >= next_level_xp:
            member_data['level'] += 1
            member_data['xp'] -= next_level_xp
            await UtilsXp.update_roles(member_data['level'], member)

        update_data = member_data
        update_data['member_id'] = str(update_data['member_id'])
        XpDao.update_xp(update_data)

    async def update_roles(level, member):
        if level == 1:
            await client.get_channel(567034199102718000).send(f"{member.mention} Você chegou no level 1, mas sua jornada está só começando! Bora juntar uns xpzinhos ai")
        elif level == 5:
            await member.add_roles(discord.utils.get(member.guild.roles, id=399279993454329867))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=347480297257828363))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Assistênte")
        elif level == 10:
            await member.add_roles(discord.utils.get(member.guild.roles, id=347479905010712576))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=399279993454329867))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Funcionário")
        elif level == 25:
            await member.add_roles(discord.utils.get(member.guild.roles, id=347480246817259520))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=347479905010712576))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Supervisor")
        elif level == 40:
            await member.add_roles(discord.utils.get(member.guild.roles, id=399279845277696001))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=347480246817259520))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Gerente")
        elif level == 60:
            await member.add_roles(discord.utils.get(member.guild.roles, id=399279475503923203))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=399279845277696001))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Diretor")
        elif level == 85:
            await member.add_roles(discord.utils.get(member.guild.roles, id=546723365721735180))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=399279475503923203))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Vice-Presidente")
        elif level == 120:
            await member.add_roles(discord.utils.get(member.guild.roles, id=546723525118001172))
            await member.remove_roles(discord.utils.get(member.guild.roles, id=546723365721735180))
            await client.get_channel(567034199102718000).send(f"{member.mention} Você foi promovido para: Presidente")
