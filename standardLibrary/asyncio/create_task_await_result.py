import asyncio


async def work(name: str, delay: int) -> str:
    print(f"{name} started")
    await asyncio.sleep(delay)

    if name == "B":
        raise Exception

    print(f"{name} finished")
    return f"value: {name}"


async def main():
    # Task 생성
    task1 = asyncio.create_task(work("A", 2))
    task2 = asyncio.create_task(work("B", 1))
    task3 = asyncio.create_task(work("C", 1))

    print("Tasks created")

    # 완료 대기
    # await task1       # thread 안전하지 않음
    # await task2

    result1 = await task1
    result2 = await task2
    result3 = await task3

    # 결과 확인
    print("Task1 result:", result1)
    print("Task2 result:", result2)
    print("Task3 result:", result3)

asyncio.run(main())
