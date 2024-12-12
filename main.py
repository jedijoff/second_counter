# This is a sample Python script.
from html.parser import interesting_normal
from time import monotonic_ns


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


class Timer:
    def __init__(self, hours = 0, mins = 0, secs = 0):
        self.hours = hours
        self.mins = mins
        self.secs = secs
        self.int_hours = hours
        self.int_mins = mins
        self.int_secs = secs

    def __str__(self):
        if self.hours < 10:
            self.__str__ = ("0" + str(self.hours))

        elif self.hours > 23:
            self.__str__ = "00"
        else:
            self.__str__ = str(self.hours)

        if self.mins < 10:
            self.__str__ += (":0" + str(self.mins))
        elif self.mins > 59:
            self.__str__ += ":00"
        else:
            self.__str__ += (":" + str(self.mins))

        if self.secs < 10:
            self.__str__ += (':0' + str(self.secs))
        elif self.secs > 59:
            self.__str__ += ':00'
        else:
            self.__str__ += ":" + str(self.secs)

        return (self.__str__)

    def next_second(self):
        self.secs = self.int_secs
        self.mins = self.int_mins
        self.secs = self.int_secs
        self.secs += 1
        if self.secs == 60:
            self.secs = 0
            self.mins += 1
            if self.mins == 60:
                self.mins = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0
        return self.__str__

    def prev_second(self):
        self.secs = self.int_secs
        self.mins = self.int_mins
        self.hours = self.int_hours
        self.secs -= 1
        if self.secs == -1:
            self.secs = 0
            self.mins -= 1
            if self.mins == -1:
                self.mins = 0
                self.hours -= 1
                if self.hours == -1:
                    self.hours = 0
        return self.__str__


timer = Timer(23,59,59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
