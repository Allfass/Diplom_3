class TestHelper():
    @staticmethod
    def replacer(source_locator, replace_with):
        result = source_locator[1].replace("#097238", replace_with)
        del source_locator[1]
        source_locator[1] = result
        return source_locator