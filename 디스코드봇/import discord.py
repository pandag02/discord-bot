from re import I
from xml.dom.minidom import Identified
import discord
from discord.ext import tasks,commands
from datetime import datetime
import asyncio
import os
import json
from gtts import gTTS

game = discord.Game("집에 보내줘") 
bot_name = "로봇 1호기"
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity = game) 



@bot.event 
async def on_ready():
    print(f'Login bot: {bot.user}')



@bot.command(aliases=['도움말','hint', 'h'])
async def dodo(ctx):
     embed = discord.Embed(title =bot_name, description="추가 자료", color = 0x00ac00)
     embed.add_field(name = "1. 일정시간마다 채팅방에 목표 달성 여부를 물어요", value = "각 목표를 달성해야 하는 방에 알림을 보내드려요!", inline = False)   
     embed.add_field(name = "2. 누른 이모지에 따라 통계를 만들어요", value = "이모티콘은 한번씩만 눌러주세요. 혹시나 실수로 선택이 해제 되었다고 놀라지 마세요. 이미 통계에는 반영 되었답니다. 여러 번 부르면 통계 자료가 이상해질 수 있어요.", inline = False)
     embed.add_field(name = "3. 한달에 한번씩 사용자 전체 통계를 보여줘요", value = "매달 첫번째 주에 이전 달의 통계를 보여줘요.", inline = False)   
     embed.add_field(name = "4. 명령어 입력시 명령 입력한 사람의 통계를 보여줘요", value = "!OOO통계", inline = False)   
     await ctx.send(embed = embed)
  

@tasks.loop(seconds=1)
async def called_once_a_second():
  
  current_time = datetime.now()
  stamp = str(current_time.year)+'.'+str(current_time.month)+'.'+str(current_time.day)

  channel_morning = bot.get_channel(1008778502679568455)
  channel_eat = bot.get_channel(1008778502679568455)
  channel_exercise = bot.get_channel(1008778502679568455)
  channel_study = bot.get_channel(1008778502679568455)
  channel_error = bot.get_channel(1008778502679568455)

  #current_time.hour == 7 and current_time.minute == 0
  if True: 
    
    msg_morning = await channel_morning.send(stamp+' 기상 체크')
    await msg_morning.add_reaction("☀")
    await msg_morning.add_reaction("😪")
    
    msg_study = await channel_eat.send(stamp+' 밥 체크')
    await msg_study.add_reaction("🍚")
    await msg_study.add_reaction("😪")
    
    msg_study = await channel_exercise.send(stamp+' 운동 체크')
    await msg_study.add_reaction("⛳")
    await msg_study.add_reaction("😪")
    
    msg_study = await channel_study.send(stamp+' 공부 체크')
    await msg_study.add_reaction("📚")
    await msg_study.add_reaction("😪")
    
    await asyncio.sleep(15)#seconds*minute*hour
    #60
  
  #current_time.day == 1 and current_time.hour == 0 and current_time.minute == 0
  if True:
   
    await subject_statistics(channel_morning, 'morning')
    await subject_statistics(channel_eat, 'eat')
    await subject_statistics(channel_exercise, 'exercise')
    await subject_statistics(channel_study, 'study')
    
    
    await asyncio.sleep(60)#seconds*minute*hour
      
    
@called_once_a_second.before_loop
async def before():
    await bot.wait_until_ready()
    print("Finished waiting")

called_once_a_second.start()




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
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
            
  if str(reaction.emoji) == "🍚":
    if user.bot == 0:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_user_data(users, user,'eat')
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
            
  if str(reaction.emoji) == "⛳":
    if user.bot == 0:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_user_data(users, user,'exercise')
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
            
  if str(reaction.emoji) == "📚":
    if user.bot == 0:
        with open('users.json', 'r') as f:
            users = json.load(f)
        await add_user_data(users, user,'study')
        with open('users.json', 'w') as f:
            json.dump(users, f, indent=4)
            
  
#처음에 인원을 추가할 때 데이터 자료가 같이 생성되게 만들기 오히려 그게 나을지도..?  

async def add_user_data(users, user,subject):
  if not f'{user.id}' in users:
    await make_user_data(users, user)
      
  users[f'{user.id}'][subject]['year'] += 1
  users[f'{user.id}'][subject]['month'] += 1 
  users[f'{user.id}'][subject]['all'] += 1   
  print(subject+f"{users[f'{user.id}'][subject]}")


async def make_user_data(users, user):  
        users[f'{user.id}']= {}
        users[f'{user.id}']['id']= user.id 
        users[f'{user.id}']['name'] = user.name 
        users[f'{user.id}']['morning'] = {}
        users[f'{user.id}']['morning']['year'] = 0
        users[f'{user.id}']['morning']['month'] = 0 
        users[f'{user.id}']['morning']['all'] = 0
        users[f'{user.id}']['eat'] = {}
        users[f'{user.id}']['eat']['year'] = 0
        users[f'{user.id}']['eat']['month'] = 0 
        users[f'{user.id}']['eat']['all'] = 0
        users[f'{user.id}']['exercise'] = {}
        users[f'{user.id}']['exercise']['year'] = 0
        users[f'{user.id}']['exercise']['month'] = 0 
        users[f'{user.id}']['exercise']['all'] = 0
        users[f'{user.id}']['study'] = {}
        users[f'{user.id}']['study']['year'] = 0
        users[f'{user.id}']['study']['month'] = 0 
        users[f'{user.id}']['study']['all'] = 0

async def subject_statistics(channel_name, subject):
  with open('users.json', 'r') as f:      #저장 파일 출력
    users = json.load(f)
    
  await channel_name.send('!:tada:이번달도 수고했습니다:tada:!')

  for i in range(1, len(users['id'])): 
    print(users['id'][i])
    user_id = users['id'][i]
    try: 
      await channel_name.send(f"{users[user_id]['name']}님은 저번달에 "+f"{users[user_id][subject]['month']}번 목표를 달성하였어요.")
      await reset_month(user_id, users, subject)
    except KeyError as e:
      print("id는 입력 되었지만 활동 없는 유저 존재: "+user_id)
      pass
    
  with open('users.json', 'w') as f: 
      json.dump(users, f, indent=4)  
  

async def reset_month(user_id, users, subject):
  user_id = (user_id)
  users[f'{user_id}'][subject]['month'] = int(0)


  
@bot.command(aliases = ['잠자기통계']) #command 함수, def hello는 #hello를 대화창에 입력 시 실행
async def jamjagiCheugjeongHwagIn(ctx):
    with open('users.json', 'r') as f:
      users = json.load(f)
    with open('users.json', 'w') as f: ####위에 이거 없으니까 실시간 반영이 안되네 신기방기
      json.dump(users, f, indent=4)
    sleeping = (f"{users[f'{ctx.message.author.id}']['morning']['month']}")
    msg = await ctx.send(":tada:"+f'{ctx.author.mention}님은 이번달 잠자기 목표를 '+sleeping+"번 지켰어요:tada:")  #채팅창에 Hi! 입력

@jamjagiCheugjeongHwagIn.error
async def jamjagiCheugjeongHwagIn_error(ctx,error):
     await ctx.send('!명령어 오류!')
     channel_error = bot.get_channel(1008778502679568455)
     await channel_error.send('잠자기통계 명령어 오류')
     print('잠자기통계 명령어 오류')
     pass
         

@bot.command(aliases = ['밥통계']) #command 함수, def hello는 #hello를 대화창에 입력 시 실행
async def bobHwagIn(ctx):
    with open('users.json', 'r') as f:
      users = json.load(f)
    with open('users.json', 'w') as f: ####위에 이거 없으니까 실시간 반영이 안되네 신기방기
      json.dump(users, f, indent=4)
    bob = (f"{users[f'{ctx.message.author.id}']['eat']['month']}")
    msg = await ctx.send(":tada:"+f'{ctx.author.mention}님은 이번달 밥 먹기 목표를 '+bob+"번 지켰어요:tada:")  #채팅창에 Hi! 입력

@bobHwagIn.error
async def bobHwagIn_error(ctx,error):
     await ctx.send('!명령어 오류!')
     channel_error = bot.get_channel(1008778502679568455)
     await channel_error.send('밥통계 명령어 오류')
     print('밥통계 명령어 오류')
     pass
   
   
@bot.command(aliases = ['운동통계']) #command 함수, def hello는 #hello를 대화창에 입력 시 실행
async def undongHwagIn(ctx):
    with open('users.json', 'r') as f:
      users = json.load(f)
    with open('users.json', 'w') as f: ####위에 이거 없으니까 실시간 반영이 안되네 신기방기
      json.dump(users, f, indent=4)
    work = (f"{users[f'{ctx.message.author.id}']['exercise']['month']}")
    msg = await ctx.send(":tada:"+f'{ctx.author.mention}님은 이번달 운동 목표를 '+work+"번 지켰어요:tada:")  #채팅창에 Hi! 입력

@undongHwagIn.error
async def undongHwagIn_error(ctx,error):
     await ctx.send('!명령어 오류!')
     channel_error = bot.get_channel(1008778502679568455)
     await channel_error.send('운동통계 명령어 오류')
     print('운동통계 명령어 오류')
     pass
    
    
@bot.command(aliases = ['공부통계']) #command 함수, def hello는 #hello를 대화창에 입력 시 실행
async def gongbuHwagIn(ctx):
    with open('users.json', 'r') as f:
      users = json.load(f)
    with open('users.json', 'w') as f: ####위에 이거 없으니까 실시간 반영이 안되네 신기방기
      json.dump(users, f, indent=4)
    study = (f"{users[f'{ctx.message.author.id}']['study']['month']}")
    msg = await ctx.send(":tada:"+f'{ctx.author.mention}님은 이번달 공부 목표를 '+study+"번 지켰어요:tada:")  #채팅창에 Hi! 입력

@gongbuHwagIn.error
async def gongbuHwagIn_error(ctx,error):
     await ctx.send('!명령어 오류!')
     channel_error = bot.get_channel(1008778502679568455)
     await channel_error.send('공부통계 명령어 오류')
     print('공부통계 명령어 오류')
     pass
    

@bot.command(aliases = ['인원추가']) #command 함수, def hello는 #hello를 대화창에 입력 시 실행
async def inwonchuga(ctx, arg):
    with open('users.json', 'r') as f:
      users = json.load(f)
    
    if not 'id' in users:
      users["id"]= ['None']
      
    uid = str(arg)
    users['id'] += [uid]        #18글자[uid] 괄호 없으면 하나씩 받아드림
    print(users['id'])   

    with open('users.json', 'w') as f: ####위에 이거 없으니까 실시간 반영이 안되네 신기방기
      json.dump(users, f, indent=4)
  
@inwonchuga.error
async def inwonchuga_error(ctx,error):
     await ctx.send('!명령어 오류!')
     print('인원추가 명령어 오류')
     pass


bot.run('') #토큰값 입력

