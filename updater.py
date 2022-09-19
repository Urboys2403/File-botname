# Kredit: @urboysyou
# DARI File-botname <https://github.com/urboys2403/File-botname/>

impor  os
 sistem impor
dari  os  import  environ , execle , system

dari  bot  impor  Bot
dari  git  impor  Repo
dari  git . exc  impor  InvalidGitRepositoryError
dari  pyrogram  import  Client , filter
dari  pirogram . jenis  pesan impor 

dari  config  impor  ADMINS , LOGGER

UPSTREAM_REPO  =  "https://github.com/urboys2403/File-botname"


def  gen_chlog ( repo , diff ):
    upstream_repo_url  =  Repo (). remote [ 0 ]. config_reader . dapatkan ( "url" ). ganti ( ".git" , "" )
    ac_br  =  repo . aktif_cabang . nama
    ch_log  =  ""
    tldr_log  =  ""
    ch  =  f"<b>pembaruan untuk <a href= { upstream_repo_url } /tree/ { ac_br } >[ { ac_br } ]</a>:</b>"
    ch_tl  =  f"pembaruan untuk { ac_br } :"
    d_form  =  "%d/%m/%y || %H:%M"
    untuk  c  dalam  repo . iter_commits ( diff ):
        ch_log  += (
            f" \n \n <b> { c . count () } </b> <b>[ { c . commit_datetime . strftime ( d_form ) } ]</b> \n <b>"
            f"<a href= { upstream_repo_url . rstrip ( '/' ) } /commit/ { c } >[ { c . ringkasan } ]</a></b> 👨‍💻 <code> { c . author } < /kode>"
        )
        tldr_log  +=  f" \n \n { c . count () } 🗓 [ { c . commit_datetime . strftime ( d_form ) } ] \n [ { c . ringkasan } ] { c . penulis } "
    jika  ch_log :
        kembali  str ( ch  +  ch_log ), str ( ch_tl  +  tldr_log )
    kembalikan  ch_log , tldr_log


 pembaruan def ():
    coba :
        repo  =  repo ()
    kecuali  InvalidGitRepositoryError :
        repo  =  repo . init ()
        asal  =  repo . create_remote ( "upstream" , USTREAM_REPO )
        asal . ambil ()
        repo . create_head ( "master" , asal . ref . master )
        repo . kepala . tuan . set_tracking_branch ( asal . referensi . master )
        repo . kepala . tuan . pembayaran ( Benar )
    ac_br  =  repo . aktif_cabang . nama
    jika  "hulu"  di  repo . remote :
        ups_rem  =  repo . jauh ( "hulu" )
    lain :
        ups_rem  =  repo . create_remote ( "upstream" , USTREAM_REPO )
    ups_rem . ambil ( ac_br )
    changelog , tl_chnglog  =  gen_chlog ( repo , f"HEAD..upstream/ { ac_br } " )
    kembali  bool ( changelog )



@ Bot . on_message ( filter . command ( " update " ) &  filter . user ( ADMINS ))
async  def  update_bot ( _ , pesan : Pesan ):
    pesan . mengobrol . Indo
    msg  =  menunggu  pesan . reply_text ( "Memeriksa pembaruan..." )
    update_avail  =  pembaru ()
    jika  update_avail :
        ditunggu  smsnya _ edit ( "✅ Pembaruan selesai!" )
        system ( "git pull -f && pip3 install --no-cache-dir -r requirements.txt" )
        execle ( sys .executable , sys .executable , " main.py " , environ )
        kembali
    ditunggu  smsnya _ mengedit (
        f"Bot **up-to-date** dengan cabang [master]( { UPSTREAM_REPO } /tree/master)" ,
        disable_web_page_preview = Benar ,
    )


@ Bot . on_message ( filter . command ( " restart " ) &  filter . user ( ADMINS ))
async  def  restart_bot ( _ , pesan : Pesan ):
    coba :
        msg  =  menunggu  pesan . reply_text ( "`Memulai ulang bot...`" )
        LOGGER ( __nama__ ). info ( "SERVER BOT DIMULAI ULANG!!" )
    kecuali  BaseException  sebagai  err :
        LOGGER ( __nama__ ). info ( f" { err } " )
        kembali
    ditunggu  smsnya _ edit_text ( "✅ Bot telah dimulai ulang ! \n \n " )
    os . system ( f"kill -9 { os . getpid () } && bash start" )