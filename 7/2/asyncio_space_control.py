import asyncio

async def fetch_data(source, duration):
    await asyncio.sleep(duration)
    print(f"Fetched data from {source} after {duration} seconds")

async def main():
    sources = [("Telemetry", 2), ("Imaging", 3), ("Navigation", 1)]
    tasks = [fetch_data(source, duration) for source, duration in sources]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
