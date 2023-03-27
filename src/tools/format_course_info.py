import json
# import classes.Course as Course


# Opening JSON file
with open('courses.json') as f:
	# returns JSON object as a dictionary
	data = json.load(f)


# courses :Course.Section = []
courses = {}

for idx, d in enumerate(data["Sections"]):
	code = d["Course"]["SubjectCode"]
	number = d["Course"]["Number"]
	section = d["Number"]
	
	title = d["Title"]
	desc = d["Course"]["Description"]

	prof = d["FacultyDisplay"]
	if len(prof) > 0:
		prof = prof[0]
	else:
		prof = 'No Professor'

	seats = d["Available"]
	meeting_info = d["FormattedMeetingTimes"]
	meeting_days = ''
	start_time = ''
	end_time = ''
	room = ''
	building = ''

	if len(meeting_info) > 0:
		meeting_info = meeting_info[0]
		meeting_days = meeting_info["DaysOfWeekDisplay"]
		start_time = meeting_info["StartTimeDisplay"]
		end_time = meeting_info["EndTimeDisplay"]
		room = meeting_info["RoomDisplay"]
		building = meeting_info["BuildingDisplay"]

	if not start_time:
		start_time = "No Time"
	if not end_time:
		end_time = "No Time"
	
	if not room:
		room = "No Room"
	if not building:
		building = "No Building"

	if not meeting_days:
		meeting_days = 'No Days'

	if code not in courses:
		courses[code] = {}
	
	if number not in courses[code]:
		courses[code][number] = {}
		
	courses[code][number]["title"] = title
	courses[code][number]["description"] = desc

	if "Sections" not in courses[code][number]:
		courses[code][number]["Sections"] = {}
	

	# courses[code][number][section] = []
	courses[code][number]["Sections"][section] = {
		
		"Seats": seats,
		"MeetingDays": meeting_days,
		"StartTime": start_time,
		"EndTime": end_time,
		"Room": room,
		"Building": building,
		"Professor": prof,
		"Books": [],
		"Materials": []
	
	}

file = open("../data/courses.json",'w')
out = json.dumps(courses)
file.write(out)

'''
{
	CSC {
		1000 [
			{
				section: 01	
			},
			{
				section: 02
			}
		]
	}
}
'''
	

