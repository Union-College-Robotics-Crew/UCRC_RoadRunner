# UCRC_robot
## Instruction for fast update on robot: (MAC)
First right click on the folder and open with Terminal.
Next make sure the folder is empty with `ls -a`
Remove everything `.` file individually with `rm -rf <file name including the dot>
Files without `.` can be simply removed all by `rm -rf *`
Then use the following code:
```
git clone https://github.com/Union-College-Robotics-Crew/UCRC_RoadRunner.git .
```

##Upload code from robot to main
```
git checkout <new branch>
```
rest is usual git commit-push stuff.
