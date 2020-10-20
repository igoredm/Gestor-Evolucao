from dao.xp import XpDao
from utils.images import ImageUtils

class Leaderboard():

  # Method for command STATS
  def get_rank(ctx):
    cursor = XpDao.get_all_ordened()
    top3_list = [c for c in cursor][:3]

    for item in top3_list:
      item['member'] = ctx.message.guild.get_member(int(item['member_id']))

    
    ImageUtils.image_rank(top3_list)

  # Method for command STATS
  def get_stats(ctx, arg):
    position = 1

    if arg:
      if len(arg) > 4:
        id = arg
      else:
        position = int(arg)
        position
        cursor = XpDao.get_all_ordened()
        member_list = [c for c in cursor]
        if len(member_list) < position-1 or position-1 < 0:
          return None, len(member_list)
        else:
          member_data = member_list[position-1]
          member_data['position'] = position
          id = None

    else:
      id = ctx.message.author.id

    if id:
      member_data = XpDao.find_by_member_id(str(id))

      if not member_data:
        XpDao.create_member_register(str(id))
        member_data = XpDao.find_by_member_id(str(id))

      cursor = XpDao.get_all_ordened()

      for item in cursor:
        if item['member_id'] == str(id):
          member_data['position'] = position
        position += 1

    member_data['member'] = ctx.message.guild.get_member(int(member_data['member_id']))
    ImageUtils.image_stats(member_data)
    return member_data['member_id']