import pytest
from fastapi.testclient import TestClient
from main import app  # Убедитесь, что импорт корректен

client = TestClient(app)  # Создаём экземпляр TestClient

@pytest.mark.asyncio
async def test_list_cameras(mocker):
    # Мокаем функцию получения данных о камерах
    mock_cameras = [
        {
            "name": "Веб-камера у переправы через Обь со стороны Лабытнанги",
            "live_url": "https://video.connect-online.ru/vsaas/embed/pereprava.labytnangi-9eba67ed01?dvr=false",
            "geo": "Лабытнанги, Россия",
            "description": "Онлайн веб-камера показывает переправу через Обь."
        },
        {
            "name": "Веб-камера на Волгоградском проспекте в Москве",
            "live_url": "https://video.connect-online.ru/vsaas/embed/volgogradskiy-prospekt-123456789?dvr=false",
            "geo": "Москва, Россия",
            "description": "Веб-камера на Волгоградском проспекте."
        }
    ]
    
    # Убедитесь, что путь к функции верный
    mocker.patch("app.services.camera_management.get_cameras_data", return_value=mock_cameras)

    response = client.get("/api/v1/cameras/1")  # Используем TestClient для запроса
    assert response.status_code == 200
    assert len(response.json()) == 2
    assert response.json()[0]["name"] == mock_cameras[0]["name"]
    assert response.json()[0]["live_url"] == mock_cameras[0]["live_url"]
    assert response.json()[0]["geo"] == mock_cameras[0]["geo"]
    assert response.json()[0]["description"] == mock_cameras[0]["description"]

@pytest.mark.asyncio
async def test_live_url_parsing(mocker):
    # Мокаем httpx.AsyncClient для тестирования функции получения live_url
    mock_html = '''
    <html>
        <body>
            <iframe width="720" height="405" src="https://video.connect-online.ru/vsaas/embed/test-camera?dvr=false" frameborder="0" allowfullscreen=""></iframe>
        </body>
    </html>
    '''
    
    mocker.patch("httpx.AsyncClient.get", return_value=mocker.Mock(text=mock_html))

    from app.services.camera_management import get_live_url

    live_url = await get_live_url("/online/test-camera/")
    assert live_url == "https://video.connect-online.ru/vsaas/embed/test-camera?dvr=false"
