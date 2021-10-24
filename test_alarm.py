import unittest
from alarm import *

class MyFirstTests(unittest.TestCase):

    def test_alarmIsOffAfterCreation(self):
        a = Alarm()
        self.assertFalse(a.isActive())
    
    def test_alarmIsNotRingingAfterCreation(self):
        a = Alarm()
        self.assertFalse(a.isRinging())

    def test_offAlarmDetectingMotionDoesNotRing(self):
        a = Alarm()
        a.deactivate()
        self.assertFalse(a.isRinging())

    def test_onAlarmDetectingMotionDoesRing(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        self.assertTrue(a.isRinging())

    def test_alarmDoesNotRingAfter_Activation_MotionDetection_Reset(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        a.reset()
        self.assertFalse(a.isRinging())

    def test_alarmIsOnAfter_Activation_MotionDetection_Reset(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        a.reset()
        self.assertTrue(a.isActive())

    def test_alarmIsOffAfter_A_D(self):
        a = Alarm()
        a.activate()
        a.deactivate()
        self.assertFalse(a.isActive())
    
    def test_alarmIsOffAfter_A_MD_D(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        a.deactivate()
        self.assertFalse(a.isActive())

    def test_alarmDoesNotRingAfter_A_MD_D(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        a.deactivate()
        self.assertFalse(a.isRinging())

    def test_alarmDoesRingAfter_A_MD_R_MD(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        a.reset()
        a.motionDetected()
        self.assertTrue(a.isRinging())

    def test_offAlarmDoesNotRingAfter_ThreeMotionDetections(self):
        a = Alarm()
        a.deactivate()
        a.motionDetected()
        a.motionDetected()
        a.motionDetected()
        self.assertFalse(a.isRinging())

    def test_a_ringing_alarm_deactivated_does_not_ring_anymore_if_it_detects_motion(self):
        a = Alarm()
        a.activate()
        a.motionDetected()
        a.deactivate()
        a.motionDetected()
        self.assertFalse(a.isRinging())
    