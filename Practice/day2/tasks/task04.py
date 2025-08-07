# TODO: Напишите асинхронную программу, которая запускает n асинхронных функции. 
#  n - задайте самостоятельно.
#  Каждая функция должна возвращать случайное целое число в диапазоне от 0 до 10
#  и выполняться за случайное время от 1 до 5 секунд
#  После завершения всех функций найдите сумму всех полученных результатов и выведите её на экран.

import asyncio
import random

async def wait_random(task_id: int) -> int:
    base_delay = random.randint(1, 5)
    await asyncio.sleep(base_delay)
    random_number = random.randint(0, 10)
    print(f"Результат задачи {task_id}: {random_number} (задержка: {base_delay:.1f}с)")
    return random_number

async def main():
    num_tasks = 4
    tasks = [asyncio.create_task(wait_random(i)) for i in range(num_tasks)]
    
    total_sum = await asyncio.gather(*tasks)
    print(f'Получен результат: {sum(total_sum)}')

if __name__ == '__main__':
    asyncio.run(main())