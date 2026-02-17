import asyncio


async def work(x: int) -> int:
    await asyncio.sleep(1)

    '''if x == 3:
        raise Exception'''

    return x * 2


async def main():
    tasks = [work(i) for i in range(5)]

    # 그룹 실행
    results = await asyncio.gather(*tasks)
    # results = await asyncio.gather(*tasks, return_exceptions=True)

    print("Results:", results)


asyncio.run(main())
