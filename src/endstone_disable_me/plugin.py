import uuid

from endstone.plugin import Plugin
from endstone.event import (
    event_handler,
    PlayerCommandEvent,
    PlayerLoginEvent,
    PlayerQuitEvent,
)


class DisableMe(Plugin):
    api_version = "0.5"

    def __init__(self) -> None:
        super().__init__()
        self._spam_counter: dict[uuid.UUID, int] = {}

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_login(self, event: PlayerLoginEvent) -> None:
        event.player.add_attachment(self, "minecraft.command.me", False)
        self._spam_counter[event.player.unique_id] = 0

    @event_handler
    def on_player_quit(self, event: PlayerQuitEvent) -> None:
        del self._spam_counter[event.player.unique_id]

    @event_handler
    def on_player_command(self, event: PlayerCommandEvent) -> None:
        command = event.command
        if command.count("@") >= 5:
            event.is_cancelled = True
            event.player.send_error_message(
                "You are not allowed to use selectors excessively."
            )
            self._spam_counter[event.player.unique_id] += 1

            if self._spam_counter[event.player.unique_id] >= 5:
                event.player.kick("You are not allowed to use selectors excessively.")
