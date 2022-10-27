import pandas as pd
import json
import utils as uts
import random
import datetime

def store_general_garmin(data,conn):
    cur = conn.cursor()
    cur.execute('DELETE FROM garmin_step_data WHERE garmin_id = %s;',(data["garmin_id"],))
    cur.execute("INSERT INTO garmin_step_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",
    (data["garmin_id"],data["summary_id"],data["activity_id"],["startTimeInSeconds"],
    data["startTimeOffsetInSeconds"],data["activityType"],["durationInSeconds"],data["steps"],data["manual"],data["group_user_id"]))


def store_health_summary(data,conn):
    cur = conn.cursor()
    for item in data:
        cur.execute('INSERT INTO garmin_health_summary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
        (item['summaryId'],item["calendarDate"],item["startTimeInSeconds"],item["startTimeOffsetInSeconds"],item["activityType"],item['durationInSeconds'],
        item['steps'],item['distanceInMeters'],item['activeTimeInSeconds'],item['activeKilocalories'],item['bmrKilocalories'],
        item['moderateIntensityDurationInSeconds'],item['vigorousIntensityDurationInSeconds'],item['floorsClimbed'],item['minHeartRateInBeatsPerMinute'],
        item['averageHeartRateInBeatsPerMinute'],item['maxHeartRateInBeatsPerMinute'],item['restingHeartRateInBeatsPerMinute'],item['averageStressLevel'],
        item['maxStressLevel'],item['stressDurationInSeconds'],item['restStressDurationInSeconds'],item['activityStressDurationInSeconds'],
        item['lowStressDurationInSeconds'],item['mediumStressDurationInSeconds'],item['highStressDurationInSeconds'],item['stressQualifier'],
        item['stepsGoal'],item['intensityDurationGoalInSeconds'],item['floorsClimbedGoal']))

def store_activity_summary(data,conn):
    cur = conn.cursor()
    for item in data:
        cur.execute('INSERT INTO garmin_activity_summary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);',
        (item['summaryId'],item['activityId'],item['startTimeInSeconds'],
        item['startTimeOffsetInSeconds'],item['activityType'],item['durationInSeconds'],
        item['activeKilocalories'],item['deviceName'],item['distanceInMeters'],
        ))

def store_sleep_summary(data,conn):
    cur = conn.cursor()
    for item in data:
        new_sleep_summary = {}
        new_sleep_summary['summaryId'] = item[0]['summaryId']
        new_sleep_summary['calendarDate'] = item[0]['calendarDate']
        new_sleep_summary['startTimeInSeconds'] = item[0]['startTimeInSeconds']
        new_sleep_summary['startTimeOffsetInSeconds'] = item[0]['startTimeOffsetInSeconds']
        new_sleep_summary['sleepLevelsMap'] = {"deep":[],"light":[],"rem":[],'awake':[]}
        unmeasurableSleepDuration, deepSleepDuration, lightSleepDuration = 0,0,0
        remSleep, awakeDuration, duration = 0,0,0
        for subData in item:
            unmeasurableSleepDuration += subData['unmeasurableSleepDurationInSeconds']
            deepSleepDuration += subData['deepSleepDurationInSeconds']
            lightSleepDuration += subData['lightSleepDurationInSeconds']
            remSleep += subData['remSleepInSeconds']
            awakeDuration += subData['awakeDurationInSeconds']
            duration += subData['durationInSeconds']
            if 'deep' in subData['sleepLevelsMap']:
                for deepData in subData['sleepLevelsMap']['deep']:
                    new_sleep_summary['sleepLevelsMap']['deep'].append(deepData)
            if 'light' in subData['sleepLevelsMap']:
                for lightData in subData['sleepLevelsMap']['light']:
                    new_sleep_summary['sleepLevelsMap']['light'].append(lightData)
            if 'rem' in subData['sleepLevelsMap']:
                for remData in subData['sleepLevelsMap']['rem']:
                    new_sleep_summary['sleepLevelsMap']['rem'].append(remData)
            if 'awake' in subData['sleepLevelsMap']:
                for awakeData in subData['sleepLevelsMap']['awake']:
                    new_sleep_summary['sleepLevelsMap']['awake'].append(awakeData)
        cur.execute('INSERT INTO garmin_sleep_summary VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
        (new_sleep_summary['summaryId'],new_sleep_summary["calendarDate"],new_sleep_summary['startTimeInSeconds'],
        new_sleep_summary['startTimeOffsetInSeconds'],duration, unmeasurableSleepDuration,deepSleepDuration,
        lightSleepDuration,remSleep,awakeDuration,json.dumps(new_sleep_summary['sleepLevelsMap'])))



def store_hrv_summary(data,conn):
    cur = conn.cursor()
    for item in data:
        cur.execute("INSERT INTO garmin_hrv_summary VALUES (%s,%s,%s,%s,%s,%s,%s,%s);",
        (item['summaryId'],item['calendarDate'],item['startTimeInSeconds'],item['durationInSeconds'],
        item['startTimeOffsetInSeconds'],item['lastNightAvg'],item['lastNight5MinHigh'],json.dumps(item['hrvValues'])))
