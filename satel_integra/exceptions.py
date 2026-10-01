"""Custom exceptions for the Satel Integra library."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from satel_integra.commands import SatelOutboundCommand
    from satel_integra.models import SatelCommandResult


class SatelIntegraError(Exception):
    """Base exception for all library-specific errors."""


class SatelConnectionError(SatelIntegraError):
    """Raised when transport connection setup fails."""


class SatelConnectFailedError(SatelConnectionError):
    """Raised when the TCP connection to the panel cannot be established."""


class SatelConnectionSetupError(SatelConnectionError):
    """Raised when a TCP connection cannot be prepared for use."""


class SatelPanelBusyError(SatelConnectionSetupError):
    """Raised when the panel session is occupied by another client."""


class SatelConnectionInitializationError(SatelConnectionSetupError):
    """Raised when the panel does not complete connection setup successfully."""


class SatelConnectionStoppedError(SatelConnectionError):
    """Raised when the connection has been terminally stopped."""


class SatelUnexpectedResponseError(SatelIntegraError):
    """Raised when a panel response does not match the requested command."""


class SatelCommandRejectedError(SatelIntegraError):
    """Raised when the panel explicitly rejects a command with result 0xEF."""

    def __init__(
        self,
        command: SatelOutboundCommand,
        result: SatelCommandResult,
    ) -> None:
        self.command = command
        self.result = result
        super().__init__(
            f"Command {command} rejected with result 0x{int(result.code):02X}"
        )


class SatelMonitoringStartError(SatelIntegraError):
    """Raised when monitoring startup receives no successful acknowledgement."""


class SatelNotConnectedError(SatelConnectionError):
    """Command rejected because there is no connection to the panel (it is not queued until reconnection)."""


class SatelCommandExpiredError(SatelConnectionError):
    """Control command expired or was issued on a connection that no longer exists -
    it was not sent. Control commands are never sent late after a reconnection."""


class SatelNoResponseError(SatelIntegraError):
    """The panel did not acknowledge the command (no 0xEF in time) - the command may not have been
    executed, or the answer was lost; check the device state before retrying."""
