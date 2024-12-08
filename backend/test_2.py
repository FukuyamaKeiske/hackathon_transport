import httpx
from bs4 import BeautifulSoup
from typing import List, Dict

async def get_cameras_data() -> List[Dict]:
    cameras = []
    base_url = "https://www.geocam.ru/in/all/traffic/"
    
    async with httpx.AsyncClient() as client:
        for page in range(1, 60):  # 59 страниц
            print(f"Loading page {page}")
            url = f"{base_url}{page}/" if page > 1 else base_url
            response = await client.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            cam_cards = soup.find_all('li', class_='cam_card')
            for cam in cam_cards:
                link_tag = cam.find('a')
                name = link_tag.find('b').text.strip()
                print(f"found {name}")
                camera_page_url = link_tag['href']  # Ссылка на страницу камеры
                geo = cam.find('span', class_='cam_geo').text.strip()
                description = cam.find('div', class_='cam_small_info').text.strip()

                # Получаем ссылку на трансляцию с отдельной страницы камеры
                live_url = await get_live_url(camera_page_url)

                cameras.append({
                    "name": name,
                    "live_url": live_url,
                    "geo": geo,
                    "description": description
                })
    
    return cameras

async def get_live_url(camera_page_url: str) -> str:
    # Полный URL страницы камеры
    print(f"working with https://www.geocam.ru{camera_page_url}")
    full_url = f"https://www.geocam.ru{camera_page_url}"
    
    async with httpx.AsyncClient() as client:
        response = await client.get(full_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Ищем тег <iframe> для получения ссылки на трансляцию
        iframe = soup.find('iframe')
        if iframe and 'src' in iframe.attrs:
            print(f"catched {iframe['src']}")
            return iframe['src']  # Возвращаем ссылку на трансляцию

    return ""  # Возвращаем пустую строку, если трансляция не найдена

import asyncio
print(asyncio.run(get_cameras_data()))
