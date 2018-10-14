import os, io, sys, thread, time, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap as Leap
from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import keys


class MusicListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    change_gesture = None
    playing = False
    last_update = 0.0

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"



    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        for hand in frame.hands:
            for finger in hand.fingers:
                int extendedFingers = 0
                for (int f = 0; f < hand.fingers().count(); f++)
                {
                    Leap::Finger finger = hand.fingers()[f];
                    if(finger.isExtended()) extendedFingers++;
                }
            print(finger)

        # Get gestures
        for gesture in frame.gestures():
            diff = time.time() - self.last_update
            # if gesture.type
            # print hand.fingers
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                if not change_gesture:
                    change_gesture = gesture

                circle = CircleGesture(gesture)

                # clockwise
                if diff > 0.3:
                    if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_SOUND_UP)
                        print 'volume up', time.time()
                    else:
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_SOUND_DOWN)
                        print 'volume down', time.time()
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
                    # swipe right
                    elif swipe.direction[0] > 0.8:
                        print 'next track'
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_NEXT)
                        self.last_update = time.time()
                    # swipe down
                    elif swipe.direction[1] < 0.8:
                        self.playing = not self.playing
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_PLAY)
                        print 'is playing: ', self.playing
                        self.last_update = time.time()
                        
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