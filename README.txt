CSC 212 | p4-skeleton.py | Bruinsma, Chi, Feliciano, Li, Paden

This project takes the inputs from the face and outputs a facial gesture when there is a heuristic for that gesture
The script will stop printing if none of the conditions below are met. 


The main types we highlighted were:

- Nodding: Associated with a change in the pitch of the users head
- Indian Nodding: Associated with a change in the roll of a person's head
- Shaking: Which is Associated with a significant change in the yaw of a person's head.

- Smiling: Which is associated with the ratio between the sides of the mouth and the middle of the mouth. Points: 62,66,48,54
- Surprise: Which is associated with the ratio between the distance of the  eyebrows to the top of the eyes and the distance of the
  bottom of the mouth to the chin -- Essentially, how far apart are the eyebrows to the bottom of the mouth. 8, 19, 24, 57 

This has been shown to work on both men and women.  

It occasionally throws a : divide by zero error, this occurs when either A, the system has crashed or B, the person is not being seen in the Frame.


