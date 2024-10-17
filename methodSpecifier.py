
import main

class pingInvoker:

    def __init__(self) -> None:
        networkFunction: main.webPockets = main.webPockets(200, 100)
        networkFunction.webster_message()

pingInject: pingInvoker = pingInvoker()