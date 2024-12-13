from pyrogram import Client

plugins = dict(root="plugins")

app = Client('selfbot', api_id=6204272, api_hash='f935feb4ce106e741675d2e0894c6155',
             bot_token='7547643768:AAGQ3DmHQM3jDZUmabA36UJuRQbjNYtoKtk', plugins=plugins)

print('Bot is running...')
app.run()
