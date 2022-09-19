aris (61 sloc)  1,93 KB
 # Kredit: @urboysyou
# DARI File-botname <https://github.com/urboys2403/File-botname/>

impor  os

dari  bot  impor  Bot
dari  impor konfigurasi  (
    ADMIN ,
    API_HASH ,
    APP_ID ,
    CHANNEL_ID ,
    DB_URI ,
    FORCE_MSG ,
    FORCE_SUB_CHANNEL ,
    FORCE_SUB_CHANNEL2 ,
    FORCE_SUB_CHANNEL3 ,
    FORCE_SUB_CHANNEL4 ,
    FORCE_SUB_CHANNDL5 ,
    FORCE_SUB_GROUP ,
    HEROKU_API_KEY ,
    HEROKU_APP_NAME ,
    pencatat ,
    PEMILIK ,
    PROTECT_CONTENT ,
    START_MSG ,
    TG_BOT_TOKEN ,
)
dari  filter impor pyrogram  
dari  pirogram . jenis  pesan impor 


@ Bot . on_message ( filter . command ( " log " ) &  filter . user ( ADMINS ))
async  def  get_bot_logs ( klien : Bot , m : Pesan ):
    bot_log_path  =  "logs.txt"
    jika  os . jalan . ada ( bot_log_path ):
        coba :
            menunggu  m . balasan_dokumen (
                bot_log_path ,
                kutipan = Benar ,
                caption = "<b>Ini Logs Bot ini</b>" ,
            )
        kecuali  Pengecualian  sebagai  e :
            os . hapus ( bot_log_path )
            LOGGER ( __nama__ ). peringatan ( e )
    elif  tidak  os . jalan . ada ( bot_log_path ):
        menunggu  m . reply_text ( "❌ <b>Tidak ada log yang ditemukan!</b>" )


@ Bot . on_message ( filter . command ( "vars" ) &  filter . user ( ADMINS ))
async  def  varsFunc ( klien : Bot , pesan : Pesan ):
    Man  =  menunggu  pesan . reply_text ( "Tunggu Sebentar..." )
    text  =  f"""<u><b>CONFIG VARS</b></u> @ { client . username }
APP_ID = <code> { APP_ID } </code>
API_HASH = <code> { API_HASH } </code>
TG_BOT_TOKEN = <code> { TG_BOT_TOKEN } </code>
DATABASE_URL = <code> { DB_URI } </code>
PEMILIK = <code> { PEMILIK } </code>
ADMIN = <code> { ADMIN } </code>
    
<u><b>VARS KUSTOM</b></u>
CHANNEL_ID = <code> { CHANNEL_ID } </code>
FORCE_SUB_CHANNEL = <code> { FORCE_SUB_CHANNEL } </code>
FORCE_SUB_CHANNEL2 = <code> { FORCE_SUB_CHANNEL2 } </code>
FORCE_SUB_CHANNEL3 = <code> { FORCE_SUB_CHANNEL3 } </code>
FORCE_SUB_CHANNEL4 = <code> { FORCE_SUB_CHANNEL4 } </code>
FORCE_SUB_CHANNEL5 = <code> { FORCE_SUB_CHANNEL5 } </code>
FORCE_SUB_GROUP = <code> { FORCE_SUB_GROUP } </code>
PROTECT_CONTENT = <code> { PROTECT_CONTENT } </code>
START_MSG = <code> { START_MSG } </code>
FORCE_MSG = <code> { FORCE_MSG } </code>
<u><b>CONFIGVARS HEROKU</b></u>
HEROKU_APP_NAME = <code> { HEROKU_APP_NAME } </code>
HEROKU_API_KEY = <code> { HEROKU_API_KEY } </code>
    """
    menunggu  Manusia . edit_teks ( teks )