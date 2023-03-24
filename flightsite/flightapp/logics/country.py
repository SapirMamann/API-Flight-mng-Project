from ..dal.country import CountryDal


class CountryLogic():
    dal = CountryDal()

    def get_all(self):
        """
        Get all countries.
        """
        return self.dal.get_all() 