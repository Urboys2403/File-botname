benang impor

dari  sqlalchemy  import  TEXT , Column , Numeric , create_engine
dari  sqlalchemy . ext . impor deklaratif  declarative_base 
dari  sqlalchemy . orm  import  scoped_session , pembuat sesi

dari  config  impor  DB_URI


def  mulai () ->  scoped_session :
    engine  =  create_engine ( DB_URI , client_encoding = "utf8" )
    DASAR . metadata . mengikat  =  mesin
    DASAR . metadata . buat_semua ( mesin )
    kembalikan  scoped_session ( pembuat sesi ( bind = engine , autoflush = False ))


BASE  =  deklaratif_base ()
SESI  =  mulai ()

INSERTION_LOCK  =  merangkai . Kunci ()


kelas  Siaran ( BASE ):
    __namatabel__  =  "siaran"
    id  =  Kolom ( Numerik , primary_key = True )
    nama_pengguna  =  Kolom ( TEKS )

    def  __init__ ( diri , id , nama_pengguna ):
        diri . id  =  id
        diri . nama_pengguna  =  nama_pengguna


Siaran . __meja__ . buat ( centang dulu = True )


# Tambahkan detail pengguna -
async  def  add_user ( id , user_name ):
    dengan  INSERTION_LOCK :
        pesan  =  SESI . permintaan ( Siaran ). dapatkan ( id )
        kalo  gak  sms :
            usr  =  Siaran ( id , nama_pengguna )
            SESI . tambahkan ( usr )
            SESI . komit ()


async  def  full_userbase ():
    pengguna  =  SESI . permintaan ( Siaran ). semua ()
    SESI . tutup ()
     pengguna kembali


async  def  query_msg ():
    coba :
        kembali  SESI . kueri ( Siaran . id ). order_by ( Siaran .id ) _
    akhirnya :
        SESI . tutup ()