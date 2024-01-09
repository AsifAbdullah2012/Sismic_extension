import asyncio

async def execute_program():
    while True:
        # Replace with your program's logic
        await asyncio.sleep(1)  # Simulating async work with sleep
        print("Program is running")

async def listen_for_input():
    while True:
        user_input = await asyncio.to_thread(input, "Enter your command: ")
        if user_input == 'exit':
            break
        print(f"Received input: {user_input}")

async def main():
    task1 = asyncio.create_task(execute_program())
    task2 = asyncio.create_task(listen_for_input())
    task3 = asyncio.create_task(listen_for_input())

    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
