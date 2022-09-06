

@tasks.loop(minutes=1)
async def called_once_a_day():
    message_channel = bot.get_channel(1008778502679568455)
    await message_channel.send("Your message")
    current_time = datetime.now()
    print(current_time)
    print(f'Year : {current_time.year}')
    print(f'Month : {current_time.month}')
    print(f'Day : {current_time.day}')
    print(f'Hour : {current_time.hour}')
    print(f'Minute : {current_time.minute}')
    print(f'Second : {current_time.second}')
    
    if current_time.hour == 13 and current_time.minute == 55:
      print("일어나")
      

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()











@tasks.loop(hours=24)
async def called_once_a_day():
    message_channel = bot.get_channel(1008778502679568455)
    print(f"Got channel {message_channel}")
    await message_channel.send("Your message")

@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()
  
  
  
  
  
  @bot.event 
async def message_loop():
  await bot.wait_until_ready()
  while not bot.is_closed():
    current_time = datetime.now()
    print(current_time)
    print(f'Day : {current_time.day}')
    print(f'Hour : {current_time.hour}')
    print(f'Minute : {current_time.minute}')
    print(f'Second : {current_time.second}')
    if current_time.hour == 7:  
      channel_morning = bot.get_channel(1008778502679568455)
      msg_morning = await channel_morning.send('오늘 잘 일어났나요?')
      await msg_morning.add_reaction("☀")
      await msg_morning.add_reaction("😪")
      await asyncio.sleep(60*60*1)#seconds*minute*hour
bot.loop.create_task(message_loop())















@tasks.loop(seconds=1)
async def called_once_a_day():
  current_time = datetime.now()
  stamp = str(current_time.year)+'.'+str(current_time.month)+'.'+str(current_time.day)
  if current_time.hour == 15 and current_time.minute == 7:  
    channel_morning = bot.get_channel(1008778502679568455)
    
    msg_morning = await channel_morning.send(stamp+' 기상여부 체크')
    await msg_morning.add_reaction("☀")
    await msg_morning.add_reaction("😪")
    
    channel_study = bot.get_channel(1008778502679568455)
    msg_study = await channel_study.send(stamp+' 공부여부 체크')
    await msg_study.add_reaction("📚")
    await msg_study.add_reaction("😪")
    
    await asyncio.sleep(70)#seconds*minute*hour
    
@called_once_a_day.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_day.start()



@bot.event
async def on_reaction_add(reaction, user):
    if user.bot == 1: #봇이면 패스
        return None
      
    if str(reaction.emoji) == "😀":
        await reaction.message.channel.send(user.name + "님이 좋다니 다행이에요")
        
        
    if str(reaction.emoji) == "😪":
        await reaction.message.channel.send(user.name + "님이 슬프다니 무슨 일이에요?")





##### START LEVEL COMMAND #####
 
with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 
@bot.event    
async def on_message(message):
    if message.author.bot == False:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, message.author)
        await level_up(users, message.author, message)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            await bot.process_commands(message)
 
async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 6
  print(f"{users[f'{user.id}']['level']}")
 
async def level_up(users, user, message):
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await message.channel.send(f':tada: {user.mention} has reached level {lvl_end}. Congrats! :tada:')
    users[f'{user.id}']["level"] = lvl_end
 
@bot.command()
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    await ctx.send(f'{ctx.author.mention} You are at level {userlvl}!')
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} is at level {userlvl2}!')
 
##### END LEVEL COMMAND #####





##### START LEVEL COMMAND #####
 
with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 
@bot.event    
async def on_reaction_add(reaction, user):
  
  if str(reaction.emoji) == "☀":
    if user.bot == 0:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_experience(users, user)
        await level_up(users, user)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            

async def add_experience(users, user):
  if not f'{user.id}' in users:
        users[f'{user.id}'] = {}
        users[f'{user.id}']['experience'] = 0
        users[f'{user.id}']['level'] = 0
  users[f'{user.id}']['experience'] += 6
  print(f"{users[f'{user.id}']['level']}")
 
async def level_up(users, user):
  channel_morning = bot.get_channel(1008778502679568455)
  experience = users[f'{user.id}']["experience"]
  lvl_start = users[f'{user.id}']["level"]
  lvl_end = int(experience ** (1 / 4))
  if lvl_start < lvl_end:
    await channel_morning.send(f':tada: {user.mention} has reached level {lvl_end}. Congrats! :tada:')
    users[f'{user.id}']["level"] = lvl_end
 
@bot.command()
async def rank(ctx, member: discord.Member = None):
  if member == None:
    userlvl = users[f'{ctx.author.id}']['level']
    await ctx.send(f'{ctx.author.mention} You are at level {userlvl}!')
  else:
    userlvl2 = users[f'{member.id}']['level']
    await ctx.send(f'{member.mention} is at level {userlvl2}!')
 
##### END LEVEL COMMAND #####




##### START LEVEL COMMAND #####
 
with open("users.json", "ab+") as ab:
    ab.close()
    f = open('users.json','r+')
    f.readline()
    if os.stat("users.json").st_size == 0:
      f.write("{}")
      f.close()
    else:
      pass
 
with open('users.json', 'r') as f:
  users = json.load(f)
 
@bot.event    
async def on_reaction_add(reaction, user):
  
  if str(reaction.emoji) == "☀":
    if user.bot == 0:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_user_data(users, user,'morning')
        await achievement_rate(users, user)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            
  if str(reaction.emoji) == "📚":
    if user.bot == 0:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_user_data(users, user,'study')
        await achievement_rate(users, user)
        with open('users.json', 'w') as f:
            json.dump(users, f)
            

async def add_user_data(users, user,subject):
  if not f'{user.id}' in users:
        await make_user_data(users, user)  
  users[f'{user.id}'][subject]['year'] += 1
  users[f'{user.id}'][subject]['month'] += 1 
  users[f'{user.id}'][subject]['all'] += 1   
  print(f"{users[f'{user.id}'][subject]}")

  
async def make_user_data(users, user):  
        users[f'{user.id}'] = {}
        users[f'{user.id}']['morning'] = {}
        users[f'{user.id}']['morning']['year'] = 0
        users[f'{user.id}']['morning']['month'] = 0 
        users[f'{user.id}']['morning']['all'] = 0
        users[f'{user.id}']['study'] = {}
        users[f'{user.id}']['study']['year'] = 0
        users[f'{user.id}']['study']['month'] = 0 
        users[f'{user.id}']['study']['all'] = 0  
 
 
async def achievement_rate(users, user):
  morning = users[f'{user.id}']["morning"]
  
  

##### END LEVEL COMMAND #####




user_id_all = [365136831383076874]
user_id = [365136831383076874]  
async def add_user_data(users, user,subject):
  if not f'{user.id}' in users:
        await make_user_data(users, user)  
  users[f'{user.id}'][subject]['year'] += 1
  users[f'{user.id}'][subject]['month'] += 1 
  users[f'{user.id}'][subject]['all'] += 1   
  print(subject+f"{users[f'{user.id}'][subject]}")
  user_id_all.append(str(f"{users[f'{user.id}']['id']}"))
  result1 = set(user_id_all)
  user_id = list(result1)
  print(*user_id)