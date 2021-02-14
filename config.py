import os

class Config():

  ENV = bool(os.environ.get('ENV', False))

  if ENV:

    BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

    APP_ID = os.environ.get("APP_ID", 6)

    API_HASH = os.environ.get("API_HASH", None)

  else:

    BOT_TOKEN = "1655330757:AAE_JQ8iEXRIgYBaMRsx1cH_0g_hfKj7b6c"

    APP_ID = "1046625"

    API_HASH = "c68afc924b92d73ce27708b155f1e5b4"

class Messages():

      HELP_MSG = [

        ".",

        "**Kick Member Tidak Aktif**\n__Kick member tidak aktif dari grup. Tambahkan saya sebagai admin dengan perijinan ban user lalu kirim perintah /inkick dengan argumen yang sesuai dan saya akan menendang pengguna dari grup.\nGunakan /instatus untuk mengecek status chat member.\n\nLihat halaman selanjutnya untuk informasi perintah & penggunaan.__",

        

        "**Perintah**\n__/instatus - Dapatkan status member saat ini.\n/dkick - Kick semua deleted account dari grup.\n/inkick (argumen) - Keluarkan member tidak aktif dari grup.\nGunakan argumen dengan hati hati dan dipisahkan dengan spasi.__\n\n**Argumen -** __User’s Last Seen & Online status. Can be one of the following: “online”, user is online right now. “offline”, user is currently offline. “recently”, user with hidden last seen time who was online between 1 second and 2-3 days ago. “within_week”, user with hidden last seen time who was online between 2-3 and seven days ago. “within_month”, user with hidden last seen time who was online between 6-7 days and a month ago. “long_time_ago”, blocked user or user with hidden last seen time who was online more than a month ago. None, for bots.__\n\nLihat halaman selanjutnya untuk contoh.",

        

        "**Contoh**\n```/inkick within_month long_time_ago``` - __Untuk kick user yang tidak aktif lebih dari 6-7 hari.__\n\n```/inkick long_time_ago``` - __Untuk mengeluarkan member yang tidak aktif selama sebulan dan Deleted Accounts.__\n\n```/dkick``` - __Untuk mengeluarkan deleted accounts.__",

        

        "**Diterjemahkan dan dimodifikasi oleh - @YasirArisM\nCredit - @viperadnan**"

        ]

      START_MSG = "**Halo [{}](tg://user?id={})**\n__Aku bisa mengeluarkan member yang tidak aktif dari grup.\nSelengkapnya di /help__"

      

      CREATOR_REQUIRED = "❗ **Kamu harus jadi pembuat grup atau admin untuk melakukan itu.**"

      

      INPUT_REQUIRED = "❗ **Argumen dibutuhkan**\n__Lihbat /help di pesan pribadi untuk informasi lebih lanjut.__"

      

      KICKED = "✔️ **Berhasil membersihkan {} pengguna berdasarkan argumen yang diberikan.**"

      

      START_KICK = "🚮**Menghapus pengguna tidak aktif mungkin butuh waktu beberapa saat...**"

      

      ADMIN_REQUIRED = "❗**Saya bukan admin disini**\n__Pergi meninggalkan chat ini seperti saat dia meninggalkan aku, tambahkan aku sebagai admin dengan perijinan ban user.__"

      

      DKICK = "✔️ **Berhasil membersihkan {} Deleted Accounts.**"

      

      FETCHING_INFO = "**Mengumpulkan informasi user...**"

      

      STATUS = "**{}\nChat Member Status**\n\n```recently``` - {}\n```within_week``` - {}\n```within_month``` - {}\n```long_time_ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}"
