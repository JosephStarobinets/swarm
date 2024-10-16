from swarm.repl import run_demo_loop
from agents import triage_agent
from dotenv import load_dotenv
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the .env file
dotenv_path = os.path.join(current_dir, '.env')
# Load the .env file
load_dotenv(dotenv_path)

if __name__ == "__main__":
    run_demo_loop(triage_agent)
