#######################################
#
#      Create int_trmr experiment using PsychoPy
#
#######################################
#
# Author: Julius Welzel (Neurogeriatrie, UKSH Kiel,University of Kiel)
# Contact: j.welzel@neurologie.uni-kiel.de
# Version: 1.0 // setting up default (15.12.2020)
# -*- coding: utf-8 -*-

from psychopy import locale_setup, visual, core, event
import numpy as np
import time
from pylsl import StreamInfo, StreamOutlet, local_clock

## ################    Setup     ####################
# set LSL streams
s_info      = StreamInfo(name='PsychoPyTrigger', type = 'Markers', channel_count=1,
                  channel_format='string')

trig_out    = StreamOutlet(s_info)

input('Start LabRecorder and than press enter')


# Set window and remove mouse during experiment:
win_size = (1920,1200)
win = visual.Window(size = win_size, fullscr = True, allowGUI = False,
                    monitor='testMonitor', units='norm',color = [-1,-1,-1])



# Experimental settings
dur_exp     = 0.2 # full exprimental time
dur_hit     = 0.5


## ################    Stimuli     ####################

## intro
intro_text = visual.TextStim(win,
                             pos=[0,0],
                             color = (1,1,1)
                             )
intro_text.text = """
Gleich sehen Sie einen schwarzen Bildschirm. Sobald eine rote Zahl erscheint, drücken Sie die Leertaste so schnell Sie können.
Das Ganze Experiment dauert 5 Minuten. Starten Sie das Experiment mit der Leertaste.
"""

# text ms for display
ms_text = visual.TextStim(win,
                             pos=[0,0],
                             color = (1,-1,-1),
                             height = 0.6
                             )


fixation =  visual.TextStim(win,
                            pos=[0,0],
                            text = '+',
                            height = 0.7,
                            color = (1,1,1)
                            )

jit_list = np.array(0)

while jit_list.sum() < 300:
    jit_list = np.random.randint(20,100,50)/10


resp_key    = event.getKeys()
resp_mouse  = event.Mouse()

# INTRO
intro_text.draw()
win.flip()
event.waitKeys()

intro_text.text = "TRAINING"
intro_text.draw()
win.flip()
core.wait(3)


####################  Training Block ###################################

#Set timer:
cntdwn_exp = core.CountdownTimer(dur_exp * 60)
init_ts = local_clock()
trig_out.push_sample(['Experiment start'])

for i in range(8):

    fixation.draw()
    win.flip()
    trig_out.push_sample(['BL start'])
    jitter = jit_list[np.random.randint(1,49)]
    core.wait(jitter)

    #TRIAL

    bp_space = True
    timer = core.getTime() # start trial timer

    all_rt = []
    trig_out.push_sample(['Trial start'])

    # clear events from keyboard and mouse
    event.clearEvents()
    resp_mouse.clickReset(buttons=(0, 1, 2))

    while bp_space:
        # check for mouse presses
        buttons, times = resp_mouse.getPressed(getTime=True)

        tmp_t = int(round((core.getTime() - timer)*1000,0))
        ms_text.text = (str(tmp_t))
        ms_text.draw()
        win.flip()

        # check mouse button
        if times[0] != 0.0:
            bp_space = False
            trig_out.push_sample(['BP'])

        for key in event.getKeys():
            if key in ['space']:
                bp_space = False
                trig_out.push_sample(['BP'])
            elif key in ['q']:
                bp_space = False
                trig_out.push_sample(['Experiment stopped'])
                win.close()
                core.quit()



    all_rt.append(tmp_t)
    core.wait(dur_hit)
    event.clearEvents()

    key = event.getKeys()
    if key == 'q':
        win.close()
        core.quit()




####################  Full Block ###################################
intro_text.text = "Jetzt geht es gleich los. Starten Sie das Experiment mit der Leertaste."
intro_text.draw()
win.flip()
event.waitKeys()

intro_text.text = " "
intro_text.draw()
win.flip()
core.wait(3)

#Set timer:
cntdwn_exp = core.CountdownTimer(dur_exp * 60)
init_ts = local_clock()
trig_out.push_sample(['Experiment start'])
ms_text.text = str(0)

for i in range(50):

    fixation.draw()
    win.flip()
    trig_out.push_sample(['BL start'])
    jitter = jit_list[i]
    core.wait(jitter)

    #TRIAL

    bp_space = True
    timer = core.getTime() # start trial timer

    all_rt = []
    trig_out.push_sample(['Trial start'])

    # clear events from keyboard and mouse
    event.clearEvents()
    resp_mouse.clickReset(buttons=(0, 1, 2))

    while bp_space:
        # check for mouse presses
        buttons, times = resp_mouse.getPressed(getTime=True)

        tmp_t = int(round((core.getTime() - timer)*1000,0))
        ms_text.text = (str(tmp_t))
        ms_text.draw()
        win.flip()

        # check mouse button
        if times[0] != 0.0:
            bp_space = False
            trig_out.push_sample(['BP'])

        for key in event.getKeys():
            if key in ['space']:
                bp_space = False
                trig_out.push_sample(['BP'])
            elif key in ['q']:
                bp_space = False
                trig_out.push_sample(['Experiment stopped'])
                win.close()
                core.quit()


    all_rt.append(tmp_t)
    core.wait(dur_hit)
    event.clearEvents()

    key = event.getKeys()
    if key == 'q':
        win.close()
        core.quit()




## ################    FINISH UP     ####################

# Cleanup (always!)
win.close()
core.quit()
print ("DONE")
mean_rt = np.asarray(all_rt).mean()
print ('Average RT is {} ms'.format(mean_rt))
