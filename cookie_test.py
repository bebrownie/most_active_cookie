from most_active_cookie import cookie_analyzer
import unittest


class CookieTestMethod(unittest.TestCase):
    """
    unit test to check for tests where single cookies appears the most. 
    """

    def test_single_cookie(self):
        cookieanalyzer = cookie_analyzer()
        cookieanalyzer.cookie_counter("simple_test.csv")
        answer = list(cookieanalyzer.max_target_cookies_set("2018-12-09"))
        self.assertEqual(answer[0], "AtY0laUfhglK3lC7")
        answer = list(cookieanalyzer.max_target_cookies_set("2018-12-07"))
        self.assertEqual(answer[0], "4sMM2LxV07bPJzwf")
    """
     unit test to check for tests where a set of cookies appears the most. 
    """

    def test_multiple_cookies(self):
        cookieanalyzer = cookie_analyzer()
        cookieanalyzer.cookie_counter("simple_test.csv")
        answer = cookieanalyzer.max_target_cookies_set("2018-12-08")
        self.assertEqual({"SAZuXPGUrfbcn5UA", "fbcn5UAVanZf6UtG",
                          "4sMM2LxV07bPJzwf"}, answer)
    """
    unit test to check for funtionality of date format checker.
    """

    def test_date_format(self):
        cookieanalyzer = cookie_analyzer()
        cookieanalyzer.cookie_counter("simple_test.csv")
        input = "2019-01-51"
        self.assertRaises(ValueError, cookieanalyzer.validate_date, input)
    """
    unit test to check for wether the date give has any date at all. 
    """

    def test_is_date_empty(self):
        cookieanalyzer = cookie_analyzer()
        cookieanalyzer.cookie_counter("simple_test.csv")
        answer = cookieanalyzer.max_target_cookies_set("2018-12-05")

        self.assertEqual(None, answer)


if __name__ == "__main__":
    unittest.main()
