import asyncio
import random

async def wait_random():
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    print(f"Задача завершилась через {delay} секунд")
    return delay


# TODO: дана асинхронная функция которая ждет случайное количество секунд (от 1 до 5)
#  Создайте 3 корутины, и запустите их асинхронно с помощью asyncio.gather().

async def main():
    # Создаем 3 задачи
    task1 = asyncio.create_task(wait_random())
    task2 = asyncio.create_task(wait_random())
    task3 = asyncio.create_task(wait_random())
    
    results = await asyncio.gather(task1, task2, task3)
    #print("Результаты:", *results)

if __name__ == '__main__':
    asyncio.run(main())