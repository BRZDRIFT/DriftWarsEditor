# Math Library

## Constants
- `RAND_MAX` - Constant 64-bit int value of 0x00000000FFFFFFFF
    - (do not rely on the constant value staying the same)
- `PI` - Constant float value for PI (3.14159...)

## Functions
- `float sqrt(x)` - returns square root of x
- `float sin(x)` - return sin of x
- `float asin(x)` - arcsin of x
- `float cos(x)` - return cos of x
- `float acos(x)` - arccos of x
- `float tan(x)` - return tan of x
- `float atan(x)` - arctan of x
- `float atan2(y, x)` - arctan2 of x
- `int rand()` - return random integer from [0, RAND_MAX]
- `mixed abs(x)` - return absolute value of x.
- `mixed min(x, y)` - returns the minimum of x and y.
- `mixed max(x, y)` - returns the maximum of x and y.
- `mixed clamp(val, min, max)` - clamps val to be between min and max
- `float lerp(x, y, a)` - linearly interpolate x -> y based on a [0, 1]
- `float floor(x)`
- `float ceil(x)`
- `float fmod(x, y)` - floating point modulo

## Note
- Many of these functions are optimized for speed and not accuracy
