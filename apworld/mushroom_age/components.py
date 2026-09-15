from worlds.LauncherComponents import Component, Type, components, launch


def run_client(*args: str) -> None:
    ...

components.append(
    Component(
        "Mushroom Age Client",
        func=run_client,
        game_name="Mushroom Age",
        component_type=Type.CLIENT,
        supports_uri=True,
    )
)