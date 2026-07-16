import datetime
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        date_obj = datetime.date(year, month, day)        
        return date_obj.strftime("%A")