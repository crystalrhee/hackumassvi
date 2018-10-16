import os, io, sys, thread, time, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap as Leap
from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import keys
import requests
'''
    This contains all the logic for the music state.

    It's able to recognize multiple gestures including:
        * [left, right, down] swipes for play/pause, prev track, and next track
        * (index finger out) circular motions (clock/counter clock wise) for vol up/down
    
    Two things happen when a command is triggered:
        1. simulate the key press for the specific command (works only for Mac)
        2. send a POST request of the command to the server (used for the front-end)
'''

SERVER_IP = 'http://localhost:5000'


class MusicListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    playing = False
    last_update = 0.0

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        index_extended = False

        for hand in frame.hands:
            index_extended = True
            for i, finger in enumerate(hand.fingers):
                index_extended = index_extended and (
                    (i == 1) == finger.is_extended)

        # Get gestures
        for gesture in frame.gestures():
            diff = time.time() - self.last_update

            if gesture.type == Leap.Gesture.TYPE_CIRCLE and index_extended:
                circle = CircleGesture(gesture)

                # don't update too often, make sure last command was x seconds ago
                if diff > 0.3:
                    # clockwise
                    if circle.pointable.direction.angle_to(
                            circle.normal) <= Leap.PI / 2:
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_SOUND_UP)
                        print 'volume up', time.time()
                        r = requests.post(
                            SERVER_IP, json={'command': 'volume_up'})
                    else:
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_SOUND_DOWN)
                        print 'volume down', time.time()
                        r = requests.post(
                            SERVER_IP, json={'command': 'volume_down'})
                    self.last_update = time.time()

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                diff = time.time() - self.last_update
                if diff > 1:
                    # swipe left
                    if swipe.direction[0] < -0.8:
                        print 'prev track'
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_PREVIOUS)
                        self.last_update = time.time()
                        r = requests.post(
                            SERVER_IP, json={'command': 'swipe_left'})
                    # swipe right
                    elif swipe.direction[0] > 0.8:
                        print 'next track'
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_NEXT)
                        self.last_update = time.time()
                        r = requests.post(
                            SERVER_IP, json={'command': 'swipe_right'})
                    # swipe down
                    elif swipe.direction[1] < 0.8:
                        self.playing = not self.playing
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_PLAY)
                        print 'is playing: ', self.playing
                        self.last_update = time.time()
                        r = requests.post(
                            SERVER_IP, json={'command': 'play_pause'})


# For debugging purposes
if __name__ == "__main__":
    # Create a sample listener and controller
    listener = MusicListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)