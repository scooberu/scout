# scout
A simple interview scheduler

## Raison d'Etre

I've had to schedule a TON of interviews latesly, and the process is awful. People email me asking for four times when I'm free, then they get back to me and tell me none of those work, but maybe next week, unless--UNLESS--I could do a 7am meeting. Eugh. This is why we have computers.

- This application makes it easier for me (by automating schedule requests, integrating with my Google calendars, and accommodating my preferences.
- This also helps the person asking to schedule by cutting down on email chatter and allowing them to 

## Workflow

1. If you're trying to book time on my calendar, you need to tell me the following:
- What name should the appointment look like on my calendar?
- How much of my time do you need? (How long will the appointment be?)
- Any start times in particular you'd like me to consider?
- This week? Next week? The week after? (Tick each week you'd like options for)
2. Run an API query back to my aggregated GCal to see what times are available
3. With the request we got from the user, compute some available times (say, three preferred times for each week the user requested).
4. Return the list of times to the user as text, ask if any of them work.
- If none of them works for the user, get three NEW dates for each week.
- If one of them works, generate an .ics file for the user and offer to download it.
5. If the user selected a time/date, add an appointment to my calendar.

## Concerns

1. Security: this is going to be public. Might need to put in a captcha to ensure my calendar doesn't get spammed.
