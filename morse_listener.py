import os, io, sys, thread, time, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap as Leap
from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import keys
# import numpy as np
import math

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
    	if self.size() >= 10:
    		self.dequeue()
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def average(self):
    	return float(sum(self.items) / 10.0)

class MorseListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
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
    	def distance(p1, p2):
			"""Calculates the distance between two points in a 3d space.

			Args:
				p1 (triplet): first point  (x, y, z)
				p2 (triplet): second point (x, y, z)

			Returns:
				float: the distance between two points

			"""
			return int(math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2))

        # Get the most recent frame and report some basic information
        frame = controller.frame()

        prevs = Queue()

        for hand in frame.hands:
        	pos = []
	        for finger in hand.fingers:
	        	pos.append(finger.tip_position)
	        dist = distance(pos[0], pos[1])
	        print prevs.average()
	        # print abs(prevs.average() - dist)
	        # if abs(prevs.average() - dist) > 30:
	        # 	print 'DOT', time.time()
	        prevs.enqueue(dist)
	        print prevs.items 

def main():
    # Create a sample listener and controller
    listener = MorseListener()
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


if __name__ == "__main__":
    main()
