import asyncio


async def work(name: str, delay: int):
    await asyncio.sleep(delay)

    if name == 'B':
        raise Exception

    return f"{name} done"


async def main():
    async with asyncio.TaskGroup() as tg:
        t1 = tg.create_task(work("A", 2))
        t2 = tg.create_task(work("B", 1))
        t3 = tg.create_task(work("C", 1))

    # TaskGroup 블록 종료 시 모든 task 완료 보장
    print(t1.result())
    print(t2.result())
    print(t3.result())


asyncio.run(main())
