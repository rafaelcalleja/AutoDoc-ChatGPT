import os
import argparse
from modules.autodoc import AutoDoc
from modules.file import File
from modules.settings import *
import configparser

config = configparser.ConfigParser()
config.add_section("ChatGPT")
config.set("ChatGPT", "api_key", 'sk-')
config.read("config.ini")

auth = {
    "api_key": config["ChatGPT"]["api_key"],
}


parser = argparse.ArgumentParser(
    description="AutoDoc is a console application for generating code documentation using ChatGPT. Currently supports 1 language: Python. You can use an example file for any language using -example."
)


parser.add_argument("-file", type=str, help="Path to the code file.", required=True)

args = parser.parse_args()


if not os.path.exists(args.file):
    exit(f"[{RED}Error{RESET}] Code file does not exist")


file = File(args.file)

autodoc = AutoDoc(
    chatbot_config=auth,
    code=file.content(),
    language=file.language(),
)

result = autodoc.start()
file.create_commented_file(result)
