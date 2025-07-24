"""Support for Visonic alarm control panel."""

from homeassistant.components.alarm_control_panel import AlarmControlPanelEntity
from homeassistant.const import STATE_ALARM_ARMED_AWAY, STATE_ALARM_DISARMED

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    async_add_entities([VisonicAlarm()])

class VisonicAlarm(AlarmControlPanelEntity):
    def __init__(self):
        self._state = STATE_ALARM_DISARMED

    @property
    def name(self):
        return "Visonic Alarm"

    @property
    def state(self):
        return self._state

    async def async_alarm_arm_away(self, code=None):
        self._state = STATE_ALARM_ARMED_AWAY
        self.async_write_ha_state()

    async def async_alarm_disarm(self, code=None):
        self._state = STATE_ALARM_DISARMED
        self.async_write_ha_state()
