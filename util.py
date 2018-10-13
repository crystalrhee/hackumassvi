################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

import os, io, sys, thread, time, inspect

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import lib.Leap as Leap
from lib.Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import keys


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    playing = False
    last_update = 0.0

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        # controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()

        # print "Frame id: %d, timestamp: %d, hands: %d, fingers: %d, tools: %d, gestures: %d" % (
        #       frame.id, frame.timestamp, len(frame.hands), len(frame.fingers), len(frame.tools), len(frame.gestures()))

        # Get gestures
        for gesture in frame.gestures():
            # if gesture.type == Leap.Gesture.TYPE_CIRCLE:
            #     circle = CircleGesture(gesture)

            #     # Determine clock direction using the angle between the pointable and the circle normal
            #     if circle.pointable.direction.angle_to(circle.normal) <= Leap.PI/2:
            #         clockwiseness = "clockwise"
            #     else:
            #         clockwiseness = "counterclockwise"

            #     # Calculate the angle swept since the last frame
            #     swept_angle = 0
            #     if circle.state != Leap.Gesture.STATE_START:
            #         previous_update = CircleGesture(controller.frame(1).gesture(circle.id))
            #         swept_angle =  (circle.progress - previous_update.progress) * 2 * Leap.PI

            #     print "  Circle id: %d, %s, progress: %f, radius: %f, angle: %f degrees, %s" % (
            #             gesture.id, self.state_names[gesture.state],
            #             circle.progress, circle.radius, swept_angle * Leap.RAD_TO_DEG, clockwiseness)

            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                # swipe left
                if swipe.direction[0] < -0.8:
                    print 'prev track'
                    press('prevtrack')
                elif swipe.direction[0] > 0.8:
                    print 'next track'
                    press('nexttrack')
                elif swipe.direction[1] < 0.8:
                    diff = time.time() - self.last_update
                    if diff < 1:
                        print 'ignore, diff is:', diff, 'it is now playing: ', self.playing
                    else:
                        self.playing = not self.playing
                        self.last_update = time.time()
                        keys.HIDPostAuxKey(keys.NX_KEYTYPE_PLAY)
                        print 'play pause', self.playing
                        
                # time.sleep(1)

                # print "  Swipe id: %d, state: %s, position: %s, direction: %s, speed: %f" % (
                #         gesture.id, self.state_names[gesture.state],
                #         swipe.position, swipe.direction, swipe.speed)
