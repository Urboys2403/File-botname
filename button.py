# Kredit: @urboysyou
# DARI File-botname <https://github.com/urboys2403/File-botname/>

dari  config  impor  FORCE_SUB_CHANNEL , FORCE_SUB_GROUP
dari  pirogram . jenis  impor  InlineKeyboardButton


def  start_button ( klien ):
    jika  bukan  FORCE_SUB_CHANNEL  dan  bukan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink4 ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink6 ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink5 ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink4 ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink3 ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink2 ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  FORCE_SUB_CHANNEL  dan  bukan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴄʜᴀɴɴᴇʟ" , url = klien . invitelink ),
            ],
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
                InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" ),
            ],
        ]
         tombol kembali
    jika  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( text = "ʜᴇʟᴘ & s" , callback_data = "help" ),
            ],
            [
               InlineKeyboardButton ( teks = "ᴄʜᴀɴɴᴇʟ" , url = klien . invitelink6 ),
               InlineKeyboardButton ( teks = "ᴄʜᴀɴɴᴇʟ" , url = klien . invitelink5 ),
               InlineKeyboardButton ( teks = "ᴄʜᴀɴɴᴇʟ" , url = klien . invitelink4 ),
               InlineKeyboardButton ( teks = "ᴄʜᴀɴɴᴇʟ" , url = klien . invitelink3 ),
                InlineKeyboardButton ( teks = "ᴄʜᴀɴɴᴇʟ" , url = klien . invitelink2 ),
                InlineKeyboardButton ( teks = "ɢʀᴏᴜᴘ" , url = klien . invitelink ),
            ],
            [ InlineKeyboardButton ( teks = "ᴛᴜᴛᴜᴘ" , callback_data = "tutup" )],
        ]
         tombol kembali

def  fsub_button ( klien , pesan ):
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink6 ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali
def  fsub_button ( klien , pesan ):
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink5 ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali
def  fsub_button ( klien , pesan ):
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink4 ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali
def  fsub_button ( klien , pesan ):
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink3 ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali
def  fsub_button ( klien , pesan ):
    jika  bukan  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink2 ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali
    jika  FORCE_SUB_CHANNEL  dan  bukan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali
    jika  FORCE_SUB_CHANNEL  dan  FORCE_SUB_GROUP :
        tombol  = [
            [
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink ),
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink2 ),
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink3 ),
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink3 ),
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink4 ),
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink5 ),
                InlineKeyboardButton ( teks = "ᴊᴏɪɴ " , url = klien . invitelink6 ),
            ],
        ]
        coba :
            tombol . tambahkan (
                [
                    Tombol Keyboard Sebaris (
                        teks = "ᴄᴏʙᴀ " ,
                        url = f"https://t.me/ { klien . nama pengguna } ?start= { pesan . perintah [ 1 ] } " ,
                    )
                ]
            )
        kecuali  IndexError :
            lulus
         tombol kembali