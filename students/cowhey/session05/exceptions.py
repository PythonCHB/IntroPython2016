def safe_return():
    try:
        answer = input("What Is the Airspeed Velocity of an Unladen Swallow?: ")
        return answer
    except (EOFError, KeyboardInterrupt):
        return None

print(safe_return())
