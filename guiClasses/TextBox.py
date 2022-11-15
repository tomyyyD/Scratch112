class TextBox:
    def __init__(self, x, y, label) -> None:
        self.text = label
        self.x = x
        self.y = y
        self.fontSize = 20
        self.width = 0
        self.setTextLength()
        self.coords = [[self.x - self.width//2, self.y - 15],
                       [self.x + self.width//2, self.y + 15]]

    def draw(self, app, canvas, parentX, parentY):
        self.x = parentX
        self.y = parentY
        self.coords = [[self.x - self.width//2, self.y - 15],
                       [self.x + self.width//2, self.y + 15]]
        canvas.create_rectangle(self.coords[0][0], self.coords[0][1], self.coords[1]
                                [0], self.coords[1][1], fill="white", outline="black", width=2)
        canvas.create_text(self.x, self.y, text=self.text,
                           font=f"Times {self.fontSize}", fill="black")

    # if textbox clicked the input pops up
    def setText(self, app):
        self.text = app.getUserInput(self.text)
        self.setTextLength()

    def getText(self):
        return self.text

    def setTextLength(self):
        sum = 0
        for c in self.text:
            if c.lower() in ("m", 'w'):
                sum += 8.5
            if c.lower() in ('q', 'e', 'r', 'y', 'u', 'o', 'p', 'a', 's', 'd', 'g', 'h', 'k', 'z', 'x', 'c', 'v', 'b', 'n'):
                sum += 6
            if c.lower() in ('t', 'i', 'f', 'j', 'l'):
                sum += 4
        self.width = sum * (self.fontSize//10) + 5
