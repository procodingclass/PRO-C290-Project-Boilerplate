from controller import Robot
from controller import Keyboard
from controller import Pen

# create the Robot instance.
robot = Robot()
kb= Keyboard()

timestep = int(robot.getBasicTimeStep())

motorA = robot.getDevice("A motor")
motorB = robot.getDevice("B motor")
motorC = robot.getDevice("C motor")
motorD = robot.getDevice("D motor")
motorE = robot.getDevice("E motor")
motorF = robot.getDevice("F motor")

pen=robot.getDevice("pen")

kb.enable(timestep)

ds= robot.getDevice("ds")
ds.enable(timestep)

motorA_pos=3.14
motorB_pos=0
motorC_pos=0
motorD_pos=0
motorE_pos=0
motorF_pos=0

draw=True

colors=[0xF01010,0xFF7F00,0xFFFF00,0x00FF00,0x0000FF,0x4B0082,0x9400D3]
color_index=0

  
        
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    ds_val=ds.getValue()
    # print(movement)
    
    
     
    motorA.setPosition(motorA_pos)
    motorB.setPosition(motorB_pos)
    motorC.setPosition(motorC_pos)
    motorD.setPosition(motorD_pos)
    motorE.setPosition(motorE_pos)
    motorF.setPosition(motorF_pos)