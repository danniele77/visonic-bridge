import requests
import logging
from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity
from homeassistant.const import STATE_ALARM_ARMED_AWAY, STATE_ALARM_DISARMED

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([VisonicBridgeAlarm()])

class VisonicBridgeAlarm(AlarmControlPanelEntity):
    def __init__(self):
        self._state = STATE_ALARM_DISARMED

    @property
    def name(self):
        return "Visonic Alarm"

    @property
    def state(self):
        return self._state

    def alarm_arm_away(self, code=None):
        try:
            requests.get("http://IP_DEL_BRIDGE:PORT/arm")
            self._state = STATE_ALARM_ARMED_AWAY
        except Exception as e:
            _LOGGER.error(f"Error arming: {e}")

    def alarm_disarm(self, code=None):
        try:
            requests.get("http://IP_DEL_BRIDGE:PORT/disarm")
            self._state = STATE_ALARM_DISARMED
        except Exception as e:
            _LOGGER.error(f"Error disarming: {e}")
