## Use `local` for defining variables
- Variables must be defined using `local`
```
local myVariable = 7    // good!

myVariable2 = 8         // script-error! Forgot local keyword.
```

## Must use `<-` operator to add new key/value to dictionary
```
// need to use <- to add new key/value to dictionary
local myDictionary = {}
myDictionary["abc"] <- 7        // works
myDictionary["def"] = 9         // script error! key "def" does not exist!

// however, you can use = to modify existing value
myDictionary["abc"] = 10        // works, since key "abc" already exists
myDictionary["abc"] <- 12       // also works

// note: can also create dictionaries in-place
local myNewDictionary = { abc = 6, def = 9}   // no quotes for in-place string keys
myNewDictionary[15] <- "some string"        // keys can also be integers
```

## `==` checks for reference equality, not value equality!
- `==` and `!=` does not work as expected for Vec2, Vec3, Vec4, AABR and non-primitive types!   
- `==` for non-primitive types check if references point to same object, which is usually not what you want
- Instead use their defined `.Equals(other)` functions!  
- `==` equality operator for primitive types `int`, `float`, `bool`, `string` compare by value (not reference)

```
// == checks if reference points to same object, not value equality
local a = Vec2(6.0, 7.0)
local b = Vec2(1.0, 5.0)
local c = Vec2(1.0, 5.0)
local d = c
local isEqual0 = a.Equals(b)    // false
local isEqual1 = b.Equals(c)    // true
local isEqual2 = (b == c)       // THIS IS FALSE!!!
                                // ^ References point to different objects.
local isEqual3 = (c == d)       // true. References are the same.

// However,
// == works as expected for int, float, bool, string types
local q = 3
local w = 3
local isEqual4 = (q == w)       // true 
```

## `=` assignment operator copies reference, not value! (for custom types)
```
local a = Vec2(2.0, 6.0)
local b = a			// reference copy
local c = a.Copy()	// value copy
local d = clone a	// same as .Copy()
print(a == b)		// true, a and b reference same object
print(a == c)		// false, a and c reference different objects
print(a.Equals(c))	// true
print(a.Equals(d))	// true
```
- this behavior is only for non-primitive types (not `int`, `float`, `bool`, `string`)
- `=` assignment operator primitive types `int`, `float`, `bool`, `string` copy by value (not by reference)
- To make a copy of an object, use squirrel's builtin `clone` operator, or use `.Copy()` function if available.
- If you make your own types, it's a good idea to create your own `.Copy()` and `.Equal(other)` functions.

## Casting, ints, floats, strings, etc...
```
local a = 5     // a is type 'integer' of value 5
print(a)        // prints '5'
print(a / 2)    // prints '2',  	# integer division is truncated 

local b = 5.0   // a is type 'float' of value 5.0
print(b)        // prints '5.00', 	# floats always outputs to 2 decimals
print(b / 2)    // prints '2.50',  	# float division acts as normal

// You can cast an integer to float or float to integer
// using the .tointeger() and .tofloat() functions

local c = b.tointeger()     // 'c' is now an integer with value 5
local d = a.tofloat()       // 'd' is now a float with value 5.0
local e = a.tointeger()     // .tointeger() acts a dummy functions
							// for casting from 'int' -> 'int'
local f = b.tofloat()       // .tofloat() acts a dummy functions
							// for casting from 'float' -> 'float'

local myString1 = e.tostring()
print(myString1)                    // prints '5'

local myString2 = f.tostring()
print(myString2)                    // prints '5.00'

// number to string conversions happen automatically
print("abc " + a)           		// prints "abc 5"             

// Warning!
// You are not allowed to cast using '(int) expr' and '(float) expr'
// syntax. You must use .tostring(), .tofloat(), .tointeger(), etc..
// local z = (int) f       // ERROR! Cannot do this type of casting

// You can also print Vec2, Vec3, Vec4, AABR types, see below:

// Prints: "My Int Vector = (4, 5)"
print("My Int Vector = " + Vec2(4, 5))

// Prints: "My Float Vector = (4.00, 5.00)"
print("My Float Vector = " + Vec2(4, 5).ToFloat2())

// Prints: "My Float Vector = (4.00, 5.00)"
print("My Float Vector = " + Vec2(4.0, 5.0))
```

## Comments
- You can write single-line comments by using `//` or `#`
- You can write multi-line comments by using `/* multi-lines */`
```
// this is a single line comment

# this is also a comment :)

/*
this is multiple lines
of comments. this text
will be ignored by the compiler.
*/
```

## Common dictionary and array tasks
```
// deleting from dictionary
local myDictionary = { "abc": 6, "def": 7 }     // create dictionary
delete myDictionary["abc"]                  // delete "abc" from dictionary

// arrays
local myArray = ["my_string", 6, 1, 2]      // create dictionary
print(myArray[0])                   // prints "my_string"
myArray.append(7)                   // myArray:  ["my_string", 6, 1, 2, 7]
print(myArray[4])                   // prints 7
myArray.remove(1)           // remove at index 1, myArray: ["my_string", 1, 2, 7]
```
- See [http://squirrel-lang.org/squirreldoc/reference/language.html](http://squirrel-lang.org/squirreldoc/reference/language.html) for more language features.

## Dictionary and array foreach loops
```
// dictionary initializer syntax #1: { key = val }
// Possible Output (dictionary iteration order is unspecified):
// a -> 5
// c -> dog
// b -> 2
local myDict1 = { a = 5, b = 2, c = "dog"}
foreach (key, val in myDict1) {
	print(key + " -> " + val)
}

// dictionary initializer syntax #2: { "key": val }
// Possible Output (dictionary iteration order is unspecified):
// a -> 5
// c -> dog
// b -> 2
local myDict2 = { "a": 5, "b": 2, "c": "dog"}
foreach (key, val in myDict2) {
	print(key + " : " + val)
}

// dictionary single variable iteration..
// NOTE: this syntax outputs value, not key as in languages like python
// Possible Output (dictionary iteration order is unspecified):
// 5
// dog
// 2
local myDict3 = { "a": 5, "b": 2, "c": "dog"}
foreach (val in myDict3) {
	print(val)
}

// array initializer syntax: [val0, val1, etc]
// Output (array foreach iteration is ordered):
// 4
// 6
// dog
// 3
local myArray = [4, 6, "dog", 3]
foreach (val in myArray) {
	print(val)
}
```
- Please note, single variable foreach loop with dictionary outputs `value` and not `key`.
    - This is different from other languages like `Python`.
- dictionary foreach iteration order is `unspecified` (which is different than random)

## Other
- semicolons `;` at the end of lines are optional, similar to `Python`