# TDD example (pytdd)

This code demonstrates the Test Driven Development (TDD) approach. It uses the `unittest` module.

The class under test is an alarm class. Its methods are:

  * `activate()`: turns on the alarm;
  * `deactivate()`: turns off the alarm;
  * `motionDetected()`: the alarm detects environmental motion through its sensors;
  * `reset()`: used to stop the alarm sound when it is ringing;
  * `isActive(): bool`: predicate indicating if the alarm is turned on;
  * `isRinging(): bool`: predicate indicating if the alarm is ringing.

The test methods check that the alarm responds as expected depending on its current state and the received inputs.

## Implementation details

The alarm is implemented using the state pattern (see: https://refactoring.guru/design-patterns/state/python/example).

The following command can be used to run the tests:

```
python -m unittest -v test_alarm.py
```
