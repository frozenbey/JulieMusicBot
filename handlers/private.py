from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
#Bir_Beyfendi

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
    await message.reply_photo("https://i.ibb.co/MpdcXYM/IMG-20211023-135851-221.jpg")
    await message.reply_text(
        f"""**Merhaba, {message.from_user.mention} 🎵
Ben {bot}! Sesli sohbetlerde müzik çalabilen botum. Ban yetkisiz, Ses yönetimi yetkisi verip, Asistanı gruba ekleyiniz. Komutlar için /bilgi komutunu kullanın.**""",

        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🏷️ Destek Grubu", url="https://t.me/SohbetOdagi"
                    ),
                    InlineKeyboardButton(
                        "🔧 Geliştirici", url = "https://t.me/Bir_Beyfendi"
                    )
                  ],[
                    InlineKeyboardButton(
                        "🛠 Kurucu" , url = "https://t.me/Mahoaga"
                    ),
                    InlineKeyboardButton(
                        "🔊 Asistan" , url = "https://t.me/HerTeldenAsistan"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "🌀 Komutlar" , url = "https://telegra.ph/Komutlar-10-22"
                    ),
                    InlineKeyboardButton(
                        "🎮 Oyun Botu", url="https://t.me/BasitOyunBot"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command(["yenile", f"yenile@{BOT_USERNAME}"]) & ~filters.private & ~filters.channel)
async def yenile(_, message: Message):
      await message.reply_text("""**Yeniden başlatıldı. Bot çalışıyor ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙ Geliştirici", url="https://t.me/Bir_Beyfendi")
                ]
            ]
        )
   )

@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"])) 
async def bilgi(_, message: Message):
      await message.reply_text(f"**Selam {message.from_user.mention}!\n Bu botun bilgi menüsü 🤩\n\n ▶️ /oynat - şarkı çalmak için youtube url'sine veya şarkı dosyasına yanıt verme\n ▶️ /oynat <song name> - istediğiniz şarkıyı çal\n 🔴 /ytp <Sorgu> - youtube üzerinden çalma\n 🎵 /bul <song name> - istediğiniz şarkıları hızlı bir şekilde bulun\n 🎵 /vbul istediğiniz videoları hızlı bir şekilde bulun\n 🔍 /ara <query> - youtube'da ayrıntıları içeren videoları arama\n 🔄 /yenile botu tekrar başlatır\n\n Yalnızca yöneticiler için..\n ▶️ /devam - şarkı çalmaya devam et\n ⏹ /bitir - müzik çalmayı durdurma\n 🔼 /ver botun sadece yönetici için kullanılabilir olan komutlarını kullanabilmesi için kullanıcıya yetki ver\n 🔽 /al botun yönetici komutlarını kullanabilen kullanıcının yetkisini al\n 🎚 /ses asistan hesabın ses seviyesini kontrol et\n\n ⚪ /katil - Müzik asistanı grubunuza katılır\n ⚫ /ayril - Müzik asistanı grubunuzu terk eder.**", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "⚙ Geliştirici", url="https://t.me/Bir_Beyfendi")
                 ]
             ]
         )
    )
