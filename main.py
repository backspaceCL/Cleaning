import discord #모듈 불러오기
token = "YOUR TOKEN" #봇 토큰 설정하기
client = discord.Client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready(): #봇이 준비되었을 때
    print("봇 준비 완료!")
    print(client.user)
    print("===========================")


# 청소하기
@bot.tree.command(name="청소", description="입력한 개수만큼 채팅 메시지를 삭제합니다.")
async def 청소(interaction: discord.Interaction,
             채널: discord.TextChannel = None,
             개수: int = None):
  if 채널 is None:
    channel = interaction.channel
  if 개수 is not None:
    await interaction.response.send_message(f"{채널} 에서 {개수} 개의 메시지가 삭제되었습니다.",
                                            ephemeral=True)
    await 채널.purge(limit=개수)
  if 개수 is None:
    await interaction.response.send_message(f"Channel {채널} purged.",
                                            ephemeral=True)
    await 채널.purge()
