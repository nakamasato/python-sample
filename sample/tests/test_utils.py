from utils.database import get_database

def test_get_database():
    assert get_database() == 'database'