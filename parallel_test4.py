import asyncio

async def producer(queue):
    for i in range(5):
        await queue.put(i)
        print(f"Produced {i}")
        await asyncio.sleep(1)
    await queue.put(None)  # Sentinel value to indicate the end

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:
            queue.task_done()
            break  # End when the sentinel value is seen
        print(f"Consumed {item}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()
    prod_task = asyncio.create_task(producer(queue))
    cons_task = asyncio.create_task(consumer(queue))

    await asyncio.gather(prod_task, cons_task)

asyncio.run(main())
