import asyncio
import os
from concurrent.futures import ProcessPoolExecutor


def cpu_heavy(n: int) -> int:
    s = 0
    for i in range(n):
        s += (i * i) % 97
    return s


async def run_one(loop, pool, sem: asyncio.Semaphore, n: int, timeout_s: float) -> int | Exception:
    async with sem:
        try:
            # 개별 작업 타임아웃
            return await asyncio.wait_for(loop.run_in_executor(pool, cpu_heavy, n), timeout=timeout_s)
        except Exception as e:
            return e


async def main():
    loop = asyncio.get_running_loop()
    job_sizes = [30_000_000, 20_000_000, 25_000_000, 15_000_000, 40_000_000]
    concurrency = 2
    timeout_s = 3.0

    sem = asyncio.Semaphore(concurrency)
    with ProcessPoolExecutor(max_workers=os.cpu_count() or 1) as pool:
        tasks = [asyncio.create_task(run_one(loop, pool, sem, n, timeout_s)) for n in job_sizes]
        results = await asyncio.gather(*tasks)

    for n, r in zip(job_sizes, results):
        if isinstance(r, Exception):
            print(f"n={n}: FAILED -> {type(r).__name__}: {r}")
        else:
            print(f"n={n}: OK -> {r}")


if __name__ == "__main__":
    asyncio.run(main())
