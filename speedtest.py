impor  os

 tes kecepatan impor
impor  wget
dari  filter impor pyrogram  
dari  pirogram . jenis  pesan impor 

dari  bot  impor  Bot
dari  konfigurasi  impor  ADMINS


@ Bot . on_message ( filter . command ( " speedtest " ) &  filter . user ( ADMINS ))
async  def  run_speedtest ( klien : Bot , pesan : Pesan ):
    m  =  menunggu  pesan . reply_text ( "⚡️ Menjalankan Tes Kecepatan Server" )
    coba :
        tes  = tes  kecepatan . Tes kecepatan ()
        tes . get_best_server ()
        m  =  menunggu  m . edit ( "⚡️ Menjalankan Unduhan Speedtest.." )
        tes . unduh ()
        m  =  menunggu  m . edit ( "⚡️ Menjalankan Tes Kecepatan Unggah..." )
        tes . unggah ()
        tes . hasil . bagikan ()
        hasil  =  tes . hasil . dikte ()
    kecuali  Pengecualian  sebagai  e :
        menunggu  m . edit ( ) _
        kembali
    m  =  menunggu  m . edit ( "🔄 Berbagi Hasil Speedtest" )
    jalan  =  wget . unduh ( hasil [ "bagikan" ])

    output  =  f"""💡 <b>Hasil Tes Kecepatan</b>
    
<u><b>Klien:<b></u>
<b>ISP:</b> { hasil [ 'klien' ][ 'isp' ] }
<b>Negara:</b> { hasil [ 'klien' ][ 'negara' ] }
  
<u><b>Server:</b></u>
<b>Nama:</b> { hasil [ 'server' ][ 'nama' ] }
<b>Negara:</b> { hasil [ 'server' ][ 'negara' ] } , { hasil [ 'server' ][ 'cc' ] }
<b>Sponsor:</b> { hasil [ 'server' ][ 'sponsor' ] }
️ <b>Ping:</b> { hasil [ 'ping' ] } """
    msg  =  menunggu  klien . kirim_foto (
        chat_id = pesan . mengobrol . id , foto = jalur , keterangan = keluaran
    )
    os . hapus ( jalan )
    menunggu  m . hapus ()