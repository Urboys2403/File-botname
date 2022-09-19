# (©)Codexbotz
# Recode oleh @urbosyou

impor  asyncio
dari  datetime  impor  datetime
dari  waktu  impor  waktu

dari  bot  impor  Bot
dari  impor konfigurasi  (
    ADMIN ,
    KUSTOM_CAPTION ,
    DISABLE_CHANNEL_BUTTON ,
    FORCE_MSG ,
    PROTECT_CONTENT ,
    START_MSG ,
)
dari  basis data . sql  impor  add_user , full_userbase , query_msg
dari  filter impor pyrogram  
dari  pirogram . kesalahan  impor  FloodWait , InputUserDeactivated , UserIsBlocked
dari  pirogram . jenis  impor  InlineKeyboardMarkup , Pesan

dari  helper_func  import  decode , get_messages , subsall , subsch , subsgc

dari . tombol  impor  fsub_button , start_button

START_TIME  =  waktu tanggal . tahu ()
START_TIME_ISO  =  START_TIME . ganti ( mikrodetik = 0 ). format iso ()
TIME_DURATION_UNITS  = (
    ( "minggu" , 60  *  60  *  24  *  7 ),
    ( "hari" , 60 ** 2  *  24 ),
    ( "jam" , 60 ** 2 ),
    ( "menit" , 60 ),
    ( "detik" , 1 ),
)


async  def  _human_time_duration ( detik ):
    jika  detik  ==  0 :
        kembali  "inf"
    bagian  = []
    untuk  unit , div  dalam  TIME_DURATION_UNITS :
        jumlah , detik  =  divmod ( int ( detik ), div )
        jika  jumlah  >  0 :
            bagian . tambahkan ( f' { jumlah }  { satuan } { ""  if  jumlah  ==  1  else  "s" } ' )
    kembali  "," . bergabung ( bagian )


@ Bot . on_message ( filter . command ( " start " ) &  filter . private  &  subsall  &  subsch  &  subsgc )
async  def  start_command ( klien : Bot , pesan : Pesan ):
    id  =  pesan . dari_pengguna . Indo
    nama_pengguna  = (
        f"@ { pesan . dari_pengguna . nama pengguna } "
        jika  pesan . dari_pengguna . nama belakang
        lain  Tidak ada
    )

    coba :
        tunggu  add_user ( id , user_name )
    kecuali :
        lulus
    teks  =  pesan . teks
    jika  len ( teks ) >  7 :
        coba :
            base64_string  =  teks . membagi ( " " , 1 )[ 1 ]
        kecuali  BaseException :
            kembali
        string  =  menunggu  dekode ( base64_string )
        argumen  =  string . membagi ( "-" )
        if  len ( argumen ) ==  3 :
            coba :
                mulai  =  int ( int ( argumen [ 1 ]) /  abs ( klien . db_channel . id ))
                end  =  int ( int ( argumen [ 2 ]) /  abs ( klien . db_channel . id ))
            kecuali  BaseException :
                kembali
            jika  mulai  <=  akhir :
                id  =  rentang ( mulai , akhir  +  1 )
            lain :
                ID  = []
                saya  =  mulai
                sedangkan  Benar :
                    id . tambahkan ( i )
                    saya  -=  1
                    jika  saya  <  akhir :
                        merusak
        elif  len ( argumen ) ==  2 :
            coba :
                id  = [ int ( int ( argumen [ 1 ]) /  abs ( klien . db_channel . id ))]
            kecuali  BaseException :
                kembali
        temp_msg  =  menunggu  pesan . reply ( "<code>Tunggu Sebentar...</code>" )
        coba :
            pesan  =  menunggu  get_messages ( klien , id )
        kecuali  BaseException :
            menunggu  pesan . reply_text ( "<b>Telah Terjadi Kesalahan </b>🥺" )
            kembali
        tunggu  temp_msg . hapus ()

        untuk  pesan  di  pesan :

            if  bool ( CUSTOM_CAPTION ) &  bool ( msg . document ):
                keterangan  =  CUSTOM_CAPTION . format (
                    keterangan sebelumnya = pesan . keterangan . html  jika  pesan . keterangan  lain  "" ,
                    nama file = pesan . dokumen . nama_file ,
                )

            lain :
                keterangan  =  pesan . keterangan . html  jika  pesan . keterangan  lain  ""

            reply_markup  =  pesan . reply_markup  jika  DISABLE_CHANNEL_BUTTON  yang lain  Tidak ada
            coba :
                ditunggu  smsnya _ salinan (
                    chat_id = pesan . dari_pengguna . identitas ,
                    keterangan = keterangan ,
                    parse_mode = "html" ,
                    protect_content = PROTECT_CONTENT ,
                    reply_markup = balasan_markup ,
                )
                menunggu  asyncio . tidur ( 0,5 )
            kecuali  FloodTunggu  sebagai  e :
                menunggu  asyncio . tidur ( e . x )
                ditunggu  smsnya _ salinan (
                    chat_id = pesan . dari_pengguna . identitas ,
                    keterangan = keterangan ,
                    parse_mode = "html" ,
                    protect_content = PROTECT_CONTENT ,
                    reply_markup = balasan_markup ,
                )
            kecuali  BaseException :
                lulus
    lain :
        keluar  =  start_button ( klien )
        menunggu  pesan . balasan_teks (
            teks = START_MSG . format (
                pertama = pesan . dari_pengguna . nama_depan ,
                terakhir = pesan . dari_pengguna . nama_belakang ,
                username = f"@ { pesan . from_user . nama pengguna } "
                jika  pesan . dari_pengguna . nama belakang
                lain  Tidak ada ,
                sebutkan = pesan . dari_pengguna . menyebutkan ,
                id = pesan . dari_pengguna . identitas ,
            ),
            reply_markup = InlineKeyboardMarkup ( keluar ),
            disable_web_page_preview = Benar ,
            kutipan = Benar ,
        )


    kembali


@ Bot . on_message ( filter . command ( " start " ) &  filter . private )
async  def  not_joined ( klien : Bot , pesan : Pesan ):
    tombol  =  fsub_button ( klien , pesan )
    menunggu  pesan . membalas (
        teks = FORCE_MSG . format (
            pertama = pesan . dari_pengguna . nama_depan ,
            terakhir = pesan . dari_pengguna . nama_belakang ,
            username = f"@ { pesan . from_user . nama pengguna } "
            jika  pesan . dari_pengguna . nama belakang
            lain  Tidak ada ,
            sebutkan = pesan . dari_pengguna . menyebutkan ,
            id = pesan . dari_pengguna . identitas ,
        ),
        reply_markup = InlineKeyboardMarkup ( tombol ),
        kutipan = Benar ,
        disable_web_page_preview = Benar ,
    )


@ Bot . on_message ( filter . command ([ "users" , "stats" ]) &  filter . user ( ADMINS ))
async  def  get_users ( klien : Bot , pesan : Pesan ):
    msg  =  menunggu  klien . kirim_pesan (
        chat_id = pesan . mengobrol . id , teks = "<code>Memproses ...</code>"
    )
    pengguna  =  menunggu  full_userbase ()
    ditunggu  smsnya _ edit ( f" { len ( users ) } <b>Pengguna menggunakan bot ini</b>" )


@ Bot . on_message ( filter . command ( "broadcast" ) &  filter . user ( ADMINS ))
async  def  send_text ( klien : Bot , pesan : Pesan ):
    jika  pesan . reply_to_message :
        query  =  menunggu  query_msg ()
        broadcast_msg  =  pesan . balas_ke_pesan
        jumlah  =  0
        berhasil  =  0
        diblokir  =  0
        dihapus  =  0
        gagal  =  0

        pls_wait  =  menunggu  pesan . membalas (
            "<code>Pesan Siaran Tunggu Sebentar...</code>"
        )
        untuk  baris  dalam  kueri :
            chat_id  =  int ( baris [ 0 ])
            jika  chat_id  tidak ada  di  ADMINS :
                coba :
                    tunggu  broadcast_msg . salin ( chat_id , protect_content = PROTECT_CONTENT )
                    berhasil  +=  1
                kecuali  FloodTunggu  sebagai  e :
                    menunggu  asyncio . tidur ( e . x )
                    tunggu  broadcast_msg . salin ( chat_id , protect_content = PROTECT_CONTENT )
                    berhasil  +=  1
                kecuali  UserIsBlocked :
                    diblokir  +=  1
                kecuali  InputUserDeactivated :
                    dihapus  +=  1
                kecuali  BaseException :
                    gagal  +=  1
                jumlah  +=  1
        status  =  f"""<b><u>Berhasil Siaran</u>
Jumlah Pengguna: <code> { total } </code>
Berhasil: <code> { berhasil } </code>
Gagal: <code> { gagal } </code>
Pengguna diblokir: <code> { diblokir } </code>
Akun Terhapus: <code> { dihapus } </code></b>"""
        kembali  menunggu  pls_wait . edit ( status )
    lain :
        msg  =  menunggu  pesan . membalas (
            "<code>Gunakan Perintah Ini Harus Sambil Balas ke pesan telegram yang ingin di Broadcast.</code>"
        )
        menunggu  asyncio . tidur ( 8 )
        ditunggu  smsnya _ hapus ()


@ Bot . on_message ( filter . perintah ( "ping" ))
async  def  ping_pong ( klien , m : Pesan ):
    mulai  =  waktu ()
    saat_waktu  = tanggal  waktu . tahu ()
    uptime_sec  = ( waktu_saat ini  -  START_TIME ). total_detik ()
    uptime  =  menunggu  _human_time_duration ( int ( uptime_sec ))
    m_reply  =  menunggu  m . reply_text ( "Ping..." )
    delta_ping  =  waktu () -  mulai
    tunggu  m_reply . edit_teks (
        "<b>PONG!!</b>🏓 \n "
        f"<b>• Pinger -</b> <code> { delta_ping  *  1000 :.3f } ms</code> \n "
        f"<b>• Waktu beroperasi -</b> <code> { waktu aktif } </code> \n "
    )


@ Bot . on_message ( filter . command ( "uptime" ))
async  def  get_uptime ( klien , m : Pesan ):
    saat_waktu  = tanggal  waktu . tahu ()
    uptime_sec  = ( waktu_saat ini  -  START_TIME ). total_detik ()
    uptime  =  menunggu  _human_time_duration ( int ( uptime_sec ))
    menunggu  m . balasan_teks (
        "🤖 <b>Status Bot:</b> \n "
        f"• <b>Waktu beroperasi:</b> <code> { waktu aktif } </code> \n "
        f"• <b>Waktu Mulai:</b> <code> { START_TIME_ISO } </code>"
    )