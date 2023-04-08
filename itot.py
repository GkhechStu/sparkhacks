from __future__ import print_function

from datetime import date
from datetime import datetime
from datetime import timedelta
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


className = "Programming Language Design"
startTimeH = 12
startTimeM = 0
endTimeH = 14
endTimeM = 50
isoformDay = "2023-04-09 10:00:00"
location = "temporary location"

def get_date_from_weekday(weekday, start):
    # 0 is monday
    today = date.today()
    print("TODAYS DATE")
    print(today)
    print("ITS OUT")
    days_ahead = weekday - today.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    if start > 0:
        target_date = today + timedelta(hours=startTimeH, minutes = startTimeM)
    else:
        target_date = today + timedelta(hours=endTimeH, minutes = endTimeM)
    return target_date.isoformat()


def main():
    """Shows basic usage of the Google Calendar API."""

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        FA23start = "20230822T170000Z"
        FA23end = "20231213T170000Z"

        recurrenceRule = "RRULE:FREQ=WEEKLY;UNTIL="
        recurrencceForm = recurrenceRule + FA23end

        #d = get_date_from_weekday(0)
        #tomorrow = datetime(d.year, d.month, d.day, 10)+timedelta(hours = startTimeH, minutes = startTimeM)
        #print(tomorrow)
        #print(get_date_from_weekday(0))
        start = get_date_from_weekday(0, 0)
        end = get_date_from_weekday(0, 1)
        print(start)
        print(end)
        event_result = service.events().insert(calendarId='primary',
            body={
                "summary": className,
                "description": location,
                "start": {"dateTime": start, "timeZone": "America/Chicago"},
                "recurrence":[recurrencceForm],

                "end": {"dateTime": end, "timeZone": "America/Chicago"},
        }).execute()

        print("created event")
        print("id: ", event_result['id'])
        print("summary: ", event_result['summary'])
        print("starts at: ", event_result['start']['dateTime'])
        print("ends at: ", event_result['end']['dateTime'])

        # Call the Calendar API
        # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # print('Getting the upcoming 10 events')
        # events_result = service.events().list(calendarId='primary', timeMin=now,
        #                                      maxResults=10, singleEvents=True,
        #                                      orderBy='startTime').execute()
        # events = events_result.get('items', [])
        #
        # if not events:
        #    print('No upcoming events found.')
        #    return


        # Prints the start and name of the next 10 events
        # for event in events:
        #    start = event['start'].get('dateTime', event['start'].get('date'))
        #    print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()