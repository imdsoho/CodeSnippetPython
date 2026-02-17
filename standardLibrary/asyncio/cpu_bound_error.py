import asyncio
from concurrent.futures import ProcessPoolExecutor


def cpu_heavy(x):
    return sum(i * i for i in range(10000000))


'''
def main():
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(cpu_heavy, range(10)))
        print(results)

if __name__ == '__main__':
    main()
'''


async def main():
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_heavy, 10)
        print(result)


asyncio.run(main())         # Error
# CPU-bound 작업은 event loop를 block 합니다.
# concurrent.futures.process.BrokenProcessPool:
# A process in the process pool was terminated abruptly while the future was running or pending.


'''if __name__ == '__main__':
    asyncio.run(main())     # 333333283333335000000'''

