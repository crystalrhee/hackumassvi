import sys, os, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap as Leap
from music_listener import MusicListener
# from morse_listener import MorseListener
'''
    This is the main file that is in charge of creating a Leap controller
    object and attach listeners to it.
'''


def main():
    '''
    TODO:   Idea we had: able to change to a different state by using 
            a specific hand gesture.
            E.g. when thumb and pinky touches together, we transition to state
            A, when thumb and ring finger touches together we transition
            to state B.
            This can *possibly* be done by always having two active listeners
            on the Leap controller. One is listening for "state change" gestures
            and the other one is the current active state's listener.
    '''

    # Create a sample listener and controller
    music_listener = MusicListener()
    # morse_listener = MorseListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(music_listener)
    # controller.add_listener(morse_listener)

    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
