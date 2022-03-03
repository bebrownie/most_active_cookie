import argparse
import csv
import sys
import datetime


class cookie_analyzer:
    def __init__(self):
        """
        keys are date of cookie occurance,values are dictionary of cookie and frequency
        which it appears in that day
        This is used to keep track of the amount of times a certain cookies that have been visited
        on a given day 
        """
        self.cookies_occurance = {}
        """
        keys are date of cookie occurance,values are dictionary of frequency it appears in
        a day, and the set of the cookies that appeared that many times in that day
        This is used to keep track of the set of cookies that are grouped using their count
         on a given date. 
        """
        self.cookie_total_count = {}

    """
    returns the set of cookies that appears the most frequent at the date given by the parameter
    date, return none if there isn't any cookie at that date
    :param date: the date of the cookie 
    :return:set of cookies that have the maximum occurancy at the desired date.
    """

    def max_target_cookies_set(self, date):
        self.validate_date(date)
        if date in self.cookie_total_count:
            max_occurance = max(self.cookie_total_count[date].keys())
            max_occurance_cookies = self.cookie_total_count[date][max_occurance]
            for cookies in max_occurance_cookies:
                print(cookies)
            return max_occurance_cookies
        else:
            return None

    """
        a seperate date processing function to parse the date of command line in case
        date format changed in the future
        :param date:date of the desired maximum cookie. 
        :return: string of the date
        """

    def target_date(self, date):
        return date.split("T")[0]

    """
    Open CSV file and reads it in rows.
    :param file_path: path of the csv cookie log file
    :return: void
    """

    def cookie_counter(self, file_path):
        with open(file_path, newline="") as content:
            reader = csv.DictReader(content)
            for lines in reader:
                self.cookie_processor(lines)

    """
    reads the rows of the csv file. 
    :param line: rows of the csv file
    :return: void
    """

    def cookie_processor(self, line):
        cookie, date = line["cookie"], line["timestamp"]
        date = self.target_date(date)
        # check if the date is present at cookies_occurance, and update it
        if date not in self.cookies_occurance:
            self.cookies_occurance[date] = {cookie: 1}
        else:
            if cookie not in self.cookies_occurance[date]:
                self.cookies_occurance[date][cookie] = 1
            else:
                self.cookies_occurance[date][cookie] += 1
        occurance = self.cookies_occurance[date][cookie]
        # check if the date is present at cookie_total_count, and update it
        if date not in self.cookie_total_count:
            self.cookie_total_count[date] = {occurance: set([cookie])}
        else:
            if occurance not in self.cookie_total_count[date]:
                self.cookie_total_count[date][occurance] = set([cookie])
            else:
                self.cookie_total_count[date][occurance].add(cookie)
                if occurance > 1:
                    self.cookie_total_count[date][occurance-1].remove(cookie)

    """
    Validate the format of the date. 
    :param date: Date of cookie log search
    :return: void
    """

    def validate_date(self, date):
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            raise ValueError(
                "Incorrect Date Time format, should be YYYY-MM-DD")


if __name__ == '__main__':
    # processing command line interface
    argument_parser = argparse.ArgumentParser(
        description="Find most active cookie from the cookie log",
        prog="most_active_cookie.py",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    argument_parser.add_argument("csv_path")
    argument_parser.add_argument("--date", "-d")
    argument = vars(argument_parser.parse_args(sys.argv[1:]))
    # initialize the cookie analyzer and pass path of cookie log and desired date.
    cookieanalyzer = cookie_analyzer()
    cookieanalyzer.cookie_counter(argument["csv_path"])
    cookieanalyzer.max_target_cookies_set(argument["date"])
