import unittest
from alarm import *

class MyFirstTests(unittest.TestCase):

    def setUp(self):
        self.a = Alarm()

    def test_alarmIsOffAfterCreation(self):
        self.assertFalse(self.a.isActive())
    
    def test_alarmIsNotRingingAfterCreation(self):
        self.assertFalse(self.a.isRinging())

    def test_offAlarmDetectingMotionDoesNotRing(self):

        self.a.deactivate()
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())

    def test_onAlarmDetectingMotionDoesRing(self):
        self.a.activate()
        self.a.motionDetected()
        self.assertTrue(self.a.isRinging())

    def test_alarmDoesNotRingAfter_Activation_MotionDetection_Reset(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.assertFalse(self.a.isRinging())

    def test_alarmIsOnAfter_Activation_MotionDetection_Reset(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.assertTrue(self.a.isActive())

    def test_alarmIsOffAfter_Activation_Deactivation(self):
        self.a.activate()
        self.a.deactivate()
        self.assertFalse(self.a.isActive())
    
    def test_alarmIsOffAfter_Activation_MotionDetection_Deactivation(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.deactivate()
        self.assertFalse(self.a.isActive())

    def test_alarmDoesNotRingAfter_Activation_MotionDetection_Deactivation(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.deactivate()
        self.assertFalse(self.a.isRinging())

    def test_alarmDoesRingAfter_Activation_MotionDetection_Reset_MotionDetection(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.reset()
        self.a.motionDetected()
        self.assertTrue(self.a.isRinging())

    def test_offAlarmDoesNotRingAfter_ThreeMotionDetections(self):
        self.a.deactivate()
        self.a.motionDetected()
        self.a.motionDetected()
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())

    def test_a_ringing_alarm_deactivated_does_not_ring_anymore_if_it_detects_motion(self):
        self.a.activate()
        self.a.motionDetected()
        self.a.deactivate()
        self.a.motionDetected()
        self.assertFalse(self.a.isRinging())
