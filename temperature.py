"""
CPU temperature component for iTerm 2
Author: Ryan Sheatsley
Sat FEb 29 2020
"""

import iterm2
from subprocess import check_output


async def main(connection, update_cadence=5):

    # configure iTerm2 status bar interface
    knobs = [iterm2.StringKnob("CPU Temperature", "N/A", "", "CPU")]
    component = iterm2.StatusBarComponent(
        short_description="CPU temperature",
        detailed_description="Reads CPU temperature at a specified refresh rate",
        knobs=knobs,
        exemplar="48.8°C",
        update_cadence=update_cadence,
        identifier="com.github.sheatsley.temperature",
    )

    @iterm2.StatusBarRPC
    async def temperature_component(knobs):
        return check_output("/usr/local/bin/osx-cpu-temp", encoding="utf-8").strip()

    await component.async_register(connection, temperature_component)


iterm2.run_forever(main)
