from telethon.sync import TelegramClient
from telethon import events
from telethon.tl import types

api_id = 21827985
api_hash = '249159e0fc539bb9bce0d5e974c44f88'

phone = '+601156292264'
session_file = 'xzy0207'
password = '0207'

response_message = "11"  # Updated auto-reply message
group_chat_ids = [-1001766161750, -1001863685543]
sender_ids = [1814850031, 6070986947, 1518090731, 5042719163]

async def main():
    async with TelegramClient(session_file, api_id, api_hash) as client:
        @client.on(events.NewMessage())
        async def auto_reply(event):
            if (
                event.media
                and isinstance(event.media, types.MessageMediaPhoto)
                and event.chat_id in group_chat_ids
                and event.sender_id in sender_ids
            ):
                sender = await event.get_sender()

                # Respond with the updated message "11"
                await event.respond(response_message)

        await client.start(phone)
        await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
