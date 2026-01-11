import asyncio

async def prepare_order():
    print("Preeparing order...")
    await asyncio.sleep(2)
    print("Order is ready")
    
    
asyncio.run(prepare_order())