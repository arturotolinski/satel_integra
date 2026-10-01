"""Constants for the Satel Integra integration."""

from collections.abc import Awaitable, Callable

FRAME_START = bytes([0xFE, 0xFE])
FRAME_END = bytes([0xFE, 0x0D])

FRAME_SPECIAL_BYTES = bytes([0xFE])
FRAME_SPECIAL_BYTES_REPLACEMENT = bytes([0xFE, 0xF0])

MESSAGE_RESPONSE_TIMEOUT = 5
KEEPALIVE_INTERVAL = 15

ConnectionStateCallback = Callable[[], None | Awaitable[None]]
UnsubscribeCallback = Callable[[], None]

# Re-send 0x7F (+12 bytes) on the same connection this often; the module then re-sends the full monitored state
MONITORING_REFRESH_S = 300

# A control command (outputs, arming) is valid only this long after being issued, and only on that connection
CONTROL_COMMAND_TTL_S = 3

# This many seconds without any frame from the panel (with keepalive every KEEPALIVE_INTERVAL) = dead link
INBOUND_SILENCE_S = 45
