from main import get_ptt_boards, insert_ptt_board
from models import Board
from sqlalchemy import Column, String

def test_get_ptt_boards():
    expected = "Stock"

    result = get_ptt_boards()
    print(result)

    assert expected in result


def test_insert_ptt_board(sqlite_session):
    expected = "test"

    insert_ptt_board(name=expected, session=sqlite_session)

    assert sqlite_session.query(Board).first().name == expected
