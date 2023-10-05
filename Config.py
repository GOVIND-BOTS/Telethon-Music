import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29981514"))
    API_HASH = os.environ.get("API_HASH", "8f913218d44ff822f6c85a8622a15b36")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6629814664:AAFo6uDrjUEJt5okpFVVaa151HBtgIvto0c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCwCPkb7DP7x_6xOUI3lgYTllY-GabKuv2Asn3yiacIvj0kyqNmtMquVaW-Gvh_7lCZSSjxYNKyWwr3J5iqwDjU1JMizF2TS5_K75wuBzKdb-99Dsre3QFBrN80QDMgWWZ2trkLNpcsqO7ESlFpRfuJ4729-g3qzYXwFVrwa8qtEyon5xDS4EJHPBVnRX-L0UtyDAkIw7RRqhWD7FwCeveXNWSr50flg_1F-ZzPA3zHO0U5IDtMaK27nDHQ7j5H8tUxsO-ygbtVBA1F1kY4JYBeOyql1enfw7l99tAbGExVYyyUfLfWa8JmJuupltlJeD78ISjPyIzQkt2poP_9a09dAAAAAT7sTVUA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@The_official_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "GOVIND_USERBOT_SPPORT") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "GOVIND_USERBOT_UPDATE") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b3706d0b086f1da018488.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/b3706d0b086f1da018488.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5350640981")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
