This started of as a small project for me to finally learn C++, but I coincidentally needed it for a PHP project so afterwards I translated it and added the string → integer functionality. Anyhow, because it is a translated project, the layout might look a bit weird for PHP.

### Usage:
string or int roman(string or int number);
- - -
### Examples:
#\#1: Decimal to Roman:
* __input__: roman(1992);
* __output__: MCMXCII

#\#2: Roman to decimal:
* __input__: roman('MCMXCII');
* __output__: 1992

#\#3: This function can also be "abused" (see notes below) to make invalid Roman numerals valid:
* __input__: roman(roman('IC')); // invalid
* __output__: XCIX // valid
- - -

### Notes:
* Because of the limited range the basic Roman numerals have, the integer input has to be between 1 and 3999.
* The string input is case-insensitive.
* As example #3 shows, this function cannot be used for full input validation. I simply did not put in full validation according to the rules because it's a lot of work for a function which soul purpose isn't validating but converting.
