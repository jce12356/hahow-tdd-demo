import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from sqlalchemy import String
from models import Board
from datetime import datetime


def get_ptt_boards():
    url = "https://www.ptt.cc/bbs/index.html"

    resp = requests.get(url=url)
    soup = BeautifulSoup(resp.text, "lxml")

    result = []
    for tmp in soup.find_all(name="div", attrs={"class": "board-name"}):
        result.append(tmp.text)

    return result


def insert_ptt_board(name: str, session: Session):
    board = Board(
        name=name,
        created_time=datetime.now()
    )
    session.add(board)
