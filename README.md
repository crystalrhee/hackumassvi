# Air Keys
<img src="https://user-images.githubusercontent.com/25557896/46908646-c1499580-cef3-11e8-93c7-9a2243e19933.png"/>
  
Created for HackUMass VI, this project is a motion activated music player that uses Leap Motion to detect gestures. These gestures are linked to media commands and can be used to control any music player.  
## Table of Contents  :smile::smile::smile:
- [Installation](#installation)  
- [Commands](#commands)  
- [Features](#features)
- [Software Stack](#software-stack)
- [Next Steps](#next-steps)  
- [FAQ](#faq)  
- [Credits](#credits)  
## Installation
:wink: :kissing_smiling_eyes:
### Please Install:  
  Python 2.7  - https://www.python.org/downloads/release/python-2715/  
  Leap Motion (V2 Tracking) - https://www.leapmotion.com/setup/desktop/  
  Flask - https://pypi.org/project/Flask/
### And Buy  
  Leap Motion Controller  
  ![leap560](https://user-images.githubusercontent.com/25557896/46907770-abcd6f00-cee5-11e8-8a68-b1144c110064.jpg)
## Commands
:open_mouth:    
Keytap -  a quick, downward tapping movement  
:point_up_2:
Keytap - Play/Pause  
![leap_gesture_tap](https://user-images.githubusercontent.com/25557896/46910611-822c3c00-cf15-11e8-9012-db2364a5478e.png)  

Swipe - a linear movement of a finger to the left or right  
:point_left:  :point_right:  
Swipe left - Previous Track  
Swipe right - Next Track  
![leap_gesture_swipe resized](https://user-images.githubusercontent.com/25557896/46910758-40e95b80-cf18-11e8-889c-39430127dc51.png)  

Circles - A finger tracing a circle in space  
:point_up_2:
Clockwise-circle - Volume Up  
Counter-clockwise circle - Volume Down  
![leap_gesture_circle](https://user-images.githubusercontent.com/25557896/46910609-7fc9e200-cf15-11e8-9b25-c09985cea990.png)  

![ezgif-1-aca0cc16fcd5](https://user-images.githubusercontent.com/25557896/46909380-7c2b6080-ceff-11e8-8fab-c86d151e9dfd.gif)  
## Features  
- Our Flask server supports multiple clients concurrently viewing one user's music play experience.  
## Software Stack
Main.py uses Leap Motion hardware to record gestures and corresponding commands and posts them to the Flask server which renders it for the user.  
![hackumassstack](https://user-images.githubusercontent.com/25557896/46913071-2634d800-cf54-11e8-905e-301e9214e537.jpg)  
## Next Steps  
:smile_cat::smile_cat::smile_cat:  
With more time, we would create greater user interactoin. We would use Unity to create a 3D menu of options to configure personal settings. Along with the menu, we would create interactive blocks for more complicated commands such as choosing the next song from a favorites playlist.
![20151106-155554b-1024x564](https://user-images.githubusercontent.com/25557896/46912083-0644ea80-cf3b-11e8-9c79-6972cdd30b76.jpg)  
Additionally, we would create multiple modes where users could access additional features. One mode would be the Morse Code Interpreter where users could enter morse code dots with a swipe down motion and see their completed message when ending the Morse Code mode with the swith modes command.  
Command to Switch Modes  
![close-up-two-hands-putting-fingers-together-gesture-count-body-parts-concept-forefingers-69189651](https://user-images.githubusercontent.com/25557896/46912181-57091300-cf3c-11e8-90f7-31f93c17897b.jpg)  
## FAQ
:japanese_ogre: :pouting_cat: :heart_eyes_cat:
- How can I learn more about Leap Motion?  
The official website for Leap Motion has a great start-up guide for new users, however their sample code for the Python SDK may have some errors. If one finds errors, they can reference our code above.  
https://developer.leapmotion.com/#101  
- Are there similar music-related Leap Motion technologies?  
Composers may be interested in http://lyravr.com/ which allows users to compose music through interactive blocks
- Will this work on any OS?
It has been tested the most on OSX, but it will run on Windows as well. Feel free to submit issues here.
## Credits
:grin: :smiley_cat:
- **Crystal Rhee**  
  Northeastern University  
  Computer Science and Finance Major  

- **Ivan Chen**  
  Northeastern University  
  Computer Science Major  

- **Jonathan Shee**  
  UMass Amherst  
  Computer Science Major  

- **Timothy Shee**:  High School :love_letter: :eyes: :tongue: :lips: :trollface:
## Licensing  
  MIT License
