from dotenv import load_dotenv
from pydantic.v1 import BaseSettings

load_dotenv()


class Settings(BaseSettings):

    class Config:
        env_file = '.env'


settings = Settings()