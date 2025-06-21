from onepush import notify
import yaml
import asyncio

with open("users.yaml", "r", encoding="utf-8") as f:
    users = yaml.load(f, Loader=yaml.FullLoader)

async def main():
    notifier = users["MOREPUSH"]["notifier"]
    params = users["MOREPUSH"]["params"]
    resp = await notify(
        notifier,
        title=f"【B站粉丝牌助手推送】",
        content="test",
        **params,
        proxy=users.get("PROXY"),
        )
    import inspect
    if inspect.iscoroutine(resp):
        resp = await resp
    print(f"{notifier} 已推送")
    print(resp)

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())