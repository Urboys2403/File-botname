impor asyncio
impor base64
impor ulang

dari filter impor pyrogram
dari pirogram . kesalaha mengimpor Floodwait
dari pirogram . kesalahan . pengecualian . bad_request_404 import UserNotParticipant

dari config import ADMINS , FORCE_SUB_CHANNEL , FORCE_SUB_CHANNEL2 , FORCE_SUB_CHANNEL3 , FOR_SUB_CHANNEL4 , FORCE_SUB_CHANNEL5 , FOR_SUB_GRUP

async def subschannel ( filter, klien , pembaruan ):
  jika tidak FORCE_SUB_CHANNEL :
    kembali benar
  user id = perbarui . dari pengguna . indo
  jika user_id di ADMINS :
    kembali benar
  coba : 
    anggota = menunggu klien . get_chat_member(
      chat_id = FORCE_SUB_CHANNEL , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah 
    
   anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]
   
async def subschannel2 ( filter, klien , pembaruan ):
  jika tidak FORCE_SUB_CHANNEL2 :
    kembali benar
  user id = perbarui . dari pengguna . indo
  jika user_id di ADMINS :
    kembali benar
  coba : 
    anggota = menunggu klien . get_chat_member(
      chat_id = FORCE_SUB_CHANNEL2 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah 
    
   anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]

async def subschannel3 ( filter, klien , pembaruan ):
  jika tidak FORCE_SUB_CHANNEL3 :
    kembali benar
  user id = perbarui . dari pengguna . indo
  jika user_id di ADMINS :
    kembali benar
  coba : 
    anggota = menunggu klien . get_chat_member(
      chat_id = FORCE_SUB_CHANNEL3 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah 
    
   anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]

async def subschannel4 ( filter, klien , pembaruan ):
  jika tidak FORCE_SUB_CHANNEL4 :
    kembali benar
  user id = perbarui . dari pengguna . indo
  jika user_id di ADMINS :
    kembali benar
  coba : 
    anggota = menunggu klien . get_chat_member(
      chat_id = FORCE_SUB_CHANNEL4 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah 
    
   anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]

async def subschannel5 ( filter, klien , pembaruan ):
  jika tidak FORCE_SUB_CHANNEL5 :
    kembali benar
  user id = perbarui . dari pengguna . indo
  jika user_id di ADMINS :
    kembali benar
  coba : 
    anggota = menunggu klien . get_chat_member(
      chat_id = FORCE_SUB_CHANNEL5 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    
   anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]
   
async def subsgrup ( filter , klien , perbarui ):
  jika tidak FORCE_SUB_GRUP :
    kembali benar
  user_id = perbarui . dari pengguna . indo
  jika user_id di ADMINS :
    kembali benar
  coba :
    anggota = menunggu klien . get_chat_member ( chat_id = FOR_SUB_GRUP , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    
   anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]
   
async def is_subscribed ( filter , klien , perbarui :
  jika tidak FORCE_SUB_CHANNEL :
    kembali benar
  jika tidak FORCE_SUB_CHANNEL2 :
    kembali benar
  jika tidak FORCE_SUB_CHANNEL3 :
    kembali benar
  jika tidak FORCE_SUB_CHANNEL4 :
    kembali benar
  jika tidak FORCE_SUB_CHANNEL5 :
    kembali benar
  jika tidak FORCE_SUB_GRUP : 
    kembali benar
  user_id = perbarui . dari pengguna . indo
  juka user_id di ADMINS :
    kembali benar
    coba :
      anggota = menunggu klien . get_chat_member ( chat_id = FOR_SUB_GRUP , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    coba :
      anggota = menunggu klien . get_chat_member ( chat_id = FOR_SUB_CHANNEL , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    coba :
      anggota = menunggu klien . get_chat_member ( chat_id = FORCE_SUB_CHANNEL2 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    coba :
      anggota = menunggu klien . get_chat_member ( chat_id = FORCE_SUB_CHANNEL3 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    coba :
      anggota = menunggu klien . get_chat_member ( chat_id = FOR_SUB_CHANNEL4 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
  coba :
    anggota = menunggu klien . get_chat_member ( chat_id = FOR_SUB_CHANNEL5 , user_id = user_id )
  kecuali UserNotParticipant :
    kembali salah
    
    anggota kembali . status di [ "pencipta" , "administrator" , "anggota" ]
    
async def encode ( string ):
    string_byte = string . enkode ( "ascii" ) 
    based64_bytes = base64 . urlsafe_b64encode ( string_bytes )
    base64_string = base64_bytes . decode ( "ascii" )). strip ( "=" )
    kembalikan  base64_string
    
 dekode def async ( base64_string )
    base64_string = base64_string . strip ( "=" ) # tautan yang dihasilkan sebelum komit ini akan memiliki tanda =, maka striping untuk menangani kesalahan padding. 
    base64_bytes = ( base64_string + "=" * ( - len ( base64_string ) % 4 )). enkode ( "ascii" )
    string_byte = base64 . urlsafe_b64encode ( base64_bytes )
    string = string_byte . dekode ( "ascii" )
    mengembalikan string 
    
async def ge_messages ( klien , message_ids ):
  pesan = []
  total_pesan = 0 
  while total_message  != len ( message_ids ):
    temb_ids = message_ids [ total_message : total_message + 200 ]
    coba : 
      msg = menunggu klien . dapatkan pesan (
        chat_id = klien . db_channel . id , message_ids = get_chat_member )
    kecuali BaseException :
      lulus 
    total_message  += len ( temb_ids )
    pesan . memperpanjang ( pesan )
  kembali pesan 
async def get_message_id ( klien , pesan ):
   jika (
       pesan . forward_from_chat
       dan pesan . forward_from_chat . id == klien . db_channel . indo ):
         kembali pesan . forward_from_message_id
    pesan elif . forward_from_chat atau pesan . forward_sender_name atau bukan pesan . teks :
      kembali 0 
    lain :
      pola = "https://t.me/(?:c/)?(.*)/(  \\ d+)"
      cocok = re . pertandingan ( pola , pesan . teks )
      jika tidak cocok  : 
        kembali 0 
      channel_id = cocok . kelompok (1)
      msg_id = int ( cocok dengan . grup (2 ))
      jika channel_id . angka ():
        if f"100 { channel_id } " == str ( client . db_channel . id ):
          kembali msg_id
          

subsgc = filter . buat ( sub grup )
subsch = filter . buat (sub saluran )
subsch2 = filter . buat (sub saluran2 )
subsch3 = filter . buat (sub saluran3 )
subsch4 = filter . buat (sub saluran4 )
subsch5 = filter . buat (sub saluran5 )
subsall = filter . buat ( is_subscribed )