#  automate-home - This is an automation framework.

# Github: https://github.com/majamassarini/automate-home
# Docs: https://automate-home.readthedocs.io/en/latest/?badge=latest


import home


state = home.appliance.curtain.outdoor.state.opened.State()

state.compute()
'Opened'

state = state.next(home.appliance.curtain.event.forced.Event.Closed)

state.compute()
'Forced Closed'

state = state.unforce()

state.compute()
'Opened'

state = state.next(home.event.sun.twilight.civil.Event.Sunset)

state.compute()
'Closed'

state = state.next(home.event.sun.twilight.civil.Event.Sunrise)

state.compute()
'Opened'


# Default state is Off.

import home


p = home.appliance.light.presence.Appliance("an indoor presence light", [])
_, new = p.notify(home.appliance.light.event.forced.Event.On)
new.compute()
# 'Forced On'
_, new = p.notify(home.event.presence.Event.Off)
# new.compute()
# 'Off'
_, new = p.notify(home.event.presence.Event.On)
# new.compute()
# 'Off'
