import os
import dotenv

def load_env():
    env_path = os.path.abspath(os.path.join(__file__, "..", "..", ".env"))
    path_migrate = os.path.abspath(os.path.join(__file__, "..", "migrations"))
    
    if os.path.exists(path= env_path):
        dotenv.load_dotenv(dotenv_path= env_path)
        if not os.path.exists(path= path_migrate):
            os.system(command= os.environ["DB_INIT"])
            
        os.system(command= os.environ["DB_MIGRATE"])
        os.system(command= os.environ["DB_UPGRADE"])