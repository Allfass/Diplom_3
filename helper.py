class TestHelper():
    @staticmethod
    def replacer(source_locator, replace_with):
        result = source_locator[1].replace("98557", replace_with)
        del source_locator[1]
        source_locator.append(result)
        return source_locator