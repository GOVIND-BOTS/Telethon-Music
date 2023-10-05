import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "29981514"))
    API_HASH = os.environ.get("API_HASH", "8f913218d44ff822f6c85a8622a15b36")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6629814664:AAFo6uDrjUEJt5okpFVVaa151HBtgIvto0c")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKABuyyKYTpmq1N-f9LAAG3BESWZJVH46hhFnuIiuy-NUgClxfacg2FnSNFNHdXcGTcL6BuXAb8FQ-TjALTf58XNr-l6pjmQuMtBycD0FW5fNN_1S0m0KhJDM8J-sfgWoMGWu0izZ5Vbb6LCRg6ohaSSGAev6LGq0VjArgnjJKTEkmJ3PdOKrjgGyh4pKthz_u_OWTYyMy4TsfgV3xYMZpkfPhmwSxIV4izlZ5EkU_8OvK0_RMZDZVFTxt6yCyGfTm8EE0VgH86PlLQUpcMtfSQv67inBHd2Ga1DRcnmYcSPNfChUNP9Rr0FSsS0UV8-2GhivK4UhE1PlA1XOvCOwhY2I3k=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", "true")
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "@The_official_music_bot")
    SUPPORT = os.environ.get("SUPPORT", "GOVIND_USERBOT_SPPORT") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "GOVIND_USERBOT_UPDATE") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/b3706d0b086f1da018488.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/b3706d0b086f1da018488.jpg")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5350640981")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
