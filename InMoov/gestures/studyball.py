def studyball():
  i01.disableRobotRandom(30)
  ##keepball():
  sleep(3)
  i01.setHandSpeed("left", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setHandSpeed("right", 0.65, 0.65, 0.65, 0.65, 0.65, 1.0)
  i01.setArmSpeed("right", 0.75, 0.85, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.95, 0.85)
  i01.setHeadSpeed(0.9, 0.9)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,70)
  i01.moveArm("left",5,84,16,20)
  i01.moveArm("right",54,77,55,10)
  i01.moveHand("left",50,50,40,20,20,90)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,90,90)
  sleep(3)
  ##approachlefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.setTorsoSpeed(0.75, 0.55, 1.0)
  i01.moveHead(20,84)
  i01.moveArm("left",65,42,62,23)
  i01.moveArm("right",60,50,45,10)
  i01.moveHand("left",130,0,0,10,10,0)
  i01.moveHand("right",180,145,145,3,0,11)
  i01.moveTorso(90,85,90)
  sleep(4)
  ##uselefthand():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 0.25, 0.25, 0.25, 0.25)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(10,80)
  i01.moveArm("left",80,42,59,23)
  i01.moveArm("right",85,50,50,10)
  i01.moveHand("left",130,0,40,10,10,0)
  i01.moveHand("right",180,140,145,3,0,11)
  sleep(4)
  ##more():
  i01.setHandSpeed("right", 0.75, 0.75, 0.75, 0.75, 0.75, 0.65)
  i01.setArmSpeed("left", 0.85, 0.80, 0.85, 0.95)
  i01.setArmSpeed("right", 0.75, 0.65, 0.65, 0.65)
  i01.setHeadSpeed(0.65, 0.65)
  i01.moveHead(13,80)
  i01.moveArm("left",80,42,59,23)
  i01.moveArm("right",85,50,50,10)
  i01.moveHand("left",160,148,140,10,10,0)
  i01.moveHand("right",60,75,75,3,0,11)
  sleep(3)
  ##handdown():
  i01.setHandSpeed("left", 0.75, 0.75, 0.75, 0.75, 0.75, 0.75)
  i01.setHandSpeed("right", 0.70, 0.70, 0.70, 0.70, 0.70, 1.0)
  i01.setArmSpeed("right", 0.85, 0.65, 0.65, 0.65)
  i01.moveHead(18,75)
  i01.moveArm("left",80,42,59,23)
  i01.moveArm("right",59,50,50,10)
  i01.moveHand("left",160,148,140,10,10,0)
  i01.moveHand("right",40,60,40,0,0,11)
  sleep(2)
  #isitaball():
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 0.8, 0.8, 0.90)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 0.95, 0.95, 0.85)
  i01.setArmSpeed("left", 0.75, 0.85, 0.90, 0.85)
  i01.setHeadSpeed(0.65, 0.75)
  i01.moveHead(70,82)
  i01.moveArm("left",80,59,95,15)
  i01.moveArm("right",12,74,33,15)
  i01.moveHand("left",170,150,180,180,180,164)
  i01.moveHand("right",105,81,78,57,62,105)
  #i01.mouth.speakBlocking("I will start tracking the object")
  sleep(2)
  i01.mouth.speakBlocking("I think it is a ball")
  #i01.mouth.speakBlocking("you need to set the point")
  fullspeed()
  
  i01.headTracking.startLKTracking()
  i01.eyesTracking.startLKTracking()