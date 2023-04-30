import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6105046691:AAGfz5sTkZX20EaNW_U2AQ_FCIVQxePAxIk")
    STRING_SESSION = os.environ.get("STRING_SESSION", "AQGIInsABuNr2vi-VJCr6EVlhmFxwWzk5_DtbEB5tM_CBrGEYrmcx-saCl1CZqhMvjUXMMFdiRctNr8bJJv49PbP48B8cBGU5Uks6E4SKBJgSKAKWL0aqZiNXaLWf-6Z-U-MNpvItlPJb7x9tAtIpZv_C-cxuIPdmsgGAZ37BiXePbwAIBFac1Ct28gsrYExbiEMYime3_tGthXS1_h_IPHNph9BOmDJqZ3Tr5XeLEI5HlNiXr4AiEP3yKDvTc10P1eqtJJMRn53kvoTGM5p9JHSRATUwn_-HFdgXu3fQWftFxfYO--jFidzKW1hOF47Q_HOeeHVxHcolLP_KegE57VW4MZTKQAAAAFyb8lPAA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
