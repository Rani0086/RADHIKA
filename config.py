from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = "16457832"
# -------------------------------------------------------------
API_HASH = "3030874d0befdb5d05597deacc3e83ab"
# --------------------------------------------------------------
BOT_TOKEN = getenv("BOT_TOKEN", "7153932073:AAE_YH8iy2Rf6p3gqEnyu0GGMqX-O8HYxUc")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://teamdaxx123:teamdaxx123@cluster0.ysbpgcp.mongodb.net/?retryWrites=true&w=majority")
OWNER_ID = int(getenv("OWNER_ID", "7526369190"))
SUPPORT_GRP = "waifexanime"
UPDATE_CHNL = "Planetsadala"
OWNER_USERNAME = "queen143np"
