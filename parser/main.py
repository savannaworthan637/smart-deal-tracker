import asyncio
import aiohttp
from sources import steam, epicgames, amazon

async def main():
    tasks = [
        steam.fetch_deals(),
        epicgames.fetch_deals(),
        amazon.fetch_deals(),
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
