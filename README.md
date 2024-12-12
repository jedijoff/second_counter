This script takes a time as an input, this is defined on line 75 when the variable timer is set, in the form "hh:mm:ss".
The class Timer has a __str__ method that returns a strinfg in the form of "hh:mm:ss" that will display the input time on printing an object created from this class.
The class also has 2 methods: next_second() and prev_second() these will first reset the self.secs, self.mins and self.hours to the original input values, and then add or subtract one second from the input time and return the new __str__() value that results.
