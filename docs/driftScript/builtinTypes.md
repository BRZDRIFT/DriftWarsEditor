## Vec2

```
class Vec2 {
    constructor(x=0.0, y=0.0)
    function _add(Vec2 other)               // returns Vec2
    function _sub(Vec2 other)               // returns Vec2
    function _mul((float|int|Vec2) other)   // returns Vec2
    function _div((float|int|Vec2) other)   // returns Vec2
    function _unm(Vec2 other)               // returns Vec2
    function _tostring()                    // returns string
    function Equals(other)                  // returns bool
    function Copy()                         // returns Vec2<int|float>
    function IsZero(other)                  // returns bool
    function Dot(Vec2 other)                // returns float or int
    function Length()                       // returns float
    function LengthSquared()                // returns float or int
    function Normalize()                    // returns Vec2<float>
    m_x = 0.0
    m_y = 0.0
}
```

- By default `Vec2` has scalar type of `float`.
- However you can change scalar type to be `int` by passing integers into the constructor
    - (or by setting `m_x`, `m_y` to integers manually)
- Warning: `==`/`!=` compares reference equality! Not value equality!
- Use `.Equals(other)` to compare `Vec2` values.
- Use `.Copy()` to create copies of `Vec2` values.
- Assignment operator `=` will only copy reference (not create a new `Vec2`)

## Vec3
```
class Vec3 {
    constructor(x=0.0, y=0.0, z=0.0)
    function _add(Vec3 other)               // returns Vec3
    function _sub(Vec3 other)               // returns Vec3
    function _mul((float|int|Vec3) other)   // returns Vec3
    function _div((float|int|Vec3) other)   // returns Vec3
    function _unm(Vec3 other)               // returns Vec3
    function _tostring()                    // returns string
    function Equals(other)                  // returns bool
    function Copy()                         // returns Vec3<int|float>
    function IsZero(other)                  // returns bool
    function Dot(Vec3 other)                // returns float or int
    function Length()                       // returns float
    function LengthSquared()                // returns float or int
    function Normalize()                    // returns Vec3<float>
    function xy()                           // returns Vec2(m_x, m_y)
    m_x = 0.0
    m_y = 0.0
    m_z = 0.0
}

```

- By default `Vec3` has scalar type of `float`.
- However you can change scalar type to be `int` by passing integers into the constructor
    - (or by setting `m_x`, `m_y`, `m_z` to integers manually)
- Warning: `==`/`!=` compares reference equality! Not value equality!
- Use `.Equals(other)` to compare `Vec3` values.
- Use `.Copy()` to create copies of `Vec3` values.
- Assignment operator `=` will only copy reference (not create a new `Vec3`)

## Vec4
```
class Vec4 {
    constructor(x=0.0, y=0.0, z=0.0, w=0.0)
    function _add(Vec4 other)               // returns Vec4
    function _sub(Vec4 other)               // returns Vec4
    function _mul((float|int|Vec4) other)   // returns Vec4
    function _div((float|int|Vec4) other)   // returns Vec4
    function _unm(Vec4 other)               // returns Vec4
    function _tostring()                    // returns string
    function Equals(other)                  // returns bool
    function Copy()                         // returns Vec4<int|float>
    function IsZero(other)                  // returns bool
    function Dot(Vec4 other)                // returns float or int
    function Length()                       // returns float
    function LengthSquared()                // returns float or int
    function Normalize()                    // returns Vec4<float>
    function xy()                           // returns Vec2(m_x, m_y)
    function xyz()                          // returns Vec3(m_x, m_y, m_z)
    m_x = 0.0
    m_y = 0.0
    m_z = 0.0
    m_w = 0.0
}

```

- By default `Vec4` has scalar type of `float`.
- However you can change scalar type to be `int` by passing integers into the constructor
    - (or by setting `m_x`, `m_y`, `m_z`, `m_w` to integers manually)
- Warning: `==`/`!=` compares reference equality! Not value equality!
- Use `.Equals(other)` to compare `Vec4` values.
- Use `.Copy()` to create copies of `Vec4` values.
- Assignment operator `=` will only copy reference (not create a new `Vec4`)

## AABR
Axis aligned bounding rectangle

```
class AABR {
    constructor(minPt = Vec2(), maxPt = Vec2())
    function _tostring()            // returns string
    function Equals(other)          // returns bool
    function Copy()                 // returns AABR<int|float>
    function GetSize()              // returns Vec2<int|float>
    function GetTopLeft()           // returns Vec2<int|float>
    function GetTopRight()          // returns Vec2<int|float>
    function GetBottomLeft()        // returns Vec2<int|float>
    function GetBottomRight()       // returns Vec2<int|float>
    function GetCenter()            // returns Vec2<float>
    m_minPt = Vec2()
    m_maxPt = Vec2() 
}

```

- By default `AABR` has scalar type of `float`.
- However you can change scalar type to be `int` by passing `Vec2<int>`'s into the constructor
    - (or by setting `m_minPt` and `m_maxPt` to `Vec2<int>` manually)
- Warning: `==`/`!=` compares reference equality! Not value equality!
- Use `.Equals(other)` to compare `AABR` values.
- Use `.Copy()` to create copies of `AABR` values.
- Assignment operator `=` will only copy reference (not create a new `AABR`)

## Future additions
- More types and member functions to be added later
