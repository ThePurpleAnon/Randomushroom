from worlds.LauncherComponents import Component, Type, components, launch
import settings
import asyncio


def run_client(ap_url = None) -> None:
    asyncio.run(run_client_async(ap_url))

async def run_client_async(ap_url = None):
    from .client import MushroomAgeClientRunner

    client = MushroomAgeClientRunner()
    await client.initialize()
    await client.start(ap_url)

components.append(
    Component(
        "Mushroom Age Client",
        func = run_client,
        game_name = "Mushroom Age",
        component_type = Type.CLIENT,
        supports_uri = True,
    )
)


class MushroomAgeSettings(settings.Group):
    class GameExecutable(settings.FilePath):
        """
        Path to your Mushroom Age game executable.
        """

        description = "Path to your game's executable file"
        is_exe = True

    game_exe: GameExecutable = GameExecutable("")