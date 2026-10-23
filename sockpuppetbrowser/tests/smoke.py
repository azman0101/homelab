import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for attempt in range(40):
            try:
                browser = await p.chromium.connect_over_cdp("ws://browser:3000/?--no-sandbox", timeout=5000)
                break
            except Exception:
                if attempt == 39:
                    raise
                await asyncio.sleep(1)
        page = await browser.new_page()
        await page.set_content("<div id='result'></div><script>document.querySelector('#result').textContent = String(6 * 7)</script>")
        assert await page.locator('#result').inner_text() == '42'
        assert (await page.screenshot()).startswith(b'\x89PNG')
        print('JavaScript rendering and PNG screenshot passed')
        await browser.close()

asyncio.run(main())
