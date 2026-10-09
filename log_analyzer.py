info_count = 0
warning_count = 0
error_count = 0

error_messages = []

try:

    with open("server.log", "r") as file:

        for line in file:

            line = line.strip()

            if line.startswith("INFO"):
                info_count += 1

            elif line.startswith("WARNING"):
                warning_count += 1

            elif line.startswith("ERROR"):
                error_count += 1

                error_message = line.replace("ERROR ", "")
                error_messages.append(error_message)

    print("\n========== LOG ANALYZER ==========")

    print("INFO messages    :", info_count)
    print("WARNING messages :", warning_count)
    print("ERROR messages   :", error_count)

    print("\n========== ERROR MESSAGES ==========")

    for error in error_messages:
        print("-", error)

except FileNotFoundError:
    print("Log file not found.")