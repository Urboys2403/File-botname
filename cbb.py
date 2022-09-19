# (©)Codexbotz
# Recode oleh @urboysyou

dari  bot  impor  Bot
dari  config  impor  PEMILIK
dari  Data  impor  Data
dari  filter impor pyrogram  
dari  pirogram . kesalahan  mengimpor  MessageNotModified
dari  pirogram . jenis  impor  CallbackQuery , InlineKeyboardMarkup , Pesan


@ Bot . on_message ( filter . private  &  filter . incoming  &  filter . command ( "about" ))
async  def  _about ( klien : Bot , pesan : Pesan ):
    menunggu  klien . kirim_pesan (
        pesan _ mengobrol . identitas ,
        Data . TENTANG . format ( klien . nama pengguna , PEMILIK ),
        disable_web_page_preview = Benar ,
        reply_markup = InlineKeyboardMarkup ( Data . mbuttons ),
    )


@ Bot . on_message ( filter . private  &  filter . incoming  &  filter . command ( "help" ))
async  def  _help ( klien : Bot , msg : Pesan ):
    menunggu  klien . kirim_pesan (
        pesan _ mengobrol . identitas ,
        "<b>Cara Menggunakan Bot ini</b> \n "  +  Data . BANTUAN ,
        reply_markup = InlineKeyboardMarkup ( Tombol Data . ),
    )


@ Bot . on_callback_query ()
async  def  cb_handler ( klien : Bot , kueri : CallbackQuery ):
    data  =  permintaan . data
    jika  data  ==  "tentang" :
        coba :
            menunggu  permintaan . pesan . edit_teks (
                teks = Data . TENTANG . format ( klien . nama pengguna , PEMILIK ),
                disable_web_page_preview = Benar ,
                reply_markup = InlineKeyboardMarkup ( Data . mbuttons ),
            )
        kecuali  MessageNotModified :
            lulus
     data  elif ==  "bantuan" :
        coba :
            menunggu  permintaan . pesan . edit_teks (
                text = "<b>Cara Menggunakan Bot ini</b> \n "  +  Data . BANTUAN ,
                disable_web_page_preview = Benar ,
                reply_markup = InlineKeyboardMarkup ( Tombol Data . ),
            )
        kecuali  MessageNotModified :
            lulus
     data  elif ==  "tutup" :
        menunggu  permintaan . pesan . hapus ()
        coba :
            menunggu  permintaan . pesan . balas_ke_pesan . hapus ()
        kecuali  BaseException :
            lulus