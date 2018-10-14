import sys, os, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap as Leap
from music_listener import MusicListener
# from morse_listener import MorseListener

def main():
    # Create a sample listener and controller
    music_listener = MusicListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(music_listener)

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


