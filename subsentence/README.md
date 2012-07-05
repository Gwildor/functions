A function which works exactly like [PHP's substr()](http://php.net/manual/en/function.substr.php) function, including the points where it should return false instead of a string. It "splits" on spaces so it counts words instead of characters.

Note that there is one difference to PHP's implementation: you can't use null as length to get an empty string. In that case you need to use 0 as an argument.

### Examples:


__Input:__ subsentence('Lorem ipsum dolor sit amet, consectetur adipiscing elit.', 0, 3)

__Output:__ Lorem ipsum dolor


__Input:__ subsentence('a b c d e f', 3, 2)

__Output:__ d e


__Input:__ subsentence('a b c d e f', -1)

__Output:__ f


__Input:__ subsentence('a b c d e f', -2)

__Output:__ e f


__Input:__ subsentence('a b c d e f', -3, 1)

__Output:__ d


__Input:__ subsentence('a b c d e f', 0, -1)

__Output:__ a b c d e


__Input:__ subsentence('a b c d e f', 2, -1)

__Output:__ c d e


__Input:__ subsentence('a b c d e f', 4, -4)

__Output:__ _false_


__Input:__ subsentence('a b c d e f', -3, -1)

__Output:__ d e


__Input:__ subsentence('a b c d e f', 1)

__Output:__ b c d e f


__Input:__ subsentence('a b c d e f', 1, 3)

__Output:__ b c d


__Input:__ subsentence('a b c d e f', 0, 4)

__Output:__ a b c d


__Input:__ subsentence('a b c d e f', 0, 8)

__Output:__ a b c d e f


__Input:__ subsentence('a b c d e f', -1, 1)

__Output:__ f

