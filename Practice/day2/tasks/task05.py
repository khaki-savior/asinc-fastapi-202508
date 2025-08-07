# TODO: Создайте корутину, которая ждет 5 секунд.
#  Запустите ее как задачу и отмените ее через 2 секунды.

import asyncio


async def my_coroutine(n: int):
    await asyncio.sleep(5)
    print(f'Корутина {n} завершилась.')
    return f"Результат {n}"

async def main():
    task = asyncio.create_task(my_coroutine(1))

    try:
        result = await asyncio.wait_for(task, timeout=2.0)
    except asyncio.TimeoutError:
        task.cancel()
        try:
            await task  # Ждем !!завершения ОТМЕНЫ!!
        except asyncio.CancelledError:
            print("Задача была отменена")

    print(f"Статус задачи: отменена={task.cancelled()}, завершена={task.done()}")

if __name__ == '__main__':
    asyncio.run(main())