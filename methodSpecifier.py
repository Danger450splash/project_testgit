
import main

class pingInvoker:

    def __init__(self) -> None:
        networkFunction: main.webPockets = main.webPockets(200, 100)
        networkFunction.webster_message()
        print("")
        print(f"Delta Team has joined the server.")
        print(f'Alpha Team has joined the server.')

pingInject: pingInvoker = pingInvoker()