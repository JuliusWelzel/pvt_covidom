#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Mon Dec 20 17:01:31 2021
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019)
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195.
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy.sound import Sound # added to Julian script

prefs.hardware['audioLib'] = ['PTB','pyo']
prefs.hardware['audioLatencyMode'] = '3'

from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'MSI'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=os.path.join(os.path.pardir,'101_software','stim90sequence.xlsx'),
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1536, 864], fullscr=True, screen=0,
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[-1.0, -1.0, -1.0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructions_screen"
instructions_screenClock = core.Clock()
textinsctructions = visual.TextStim(win=win, name='textinsctructions',
    text='Das Experiment beginnt gleich.\n\nBitte schauen Sie durchgängig auf den roten Punkt in der Mitte des Bildschirms.\n\nDrücken Sie die Leertaste, wenn Sie einen Lichtblitz sehen oder einen Ton hören. Sie können einzeln oder zusammen auftreten.\n\nReagieren Sie so schnell und genau wie möglich.\n\nDrücken Sie die Leertaste, um das Experiment zu beginnen.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='white', colorSpace='rgb', opacity=0.0,
    languageStyle='LTR',
    depth=0.0);
keyresponse_instructions = keyboard.Keyboard()

# Initialize components for Routine "isi_screen"
isi_screenClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon',units='deg',
    size=(0.09, 0.09), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,      lineColor='red', fillColor='red',
    opacity=0, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial1"
trial1Clock = core.Clock()
disk = visual.ShapeStim(
    win=win, name='disk',units='deg',
    size=(0.75, 0.75), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,    lineColor=[-0.1552, -0.1552, -0.1552], fillColor=[-0.1552, -0.1552, -0.1552],
    opacity=1.0, depth=0.0, interpolate=True)
reddot = visual.ShapeStim(
    win=win, name='reddot',units='deg',
    size=(0.09, 0.09), vertices='circle',
    ori=0.0, pos=(0, 0),
    lineWidth=1.0,     lineColor='red', fillColor='red',
    opacity=0, depth=-1.0, interpolate=True)
tone = sound.Sound('A', secs=0.1, stereo=True, hamming=True,
    name='tone')
tone.setVolume(1.0)
key_response = keyboard.Keyboard()

# Initialize components for Routine "goodbye_screen"
goodbye_screenClock = core.Clock()
text_goodbye = visual.TextStim(win=win, name='text_goodbye',
    text='Sie haben das Experiment erfolgreich beendet.\n\nVielen Dank für Ihre Teilnahme!',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0,
    color='white',  opacity=0,
    languageStyle='LTR',
    depth=0.0);
keypress_end = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine

# ------Prepare to start Routine "instructions_screen"-------
continueRoutine = True
# update component parameters for each repeat
keyresponse_instructions.keys = []
keyresponse_instructions.rt = []
_keyresponse_instructions_allKeys = []
# keep track of which components have finished
instructions_screenComponents = [textinsctructions, keyresponse_instructions]
for thisComponent in instructions_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructions_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructions_screen"-------
while continueRoutine:
    # get current time
    t = instructions_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructions_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *textinsctructions* updates
    if textinsctructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textinsctructions.frameNStart = frameN  # exact frame index
        textinsctructions.tStart = t  # local t and not account for scr refresh
        textinsctructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textinsctructions, 'tStartRefresh')  # time at next scr refresh
        textinsctructions.setAutoDraw(True)

    # *keyresponse_instructions* updates
    waitOnFlip = False
    if keyresponse_instructions.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        keyresponse_instructions.frameNStart = frameN  # exact frame index
        keyresponse_instructions.tStart = t  # local t and not account for scr refresh
        keyresponse_instructions.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keyresponse_instructions, 'tStartRefresh')  # time at next scr refresh
        keyresponse_instructions.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keyresponse_instructions.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keyresponse_instructions.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keyresponse_instructions.status == STARTED and not waitOnFlip:
        theseKeys = keyresponse_instructions.getKeys(keyList=['space'], waitRelease=False)
        _keyresponse_instructions_allKeys.extend(theseKeys)
        if len(_keyresponse_instructions_allKeys):
            keyresponse_instructions.keys = _keyresponse_instructions_allKeys[-1].name  # just the last key pressed
            keyresponse_instructions.rt = _keyresponse_instructions_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructions_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructions_screen"-------
for thisComponent in instructions_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textinsctructions.started', textinsctructions.tStartRefresh)
thisExp.addData('textinsctructions.stopped', textinsctructions.tStopRefresh)
# check responses
if keyresponse_instructions.keys in ['', [], None]:  # No response was made
    keyresponse_instructions.keys = None
thisExp.addData('keyresponse_instructions.keys',keyresponse_instructions.keys)
if keyresponse_instructions.keys != None:  # we had a response
    thisExp.addData('keyresponse_instructions.rt', keyresponse_instructions.rt)
thisExp.addData('keyresponse_instructions.started', keyresponse_instructions.tStartRefresh)
thisExp.addData('keyresponse_instructions.stopped', keyresponse_instructions.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructions_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
block = data.TrialHandler(nReps=1.0, method='sequential',
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stim90sequence.xlsx'),
    seed=None, name='block')
thisExp.addLoop(block)  # add the loop to the experiment
thisBlock = block.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in block:
    currentLoop = block
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))

    # ------Prepare to start Routine "isi_screen"-------
    continueRoutine = True
    # update component parameters for each repeat
    import random
    isi_duration = random.uniform(1.5,2.5) # values will range from 1.5 to 2.5
    thisExp.addData('random_isi_duration', isi_duration)
    # keep track of which components have finished
    isi_screenComponents = [polygon]
    for thisComponent in isi_screenComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    isi_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "isi_screen"-------
    while continueRoutine:
        # get current time
        t = isi_screenClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=isi_screenClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *polygon* updates
        if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            polygon.frameNStart = frameN  # exact frame index
            polygon.tStart = t  # local t and not account for scr refresh
            polygon.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
            polygon.setAutoDraw(True)
        if polygon.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > polygon.tStartRefresh + isi_duration-frameTolerance:
                # keep track of stop time/frame for later
                polygon.tStop = t  # not accounting for scr refresh
                polygon.frameNStop = frameN  # exact frame index
                win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
                polygon.setAutoDraw(False)

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in isi_screenComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "isi_screen"-------
    for thisComponent in isi_screenComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('polygon.started', polygon.tStartRefresh)
    block.addData('polygon.stopped', polygon.tStopRefresh)
    # the Routine "isi_screen" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "trial1"-------
    continueRoutine = True
    # update component parameters for each repeat
    tone.setSound('3500', secs=0.1, hamming=True)
    tone.setVolume(sound_volume, log=False)
    key_response.keys = []
    key_response.rt = []
    _key_response_allKeys = []
    # keep track of which components have finished
    trial1Components = [disk, reddot, tone, key_response]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trial1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1

    # -------Run Routine "trial1"-------
    while continueRoutine:
        # get current time
        t = trial1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trial1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *disk* updates
        if disk.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            disk.frameNStart = frameN  # exact frame index
            disk.tStart = t  # local t and not account for scr refresh
            disk.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(disk, 'tStartRefresh')  # time at next scr refresh
            disk.setAutoDraw(True)
        if disk.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > disk.tStartRefresh + disk_duration-frameTolerance:
                # keep track of stop time/frame for later
                disk.tStop = t  # not accounting for scr refresh
                disk.frameNStop = frameN  # exact frame index
                win.timeOnFlip(disk, 'tStopRefresh')  # time at next scr refresh
                disk.setAutoDraw(False)

        # *reddot* updates
        if reddot.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            reddot.frameNStart = frameN  # exact frame index
            reddot.tStart = t  # local t and not account for scr refresh
            reddot.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(reddot, 'tStartRefresh')  # time at next scr refresh
            reddot.setAutoDraw(True)
        # start/stop tone
        if tone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tone.frameNStart = frameN  # exact frame index
            tone.tStart = t  # local t and not account for scr refresh
            tone.tStartRefresh = tThisFlipGlobal  # on global time
            tone.play(when=win)  # sync with win flip
        if tone.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > tone.tStartRefresh + 0.1-frameTolerance:
                # keep track of stop time/frame for later
                tone.tStop = t  # not accounting for scr refresh
                tone.frameNStop = frameN  # exact frame index
                win.timeOnFlip(tone, 'tStopRefresh')  # time at next scr refresh
                tone.stop()

        # *key_response* updates
        waitOnFlip = False
        if key_response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_response.frameNStart = frameN  # exact frame index
            key_response.tStart = t  # local t and not account for scr refresh
            key_response.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
            key_response.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_response.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_response.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                key_response.tStop = t  # not accounting for scr refresh
                key_response.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_response, 'tStopRefresh')  # time at next scr refresh
                key_response.status = FINISHED
        if key_response.status == STARTED and not waitOnFlip:
            theseKeys = key_response.getKeys(keyList=['space'], waitRelease=False)
            _key_response_allKeys.extend(theseKeys)
            if len(_key_response_allKeys):
                key_response.keys = _key_response_allKeys[-1].name  # just the last key pressed
                key_response.rt = _key_response_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "trial1"-------
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    block.addData('disk.started', disk.tStartRefresh)
    block.addData('disk.stopped', disk.tStopRefresh)
    block.addData('reddot.started', reddot.tStartRefresh)
    block.addData('reddot.stopped', reddot.tStopRefresh)
    tone.stop()  # ensure sound has stopped at end of routine
    block.addData('tone.started', tone.tStartRefresh)
    block.addData('tone.stopped', tone.tStopRefresh)
    # check responses
    if key_response.keys in ['', [], None]:  # No response was made
        key_response.keys = None
    block.addData('key_response.keys',key_response.keys)
    if key_response.keys != None:  # we had a response
        block.addData('key_response.rt', key_response.rt)
    block.addData('key_response.started', key_response.tStartRefresh)
    block.addData('key_response.stopped', key_response.tStopRefresh)
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()

# completed 1.0 repeats of 'block'


# ------Prepare to start Routine "goodbye_screen"-------
continueRoutine = True
# update component parameters for each repeat
keypress_end.keys = []
keypress_end.rt = []
_keypress_end_allKeys = []
# keep track of which components have finished
goodbye_screenComponents = [text_goodbye, keypress_end]
for thisComponent in goodbye_screenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
goodbye_screenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "goodbye_screen"-------
while continueRoutine:
    # get current time
    t = goodbye_screenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=goodbye_screenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame

    # *text_goodbye* updates
    if text_goodbye.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_goodbye.frameNStart = frameN  # exact frame index
        text_goodbye.tStart = t  # local t and not account for scr refresh
        text_goodbye.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_goodbye, 'tStartRefresh')  # time at next scr refresh
        text_goodbye.setAutoDraw(True)

    # *keypress_end* updates
    waitOnFlip = False
    if keypress_end.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        keypress_end.frameNStart = frameN  # exact frame index
        keypress_end.tStart = t  # local t and not account for scr refresh
        keypress_end.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(keypress_end, 'tStartRefresh')  # time at next scr refresh
        keypress_end.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(keypress_end.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(keypress_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if keypress_end.status == STARTED and not waitOnFlip:
        theseKeys = keypress_end.getKeys(keyList=['space'], waitRelease=False)
        _keypress_end_allKeys.extend(theseKeys)
        if len(_keypress_end_allKeys):
            keypress_end.keys = _keypress_end_allKeys[-1].name  # just the last key pressed
            keypress_end.rt = _keypress_end_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False

    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()

    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in goodbye_screenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished

    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "goodbye_screen"-------
for thisComponent in goodbye_screenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_goodbye.started', text_goodbye.tStartRefresh)
thisExp.addData('text_goodbye.stopped', text_goodbye.tStopRefresh)
# check responses
if keypress_end.keys in ['', [], None]:  # No response was made
    keypress_end.keys = None
thisExp.addData('keypress_end.keys',keypress_end.keys)
if keypress_end.keys != None:  # we had a response
    thisExp.addData('keypress_end.rt', keypress_end.rt)
thisExp.addData('keypress_end.started', keypress_end.tStartRefresh)
thisExp.addData('keypress_end.stopped', keypress_end.tStopRefresh)
thisExp.nextEntry()
# the Routine "goodbye_screen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip()
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
