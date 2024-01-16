import asyncio

async def producer(queue):
    for i in range(1):
        in_p = input("number\n")
        await queue.put(in_p)
        print(f"Produced {in_p}")

    await asyncio.sleep(1)

    for i in range(1):
        in_p = input("number\n")
        await queue.put(in_p)
        print(f"Produced {in_p}")



async def consumer(queue):
    
    while True:
        while True:
            await asyncio.sleep(1)
            if queue.empty():
                await producer(queue)
                break
            else:
                item = await queue.get()
            print(f"Consumed {item}")
            queue.task_done()

        print("break\n")

        


async def main():
    queue = asyncio.Queue()
    produce_event = asyncio.Event()

    # Initially set the event to start production
    produce_event.set()
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))
    await asyncio.gather(consumer_task, producer_task)
    
    # await asyncio.sleep(1)  # Give some time for the producer to add items
    # await queue.join()      # Wait until all items are processed

    # consumer_task.cancel()  # Cancel the consumer

asyncio.run(main())
