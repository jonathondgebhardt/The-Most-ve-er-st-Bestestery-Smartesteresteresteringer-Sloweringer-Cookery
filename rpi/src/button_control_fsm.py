from state_machine import state_machine

# can I set universal variable here? I want read ports for the buttons
# and  inputs from the app.. they need to be visible to almost all the
# states..

# return seems to control which state is next so probably don't need 
# the clocked process to control
def idle_state():
	if(POWER == high):
		next_state <= "on_off_state"
	else:
		next_state <= "idle_state"
	previous_state <= "idle_state"
    return (next_state)

def on_off_state():
	if(POWER == low):
		next_state <= "idle_state"
	elif(ON_OFF == high):
		next_state <= "sel_state"
	else:
		next_state <= "on_off_state"
	previous_state <= "on_off_state"
    return (next_state)

def sel_state():
	if(POWER == low):
		next_state <= "idle_state"
	elif(ON_OFF == high || INACTIVITY_TIMER_MET == high):
		next_state <= "on_off_state"
	elif(PROGRAM_R == high):
		next_state <= "cook_time_state"
	elif(PROBE_R == high || MANUAL_R == high):
		next_state <= "heat_setting_state"
	else:
		next_state <= "sel_state"
	previous_state <= "sel_state"
    return (next_state)

def cook_time_state():
	if(POWER == low):
		next_state <= "idle_state"
	elif(ON_OFF == high):
		next_state <= "on_off_state"
	elif(INACTIVITY_TIMER_MET == high):
		next_state <= "sel_state"
	elif(ENTER_R == high):
		next_state <= "heat_setting_state"
	elif(MANUAL_R == high || PROBE_R == high):
		next_state <= "heat_setting_state"
	else:
		next_state <= "cook_time_state"
	previous_state <= "cook_time_state"
    return (next_state)

def heat_setting_state():
	if(POWER == low):
		next_state <= "idle_state"
	elif(ON_OFF == high):
		next_state <= "on_off_state"
	elif(INACTIVITY_TIMER_MET == high && user_selection == probe):
		next_state <= "sel_state"
	elif(START_TIMER_MET == high && user_selection != probe):
		next_state <= "display_state"
	elif(ENTER_R == high):
		if(user_selection != probe):
			next_state <= "display_state"
		elif(heat_selection == _warm):
			next_state <= "display_state"
		else:
			next_state <= "temp_setting_state"
	elif(PROGRAM_R == high):
		next_state <= "cook_time_state"
	else
		next_state <= "heat_setting_state"
	previous_state <= "heat_setting_state"
    return (next_state)
	
def temp_setting_state():
	if(POWER == low):
		next_state <= "idle_state"
	elsif(ON_OFF == high):
		next_state <= "on_off_state"
	elsif(START_TIMER_MET == high || ENTER_R == high):
		next_state <= "display_state"
	elsif(MANUAL_R == high):
		next_state <= "heat_setting_state"
	elsif(PROGRAM_R == high):
		next_state <= "cook_time_state"
	else
		next_state <= "temp_setting_state"
	previous_state <= "temp_setting_state"
	return (next_state)

def display_state():
	if(POWER == low):
		next_state <= "idle_state;"
	elif(ON_OFF == high):
		next_state <= "on_off_state"
	elif(ON_OFF_TIMER_MET == high):
		next_state <= "idle_state"
	elif(PROGRAM_R == high):
		next_state <= "cook_time_state"
	elif(MANUAL_R == high || PROBE_R == high):
		next_state <= "heat_setting_state"
	else:
		next_state <= "display_state"
	previous_state <= "display_state"
	return (next_state)

def power_time_met_state():
	return (next_state)

if __name__== "__main__":
    m = StateMachine()
    m.add_state("idle", idle_state)
    m.add_state("on_off", on_off_state)
    m.add_state("select", sel_state)
    m.add_state("cook_time", cook_time_state)
    m.add_state("heat_setting", heat_setting_state)
    m.add_state("temp_setting", temp_setting_state)
    m.add_state("display", display_state)
	m.add_state("power_time_met_state", None, end_state=1)
    m.set_start("idle") #this is the start command
