
def write_event_file(sorted_list_of_events):
    try:
        if not sorted_list_of_events:
            print("No events to write to the file.")  # Debugging output
            return
        else:
            with open("ISU_Events.txt", "w") as file:
                for item in sorted_list_of_events:
                    file.write(f"{item['event_name']}\n")
                    file.write(f"{item['event_date']}\n")
                    file.write(f"{item['event_location']}\n\n")
            print("Events successfully written to the file.")  # Debugging output
    except Exception as e:
        print(f"Error: {e}")

