from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerLoginEvent


class DisableMe(Plugin):
    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_login(self, event: PlayerLoginEvent) -> None:
        event.player.add_attachment(self, "minecraft.command.me", False)
