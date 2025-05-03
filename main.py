import aiohttp
import asyncio
from holfuy import HolfuyService


async def main():
    async with aiohttp.ClientSession() as session:
        s = HolfuyService("", session)
        data = await s.fetch_data(["101"])
        print(data)


if __name__ == "__main__":
    asyncio.run(main())
