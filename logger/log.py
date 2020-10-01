import sys
import os
from datetime import datetime
from pathlib import Path

os.system("")

reset = "\u001b[0m"

class Styling:
    bold = "\33[1m"
    italic = "\33[3m"
    url = "\33[4m"
    blink = "\33[5m"
    underline = "\u001b[4m"
    reversed = "\u001b[7m"


class Color:
    black = "\u001b[38;5;0m"
    gray = "\u001b[38;5;8m"
    red = "\u001b[38;5;9m"
    green = "\u001b[38;5;10m"
    yellow = "\u001b[38;5;11m"
    blue = "\u001b[38;5;12m"
    purple = "\u001b[38;5;13m"
    cyan = "\u001b[38;5;14m"
    white = "\u001b[38;5;15m"


class BGColor:
    bg_black = "\u001b[48;5;0m"
    bg_gray = "\u001b[48;5;8m"
    bg_red = "\u001b[48;5;9m"
    bg_green = "\u001b[48;5;10m"
    bg_yellow = "\u001b[48;5;11m"
    bg_blue = "\u001b[48;5;12m"
    bg_purple = "\u001b[48;5;13m"
    bg_cyan = "\u001b[48;5;14m"
    bg_white = "\u001b[48;5;15m"


logger_options = {
    "save_to_file": False,
    "log_path": Path.cwd(),
    "log_timestamp_format": "[%Y-%m-%d %H:%M:%S]",
}


def ERROR(text):
    print(reset + Color.red + Styling.bold + "[-] Error: " + reset + text + reset)
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Error", text)


def WARNING(text):
    print(reset + Color.yellow + Styling.bold + "[!] Warning: " + reset + text + reset)
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Warn", text)


def INFO(text):
    print(reset + Color.blue + Styling.bold + "[?] Info: " + reset + text + reset)
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Info", text)


def SUCCESS(text):
    print(reset + Color.green + Styling.bold + "[+] Success: " + reset + text + reset)
    if logger_options["save_to_file"]:
        save_to_txt(logger_options["log_path"], "Success", text)


def enable_save_to_txt(path=""):
    if path != "":
        logger_options["log_path"] = path

    logger_options["save_to_file"] = True


def save_to_txt(path, type, message):
    time = datetime.now()
    text = (
        time.strftime(logger_options["log_timestamp_format"])
        + " - "
        + type.capitalize()
        + ": "
        + message
        + "\n"
    )

    file = open(Path.joinpath(logger_options["log_path"], "logs.txt"), "a+")
    file.write(text)


def set_log_timestamp_format(format: str):
    logger_options["log_timestamp_format"] = format


def setCustomColor(number):
    print(f"\u001b[38;5;{number}m")


def setCustomBGColor(number):
    print(f"\u001b[48;5;{number}m")
