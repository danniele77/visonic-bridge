"""Visonic integration."""

import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup(hass, config):
    _LOGGER.info("Visonic integration initialized")
    return True
