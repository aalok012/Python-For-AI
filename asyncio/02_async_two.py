import asyncio

async def prep(name):
    print(f"Preparing{name}")
    await asyncio.sleep(2)
    print(f"{name} is ready")
    
async def main():
    await asyncio.gather (
        prep("Bao chicken"),
        prep("Kungpao chicken"),
        prep("Orange chicken"),
    )
asyncio.run(main())
    