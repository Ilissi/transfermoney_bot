from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("IP")  # Тоже str, но для айпи адреса хоста
PG_USER = env.str("PG_USER")
PG_PASSWORD = env.str("PG_PASSWORD")
DATABASE = env.str("DATABASE")
MERCHANT_ID = env.str("MERCHANT_ID")
SECRET = env.str("SECRET")
ITEM_NAME = env.str("ITEM_NAME")
QIWI_API_KEY = env.str("QIWI_API_KEY")

POSTGRES_URL = f"postgresql://{PG_USER}:{PG_PASSWORD}@{IP}/{DATABASE}"
