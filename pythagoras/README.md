### Usage:
pythagoras(side a, side b [, hypotenuse [, angle [, 3D ]]] );
- - -
### Parameters:
1. __side a__: float or null. If null is used, the 2nd and 3rd parameters are used and the length of this side is returned.
2. __side b__: float or null. See side a.
3. __hypotenuse__: Optional. Float or null. If left out or null is used and the 4th parameter is not specified, the 1st and 2nd parameters are used and the length of this side is returned. If a float is specified, while the 1st and 2nd parameters are also specified, the angle in degrees between side a and side b is returned.
4. __angle__: Optional. Float (angle in degrees) or null. If specified, the 1st and 2nd parameters are used and the length of the hypotenuse is returned.
5. __3D__: Optional. Boolean. If specified (as true), the parameters 1 through 3 are used and the length of the line between two opposite corners in a box is returned. See [this image](http://upload.wikimedia.org/wikipedia/commons/1/13/Pythagoras_3D.PNG) for a visual explanation. The 4th parameter is ignored.
- - -

### Examples:
#\#1: Calculate hypotenuse:
* __input__: pythagoras(3, 4);
* __output__: 5
* [__More info__](http://en.wikipedia.org/wiki/Pythagorean_theorem)

#\#2: Calculate cathetus/leg:
* __input__: pythagoras(55, null, 73);
* __output__: 48
* [__More info__](http://en.wikipedia.org/wiki/Pythagorean_theorem#Other_forms)

#\#3: Calculate angle:
* __input__: pythagoras(3, 4, 5);
* __output__: 90
* [__More info__](http://en.wikipedia.org/wiki/Law_of_cosines#Applications)

#\#4: Calculate hypotenuse based on angle between legs:
* __input__: pythagoras(3, 4, null, 90);
* __output__: 5
* [__More info__](http://en.wikipedia.org/wiki/Law_of_cosines#Applications)

#\#5: Calculate length of hypotenuse between opposite corners in box:
* __input__: pythagoras(3, sqrt(7), 3, null, true);
* __output__: 5
* [__More info__](http://en.wikipedia.org/wiki/Pythagorean_theorem#Solid_geometry)
