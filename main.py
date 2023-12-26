# 청소하기 기능 코드입니다. 기본적인 건 알아서 짜주세요!
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
