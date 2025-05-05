from enum import StrEnum

from httpcord import (
    CommandResponse,
    HTTPBot,
    Interaction,
)
from httpcord.enums import InteractionResponseType


CLIENT_ID = 0000000000000000000000
CLIENT_PUBLIC_KEY = "..."
CLIENT_TOKEN = "..."


bot = HTTPBot(
    client_id=CLIENT_ID,
    client_public_key=CLIENT_PUBLIC_KEY,
    register_commands_on_startup=True,
)


class Fruits(StrEnum):
    apples = "apples"
    cherries = "cherries"
    kiwis = "kiwis"
    oranges = "oranges"

@bot.command("pick")
async def pick(interaction: Interaction, *, fruit: Fruits) -> CommandResponse:
    return CommandResponse(
        InteractionResponseType.CHANNEL_MESSAGE_WITH_SOURCE,
        content=f"You picked: {fruit.value}!",
    )


bot.start(CLIENT_TOKEN)