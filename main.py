from icalendar import Calendar


def delete_from_ical_by_keywords(file_path, keywords):
    with open(file_path, 'r+', encoding='utf-8') as ics_file:
        cal = Calendar.from_ical(ics_file.read())
        new_subcomponents = []
        for event in cal.subcomponents:
            ev_sum = event['SUMMARY'].lower()
            if not any(x.lower() in ev_sum for x in keywords):
                new_subcomponents.append(event)
        cal.subcomponents = new_subcomponents

    with open(file_path, 'wb') as file:
        file.write(cal.to_ical())


if __name__ == "__main__":
    file_path = r"C:\Users\Gleb\Downloads\test.ics"
    red_flags = ['Group A', 'Group C', 'studying together']
    delete_from_ical_by_keywords(file_path, red_flags)
