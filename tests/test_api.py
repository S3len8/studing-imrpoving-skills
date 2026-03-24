import pytest
from httpx import AsyncClient, ASGITransport
from main import app


@pytest.mark.asyncio # маркер для того, щоб коректно обробляти асинхронні функції
async def test_get_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test",) as ac:
        response = await ac.get("/books")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 2


@pytest.mark.asyncio # маркер для того, щоб коректно обробляти асинхронні функції
async def test_post_book():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test",) as ac:
        response = await ac.post("/books", json={"title": "Book 1", "author": "Author"})
        assert response.status_code == 200
        data = response.json()
        assert data == {"success": True, "message": "Книга додана"}