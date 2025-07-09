"""
Time tool for getting current time and date information.
"""

import datetime
from ..models import TimeInfo

class TimeTool:
    """Tool to get current time and date information."""
    
    def get_time_info(self) -> TimeInfo:
        """Get current time, date, and season information."""
        now = datetime.datetime.now()
        
        # Determine season
        month = now.month
        if month in [12, 1, 2]:
            season = "winter"
        elif month in [3, 4, 5]:
            season = "spring"
        elif month in [6, 7, 8]:
            season = "summer"
        else:
            season = "autumn"
        
        # Determine time of day
        hour = now.hour
        if 5 <= hour < 12:
            time_of_day = "morning"
        elif 12 <= hour < 17:
            time_of_day = "afternoon"
        elif 17 <= hour < 21:
            time_of_day = "evening"
        else:
            time_of_day = "night"
        
        return TimeInfo(
            time=now.strftime("%H:%M"),
            date=now.strftime("%B %d, %Y"),
            season=season,
            time_of_day=time_of_day,
            is_bedtime=19 <= hour <= 22
        ) 