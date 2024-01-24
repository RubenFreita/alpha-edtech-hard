import asyncio

async def task(sem, task_name):
    async with sem:
        print(f"{task_name} starting")
    await asyncio.sleep(2)
    print(f"{task_name} finishing")

async def main():
    sem = asyncio.Semaphore(2)

    tasks = [task(sem, f"Task {i}") for i in range(5)]

    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
