import asyncio
import json
from aiohttp import ClientSession
from src import BiliUser, BiliApi


async def test_login_verify():
    access_key = ""
    refresh_key = ""
    user = BiliUser(access_key, refresh_key)
    async with ClientSession() as session:
        api = BiliApi(user, session)
        try:
            result = await api.refreshToken()
            print("refreshToken result:")
            print(result)
            # Save result to JSON file
            with open("refresh_token_result.json", "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print("Result saved to refresh_token_result.json")
        except Exception as e:
            print(f"refreshToken failed: {e.args}")
if __name__ == "__main__":
    asyncio.run(test_login_verify())

