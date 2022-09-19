# (©)Codexbotz
# Recode oleh @urboysyou

dari  pyrogram  import  Client , filter
dari  pirogram . jenis  impor  InlineKeyboardButton , InlineKeyboardMarkup , Pesan

dari  bot  impor  Bot
dari  konfigurasi  impor  ADMINS
dari  helper_func  import  encode , get_message_id


@ Bot . on_message ( filter . private  &  filter . user ( ADMINS ) &  filter . command ( "batch" ))
async  def  batch ( klien : Klien , pesan : Pesan ):
    sedangkan  Benar :
        coba :
            first_message  =  menunggu  klien . bertanya (
                text = "<b>Silahkan Forward Pesan/File Pertama dari Channel DataBase. (Forward with Qoute)</b> \n \n <b>atau Kirim Link Postingan dari Channel Database</b>" ,
                chat_id = pesan . dari_pengguna . identitas ,
                filter = ( filter . diteruskan  | ( filter . teks  &  ~ filter . diteruskan )),
                batas waktu = 60 ,
            )
        kecuali  BaseException :
            kembali
        f_msg_id  =  menunggu  get_message_id ( klien , first_message )
        jika  f_msg_id :
            merusak
        tunggu  first_message . membalas (
            "❌ <b>ERROR</b> \n \n <b>Postingan yang Diforward ini bukan dari Channel Database saya</b>" ,
            kutipan = Benar ,
        )
        melanjutkan

    sedangkan  Benar :
        coba :
            second_message  =  menunggu  klien . bertanya (
                text = "<b>Silahkan Teruskan Pesan/File Terakhir dari Channel DataBase. (Teruskan dengan Qoute)</b> \n \n <b>atau Kirim Link Postingan dari Database Channel</b>" ,
                chat_id = pesan . dari_pengguna . identitas ,
                filter = ( filter . diteruskan  | ( filter . teks  &  ~ filter . diteruskan )),
                batas waktu = 60 ,
            )
        kecuali  BaseException :
            kembali
        s_msg_id  =  menunggu  get_message_id ( klien , second_message )
        jika  s_msg_id :
            merusak
        menunggu  second_message . membalas (
            "❌ <b>ERROR</b> \n \n <b>Postingan yang Diforward ini bukan dari Channel Database saya</b>" ,
            kutipan = Benar ,
        )
        melanjutkan

    string  =  f"get- { f_msg_id  *  abs ( client . db_channel . id ) } - { s_msg_id  *  abs ( client . db_channel . id ) } "
    base64_string  =  menunggu  encode ( string )
    link  =  f"https://t.me/ { klien . nama pengguna } ?start= { base64_string } "
    reply_markup  =  InlineKeyboardMarkup (
        [
            [
                Tombol Keyboard Sebaris (
                    "🔁 Bagikan Tautan" , url = f"https://telegram.me/share/url?url= { tautan } "
                )
            ]
        ]
    )
    menunggu  second_message . balasan_teks (
        f"<b>File Sharing Link Berhasil Di Buat:</b> \n \n { link } " ,
        kutipan = Benar ,
        reply_markup = balasan_markup ,
    )


@ Bot . on_message ( filter . private  &  filter . user ( ADMINS ) &  filter . command ( " genlink " ))
async  def  link_generator ( klien : Klien , pesan : Pesan ):
    sedangkan  Benar :
        coba :
            channel_message  =  menunggu  klien . bertanya (
                text = "<b>Silahkan Teruskan Pesan dari Channel DataBase. (Teruskan dengan Qoute)</b> \n \n <b>atau Kirim Link Postingan dari Channel Database</b>" ,
                chat_id = pesan . dari_pengguna . identitas ,
                filter = ( filter . diteruskan  | ( filter . teks  &  ~ filter . diteruskan )),
                batas waktu = 60 ,
            )
        kecuali  BaseException :
            kembali
        msg_id  =  menunggu  get_message_id ( klien , channel_message )
        jika  msg_id :
            merusak
        tunggu  channel_message . membalas (
            "❌ <b>ERROR</b> \n \n <b>Postingan yang Diforward ini bukan dari Channel Database saya</b>" ,
            kutipan = Benar ,
        )
        melanjutkan

    base64_string  =  menunggu  encode ( f"get- { msg_id  *  abs ( client . db_channel . id ) } " )
    link  =  f"https://t.me/ { klien . nama pengguna } ?start= { base64_string } "
    reply_markup  =  InlineKeyboardMarkup (
        [
            [
                Tombol Keyboard Sebaris (
                    "🔁 Bagikan Tautan" , url = f"https://telegram.me/share/url?url= { tautan } "
                )
            ]
        ]
    )
    tunggu  channel_message . balasan_teks (
        f"<b>File Sharing Link Berhasil Di Buat:</b> \n \n { link } " ,
        kutipan = Benar ,
        reply_markup = balasan_markup ,
    )