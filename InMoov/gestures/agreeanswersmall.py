def agreeanswersmall():
  i01.disableRobotRandom(30)
  i01.setHandSpeed("left", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setHandSpeed("right", 1.0, 1.0, 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("left", 1.0, 1.0, 1.0, 1.0)
  i01.setArmSpeed("right", 1.0, 1.0, 1.0, 1.0)
  i01.setHeadSpeed(1.0, 0.90)
  i01.setTorsoSpeed(1.0, 1.0, 1.0)
  sleep(1)
  i01.moveHead(20,90)
  i01.moveArm("left",8,82,28,16)
  i01.moveArm("right",8,82,28,16)
  i01.moveHand("left",60,60,65,81,41,90)
  i01.moveHand("right",60,60,18,61,36,90)
  i01.moveTorso(90,90,90)
  sleep(0.5)
  i01.moveHead(90,90)
  sleep(1)
  relax()
