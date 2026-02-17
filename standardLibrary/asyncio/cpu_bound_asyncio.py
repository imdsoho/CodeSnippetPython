import asyncio
import os
import time
from concurrent.futures import ProcessPoolExecutor


def cpu_heavy(n: int) -> int:
    # 예시: 큰 정수 연산(파이썬 루프) -> CPU-bound
    s = 0
    for i in range(n):
        s += (i * i) % 97
    return n, s


async def run_cpu_jobs(job_sizes: list[int], workers: int | None = None) -> list[int]:
    loop = asyncio.get_running_loop()

    # 프로세스 수(기본: os.cpu_count())
    max_workers = workers or (os.cpu_count() or 1)

    results: list[int] = []
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        # CPU 작업을 프로세스 풀로 제출 (event loop가 block되지 않음)
        tasks = [
            loop.run_in_executor(pool, cpu_heavy, n) for n in job_sizes
        ]

        # 완료되는 순서대로 결과 수집
        for fut in asyncio.as_completed(tasks):
            r = await fut

            # print(r)  # (15000000, 719999710)
                        # (20000000, 960000099)
                        # (25000000, 1200000162)
                        # (30000000, 1439999839)

            results.append(r)

    return results


async def main():
    job_sizes = [30000000, 20000000, 25000000, 15000000]
    t0 = time.perf_counter()

    results = await run_cpu_jobs(job_sizes, workers=4)

    dt = time.perf_counter() - t0
    print("results(count):", len(results))
    print(f"elapsed: {dt:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
