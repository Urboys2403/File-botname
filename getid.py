"""Dapatkan id pengguna yang dibalas
Sintaks: /id"""

dari  filter impor pyrogram  
dari  pirogram . jenis  pesan impor 

dari  bot  impor  Bot


@ Bot . on_message ( filter . command ( " id " ) &  filter . private )
async  def  showid ( klien , pesan ):
    chat_type  =  pesan . mengobrol . Tipe

    jika  chat_type  ==  "pribadi" :
        user_id  =  pesan . mengobrol . Indo
        menunggu  pesan . balasan_teks (
            f"<b>User ID anda adalah:</b> <code> { user_id } </code>" , quote = True
        )

    elif  chat_type  di [ "grup" , "supergrup" ]:
        _id  =  ""
        _id  +=  f"<b>👥 ID Obrolan</b>: <code> { pesan . obrolan . id } </code>"
        jika  pesan . reply_to_message :
            _id  +=  f"<b>🙋‍♂️ Replied User ID</b>: <code> { message . reply_to_message . from_user . id } </code>"
            file_info  =  get_file_id ( pesan . reply_to_message )
        lain :
            _id  +=  "<b>👤 ID Pengguna</b>: <code>{message.from_user.id}</code>"
            file_info  =  get_file_id ( pesan )
        jika  file_info :
            _id  += (
                f"<b> { file_info . message_type } </b>: "
                f"<code> { file_info . file_id } </code> \n "
            )
        menunggu  pesan . reply_text ( _id , kutipan = Benar )


def  get_file_id ( pesan : Pesan ):
    jika  pesan . media :
        untuk  message_type  di (
            "foto" ,
            "animasi" ,
            "suara" ,
            "dokumen" ,
            "video" ,
            "video_catatan" ,
            "suara" ,
            "stiker" ,
        ):
            jika  obj  :=  getattr ( msg , message_type ):
                setattr ( obj , "message_type" , message_type )
                kembalikan  obj