import os
import redis

from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID", "17250424"))

API_HASH = os.getenv("API_HASH", "753bc98074d420ef57ddf7eb1513162b")

BOT_TOKEN = os.getenv("BOT_TOKEN", "6096692132:AAHLv_rYOtSCowWDbWbAVIR8rStmltGLqt4")

OWNER_ID = int(os.getenv("OWNER_ID", "2099942562"))

DB_URI = os.getenv(
    "DB_URI",
    "postgres://owjlzjxd:qA02MHoR8sfn-cj6OySOGAn5712sBvos@satao.db.elephantsql.com/owjlzjxd",
)

MAX_BOT = int(os.getenv("MAX_BOT", "25"))

SESSION_STRING = 'BQCW-PgAw77LHsgyZ-Yf7VTudiUku0u3mmXCnrUsQnVEEcXGTVEsQYnoNgMGeBtT3qfYQHBJe7-Xj4DGPDW8Lcm6gU_iqiF0lGseNxi_SzS_XE3zPxyIS0S-bBIFaQJ2VUQ5oV6k5K70ic7xQmf4pPA702-Bh54NkSz4SwnICcmuolzpTHDXoMDH2IQZw5PTGdjSqMJwMTPWSVfg67v1ugqObfjpgzRTLbXEC6SEPodU0o09TiAZ3pRX18IDL3giUmoxNgQt5Ou6x3T3CgowUq3exGJD88mrSCq-ePAhWr1N8C9bYhxWCfrNWxE7S_Q_Su6VJstZvy1R3nfrmHAndW8kQ7de8gAAAABqRVX4AA'  # Anda perlu membuat sesi pengguna untuk akun pengguna

DEVS = list(
    map(
        int,
        os.getenv(
            "DEVS",
            "2099942562 549827388",
        ).split(),
    )
)

REDISURL = redis.Redis(
  host='redis-16643.c321.us-east-1-2.ec2.redns.redis-cloud.com',
  port=16643,
  password='WHytJuaf63WZQ6UzzZZDHvzcqNiFr5wa'
)