import asyncio
import random


async def dynamic_work(i: int):
    delay = random.uniform(0.5, 2)
    await asyncio.sleep(delay)
    return f"Task {i} finished in {delay:.2f}s"


async def main(n: int):
    tasks = [asyncio.create_task(dynamic_work(i)) for i in range(n)]

    for task in asyncio.as_completed(tasks):
        result = await task
        print("Completed:", result)


asyncio.run(main(7))
