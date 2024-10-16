
class webPockets:

    def __init__(self, pocket1: int, pocket2: int) -> None:
        self.pock1: int = pocket1
        self.pock2: int = pocket2
        self.fixPing: int = 500
        self.fullpockets: int = self.pock1 - self.pock2 + self.fixPing
        print(f'{self.fullpockets}')

    def webster_message(self) -> None:
        print(f'Testing Web Pockets OverwrittenZ')