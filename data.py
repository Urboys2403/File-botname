dari  pirogram . jenis  impor  InlineKeyboardButton

 data kelas :
    BANTUAN  =  """
<b> Perintah untuk Pengguna BOT
/start - Mulai Bot
/about - Tentang Bot ini
/help - Bantuan Perintah Bot ini
/ping - Untuk mengecek bot hidup
/uptime - Untuk melihat status bot
 
Perintah Untuk Admin BOT
/logs - Untuk melihat bot log
/vars - Untuk melihat bot variabel
/setvar - Untuk mengatur var dengan perintah dibot
/delvar - Untuk menghapus var dengan perintah dibot
/getvar - Untuk melihat salah satu var dengan perintah dibot
/users - Untuk melihat statistik pengguna bot
/batch - Untuk membuat link lebih dari satu file
/speedtest - Untuk Mengetes kecepatan server bot
/broadcast - Untuk mengirim pesan broadcast ke pengguna bot
Dikembangkan oleh @Lunatic0de</b>
"""

    tutup  = [
        [ InlineKeyboardButton ( "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" )]
    ]

    tombol  = [
        [
            InlineKeyboardButton ( "ʜᴇʟᴘ & s" , callback_data = "bantuan" ),
            InlineKeyboardButton ( "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" )
        ],
    ]

    tombol  = [
        [
            InlineKeyboardButton ( "ᴛᴇɴᴛᴀɴɢ sᴀʏᴀ" , callback_data = "tentang" ),
            InlineKeyboardButton ( "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" )
        ],
    ]

    TENTANG  =  """
<b>Tentang Bot ini:
@{} adalah Bot Telegram untuk menyimpan Postingan atau File yang dapat Diakses melalui Link Khusus.
• Pembuat: @{}
• Kode Sumber: <a href='https://github.com/mrismanaziz/File-botname'>File-botname v4</a>
• Repo Pemilik: @urboysyou
Dikembangkan oleh @Lunatic0de</b>
"""