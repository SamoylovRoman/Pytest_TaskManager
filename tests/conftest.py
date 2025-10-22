import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base
from app.task_service import get_db

# ✅ Use in-memory SQLite database for tests
TEST_DATABASE_URL = "sqlite:///:memory:"

@pytest.fixture(scope="function")
def test_db():
    # Create an in-memory SQLite engine
    engine = create_engine(TEST_DATABASE_URL, echo=False)

    # Create tables fresh for every test
    Base.metadata.create_all(bind=engine)

    # Create a new session bound to the test engine
    TestingSessionLocal = sessionmaker(bind=engine)
    db = TestingSessionLocal()

    try:
        yield db
    finally:
        db.close()
