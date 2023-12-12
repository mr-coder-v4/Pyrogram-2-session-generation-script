import os
from pyrogram import Client
from pyrogram import errors
import pyfiglet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def initialize_app():
    clear_screen()
    print(pyfiglet.figlet_format("Radhe"))
    print("Welcome! Please register at https://my.telegram.org/apps to obtain app_id and api_hash")

    api_id = input("Insert app_id: ")
    app_hash = input("Insert api_hash: ")

    with Client(":memory:", api_id, app_hash) as app:
        session_string = app.export_session_string()
        try:
            app.send_message("me", f"Here is your generated Pyrogram session string: \n\n<code>{session_string}</code>")
        except errors.FloodWait as e:
            print(f"An error occurred: {e}")
        except errors.ChatWriteForbidden as e:
            print(f"An error occurred: {e}")

    clear_screen()
    print(f"Your session string is: {session_string}")
    print("1. You can find a copy of the session string in your Saved Messages.")
    print("2. Save this session string to a file and use it in your bot.")
    input("\nPress 'Enter' to continue")

if __name__ == "__main__":
    initialize_app()
