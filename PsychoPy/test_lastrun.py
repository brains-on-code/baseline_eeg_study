#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on August 29, 2022, at 12:56
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
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
expName = 'test'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'useDevices': False}
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
    originPath='C:\\Users\\Annabelle\\Nextcloud\\Wichtig\\PhD\\Baselinestudie\\Git\\baselinestudy_replication_package\\PsychoPy\\test_lastrun.py',
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
    size=[1920, 1080], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
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

# Initialize components for Routine "Setup"
SetupClock = core.Clock()
button_4 = visual.ButtonStim(win, 
    text='Start the study', font='Arvo',
    pos=(0, 0),
    letterHeight=0.05,
    size=None, borderWidth=0.0,
    fillColor='darkgrey', borderColor=None,
    color='white', colorSpace='rgb',
    opacity=None,
    bold=True, italic=False,
    padding=None,
    anchor='center',
    name='button_4'
)
button_4.buttonClock = core.Clock()
import pandas as pd
df_stimuli = pd.DataFrame([], columns=["startTime", "endTime", "Stimuli"])
df_answer = pd.DataFrame([], columns=["task", "answer"])
df_hash = pd.DataFrame([], columns=["hash", "task"])

participant = expInfo["participant"]
session = expInfo["session"]
use_devices = expInfo["useDevices"]

folder_name = f"./data/Session_{session}_Participant_{participant}"

from operator import imod
import os
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
eeg_logger = None
eyetracking_logger = None
from datetime import datetime
start_time = None

if use_devices==True:
    from EEGTools.Recorders.LiveAmpRecorder.liveamp_recorder import LiveAmpRecorder as Recorder
    from EyetrackerUtils.base_functionalities.logger import Logger as EyeTrackerLogger
    
    # setup eeg
    eeg_logger = Recorder()
    eeg_logger.connect()
    # setup eye tracking
    eyetracking_logger = EyeTrackerLogger(f"{folder_name}/EyeTracking.csv")
    eyetracking_logger.add_key_to_log('left_gaze_point_validity')
    eyetracking_logger.add_key_to_log('left_gaze_point_on_display_area')
    eyetracking_logger.add_key_to_log('left_pupil_diameter')
    eyetracking_logger.add_key_to_log('right_gaze_point_validity')
    eyetracking_logger.add_key_to_log('right_gaze_point_on_display_area')
    eyetracking_logger.add_key_to_log('right_pupil_diameter')
    eyetracking_logger.add_key_to_log('system_time_stamp')
    # start eeg
    eeg_logger.start_recording()
    # start eyetracking
    eyetracking_logger.start_recording()

# setup timing
start_time = datetime.now()


# Initialize components for Routine "start"
startClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Press space to start training exercises',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_18 = keyboard.Keyboard()

# Initialize components for Routine "ReadTest"
ReadTestClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='material/Read/sunQuestion.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
read_keyboard = keyboard.Keyboard()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Press space to go to answers',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ReadTestAnswer"
ReadTestAnswerClock = core.Clock()
read_test_answer_1 = visual.ImageStim(
    win=win,
    name='read_test_answer_1', 
    image='material/Read/sunAnswers.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "ProbSolvTest"
ProbSolvTestClock = core.Clock()
image_5 = visual.ImageStim(
    win=win,
    name='image_5', 
    image='material/ProbSolv/quest18.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_9 = keyboard.Keyboard()
text_8 = visual.TextStim(win=win, name='text_8',
    text='Press Space to go to answers',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ProbSolvTestAnswers"
ProbSolvTestAnswersClock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='material/ProbSolv/_M0Answer.png', mask=None,
    ori=0.0, pos=(0, 0), size=(1, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "MathTest"
MathTestClock = core.Clock()
image_10 = visual.ImageStim(
    win=win,
    name='image_10', 
    image='material/Math/MathTestQuestion.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_11 = keyboard.Keyboard()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Press space to go to answers',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "MathTestAnswer"
MathTestAnswerClock = core.Clock()
image_11 = visual.ImageStim(
    win=win,
    name='image_11', 
    image='material/Math/MathTrainingAnswers.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "ProgComprTest"
ProgComprTestClock = core.Clock()
image_15 = visual.ImageStim(
    win=win,
    name='image_15', 
    image='material/ProgCompr/Snippets/SampleForTraining.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_13 = keyboard.Keyboard()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Press Space to go to Inputs',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "ProgComprTestInput"
ProgComprTestInputClock = core.Clock()
key_resp_14 = keyboard.Keyboard()
text_12 = visual.TextStim(win=win, name='text_12',
    text='Press space to go to answers',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
image_4 = visual.ImageStim(
    win=win,
    name='image_4', 
    image='material/ProgCompr/input_training.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "ProgComprTestAnswers"
ProgComprTestAnswersClock = core.Clock()
key_resp_15 = keyboard.Keyboard()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='material/ProgCompr/answers_training.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-1.0)

# Initialize components for Routine "start_2"
start_2Clock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='Press space to start experiment tasks',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_24 = keyboard.Keyboard()

# Initialize components for Routine "Pause_2"
Pause_2Clock = core.Clock()
key_resp_17 = keyboard.Keyboard()
Break_key7 = keyboard.Keyboard()
sound_1 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_1')
sound_1.setVolume(1.0)
image_12 = visual.ImageStim(
    win=win,
    name='image_12', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "Pause2_2"
Pause2_2Clock = core.Clock()
key_resp_19 = keyboard.Keyboard()
key_resp_20 = keyboard.Keyboard()
Break_key7_2 = keyboard.Keyboard()
image_13 = visual.ImageStim(
    win=win,
    name='image_13', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "Continue"
ContinueClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Press space to continue',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_2 = sound.Sound('C', secs=-1, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "Question"
QuestionClock = core.Clock()
Question_Image = visual.ImageStim(
    win=win,
    name='Question_Image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
Question_keyboard = keyboard.Keyboard()
Question_text = visual.TextStim(win=win, name='Question_text',
    text='Press space to go to answers',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Break_key1 = keyboard.Keyboard()

# Initialize components for Routine "Answers"
AnswersClock = core.Clock()
Answers1Image = visual.ImageStim(
    win=win,
    name='Answers1Image', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_4 = keyboard.Keyboard()
text_14 = visual.TextStim(win=win, name='text_14',
    text='Press space to skip',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Break_key2 = keyboard.Keyboard()

# Initialize components for Routine "Pause"
PauseClock = core.Clock()
key_resp_16 = keyboard.Keyboard()
Break_key3 = keyboard.Keyboard()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='material/Rest_noskip.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-3.0)

# Initialize components for Routine "Pause1_2"
Pause1_2Clock = core.Clock()
key_resp = keyboard.Keyboard()
key_resp_23 = keyboard.Keyboard()
Break_key3_2 = keyboard.Keyboard()
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='material/Rest_skip.png', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "ProgComprQuestion"
ProgComprQuestionClock = core.Clock()
ProgCompr_Question = visual.ImageStim(
    win=win,
    name='ProgCompr_Question', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_3 = keyboard.Keyboard()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Press Space to go to input',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Break_key4 = keyboard.Keyboard()

# Initialize components for Routine "ProgComprInput"
ProgComprInputClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='Press space to go to answers',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_5 = keyboard.Keyboard()
Break_key5 = keyboard.Keyboard()
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-4.0)

# Initialize components for Routine "ProgComprAnswer"
ProgComprAnswerClock = core.Clock()
key_resp_2 = keyboard.Keyboard()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0.0, pos=(0, 0), size=None,
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)
text_5 = visual.TextStim(win=win, name='text_5',
    text='Press space to skip',
    font='Open Sans',
    pos=(0, -0.4), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
Break_key6 = keyboard.Keyboard()

# Initialize components for Routine "ThankYou"
ThankYouClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Thanks for your participation',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Setup"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
SetupComponents = [button_4]
for thisComponent in SetupComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
SetupClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Setup"-------
while continueRoutine:
    # get current time
    t = SetupClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=SetupClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *button_4* updates
    if button_4.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        button_4.frameNStart = frameN  # exact frame index
        button_4.tStart = t  # local t and not account for scr refresh
        button_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button_4, 'tStartRefresh')  # time at next scr refresh
        button_4.setAutoDraw(True)
    if button_4.status == STARTED:
        # check whether button_4 has been pressed
        if button_4.isClicked:
            if not button_4.wasClicked:
                button_4.timesOn.append(button_4.buttonClock.getTime()) # store time of first click
                button_4.timesOff.append(button_4.buttonClock.getTime()) # store time clicked until
            else:
                button_4.timesOff[-1] = button_4.buttonClock.getTime() # update time clicked until
            if not button_4.wasClicked:
                continueRoutine = False  # end routine when button_4 is clicked
                None
            button_4.wasClicked = True  # if button_4 is still clicked next frame, it is not a new click
        else:
            button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    else:
        button_4.wasClicked = False  # if button_4 is clicked next frame, it is a new click
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SetupComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Setup"-------
for thisComponent in SetupComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('button_4.started', button_4.tStartRefresh)
thisExp.addData('button_4.stopped', button_4.tStopRefresh)
thisExp.addData('button_4.numClicks', button_4.numClicks)
if button_4.numClicks:
   thisExp.addData('button_4.timesOn', button_4.timesOn)
   thisExp.addData('button_4.timesOff', button_4.timesOff)
else:
   thisExp.addData('button_4.timesOn', "")
   thisExp.addData('button_4.timesOff', "")
# the Routine "Setup" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_18.keys = []
key_resp_18.rt = []
_key_resp_18_allKeys = []
# keep track of which components have finished
startComponents = [text_15, key_resp_18]
for thisComponent in startComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start"-------
while continueRoutine:
    # get current time
    t = startClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_18* updates
    waitOnFlip = False
    if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_18.frameNStart = frameN  # exact frame index
        key_resp_18.tStart = t  # local t and not account for scr refresh
        key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
        key_resp_18.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_18.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_18.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_18_allKeys.extend(theseKeys)
        if len(_key_resp_18_allKeys):
            key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
            key_resp_18.rt = _key_resp_18_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start"-------
for thisComponent in startComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# check responses
if key_resp_18.keys in ['', [], None]:  # No response was made
    key_resp_18.keys = None
thisExp.addData('key_resp_18.keys',key_resp_18.keys)
if key_resp_18.keys != None:  # we had a response
    thisExp.addData('key_resp_18.rt', key_resp_18.rt)
thisExp.addData('key_resp_18.started', key_resp_18.tStartRefresh)
thisExp.addData('key_resp_18.stopped', key_resp_18.tStopRefresh)
thisExp.nextEntry()
# the Routine "start" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ReadTest"-------
continueRoutine = True
# update component parameters for each repeat
read_keyboard.keys = []
read_keyboard.rt = []
_read_keyboard_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ReadTestComponents = [image, read_keyboard, text_7]
for thisComponent in ReadTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ReadTest"-------
while continueRoutine:
    # get current time
    t = ReadTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # *read_keyboard* updates
    waitOnFlip = False
    if read_keyboard.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        read_keyboard.frameNStart = frameN  # exact frame index
        read_keyboard.tStart = t  # local t and not account for scr refresh
        read_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(read_keyboard, 'tStartRefresh')  # time at next scr refresh
        read_keyboard.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(read_keyboard.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(read_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if read_keyboard.status == STARTED and not waitOnFlip:
        theseKeys = read_keyboard.getKeys(keyList=['space'], waitRelease=False)
        _read_keyboard_allKeys.extend(theseKeys)
        if len(_read_keyboard_allKeys):
            read_keyboard.keys = _read_keyboard_allKeys[-1].name  # just the last key pressed
            read_keyboard.rt = _read_keyboard_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ReadTest"-------
for thisComponent in ReadTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# check responses
if read_keyboard.keys in ['', [], None]:  # No response was made
    read_keyboard.keys = None
thisExp.addData('read_keyboard.keys',read_keyboard.keys)
if read_keyboard.keys != None:  # we had a response
    thisExp.addData('read_keyboard.rt', read_keyboard.rt)
thisExp.addData('read_keyboard.started', read_keyboard.tStartRefresh)
thisExp.addData('read_keyboard.stopped', read_keyboard.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "Text_training_Question"]
# the Routine "ReadTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ReadTestAnswer"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ReadTestAnswerComponents = [read_test_answer_1, key_resp_8]
for thisComponent in ReadTestAnswerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ReadTestAnswerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ReadTestAnswer"-------
while continueRoutine:
    # get current time
    t = ReadTestAnswerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ReadTestAnswerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *read_test_answer_1* updates
    if read_test_answer_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        read_test_answer_1.frameNStart = frameN  # exact frame index
        read_test_answer_1.tStart = t  # local t and not account for scr refresh
        read_test_answer_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(read_test_answer_1, 'tStartRefresh')  # time at next scr refresh
        read_test_answer_1.setAutoDraw(True)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['a', 's', 'd', 'f', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ReadTestAnswerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ReadTestAnswer"-------
for thisComponent in ReadTestAnswerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('read_test_answer_1.started', read_test_answer_1.tStartRefresh)
thisExp.addData('read_test_answer_1.stopped', read_test_answer_1.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "Read_training_answer"]
if  key_resp_8.keys is not None:
    answer = key_resp_8.keys[0]
    if answer == 's' and len(key_resp_8.keys)>1:
        answer = 'k'
    df_answer.loc[len(df_answer)] = ["Read_training", answer]
# the Routine "ReadTestAnswer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ProbSolvTest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ProbSolvTestComponents = [image_5, key_resp_9, text_8]
for thisComponent in ProbSolvTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProbSolvTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProbSolvTest"-------
while continueRoutine:
    # get current time
    t = ProbSolvTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProbSolvTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_5* updates
    if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_5.frameNStart = frameN  # exact frame index
        image_5.tStart = t  # local t and not account for scr refresh
        image_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
        image_5.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProbSolvTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProbSolvTest"-------
for thisComponent in ProbSolvTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_5.started', image_5.tStartRefresh)
thisExp.addData('image_5.stopped', image_5.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "Matrix_training_Question"]
# the Routine "ProbSolvTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ProbSolvTestAnswers"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ProbSolvTestAnswersComponents = [image_6, key_resp_10]
for thisComponent in ProbSolvTestAnswersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProbSolvTestAnswersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProbSolvTestAnswers"-------
while continueRoutine:
    # get current time
    t = ProbSolvTestAnswersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProbSolvTestAnswersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['a', 's', 'd', 'f', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProbSolvTestAnswersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProbSolvTestAnswers"-------
for thisComponent in ProbSolvTestAnswersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "ProbSolv_training_answer"]
if  key_resp_10.keys is not None:
    answer = key_resp_10.keys[0]
    if answer == 's' and len(key_resp_10.keys)>1:
        answer = 'k'
    df_answer.loc[len(df_answer)] = ["ProbSolv_training", answer]
# the Routine "ProbSolvTestAnswers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MathTest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
MathTestComponents = [image_10, key_resp_11, text_10]
for thisComponent in MathTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MathTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MathTest"-------
while continueRoutine:
    # get current time
    t = MathTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MathTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_10* updates
    if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_10.frameNStart = frameN  # exact frame index
        image_10.tStart = t  # local t and not account for scr refresh
        image_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
        image_10.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MathTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MathTest"-------
for thisComponent in MathTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_10.started', image_10.tStartRefresh)
thisExp.addData('image_10.stopped', image_10.tStopRefresh)
# check responses
if key_resp_11.keys in ['', [], None]:  # No response was made
    key_resp_11.keys = None
thisExp.addData('key_resp_11.keys',key_resp_11.keys)
if key_resp_11.keys != None:  # we had a response
    thisExp.addData('key_resp_11.rt', key_resp_11.rt)
thisExp.addData('key_resp_11.started', key_resp_11.tStartRefresh)
thisExp.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "Math_training_Question"]
# the Routine "MathTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "MathTestAnswer"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
MathTestAnswerComponents = [image_11, key_resp_12]
for thisComponent in MathTestAnswerComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
MathTestAnswerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "MathTestAnswer"-------
while continueRoutine:
    # get current time
    t = MathTestAnswerClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=MathTestAnswerClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_11* updates
    if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_11.frameNStart = frameN  # exact frame index
        image_11.tStart = t  # local t and not account for scr refresh
        image_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
        image_11.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['a', 's', 'd', 'f', 'space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in MathTestAnswerComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "MathTestAnswer"-------
for thisComponent in MathTestAnswerComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_11.started', image_11.tStartRefresh)
thisExp.addData('image_11.stopped', image_11.tStopRefresh)
# check responses
if key_resp_12.keys in ['', [], None]:  # No response was made
    key_resp_12.keys = None
thisExp.addData('key_resp_12.keys',key_resp_12.keys)
if key_resp_12.keys != None:  # we had a response
    thisExp.addData('key_resp_12.rt', key_resp_12.rt)
thisExp.addData('key_resp_12.started', key_resp_12.tStartRefresh)
thisExp.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
thisExp.nextEntry()
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "Math_training_answer"]
if  key_resp_12.keys is not None:
    answer = key_resp_12.keys[0]
    if answer == 's' and len(key_resp_12.keys)>1:
        answer = 'k'
    df_answer.loc[len(df_answer)] = ["Math_training", answer]
# the Routine "MathTestAnswer" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ProgComprTest"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ProgComprTestComponents = [image_15, key_resp_13, text_11]
for thisComponent in ProgComprTestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProgComprTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProgComprTest"-------
while continueRoutine:
    # get current time
    t = ProgComprTestClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProgComprTestClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_15* updates
    if image_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_15.frameNStart = frameN  # exact frame index
        image_15.tStart = t  # local t and not account for scr refresh
        image_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_15, 'tStartRefresh')  # time at next scr refresh
        image_15.setAutoDraw(True)
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProgComprTestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProgComprTest"-------
for thisComponent in ProgComprTestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_15.started', image_15.tStartRefresh)
thisExp.addData('image_15.stopped', image_15.tStopRefresh)
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "ProgCompr_training_Question"]
# the Routine "ProgComprTest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ProgComprTestInput"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_14.keys = []
key_resp_14.rt = []
_key_resp_14_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ProgComprTestInputComponents = [key_resp_14, text_12, image_4]
for thisComponent in ProgComprTestInputComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProgComprTestInputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProgComprTestInput"-------
while continueRoutine:
    # get current time
    t = ProgComprTestInputClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProgComprTestInputClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_14* updates
    waitOnFlip = False
    if key_resp_14.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_14.frameNStart = frameN  # exact frame index
        key_resp_14.tStart = t  # local t and not account for scr refresh
        key_resp_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_14, 'tStartRefresh')  # time at next scr refresh
        key_resp_14.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_14.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_14.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_14.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_14.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_14_allKeys.extend(theseKeys)
        if len(_key_resp_14_allKeys):
            key_resp_14.keys = _key_resp_14_allKeys[-1].name  # just the last key pressed
            key_resp_14.rt = _key_resp_14_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_12* updates
    if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_12.frameNStart = frameN  # exact frame index
        text_12.tStart = t  # local t and not account for scr refresh
        text_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
        text_12.setAutoDraw(True)
    
    # *image_4* updates
    if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_4.frameNStart = frameN  # exact frame index
        image_4.tStart = t  # local t and not account for scr refresh
        image_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
        image_4.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProgComprTestInputComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProgComprTestInput"-------
for thisComponent in ProgComprTestInputComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_14.keys in ['', [], None]:  # No response was made
    key_resp_14.keys = None
thisExp.addData('key_resp_14.keys',key_resp_14.keys)
if key_resp_14.keys != None:  # we had a response
    thisExp.addData('key_resp_14.rt', key_resp_14.rt)
thisExp.addData('key_resp_14.started', key_resp_14.tStartRefresh)
thisExp.addData('key_resp_14.stopped', key_resp_14.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_12.started', text_12.tStartRefresh)
thisExp.addData('text_12.stopped', text_12.tStopRefresh)
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "ProgCompr_training_Input"]
thisExp.addData('image_4.started', image_4.tStartRefresh)
thisExp.addData('image_4.stopped', image_4.tStopRefresh)
# the Routine "ProgComprTestInput" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "ProgComprTestAnswers"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_15.keys = []
key_resp_15.rt = []
_key_resp_15_allKeys = []
current_time = datetime.now()
start_of_stimuli = current_time- start_time
# keep track of which components have finished
ProgComprTestAnswersComponents = [key_resp_15, image_2]
for thisComponent in ProgComprTestAnswersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ProgComprTestAnswersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ProgComprTestAnswers"-------
while continueRoutine:
    # get current time
    t = ProgComprTestAnswersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ProgComprTestAnswersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_15* updates
    waitOnFlip = False
    if key_resp_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_15.frameNStart = frameN  # exact frame index
        key_resp_15.tStart = t  # local t and not account for scr refresh
        key_resp_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_15, 'tStartRefresh')  # time at next scr refresh
        key_resp_15.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_15.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_15.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_15.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_15.getKeys(keyList=['a', 's', 'd', 'f', 'space'], waitRelease=False)
        _key_resp_15_allKeys.extend(theseKeys)
        if len(_key_resp_15_allKeys):
            key_resp_15.keys = _key_resp_15_allKeys[-1].name  # just the last key pressed
            key_resp_15.rt = _key_resp_15_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image_2* updates
    if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_2.frameNStart = frameN  # exact frame index
        image_2.tStart = t  # local t and not account for scr refresh
        image_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
        image_2.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ProgComprTestAnswersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ProgComprTestAnswers"-------
for thisComponent in ProgComprTestAnswersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_15.keys in ['', [], None]:  # No response was made
    key_resp_15.keys = None
thisExp.addData('key_resp_15.keys',key_resp_15.keys)
if key_resp_15.keys != None:  # we had a response
    thisExp.addData('key_resp_15.rt', key_resp_15.rt)
thisExp.addData('key_resp_15.started', key_resp_15.tStartRefresh)
thisExp.addData('key_resp_15.stopped', key_resp_15.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('image_2.started', image_2.tStartRefresh)
thisExp.addData('image_2.stopped', image_2.tStopRefresh)
current_time = datetime.now()
end_of_stimuli = current_time- start_time

df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, "ProgCompr_training_answer"]
if  key_resp_15.keys is not None:
    answer = key_resp_15.keys[0]
    if answer == 's' and len(key_resp_15.keys)>1:
        answer = 'k'
    df_answer.loc[len(df_answer)] = ["ProgCompr_training", answer]
# the Routine "ProgComprTestAnswers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "start_2"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_24.keys = []
key_resp_24.rt = []
_key_resp_24_allKeys = []
# keep track of which components have finished
start_2Components = [text_17, key_resp_24]
for thisComponent in start_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
start_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "start_2"-------
while continueRoutine:
    # get current time
    t = start_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=start_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_17* updates
    if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_17.frameNStart = frameN  # exact frame index
        text_17.tStart = t  # local t and not account for scr refresh
        text_17.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
        text_17.setAutoDraw(True)
    
    # *key_resp_24* updates
    waitOnFlip = False
    if key_resp_24.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
        # keep track of start time/frame for later
        key_resp_24.frameNStart = frameN  # exact frame index
        key_resp_24.tStart = t  # local t and not account for scr refresh
        key_resp_24.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_24, 'tStartRefresh')  # time at next scr refresh
        key_resp_24.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_24.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_24.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_24.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_24.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_24_allKeys.extend(theseKeys)
        if len(_key_resp_24_allKeys):
            key_resp_24.keys = _key_resp_24_allKeys[-1].name  # just the last key pressed
            key_resp_24.rt = _key_resp_24_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in start_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "start_2"-------
for thisComponent in start_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_17.started', text_17.tStartRefresh)
thisExp.addData('text_17.stopped', text_17.tStopRefresh)
# check responses
if key_resp_24.keys in ['', [], None]:  # No response was made
    key_resp_24.keys = None
thisExp.addData('key_resp_24.keys',key_resp_24.keys)
if key_resp_24.keys != None:  # we had a response
    thisExp.addData('key_resp_24.rt', key_resp_24.rt)
thisExp.addData('key_resp_24.started', key_resp_24.tStartRefresh)
thisExp.addData('key_resp_24.stopped', key_resp_24.tStopRefresh)
thisExp.nextEntry()
# the Routine "start_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
Trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions("Questions"+participant+".xlsx"),
    seed=None, name='Trials')
thisExp.addLoop(Trials)  # add the loop to the experiment
thisTrial = Trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in Trials:
    currentLoop = Trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Pause_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_17.keys = []
    key_resp_17.rt = []
    _key_resp_17_allKeys = []
    Break_key7.keys = []
    Break_key7.rt = []
    _Break_key7_allKeys = []
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str("Pause_2"))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str("Pause_2"))%1000000007, "Pause_2"]
    thisExp.addData("ImagePath","Pause_2")
    sound_1.setSound('A', secs=1.0, hamming=True)
    sound_1.setVolume(Pause_Volume, log=False)
    image_12.setImage(Pause_image)
    # keep track of which components have finished
    Pause_2Components = [key_resp_17, Break_key7, sound_1, image_12]
    for thisComponent in Pause_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pause_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pause_2"-------
    while continueRoutine:
        # get current time
        t = Pause_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pause_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_17* updates
        waitOnFlip = False
        if key_resp_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_17.frameNStart = frameN  # exact frame index
            key_resp_17.tStart = t  # local t and not account for scr refresh
            key_resp_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_17, 'tStartRefresh')  # time at next scr refresh
            key_resp_17.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_17.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_17.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_17.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_17.tStop = t  # not accounting for scr refresh
                key_resp_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_17, 'tStopRefresh')  # time at next scr refresh
                key_resp_17.status = FINISHED
        if key_resp_17.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_17.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_17_allKeys.extend(theseKeys)
            if len(_key_resp_17_allKeys):
                key_resp_17.keys = _key_resp_17_allKeys[-1].name  # just the last key pressed
                key_resp_17.rt = _key_resp_17_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Break_key7* updates
        waitOnFlip = False
        if Break_key7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key7.frameNStart = frameN  # exact frame index
            Break_key7.tStart = t  # local t and not account for scr refresh
            Break_key7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key7, 'tStartRefresh')  # time at next scr refresh
            Break_key7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_key7.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                Break_key7.tStop = t  # not accounting for scr refresh
                Break_key7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Break_key7, 'tStopRefresh')  # time at next scr refresh
                Break_key7.status = FINISHED
        if Break_key7.status == STARTED and not waitOnFlip:
            theseKeys = Break_key7.getKeys(keyList=['0'], waitRelease=False)
            _Break_key7_allKeys.extend(theseKeys)
            if len(_Break_key7_allKeys):
                Break_key7.keys = _Break_key7_allKeys[-1].name  # just the last key pressed
                Break_key7.rt = _Break_key7_allKeys[-1].rt
        # start/stop sound_1
        if sound_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.tStart = t  # local t and not account for scr refresh
            sound_1.tStartRefresh = tThisFlipGlobal  # on global time
            sound_1.play(when=win)  # sync with win flip
        if sound_1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_1.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_1.tStop = t  # not accounting for scr refresh
                sound_1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_1, 'tStopRefresh')  # time at next scr refresh
                sound_1.stop()
        
        # *image_12* updates
        if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_12.frameNStart = frameN  # exact frame index
            image_12.tStart = t  # local t and not account for scr refresh
            image_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
            image_12.setAutoDraw(True)
        if image_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_12.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                image_12.tStop = t  # not accounting for scr refresh
                image_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_12, 'tStopRefresh')  # time at next scr refresh
                image_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pause_2"-------
    for thisComponent in Pause_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_17.keys in ['', [], None]:  # No response was made
        key_resp_17.keys = None
    Trials.addData('key_resp_17.keys',key_resp_17.keys)
    if key_resp_17.keys != None:  # we had a response
        Trials.addData('key_resp_17.rt', key_resp_17.rt)
    Trials.addData('key_resp_17.started', key_resp_17.tStartRefresh)
    Trials.addData('key_resp_17.stopped', key_resp_17.tStopRefresh)
    # check responses
    if Break_key7.keys in ['', [], None]:  # No response was made
        Break_key7.keys = None
    Trials.addData('Break_key7.keys',Break_key7.keys)
    if Break_key7.keys != None:  # we had a response
        Trials.addData('Break_key7.rt', Break_key7.rt)
    Trials.addData('Break_key7.started', Break_key7.tStartRefresh)
    Trials.addData('Break_key7.stopped', Break_key7.tStopRefresh)
    if  Break_key7.keys is not None and len(Break_key7.keys)>0:
        if Break_key7.keys[0] == '0':
            Trials.finished=True
    sound_1.stop()  # ensure sound has stopped at end of routine
    Trials.addData('sound_1.started', sound_1.tStartRefresh)
    Trials.addData('sound_1.stopped', sound_1.tStopRefresh)
    Trials.addData('image_12.started', image_12.tStartRefresh)
    Trials.addData('image_12.stopped', image_12.tStopRefresh)
    # the Routine "Pause_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pause2_2"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    Break_key7_2.keys = []
    Break_key7_2.rt = []
    _Break_key7_2_allKeys = []
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str("Pause2_2"))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str("Pause2_2"))%1000000007, "Pause2_2"]
    thisExp.addData("ImagePath","Pause2_2")
    image_13.setImage(Pause_Image2)
    # keep track of which components have finished
    Pause2_2Components = [key_resp_19, key_resp_20, Break_key7_2, image_13]
    for thisComponent in Pause2_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pause2_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pause2_2"-------
    while continueRoutine:
        # get current time
        t = Pause2_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pause2_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_19* updates
        waitOnFlip = False
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_19.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_19.tStop = t  # not accounting for scr refresh
                key_resp_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_19, 'tStopRefresh')  # time at next scr refresh
                key_resp_19.status = FINISHED
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_20* updates
        waitOnFlip = False
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_20.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_20.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_20.tStop = t  # not accounting for scr refresh
                key_resp_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_20, 'tStopRefresh')  # time at next scr refresh
                key_resp_20.status = FINISHED
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = _key_resp_20_allKeys[-1].name  # just the last key pressed
                key_resp_20.rt = _key_resp_20_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Break_key7_2* updates
        waitOnFlip = False
        if Break_key7_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key7_2.frameNStart = frameN  # exact frame index
            Break_key7_2.tStart = t  # local t and not account for scr refresh
            Break_key7_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key7_2, 'tStartRefresh')  # time at next scr refresh
            Break_key7_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key7_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key7_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key7_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_key7_2.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                Break_key7_2.tStop = t  # not accounting for scr refresh
                Break_key7_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Break_key7_2, 'tStopRefresh')  # time at next scr refresh
                Break_key7_2.status = FINISHED
        if Break_key7_2.status == STARTED and not waitOnFlip:
            theseKeys = Break_key7_2.getKeys(keyList=['0'], waitRelease=False)
            _Break_key7_2_allKeys.extend(theseKeys)
            if len(_Break_key7_2_allKeys):
                Break_key7_2.keys = _Break_key7_2_allKeys[-1].name  # just the last key pressed
                Break_key7_2.rt = _Break_key7_2_allKeys[-1].rt
        
        # *image_13* updates
        if image_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_13.frameNStart = frameN  # exact frame index
            image_13.tStart = t  # local t and not account for scr refresh
            image_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_13, 'tStartRefresh')  # time at next scr refresh
            image_13.setAutoDraw(True)
        if image_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_13.tStartRefresh + Pause_length/2-frameTolerance:
                # keep track of stop time/frame for later
                image_13.tStop = t  # not accounting for scr refresh
                image_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_13, 'tStopRefresh')  # time at next scr refresh
                image_13.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause2_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pause2_2"-------
    for thisComponent in Pause2_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    Trials.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        Trials.addData('key_resp_19.rt', key_resp_19.rt)
    Trials.addData('key_resp_19.started', key_resp_19.tStartRefresh)
    Trials.addData('key_resp_19.stopped', key_resp_19.tStopRefresh)
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    Trials.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        Trials.addData('key_resp_20.rt', key_resp_20.rt)
    Trials.addData('key_resp_20.started', key_resp_20.tStartRefresh)
    Trials.addData('key_resp_20.stopped', key_resp_20.tStopRefresh)
    # check responses
    if Break_key7_2.keys in ['', [], None]:  # No response was made
        Break_key7_2.keys = None
    Trials.addData('Break_key7_2.keys',Break_key7_2.keys)
    if Break_key7_2.keys != None:  # we had a response
        Trials.addData('Break_key7_2.rt', Break_key7_2.rt)
    Trials.addData('Break_key7_2.started', Break_key7_2.tStartRefresh)
    Trials.addData('Break_key7_2.stopped', Break_key7_2.tStopRefresh)
    if  Break_key7.keys is not None and len(Break_key7.keys)>0:
        if Break_key7.keys[0] == '0':
            Trials.finished=True
    Trials.addData('image_13.started', image_13.tStartRefresh)
    Trials.addData('image_13.stopped', image_13.tStopRefresh)
    # the Routine "Pause2_2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Continue"-------
    continueRoutine = True
    # update component parameters for each repeat
    sound_2.setSound('C', secs=Next_time/1000, hamming=True)
    sound_2.setVolume(1.0, log=False)
    key_resp_7.keys = []
    key_resp_7.rt = []
    _key_resp_7_allKeys = []
    # keep track of which components have finished
    ContinueComponents = [text, sound_2, key_resp_7]
    for thisComponent in ContinueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ContinueClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Continue"-------
    while continueRoutine:
        # get current time
        t = ContinueClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ContinueClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            text.setAutoDraw(True)
        if text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text.tStartRefresh + Next_time-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                text.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + Next_time/1000-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        
        # *key_resp_7* updates
        waitOnFlip = False
        if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_7.frameNStart = frameN  # exact frame index
            key_resp_7.tStart = t  # local t and not account for scr refresh
            key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
            key_resp_7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_7.tStartRefresh + Next_time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_7.tStop = t  # not accounting for scr refresh
                key_resp_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_7, 'tStopRefresh')  # time at next scr refresh
                key_resp_7.status = FINISHED
        if key_resp_7.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_7_allKeys.extend(theseKeys)
            if len(_key_resp_7_allKeys):
                key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
                key_resp_7.rt = _key_resp_7_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ContinueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Continue"-------
    for thisComponent in ContinueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('text.started', text.tStartRefresh)
    Trials.addData('text.stopped', text.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    Trials.addData('sound_2.started', sound_2.tStartRefresh)
    Trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    # check responses
    if key_resp_7.keys in ['', [], None]:  # No response was made
        key_resp_7.keys = None
    Trials.addData('key_resp_7.keys',key_resp_7.keys)
    if key_resp_7.keys != None:  # we had a response
        Trials.addData('key_resp_7.rt', key_resp_7.rt)
    Trials.addData('key_resp_7.started', key_resp_7.tStartRefresh)
    Trials.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
    # the Routine "Continue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Question"-------
    continueRoutine = True
    # update component parameters for each repeat
    Question_Image.setImage(QuestionImage)
    Question_keyboard.keys = []
    Question_keyboard.rt = []
    _Question_keyboard_allKeys = []
    current_time = datetime.now()
    start_of_stimuli = current_time- start_time
    
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str(QuestionImage))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str(QuestionImage))%1000000007, QuestionImage]
    thisExp.addData("ImagePath",QuestionImage)
    Break_key1.keys = []
    Break_key1.rt = []
    _Break_key1_allKeys = []
    # keep track of which components have finished
    QuestionComponents = [Question_Image, Question_keyboard, Question_text, Break_key1]
    for thisComponent in QuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    QuestionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Question"-------
    while continueRoutine:
        # get current time
        t = QuestionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=QuestionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Question_Image* updates
        if Question_Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question_Image.frameNStart = frameN  # exact frame index
            Question_Image.tStart = t  # local t and not account for scr refresh
            Question_Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_Image, 'tStartRefresh')  # time at next scr refresh
            Question_Image.setAutoDraw(True)
        if Question_Image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Question_Image.tStartRefresh + Time_Shown-frameTolerance:
                # keep track of stop time/frame for later
                Question_Image.tStop = t  # not accounting for scr refresh
                Question_Image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Question_Image, 'tStopRefresh')  # time at next scr refresh
                Question_Image.setAutoDraw(False)
        
        # *Question_keyboard* updates
        waitOnFlip = False
        if Question_keyboard.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question_keyboard.frameNStart = frameN  # exact frame index
            Question_keyboard.tStart = t  # local t and not account for scr refresh
            Question_keyboard.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_keyboard, 'tStartRefresh')  # time at next scr refresh
            Question_keyboard.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Question_keyboard.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Question_keyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Question_keyboard.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Question_keyboard.tStartRefresh + Time_Shown-20-frameTolerance:
                # keep track of stop time/frame for later
                Question_keyboard.tStop = t  # not accounting for scr refresh
                Question_keyboard.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Question_keyboard, 'tStopRefresh')  # time at next scr refresh
                Question_keyboard.status = FINISHED
        if Question_keyboard.status == STARTED and not waitOnFlip:
            theseKeys = Question_keyboard.getKeys(keyList=['space'], waitRelease=False)
            _Question_keyboard_allKeys.extend(theseKeys)
            if len(_Question_keyboard_allKeys):
                Question_keyboard.keys = _Question_keyboard_allKeys[-1].name  # just the last key pressed
                Question_keyboard.rt = _Question_keyboard_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Question_text* updates
        if Question_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Question_text.frameNStart = frameN  # exact frame index
            Question_text.tStart = t  # local t and not account for scr refresh
            Question_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Question_text, 'tStartRefresh')  # time at next scr refresh
            Question_text.setAutoDraw(True)
        if Question_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Question_text.tStartRefresh + Time_Shown-20-frameTolerance:
                # keep track of stop time/frame for later
                Question_text.tStop = t  # not accounting for scr refresh
                Question_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Question_text, 'tStopRefresh')  # time at next scr refresh
                Question_text.setAutoDraw(False)
        
        # *Break_key1* updates
        waitOnFlip = False
        if Break_key1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key1.frameNStart = frameN  # exact frame index
            Break_key1.tStart = t  # local t and not account for scr refresh
            Break_key1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key1, 'tStartRefresh')  # time at next scr refresh
            Break_key1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key1.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_key1.tStartRefresh + Time_Shown-frameTolerance:
                # keep track of stop time/frame for later
                Break_key1.tStop = t  # not accounting for scr refresh
                Break_key1.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Break_key1, 'tStopRefresh')  # time at next scr refresh
                Break_key1.status = FINISHED
        if Break_key1.status == STARTED and not waitOnFlip:
            theseKeys = Break_key1.getKeys(keyList=['0'], waitRelease=False)
            _Break_key1_allKeys.extend(theseKeys)
            if len(_Break_key1_allKeys):
                Break_key1.keys = _Break_key1_allKeys[-1].name  # just the last key pressed
                Break_key1.rt = _Break_key1_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in QuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Question"-------
    for thisComponent in QuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('Question_Image.started', Question_Image.tStartRefresh)
    Trials.addData('Question_Image.stopped', Question_Image.tStopRefresh)
    # check responses
    if Question_keyboard.keys in ['', [], None]:  # No response was made
        Question_keyboard.keys = None
    Trials.addData('Question_keyboard.keys',Question_keyboard.keys)
    if Question_keyboard.keys != None:  # we had a response
        Trials.addData('Question_keyboard.rt', Question_keyboard.rt)
    Trials.addData('Question_keyboard.started', Question_keyboard.tStartRefresh)
    Trials.addData('Question_keyboard.stopped', Question_keyboard.tStopRefresh)
    Trials.addData('Question_text.started', Question_text.tStartRefresh)
    Trials.addData('Question_text.stopped', Question_text.tStopRefresh)
    current_time = datetime.now()
    end_of_stimuli = current_time- start_time
    
    df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, Baselinequestion_name]
    if  Break_key1.keys is not None and len(Break_key1.keys)>0:
        if Break_key1.keys[0] == '0':
            Trials.finished=True
    # check responses
    if Break_key1.keys in ['', [], None]:  # No response was made
        Break_key1.keys = None
    Trials.addData('Break_key1.keys',Break_key1.keys)
    if Break_key1.keys != None:  # we had a response
        Trials.addData('Break_key1.rt', Break_key1.rt)
    Trials.addData('Break_key1.started', Break_key1.tStartRefresh)
    Trials.addData('Break_key1.stopped', Break_key1.tStopRefresh)
    # the Routine "Question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Answers"-------
    continueRoutine = True
    # update component parameters for each repeat
    Answers1Image.setImage(AnswerImage)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    current_time = datetime.now()
    start_of_stimuli = current_time- start_time
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str(AnswerImage))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str(AnswerImage))%1000000007, AnswerImage]
    thisExp.addData("ImagePath",AnswerImage)
    Break_key2.keys = []
    Break_key2.rt = []
    _Break_key2_allKeys = []
    # keep track of which components have finished
    AnswersComponents = [Answers1Image, key_resp_4, text_14, Break_key2]
    for thisComponent in AnswersComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    AnswersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Answers"-------
    while continueRoutine:
        # get current time
        t = AnswersClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=AnswersClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Answers1Image* updates
        if Answers1Image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Answers1Image.frameNStart = frameN  # exact frame index
            Answers1Image.tStart = t  # local t and not account for scr refresh
            Answers1Image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Answers1Image, 'tStartRefresh')  # time at next scr refresh
            Answers1Image.setAutoDraw(True)
        if Answers1Image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Answers1Image.tStartRefresh + Answer_Time-frameTolerance:
                # keep track of stop time/frame for later
                Answers1Image.tStop = t  # not accounting for scr refresh
                Answers1Image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Answers1Image, 'tStopRefresh')  # time at next scr refresh
                Answers1Image.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + Answer_Time-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['a', 's', 'd', 'f', 'space'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # was this correct?
                if (key_resp_4.keys == str(correct_answer)) or (key_resp_4.keys == correct_answer):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + Answer_Time-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *Break_key2* updates
        waitOnFlip = False
        if Break_key2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key2.frameNStart = frameN  # exact frame index
            Break_key2.tStart = t  # local t and not account for scr refresh
            Break_key2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key2, 'tStartRefresh')  # time at next scr refresh
            Break_key2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_key2.tStartRefresh + Answer_Time-frameTolerance:
                # keep track of stop time/frame for later
                Break_key2.tStop = t  # not accounting for scr refresh
                Break_key2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Break_key2, 'tStopRefresh')  # time at next scr refresh
                Break_key2.status = FINISHED
        if Break_key2.status == STARTED and not waitOnFlip:
            theseKeys = Break_key2.getKeys(keyList=['0'], waitRelease=False)
            _Break_key2_allKeys.extend(theseKeys)
            if len(_Break_key2_allKeys):
                Break_key2.keys = _Break_key2_allKeys[-1].name  # just the last key pressed
                Break_key2.rt = _Break_key2_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in AnswersComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Answers"-------
    for thisComponent in AnswersComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('Answers1Image.started', Answers1Image.tStartRefresh)
    Trials.addData('Answers1Image.stopped', Answers1Image.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(correct_answer).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for Trials (TrialHandler)
    Trials.addData('key_resp_4.keys',key_resp_4.keys)
    Trials.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        Trials.addData('key_resp_4.rt', key_resp_4.rt)
    Trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    Trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    current_time = datetime.now()
    end_of_stimuli = current_time- start_time
    
    df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, Baselineanswer_name]
    if  key_resp_4.keys is not None:
        answer = key_resp_4.keys[0]
        if answer == 's' and len(key_resp_4.keys)>1:
            answer = 'k'
        df_answer.loc[len(df_answer)] = [Baseline_name, answer]
    if  Break_key2.keys is not None and len(Break_key2.keys)>0:
        if Break_key2.keys[0] == '0':
            Trials.finished=True
    Trials.addData('text_14.started', text_14.tStartRefresh)
    Trials.addData('text_14.stopped', text_14.tStopRefresh)
    # check responses
    if Break_key2.keys in ['', [], None]:  # No response was made
        Break_key2.keys = None
    Trials.addData('Break_key2.keys',Break_key2.keys)
    if Break_key2.keys != None:  # we had a response
        Trials.addData('Break_key2.rt', Break_key2.rt)
    Trials.addData('Break_key2.started', Break_key2.tStartRefresh)
    Trials.addData('Break_key2.stopped', Break_key2.tStopRefresh)
    # the Routine "Answers" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Pause"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    key_resp_16.keys = []
    key_resp_16.rt = []
    _key_resp_16_allKeys = []
    Break_key3.keys = []
    Break_key3.rt = []
    _Break_key3_allKeys = []
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str("Pause"))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str("Pause"))%1000000007, "Pause"]
    thisExp.addData("ImagePath","Pause")
    # keep track of which components have finished
    PauseComponents = [key_resp_16, Break_key3, image_8]
    for thisComponent in PauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    PauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=PauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_16* updates
        waitOnFlip = False
        if key_resp_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_16.frameNStart = frameN  # exact frame index
            key_resp_16.tStart = t  # local t and not account for scr refresh
            key_resp_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_16, 'tStartRefresh')  # time at next scr refresh
            key_resp_16.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_16.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_16.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_16.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_16.tStop = t  # not accounting for scr refresh
                key_resp_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_16, 'tStopRefresh')  # time at next scr refresh
                key_resp_16.status = FINISHED
        if key_resp_16.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_16.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_16_allKeys.extend(theseKeys)
            if len(_key_resp_16_allKeys):
                key_resp_16.keys = _key_resp_16_allKeys[-1].name  # just the last key pressed
                key_resp_16.rt = _key_resp_16_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Break_key3* updates
        waitOnFlip = False
        if Break_key3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key3.frameNStart = frameN  # exact frame index
            Break_key3.tStart = t  # local t and not account for scr refresh
            Break_key3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key3, 'tStartRefresh')  # time at next scr refresh
            Break_key3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_key3.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                Break_key3.tStop = t  # not accounting for scr refresh
                Break_key3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Break_key3, 'tStopRefresh')  # time at next scr refresh
                Break_key3.status = FINISHED
        if Break_key3.status == STARTED and not waitOnFlip:
            theseKeys = Break_key3.getKeys(keyList=['0'], waitRelease=False)
            _Break_key3_allKeys.extend(theseKeys)
            if len(_Break_key3_allKeys):
                Break_key3.keys = _Break_key3_allKeys[-1].name  # just the last key pressed
                Break_key3.rt = _Break_key3_allKeys[-1].rt
        
        # *image_8* updates
        if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_8.frameNStart = frameN  # exact frame index
            image_8.tStart = t  # local t and not account for scr refresh
            image_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
            image_8.setAutoDraw(True)
        if image_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_8.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image_8.tStop = t  # not accounting for scr refresh
                image_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_8, 'tStopRefresh')  # time at next scr refresh
                image_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pause"-------
    for thisComponent in PauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_16.keys in ['', [], None]:  # No response was made
        key_resp_16.keys = None
    Trials.addData('key_resp_16.keys',key_resp_16.keys)
    if key_resp_16.keys != None:  # we had a response
        Trials.addData('key_resp_16.rt', key_resp_16.rt)
    Trials.addData('key_resp_16.started', key_resp_16.tStartRefresh)
    Trials.addData('key_resp_16.stopped', key_resp_16.tStopRefresh)
    # check responses
    if Break_key3.keys in ['', [], None]:  # No response was made
        Break_key3.keys = None
    Trials.addData('Break_key3.keys',Break_key3.keys)
    if Break_key3.keys != None:  # we had a response
        Trials.addData('Break_key3.rt', Break_key3.rt)
    Trials.addData('Break_key3.started', Break_key3.tStartRefresh)
    Trials.addData('Break_key3.stopped', Break_key3.tStopRefresh)
    if  Break_key3.keys is not None and len(Break_key3.keys)>0:
        if Break_key3.keys[0] == '0':
            Trials.finished=True
    Trials.addData('image_8.started', image_8.tStartRefresh)
    Trials.addData('image_8.stopped', image_8.tStopRefresh)
    
    # ------Prepare to start Routine "Pause1_2"-------
    continueRoutine = True
    routineTimer.add(5.000000)
    # update component parameters for each repeat
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    key_resp_23.keys = []
    key_resp_23.rt = []
    _key_resp_23_allKeys = []
    Break_key3_2.keys = []
    Break_key3_2.rt = []
    _Break_key3_2_allKeys = []
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str("Pause1_2"))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str("Pause1_2"))%1000000007, "Pause1_2"]
    thisExp.addData("ImagePath","Pause1_2")
    # keep track of which components have finished
    Pause1_2Components = [key_resp, key_resp_23, Break_key3_2, image_9]
    for thisComponent in Pause1_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    Pause1_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Pause1_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Pause1_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=Pause1_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp* updates
        waitOnFlip = False
        if key_resp.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp.tStartRefresh + 5.0-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp, 'tStopRefresh')  # time at next scr refresh
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                key_resp.rt = _key_resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *key_resp_23* updates
        waitOnFlip = False
        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_23.frameNStart = frameN  # exact frame index
            key_resp_23.tStart = t  # local t and not account for scr refresh
            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
            key_resp_23.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_23.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_23.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_23.tStop = t  # not accounting for scr refresh
                key_resp_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_23, 'tStopRefresh')  # time at next scr refresh
                key_resp_23.status = FINISHED
        if key_resp_23.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_23.getKeys(keyList=['return'], waitRelease=False)
            _key_resp_23_allKeys.extend(theseKeys)
            if len(_key_resp_23_allKeys):
                key_resp_23.keys = _key_resp_23_allKeys[-1].name  # just the last key pressed
                key_resp_23.rt = _key_resp_23_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Break_key3_2* updates
        waitOnFlip = False
        if Break_key3_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key3_2.frameNStart = frameN  # exact frame index
            Break_key3_2.tStart = t  # local t and not account for scr refresh
            Break_key3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key3_2, 'tStartRefresh')  # time at next scr refresh
            Break_key3_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key3_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key3_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key3_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Break_key3_2.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                Break_key3_2.tStop = t  # not accounting for scr refresh
                Break_key3_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Break_key3_2, 'tStopRefresh')  # time at next scr refresh
                Break_key3_2.status = FINISHED
        if Break_key3_2.status == STARTED and not waitOnFlip:
            theseKeys = Break_key3_2.getKeys(keyList=['0'], waitRelease=False)
            _Break_key3_2_allKeys.extend(theseKeys)
            if len(_Break_key3_2_allKeys):
                Break_key3_2.keys = _Break_key3_2_allKeys[-1].name  # just the last key pressed
                Break_key3_2.rt = _Break_key3_2_allKeys[-1].rt
        
        # *image_9* updates
        if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_9.frameNStart = frameN  # exact frame index
            image_9.tStart = t  # local t and not account for scr refresh
            image_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
            image_9.setAutoDraw(True)
        if image_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_9.tStartRefresh + 5-frameTolerance:
                # keep track of stop time/frame for later
                image_9.tStop = t  # not accounting for scr refresh
                image_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
                image_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Pause1_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Pause1_2"-------
    for thisComponent in Pause1_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    Trials.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        Trials.addData('key_resp.rt', key_resp.rt)
    Trials.addData('key_resp.started', key_resp.tStartRefresh)
    Trials.addData('key_resp.stopped', key_resp.tStopRefresh)
    # check responses
    if key_resp_23.keys in ['', [], None]:  # No response was made
        key_resp_23.keys = None
    Trials.addData('key_resp_23.keys',key_resp_23.keys)
    if key_resp_23.keys != None:  # we had a response
        Trials.addData('key_resp_23.rt', key_resp_23.rt)
    Trials.addData('key_resp_23.started', key_resp_23.tStartRefresh)
    Trials.addData('key_resp_23.stopped', key_resp_23.tStopRefresh)
    # check responses
    if Break_key3_2.keys in ['', [], None]:  # No response was made
        Break_key3_2.keys = None
    Trials.addData('Break_key3_2.keys',Break_key3_2.keys)
    if Break_key3_2.keys != None:  # we had a response
        Trials.addData('Break_key3_2.rt', Break_key3_2.rt)
    Trials.addData('Break_key3_2.started', Break_key3_2.tStartRefresh)
    Trials.addData('Break_key3_2.stopped', Break_key3_2.tStopRefresh)
    if  Break_key3.keys is not None and len(Break_key3.keys)>0:
        if Break_key3.keys[0] == '0':
            Trials.finished=True
    Trials.addData('image_9.started', image_9.tStartRefresh)
    Trials.addData('image_9.stopped', image_9.tStopRefresh)
    
    # ------Prepare to start Routine "ProgComprQuestion"-------
    continueRoutine = True
    # update component parameters for each repeat
    ProgCompr_Question.setImage(ProgrammingQuestion)
    current_time = datetime.now()
    start_of_stimuli = current_time- start_time
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str(ProgrammingQuestion))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str(ProgrammingQuestion))%1000000007, ProgrammingQuestion]
    thisExp.addData("ImagePath",ProgrammingQuestion)
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    Break_key4.keys = []
    Break_key4.rt = []
    _Break_key4_allKeys = []
    # keep track of which components have finished
    ProgComprQuestionComponents = [ProgCompr_Question, key_resp_3, text_2, Break_key4]
    for thisComponent in ProgComprQuestionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ProgComprQuestionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ProgComprQuestion"-------
    while continueRoutine:
        # get current time
        t = ProgComprQuestionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ProgComprQuestionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ProgCompr_Question* updates
        if ProgCompr_Question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            ProgCompr_Question.frameNStart = frameN  # exact frame index
            ProgCompr_Question.tStart = t  # local t and not account for scr refresh
            ProgCompr_Question.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ProgCompr_Question, 'tStartRefresh')  # time at next scr refresh
            ProgCompr_Question.setAutoDraw(True)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_2* updates
        if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_2.frameNStart = frameN  # exact frame index
            text_2.tStart = t  # local t and not account for scr refresh
            text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *Break_key4* updates
        waitOnFlip = False
        if Break_key4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key4.frameNStart = frameN  # exact frame index
            Break_key4.tStart = t  # local t and not account for scr refresh
            Break_key4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key4, 'tStartRefresh')  # time at next scr refresh
            Break_key4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key4.status == STARTED and not waitOnFlip:
            theseKeys = Break_key4.getKeys(keyList=['0'], waitRelease=False)
            _Break_key4_allKeys.extend(theseKeys)
            if len(_Break_key4_allKeys):
                Break_key4.keys = _Break_key4_allKeys[-1].name  # just the last key pressed
                Break_key4.rt = _Break_key4_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ProgComprQuestionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ProgComprQuestion"-------
    for thisComponent in ProgComprQuestionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Trials.addData('ProgCompr_Question.started', ProgCompr_Question.tStartRefresh)
    Trials.addData('ProgCompr_Question.stopped', ProgCompr_Question.tStopRefresh)
    current_time = datetime.now()
    end_of_stimuli = current_time- start_time
    
    df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, Pr_question_name]
    if  Break_key4.keys is not None and len(Break_key4.keys)>0:
        if Break_key4.keys[0] == '0':
            Trials.finished=True
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    Trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        Trials.addData('key_resp_3.rt', key_resp_3.rt)
    Trials.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    Trials.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    Trials.addData('text_2.started', text_2.tStartRefresh)
    Trials.addData('text_2.stopped', text_2.tStopRefresh)
    # check responses
    if Break_key4.keys in ['', [], None]:  # No response was made
        Break_key4.keys = None
    Trials.addData('Break_key4.keys',Break_key4.keys)
    if Break_key4.keys != None:  # we had a response
        Trials.addData('Break_key4.rt', Break_key4.rt)
    Trials.addData('Break_key4.started', Break_key4.tStartRefresh)
    Trials.addData('Break_key4.stopped', Break_key4.tStopRefresh)
    # the Routine "ProgComprQuestion" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ProgComprInput"-------
    continueRoutine = True
    # update component parameters for each repeat
    current_time = datetime.now()
    start_of_stimuli = current_time- start_time
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str(ProgrammingInput))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str(ProgrammingInput))%1000000007, ProgrammingInput]
    thisExp.addData("ImagePath",ProgrammingInput)
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    Break_key5.keys = []
    Break_key5.rt = []
    _Break_key5_allKeys = []
    image_7.setImage(ProgrammingInput)
    # keep track of which components have finished
    ProgComprInputComponents = [text_3, key_resp_5, Break_key5, image_7]
    for thisComponent in ProgComprInputComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ProgComprInputClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ProgComprInput"-------
    while continueRoutine:
        # get current time
        t = ProgComprInputClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ProgComprInputClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *Break_key5* updates
        waitOnFlip = False
        if Break_key5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key5.frameNStart = frameN  # exact frame index
            Break_key5.tStart = t  # local t and not account for scr refresh
            Break_key5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key5, 'tStartRefresh')  # time at next scr refresh
            Break_key5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key5.status == STARTED and not waitOnFlip:
            theseKeys = Break_key5.getKeys(keyList=['0'], waitRelease=False)
            _Break_key5_allKeys.extend(theseKeys)
            if len(_Break_key5_allKeys):
                Break_key5.keys = _Break_key5_allKeys[-1].name  # just the last key pressed
                Break_key5.rt = _Break_key5_allKeys[-1].rt
        
        # *image_7* updates
        if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_7.frameNStart = frameN  # exact frame index
            image_7.tStart = t  # local t and not account for scr refresh
            image_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
            image_7.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ProgComprInputComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ProgComprInput"-------
    for thisComponent in ProgComprInputComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    current_time = datetime.now()
    end_of_stimuli = current_time- start_time
    
    df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, Pr_input_name]
    if  Break_key5.keys is not None and len(Break_key5.keys)>0:
        if Break_key5.keys[0] == '0':
            Trials.finished=True
    Trials.addData('text_3.started', text_3.tStartRefresh)
    Trials.addData('text_3.stopped', text_3.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    Trials.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        Trials.addData('key_resp_5.rt', key_resp_5.rt)
    Trials.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    Trials.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # check responses
    if Break_key5.keys in ['', [], None]:  # No response was made
        Break_key5.keys = None
    Trials.addData('Break_key5.keys',Break_key5.keys)
    if Break_key5.keys != None:  # we had a response
        Trials.addData('Break_key5.rt', Break_key5.rt)
    Trials.addData('Break_key5.started', Break_key5.tStartRefresh)
    Trials.addData('Break_key5.stopped', Break_key5.tStopRefresh)
    Trials.addData('image_7.started', image_7.tStartRefresh)
    Trials.addData('image_7.stopped', image_7.tStopRefresh)
    # the Routine "ProgComprInput" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "ProgComprAnswer"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    current_time = datetime.now()
    start_of_stimuli = current_time- start_time
    
    if use_devices==True: 
        eeg_logger.refresh()
        eeg_logger.set_event(hash(str(ProgrammingAnswer))%1000000007)
        df_hash.loc[len(df_hash)] = [hash(str(ProgrammingAnswer))%1000000007, ProgrammingAnswer]
    thisExp.addData("ImagePath",ProgrammingAnswer)
    image_3.setImage(ProgrammingAnswer)
    Break_key6.keys = []
    Break_key6.rt = []
    _Break_key6_allKeys = []
    # keep track of which components have finished
    ProgComprAnswerComponents = [key_resp_2, image_3, text_5, Break_key6]
    for thisComponent in ProgComprAnswerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    ProgComprAnswerClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "ProgComprAnswer"-------
    while continueRoutine:
        # get current time
        t = ProgComprAnswerClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=ProgComprAnswerClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['a', 's', 'd', 'f', 'space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # was this correct?
                if (key_resp_2.keys == str(Pr_correct_answer)) or (key_resp_2.keys == Pr_correct_answer):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *Break_key6* updates
        waitOnFlip = False
        if Break_key6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Break_key6.frameNStart = frameN  # exact frame index
            Break_key6.tStart = t  # local t and not account for scr refresh
            Break_key6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Break_key6, 'tStartRefresh')  # time at next scr refresh
            Break_key6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Break_key6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Break_key6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Break_key6.status == STARTED and not waitOnFlip:
            theseKeys = Break_key6.getKeys(keyList=['0'], waitRelease=False)
            _Break_key6_allKeys.extend(theseKeys)
            if len(_Break_key6_allKeys):
                Break_key6.keys = _Break_key6_allKeys[-1].name  # just the last key pressed
                Break_key6.rt = _Break_key6_allKeys[-1].rt
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ProgComprAnswerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ProgComprAnswer"-------
    for thisComponent in ProgComprAnswerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
        # was no response the correct answer?!
        if str(Pr_correct_answer).lower() == 'none':
           key_resp_2.corr = 1;  # correct non-response
        else:
           key_resp_2.corr = 0;  # failed to respond (incorrectly)
    # store data for Trials (TrialHandler)
    Trials.addData('key_resp_2.keys',key_resp_2.keys)
    Trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        Trials.addData('key_resp_2.rt', key_resp_2.rt)
    Trials.addData('key_resp_2.started', key_resp_2.tStartRefresh)
    Trials.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
    current_time = datetime.now()
    end_of_stimuli = current_time- start_time
    
    df_stimuli.loc[len(df_stimuli)] = [start_of_stimuli, end_of_stimuli, Pr_answer_name]
    answer = key_resp_2.keys[0]
    if answer == 's' and len(key_resp_2.keys)>1:
            answer = 'k'
    df_answer.loc[len(df_answer)] = [Pr_task_name, answer]
    if  Break_key6.keys is not None and len(Break_key6.keys)>0:
        if Break_key6.keys[0] == '0':
            Trials.finished=True
    Trials.addData('image_3.started', image_3.tStartRefresh)
    Trials.addData('image_3.stopped', image_3.tStopRefresh)
    Trials.addData('text_5.started', text_5.tStartRefresh)
    Trials.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if Break_key6.keys in ['', [], None]:  # No response was made
        Break_key6.keys = None
    Trials.addData('Break_key6.keys',Break_key6.keys)
    if Break_key6.keys != None:  # we had a response
        Trials.addData('Break_key6.rt', Break_key6.rt)
    Trials.addData('Break_key6.started', Break_key6.tStartRefresh)
    Trials.addData('Break_key6.stopped', Break_key6.tStopRefresh)
    # the Routine "ProgComprAnswer" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'Trials'


# ------Prepare to start Routine "ThankYou"-------
continueRoutine = True
routineTimer.add(10.000000)
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
ThankYouComponents = [text_6, key_resp_6]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ThankYouClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "ThankYou"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ThankYouClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ThankYouClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    if text_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_6.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            text_6.tStop = t  # not accounting for scr refresh
            text_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
            text_6.setAutoDraw(False)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_6.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_6.tStop = t  # not accounting for scr refresh
            key_resp_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
            key_resp_6.status = FINISHED
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['return'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "ThankYou"-------
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()

if use_devices:
    eeg_logger.refresh()
    eeg_logger.disconnect()
    eeg_logger.save("EEG_raw", f"./data/Session_{session}_Participant_{participant}/")
    eyetracking_logger.stop_recording()

df_stimuli.to_csv(f"{folder_name}/Stimuli_Times.csv")
df_answer.to_csv(f"{folder_name}/Task_Answers.csv")
df_hash.to_csv(f"{folder_name}/Hashs.csv")

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
