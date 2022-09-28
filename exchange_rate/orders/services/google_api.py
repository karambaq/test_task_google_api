import os
from dotenv import load_dotenv
from collections import namedtuple

import gspread
from oauth2client.service_account import ServiceAccountCredentials

load_dotenv()
SHEET_NAME = os.getenv("SHEET_NAME")
URL = os.getenv("SHEET_URL")


def auth():
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive",
    ]

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        "sec.json", scope
    )

    return gspread.authorize(credentials)


def get_worksheet():
    gc = auth()
    return gc.open_by_url(URL).worksheet(SHEET_NAME)


# print(get_worksheet())
