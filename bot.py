impor  piromod . mendengarkan
 sistem impor

dari  pyrogram  import  Client

dari  impor konfigurasi  (
    API_HASH ,
    APP_ID ,
    CHANNEL_ID ,
    FORCE_SUB_CHANNEL ,
    FORCE_SUB_CHANNEL2 ,
    FORCE_SUB_CHANNEL3 , 
    FORCE_SUB_CHANNEL4 , 
    FORCE_SUB_CHANNEL5 , 
    FORCE_SUB_GROUP ,
    pencatat ,
    PEMILIK ,
    TG_BOT_TOKEN ,
    TG_BOT_WORKERS ,
)


kelas  Bot ( Klien ):
    def  __init__ ( sendiri ):
        super (). __init__ (
            "Bot" ,
            api_hash = API_HASH ,
            api_id = APP_ID ,
            plugins = { "root" : "plugins" },
            pekerja = TG_BOT_WORKERS ,
            bot_token = TG_BOT_TOKEN ,
        )
        diri . LOGGER  =  LOGGER

    async  def  mulai ( mandiri ):
        coba :
            menunggu  super (). mulai ()
            usr_bot_me  =  menunggu  diri sendiri . dapatkan_saya ()
            diri . nama pengguna  =  usr_bot_me . nama belakang
            diri . namebot  =  usr_bot_me . nama depan
            diri . LOGGER ( __nama__ ). informasi (
                f"TG_BOT_TOKEN terdeteksi! \n Nama Depan: { self . namebot } \n Nama pengguna: @ { self . username } \n ——"
            )
        kecuali  Pengecualian  sebagai  : _
            diri . LOGGER ( __nama__ ). peringatan ( a )
            diri . LOGGER ( __nama__ ). informasi (
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys . keluar ()

        jika  FORCE_SUB_CHANNEL :
            coba :
                info  =  menunggu  diri sendiri . get_chat ( FORCE_SUB_CHANNEL )
                tautan  =  info . undangan_link
                jika  tidak  tautan :
                    menunggu  diri . export_chat_invite_link ( FORCE_SUB_CHANNEL )
                    tautan  =  info . undangan_link
                diri . tautan undangan  =  tautan
                diri . LOGGER ( __nama__ ). informasi (
                    f"FORCE_SUB_CHANNEL terdeteksi! \n Judul: { info . judul } \n ID Obrolan: { info . id } \n ——"
                )
            kecuali  Pengecualian  sebagai  : _
                diri . LOGGER ( __nama__ ). peringatan ( a )
                diri . LOGGER ( __nama__ ). peringatan (
                    "Bot tidak dapat mengambil link invite dari FORCE_SUB_CHANNEL!"
                )
                diri . LOGGER ( __nama__ ). peringatan (
                    f"Pastikan @ { self . username } adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: { FORCE_SUB_CHANNEL } "
                )
                diri . LOGGER ( __nama__ ). informasi (
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys . keluar ()
                
       jika  FORCE_SUB_CHANNEL2 :
            coba :
                info  =  menunggu  diri sendiri . get_chat ( FORCE_SUB_CHANNEL2 )
                tautan  =  info . undangan_link
                jika  tidak  tautan :
                    menunggu  diri . export_chat_invite_link ( FORCE_SUB_CHANNEL2 )
                    tautan  =  info . undangan_link
                diri . tautan undangan  =  tautan
                diri . LOGGER ( __nama__ ). informasi (
                    f"FORCE_SUB_CHANNEL2 terdeteksi! \n Judul: { info . judul } \n ID Obrolan: { info . id } \n ——"
                )
            kecuali  Pengecualian  sebagai  : _
                diri . LOGGER ( __nama__ ). peringatan ( a )
                diri . LOGGER ( __nama__ ). peringatan (
                    "Bot tidak dapat mengambil link invite dari FORCE_SUB_CHANNEL2!"
                )
                diri . LOGGER ( __nama__ ). peringatan (
                    f"Pastikan @ { self . username } adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: { FORCE_SUB_CHANNEL2 } "
                )
                diri . LOGGER ( __nama__ ). informasi (
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys . keluar ()
        
        jika  FORCE_SUB_CHANNEL3 :
            coba :
                info  =  menunggu  diri sendiri . get_chat ( FORCE_SUB_CHANNEL3 )
                tautan  =  info . undangan_link
                jika  tidak  tautan :
                    menunggu  diri . export_chat_invite_link ( FORCE_SUB_CHANNEL3 )
                    tautan  =  info . undangan_link
                diri . tautan undangan  =  tautan
                diri . LOGGER ( __nama__ ). informasi (
                    f"FORCE_SUB_CHANNEL3 terdeteksi! \n Judul: { info . judul } \n ID Obrolan: { info . id } \n ——"
                )
            kecuali  Pengecualian  sebagai  : _
                diri . LOGGER ( __nama__ ). peringatan ( a )
                diri . LOGGER ( __nama__ ). peringatan (
                    "Bot tidak dapat mengambil link invite dari FORCE_SUB_CHANNEL3!"
                )
                diri . LOGGER ( __nama__ ). peringatan (
                    f"Pastikan @ { self . username } adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: { FORCE_SUB_CHANNEL3 } "
                )
                diri . LOGGER ( __nama__ ). informasi (
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys . keluar ()
        
        jika  FORCE_SUB_CHANNEL4 :
            coba :
                info  =  menunggu  diri sendiri . get_chat ( FORCE_SUB_CHANNEL4 )
                tautan  =  info . undangan_link
                jika  tidak  tautan :
                    menunggu  diri . export_chat_invite_link ( FORCE_SUB_CHANNEL4 )
                    tautan  =  info . undangan_link
                diri . tautan undangan  =  tautan
                diri . LOGGER ( __nama__ ). informasi (
                    f"FORCE_SUB_CHANNEL4 terdeteksi! \n Judul: { info . judul } \n ID Obrolan: { info . id } \n ——"
                )
            kecuali  Pengecualian  sebagai  : _
                diri . LOGGER ( __nama__ ). peringatan ( a )
                diri . LOGGER ( __nama__ ). peringatan (
                    "Bot tidak dapat mengambil link invite dari FORCE_SUB_CHANNEL4!"
                )
                diri . LOGGER ( __nama__ ). peringatan (
                    f"Pastikan @ { self . username } adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: { FORCE_SUB_CHANNEL4 } "
                )
                diri . LOGGER ( __nama__ ). informasi (
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys . keluar ()
        
        jika  FORCE_SUB_CHANNEL5 :
            coba :
                info  =  menunggu  diri sendiri . get_chat ( FORCE_SUB_CHANNEL5 )
                tautan  =  info . undangan_link
                jika  tidak  tautan :
                    menunggu  diri . export_chat_invite_link ( FORCE_SUB_CHANNEL5 )
                    tautan  =  info . undangan_link
                diri . tautan undangan  =  tautan
                diri . LOGGER ( __nama__ ). informasi (
                    f"FORCE_SUB_CHANNEL5 terdeteksi! \n Judul: { info . judul } \n ID Obrolan: { info . id } \n ——"
                )
            kecuali  Pengecualian  sebagai  : _
                diri . LOGGER ( __nama__ ). peringatan ( a )
                diri . LOGGER ( __nama__ ). peringatan (
                    "Bot tidak dapat mengambil link invite dari FORCE_SUB_CHANNEL5!"
                )
                diri . LOGGER ( __nama__ ). peringatan (
                    f"Pastikan @ { self . username } adalah admin di Channel Tersebut, Chat ID F-Subs Channel Saat Ini: { FORCE_SUB_CHANNEL5 } "
                )
                diri . LOGGER ( __nama__ ). informasi (
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys . keluar ()
        
        jika  FORCE_SUB_GROUP :
            coba :
                info  =  menunggu  diri sendiri . get_chat ( FORCE_SUB_GROUP )
                tautan  =  info . undangan_link
                jika  tidak  tautan :
                    menunggu  diri . export_chat_invite_link ( FORCE_SUB_GROUP )
                    tautan  =  info . undangan_link
                diri . invitelink2  =  tautan
                diri . LOGGER ( __nama__ ). informasi (
                    f"FORCE_SUB_GROUP terdeteksi! \n Judul: { info . judul } \n ID Obrolan: { info . id } \n ——"
                )
            kecuali  Pengecualian  sebagai  : _
                diri . LOGGER ( __nama__ ). peringatan ( a )
                diri . LOGGER ( __nama__ ). peringatan (
                    "Bot tidak dapat mengambil link invite dari FORCE_SUB_GROUP!"
                )
                diri . LOGGER ( __nama__ ). peringatan (
                    f"Pastikan @ { self . username } adalah admin di Group Tersebut, Chat ID F-Subs Group Saat Ini: { FORCE_SUB_GROUP } "
                )
                diri . LOGGER ( __nama__ ). informasi (
                    "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
                )
                sys . keluar ()

        coba :
            db_channel  =  menunggu  diri sendiri . get_chat ( CHANNEL_ID )
            diri . db_channel  =  db_channel
            tes  =  menunggu  diri sendiri . send_message ( chat_id = db_channel .id , text = " Test Message " , disable_notification = True )
            menunggu  ujian . hapus ()
            diri . LOGGER ( __nama__ ). informasi (
                f"CHANNEL_ID Database terdeteksi! \n Judul: { db_channel . title } \n ID Obrolan: { db_channel . id } \n ——"
            )
        kecuali  Pengecualian  sebagai  e :
            diri . LOGGER ( __nama__ ). peringatan ( e )
            diri . LOGGER ( __nama__ ). peringatan (
                f"Pastikan @ { self . username } adalah admin di Channel DataBase anda, CHANNEL_ID Saat Ini: { CHANNEL_ID } "
            )
            diri . LOGGER ( __nama__ ). informasi (
                "Bot Berhenti. Gabung Group https://t.me/SharingUserbot untuk Bantuan"
            )
            sys . keluar ()

        diri . set_parse_mode ( "html" )
        diri . LOGGER ( __nama__ ). informasi (
            f"[🔥 BERHASIL DIAKTIFKAN! 🔥] \n \n BOT Dibuat oleh @ { OWNER } \n Jika @ { OWNER } membutuhkan Bantuan, Silahkan Tanyakan di Grup https://t.me/SharingUserbot"
        )

    async  def  stop ( self , * args ):
        menunggu  super (). berhenti ()
        diri . LOGGER ( __nama__ ). info ( "Bot berhenti." )