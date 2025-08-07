# TODO: Создайте несколько асинхронных задач с разными задержками.
#  Используйте asyncio.as_completed() для обработки результатов задач по мере их завершения.
#  Выведите результаты каждой задачи сразу после ее завершения.

import asyncio
import random

async def wait_random(task_id: int):
    base_delay = random.randint(1, 5)
    sleep_time = base_delay * (task_id + 1) * 0.33
    
    await asyncio.sleep(sleep_time)
    return f"Результат задачи {task_id} (задержка: {sleep_time:.1f}с)"

async def main():
    num_tasks = 5
    tasks = [asyncio.create_task(wait_random(i)) for i in range(num_tasks)]
    
    for completed_task in asyncio.as_completed(tasks):
        result = await completed_task
        print(f'Получен результат: {result}')

if __name__ == '__main__':
    asyncio.run(main())