from endstone.plugin import Plugin
from endstone.event import event_handler, ServerCommandEvent, PlayerLoginEvent


class DisableMe(Plugin):
    api_version = 0.5

    def on_enable(self) -> None:
        self.register_events(self)

    @event_handler
    def on_player_login(self, event: PlayerLoginEvent) -> None:
        event.player.add_attachment(self, "minecraft.command.me", False)

    @event_handler
    def on_command_preprocess(self, event: ServerCommandEvent) -> None:
        command = event.command
        if command.count("@") >= 5:
            event.cancelled = True
            event.sender.send_error_message("You are not allowed to use selectors excessively.")
