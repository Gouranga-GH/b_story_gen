"""
Time tool for getting current time and date information.
"""

import datetime
from ..models import TimeInfo

class TimeTool:
    """
    Tool to get current time and date information for story context.
    Determines the current season, time of day, and whether it's bedtime.
    """
    
    def get_time_info(self) -> TimeInfo:
        """
        Get current time, date, season, time of day, and bedtime status.
        Returns:
            TimeInfo: Dataclass with all time-related context for the story.
        """
        now = datetime.datetime.now()  # Get the current date and time
        
        # Determine the current season based on the month
        month = now.month
        if month in [12, 1, 2]:
            season = "winter"
        elif month in [3, 4, 5]:
            season = "spring"
        elif month in [6, 7, 8]:
            season = "summer"
        else:
            season = "autumn"
        
        # Determine the time of day based on the hour
        hour = now.hour
        if 5 <= hour < 12:
            time_of_day = "morning"
        elif 12 <= hour < 17:
            time_of_day = "afternoon"
        elif 17 <= hour < 21:
            time_of_day = "evening"
        else:
            time_of_day = "night"
        
        # Determine if it's bedtime (between 7pm and 10pm)
        return TimeInfo(
            time=now.strftime("%H:%M"),                # e.g., '21:15'
            date=now.strftime("%B %d, %Y"),            # e.g., 'April 27, 2024'
            season=season,                              # e.g., 'spring'
            time_of_day=time_of_day,                    # e.g., 'evening'
            is_bedtime=19 <= hour <= 22                 # True if between 7pm and 10pm
        ) 