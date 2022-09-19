impor  os
 soket impor

impor  dotenv
impor  heroku3
impor  urllib3
dari  bot  impor  Bot
dari  config  import  ADMINS , HEROKU_API_KEY , HEROKU_APP_NAME
dari  filter impor pyrogram  
dari  pirogram . jenis  pesan impor 

urlib3 . disable_warnings ( urllib3 . exceptions . InsecureRequestWarning )
jika  HEROKU_APP_NAME  bukan None dan HEROKU_API_KEY bukan None : _  _      
    Heroku  =  heroku3 . from_key ( HEROKU_API_KEY )
    SELAMAT  =  Heroku . aplikasi ( HEROKU_APP_NAME )
    heroku_config  =  SELAMAT . konfigurasi ()
lain :
    SELAMAT  =  Tidak ada

XCB  = [
    "/" ,
    "@" ,
    "." ,
    "com" ,
    ":" ,
    "git" ,
    "heroku" ,
    "dorong" ,
    str ( HEROKU_API_KEY ),
    "https" ,
    str ( HEROKU_APP_NAME ),
    "KEPALA" ,
    "utama" ,
]


async  def  is_heroku ():
    kembalikan  "heroku"  di  socket . getfqdn ()


@ Bot . on_message ( filter . command ( " getvar " ) &  filter . user ( ADMINS ))
async  def  varget_ ( klien : Bot , pesan : Pesan ):
    if  len ( pesan . perintah ) !=  2 :
        kembali  menunggu  pesan . reply_text ( "<b>Penggunaan:</b> \n /getvar [Nama Varian]" )
    check_var  =  pesan . teks . membagi ( Tidak ada , 2 )[ 1 ]
    jika  menunggu  is_heroku ():
        jika  HAPP  adalah  Tidak Ada :
            kembali  menunggu  pesan . balasan_teks (
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di konfigurasi vars heroku"
            )
        heroku_config  =  SELAMAT . konfigurasi ()
        jika  check_var  di  heroku_config :
            kembali  menunggu  pesan . balasan_teks (
                f"<b> { check_var } :</b> <code> { heroku_config [ check_var ] } </code>"
            )
        lain :
            kembali  menunggu  pesan . reply_text ( f"Tidak dapat menemukan var { check_var } " )
    lain :
        jalan  =  dotenv . find_dotenv ( "config.env" )
        jika  tidak  jalan :
            kembali  menunggu  pesan . reply_text ( "file .env tidak ditemukan." )
        keluaran  =  dotenv . get_key ( jalur , check_var )
        jika  tidak  keluaran :
            menunggu  pesan . reply_text ( f"Tidak dapat menemukan var { check_var } " )
        lain :
            kembali  menunggu  pesan . balasan_teks (
                f"<b> { check_var } :</b> <code> { str ( keluaran ) } </code>"
            )


@ Bot . on_message ( filter . command ( " delvar " ) &  filter . user ( ADMINS ))
async  def  vardel_ ( klien : Bot , pesan : Pesan ):
    if  len ( pesan . perintah ) !=  2 :
        kembali  menunggu  pesan . reply_text ( "<b>Penggunaan:</b> \n /delvar [Var Name]" )
    check_var  =  pesan . teks . membagi ( Tidak ada , 2 )[ 1 ]
    jika  menunggu  is_heroku ():
        jika  HAPP  adalah  Tidak Ada :
            kembali  menunggu  pesan . balasan_teks (
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di konfigurasi vars heroku"
            )
        heroku_config  =  SELAMAT . konfigurasi ()
        jika  check_var  di  heroku_config :
            menunggu  pesan . reply_text ( f"Berhasil Menghapus var { check_var } " )
            del  heroku_config [ check_var ]
        lain :
            kembali  menunggu  pesan . reply_text ( f"Tidak dapat menemukan var { check_var } " )
    lain :
        jalan  =  dotenv . find_dotenv ( "config.env" )
        jika  tidak  jalan :
            kembali  menunggu  pesan . reply_text ( "file .env tidak ditemukan." )
        keluaran  =  dotenv . unset_key ( jalur , check_var )
        jika  tidak  menghasilkan [ 0 ]:
            kembali  menunggu  pesan . reply_text ( f"Tidak dapat menemukan var { check_var } " )
        lain :
            menunggu  pesan . reply_text ( f"Berhasil Menghapus var { check_var } " )
            os . system ( f"kill -9 { os . getpid () } && bash start" )


@ Bot . on_message ( filter . command ( " setvar " ) &  filter . user ( ADMINS ))
async  def  set_var ( klien : Bot , pesan : Pesan ):
    if  len ( pesan . perintah ) <  3 :
        kembali  menunggu  pesan . reply_text ( "<b>Penggunaan:</b> \n /setvar [Var Name] [Var Value]" )
    to_set  =  pesan . teks . pisahkan ( Tidak ada , 2 )[ 1 ]. strip ()
    nilai  =  pesan . teks . membagi ( Tidak ada , 2 )[ 2 ]. strip ()
    jika  menunggu  is_heroku ():
        jika  HAPP  adalah  Tidak Ada :
            kembali  menunggu  pesan . balasan_teks (
                "Pastikan HEROKU_API_KEY dan HEROKU_APP_NAME anda dikonfigurasi dengan benar di konfigurasi vars heroku"
            )
        heroku_config  =  SELAMAT . konfigurasi ()
        jika  to_set  di  heroku_config :
            menunggu  pesan . reply_text ( f"Berhasil Mengubah var { to_set } menjadi { value } " )
        lain :
            menunggu  pesan . balasan_teks (
                f"Berhasil Menambahkan var { to_set } menjadi { value } "
            )
        heroku_config [ to_set ] =  nilai
    lain :
        jalan  =  dotenv . find_dotenv ( "config.env" )
        jika  tidak  jalan :
            kembali  menunggu  pesan . reply_text ( "file .env tidak ditemukan." )
        dotenv . set_key ( path , to_set , nilai )
        jika  dotenv . get_key ( path , to_set ):
            menunggu  pesan . reply_text ( f"Berhasil Mengubah var { to_set } menjadi { value } " )
        lain :
            menunggu  pesan . balasan_teks (
                f"Berhasil Menambahkan var { to_set } menjadi { value } "
            )
        os . system ( f"kill -9 { os . getpid () } && bash start" )