seat_type = input("Enter seat type(sleeper/ac/general/luxury) :").lower()

match seat_type:
    case "sleeper":
        print("Sleeper - Sleeper berths. Fans and pillow")
    case "ac":
        print('AC - Air Conditioning. Bedsheets, pillow and blanket.')
    case "general":
        print("Genral - Cheapest and no reservation required.")
    case "luxury":
        print("Luxury - elite coat with table and premium food service.")
    case _:
        print("No such seat type exists.")