import aiohttp, asyncio

async def fetch(session, url):
    async with session.get(url) as resp:
        data = await resp.json()
        print(data["title"])

async def main():
    urls = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1,6)]
    async with aiohttp.ClientSession() as s:
        await asyncio.gather(*(fetch(s, u) for u in urls))

asyncio.run(main())
