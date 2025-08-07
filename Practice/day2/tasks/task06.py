# TODO: Напишите асинхронную программу, которая отправляет HTTP-запросы к трём различным веб-сайтам:
#  "https://www.yandex.com", "https://www.google.com" и "https://www.python.org".
#  Как только от одного из сайтов будет получен ответ,
#  необходимо отменить выполнение запросов к остальным сайтам
#  и вывести время, затраченное на получение первого ответа.

import asyncio
import aiohttp
import time

async def fetch_data(url):
    """ Асинхронно получает содержимое URL."""
    async with aiohttp.request('GET', url) as response:
        content = await response.text()
        return url, content

async def main(urls):
    tasks = []
    for url in urls:
        task = asyncio.create_task(fetch_data(url))
        tasks.append(task)
    
    start_time = time.perf_counter()

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    first_task = list(done)[0]
    url, content = await first_task
    for task in pending:
        task.cancel()
    await asyncio.gather(*pending, return_exceptions=True)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    print(f"Первый ответ получен от: {url}")
    print(f"Время выполнения: {elapsed_time:.4f} секунд")
    print(f"Размер ответа: {len(content)} символов")


if __name__ == "__main__":
    urls = [
        "https://www.yandex.com",
        "https://www.google.com",
        "https://www.python.org"
    ]

    asyncio.run(main(urls))