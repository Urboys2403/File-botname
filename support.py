# (©)Codexbotz
# Recode oleh @urboysyou

impor  asyncio

dari  pirogram . kesalahan  mengimpor  FloodWait

dari  basis data . sql  impor  query_msg


async  def  users_info ( bot ):
    pengguna  =  0
    diblokir  =  0
    identitas  =  menunggu  query_msg ()
    untuk  id  dalam  identitas :
        nama  =  bol ()
        coba :
            nama  =  menunggu  bot . send_chat_action ( int ( id [ 0 ]), "mengetik" )
        kecuali  FloodTunggu  sebagai  e :
            menunggu  asyncio . tidur ( e . x )
        kecuali  Pengecualian :
            lulus
        jika  bool ( nama ):
            pengguna  +=  1
        lain :
            diblokir  +=  1
     pengguna kembali , diblokir