# TODO: Создайте 4 корутины, каждая из которых возвращает строку.
#  Запустите их параллельно и соберите результаты в список.

import asyncio
import random

async def get_text():
    multiplier = random.randint(1,5)
    await asyncio.sleep(multiplier)
    #print(multiplier)
    return multiplier*'42'

async def main():
    num_tasks = 4

    tasks = [asyncio.create_task(get_text()) for _ in range(num_tasks)]
    results = await asyncio.gather(*tasks)

    print("Результаты:", results)

if __name__ == '__main__':
    asyncio.run(main())