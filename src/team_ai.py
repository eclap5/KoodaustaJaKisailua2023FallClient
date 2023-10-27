from __future__ import annotations

from logging import getLogger
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apiwrapper.websocket_wrapper import ClientContext
from src.apiwrapper.models import GameState, Command


ai_logger = getLogger("ai")


def process_tick(context: ClientContext, game_state: GameState) -> Command | None:
    ai_logger.debug("processing tick")
    return None
