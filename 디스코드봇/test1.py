import discord
from discord.ext import commands

game = discord.Game("집에 보내줘") 
bot = commands.Bot(command_prefix='!', status=discord.Status.online, activity = game) #어떤 봇을 만들 것인가?
 
@bot.event  #이벤트 함수, 비동기 실행
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command(aliases=['도움말','hint'])
async def 도움(ctx):
     embed = discord.Embed(title ='노예 1호기', description = "초록판다가 만듦", color = 0x4432a8)
     embed.add_field(name = "1. 인사", value = "!hello", inline = False)  #/n은 엔터 inline은 옆에 써짐  
     await ctx.send(embed = embed)
 
@bot.command(aliases = ['안녕', 'hi', '안녕하세요']) #command 함수, def hello는 #hello를 대화창에 입력 시 실행
async def hello(ctx):
    await ctx.send(f'{ctx.author.mention}님 Hi!')  #채팅창에 Hi! 입
 
@hello.error
async def hello_error(ctx,error):
     await ctx.send('명령어 오류!!!')



bot.run('MTAwODc1MzE5MzI4ODczNjkzOQ.G1bz9w.nyTRGZCzfWcnKSVx0QyxJVlthmVLYnvJF52UPw') #토큰값 입력


#봇이 친 채팅은 무시하는 코드  if message.author == client.user: return
