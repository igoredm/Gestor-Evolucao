from PIL import Image, ImageFont, ImageDraw
import requests
from io import BytesIO


class ImageUtils():
  def image_stats(member_data):
    # Member details (fixed at moment)
    level = member_data['level']
    xp = member_data['xp']
    position = member_data['position']
    name = member_data['member'].display_name.upper()



    next_level = level + 1
    xp_to_next_level = int((5 * (next_level ** 2) + 50 * next_level + 100))
    rgb, cargo = ImageUtils.get_cargo_rgb(level)

    # opening background image
    img = Image.open("./assets/img/in/card.png")
    draw = ImageDraw.Draw(img)

    # opening font
    font_path = "./assets/font/splatch.ttf"

    # add "cargo" to image
    font = ImageFont.truetype(font_path, 15)
    draw.text((240, 211), "CARGO:", font=font)
    font = ImageFont.truetype(font_path, 35)
    draw.text((353, 175), f"{cargo}", rgb, font=font)


    # add member name to image
    if len(name) > 11:
      font = ImageFont.truetype(font_path, 20)
      draw.text((240, 56), f"< {name.upper()} >", font=font)
    else:
      font = ImageFont.truetype(font_path, 25)
      draw.text((240, 56), f"< {name.upper()} >", font=font)

    # add position
    font = ImageFont.truetype(font_path, 15)
    draw.text((590, 60), "POS:", font=font)
    font = ImageFont.truetype(font_path, 35)
    draw.text((650, 30), f"{position}", rgb, font=font)

    # add level 
    font = ImageFont.truetype(font_path, 15)
    draw.text((750, 60), "LVL:", font=font)
    font = ImageFont.truetype(font_path, 35)
    draw.text((800, 30), f"{level}", rgb, font=font)

    # add xp and xp to next level
    font = ImageFont.truetype(font_path, 15)
    draw.text((680, 130), f"XP: {xp}/{xp_to_next_level}", font=font)

    size = 190, 190
    profile = ImageUtils.get_profile_image(member_data['member'].avatar_url_as(format='png', size=1024), size)
    try:
      img.paste(profile, (35,47), mask=profile)
    except:
      img.paste(profile, (35,47))


    member_id = member_data['member_id']
    img.save(f'./assets/img/out/stats_{member_id}.png')


  def image_rank(members):

    # open default podium image
    img = Image.open("./assets/img/in/podium.png")
    draw = ImageDraw.Draw(img)

    # Get font from assets path
    font_path = "./assets/font/splatch.ttf"

    size = 128, 128

    # details from member in 1st position
    # name
    font = ImageFont.truetype(font_path, 25)
    name = members[0]['member'].display_name.upper()
    draw.text((25,15), f"1: {name}", (255, 215, 0), font=font)
    # level
    font = ImageFont.truetype(font_path, 15)
    level = members[0]['level']
    draw.text((420,25), f"LVL: {level}", (255, 215, 0), font=font)
    # profile pic
    profile = ImageUtils.get_profile_image(members[0]['member'].avatar_url_as(format='png', size=1024), size)
    try:
      # try paste a no background image 
      img.paste(profile, (195,215), mask=profile)
    except:
      # paste a background image
      img.paste(profile, (195,215))


    # details from member in 2st position
    # name
    font = ImageFont.truetype(font_path, 20)
    name = members[1]['member'].display_name.upper()
    draw.text((27,70), f"2: {name}", (192, 192, 192), font=font)
    # level
    font = ImageFont.truetype(font_path, 12)
    level = members[1]['level']
    draw.text((420,75), f"LVL: {level}", (192, 192, 192), font=font)
    # profile pic
    profile = ImageUtils.get_profile_image(members[1]['member'].avatar_url_as(format='png', size=1024), size)
    try:
      # try paste a no background image 
      img.paste(profile, (365,330), mask=profile)
    except:
      # paste a background image
      img.paste(profile, (365,330))


    # details from member in 3st position
    # name
    font = ImageFont.truetype(font_path, 15)
    name = members[2]['member'].display_name.upper()
    draw.text((29,120), f"3: {name}", (196, 156, 72), font=font)
    # level
    font = ImageFont.truetype(font_path, 9)
    level = members[2]['level']
    draw.text((420,125), f"LVL: {level}", (196, 156, 72), font=font)
    # profile pic
    profile = ImageUtils.get_profile_image(members[2]['member'].avatar_url_as(format='png', size=1024), size)
    try:
      # try paste a no background image 
      img.paste(profile, (25,375), mask=profile)
    except:
      # paste a background image
      img.paste(profile, (25,375))

    # save rank image 
    img.save('./assets/img/out/rank.png')
  
  def get_profile_image(url, size):
    if url:
      response = requests.get(url)
      profile = Image.open(BytesIO(response.content))
    else:
      profile = Image.open("./assets/img/in/profile.png")

    profile.thumbnail(size)
    return profile

  def get_cargo_rgb(level):
    rgb = (250, 0, 227)
    cargo = "ESTAGIARIO"
    if level >= 5 and level < 10:
      rgb = (248, 177, 232)
      cargo = "ASSISTENTE"
    elif level >= 10 and level < 25:
      rgb = (124, 0, 252)
      cargo = "FUNCIONARIO"
    elif level >= 25 and level < 40:
      rgb = (46, 204, 113)
      cargo = "SUPERVISOR"
    elif level >= 40 and level < 60:
      rgb = (231, 76, 60)
      cargo = "GERENTE"
    elif level >= 60 and level < 85:
      rgb = (26, 188, 156)
      cargo = "DIRETOR"
    elif level >= 85 and level < 120:
      rgb = (52, 152, 219)
      cargo = "VICE-PRESIDENTE"
    elif level >= 120:
      rgb = (0, 252, 255)
      cargo = "PRESIDENTE"

    return rgb, cargo
    
