import asyncio

async def fetch_user_input(queue, task_num):
    user_input = await asyncio.to_thread(input, f"Enter input for task {task_num}: ")
    await queue.put((task_num, user_input))

async def main():
    queue = asyncio.Queue()

    # Start input fetch tasks
    task1 = asyncio.create_task(fetch_user_input(queue, 1))
    task2 = asyncio.create_task(fetch_user_input(queue, 2))

    # Wait for one input from each task
    for _ in range(2):
        task_num, user_input = await queue.get()
        print(f"Task {task_num} got input: {user_input}")

    # Tasks are already complete here
    await asyncio.gather(task1, task2, return_exceptions=True)

asyncio.run(main())
