import pygame
from pygame.locals import Color

class App:
    def __init__(self, title: str):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption(title)

        self.font = pygame.font.Font(None, 38)

        self.running = True

        self.texts = [
            Text(self, 'Number of elements: ', (295, 50))
        ]

        self.generate_button = Button(self, 'Generate', (740, 50), on_click=self.generate_numbers, padding=(20, 10))
        self.sort_button = Button(self, 'Sort', (560, 125), on_click=self.sort_numbers, padding=(250, 15))
        # must generate numbers first before sorting
        self.sort_button.clickable = False
        self.reset_button = Button(self, 'Reset', (1090, 150), on_click=self.reset, padding=(20, 10))

        self.buttons = [
            self.generate_button,
            self.sort_button,
            self.reset_button
        ]

        self.elements_input = InputField(self, 135, 45, (570, 40))
        self.input_fields = [
            self.elements_input
        ]
    
    def generate_numbers(self):
        #TODO: ADD LOGIC
        self.sort_button.clickable = True
    
    def reset(self) -> None:
        #TODO: ADD LOGIC
        self.elements_input.text = "50"
        self.sort_button.clickable = False

    def sort_numbers(self):
        #TODO: ADD LOGIC
        pass

    def run(self) -> None:
        # flag to check if any input is in focus
        any_input_active = False
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_on_input = False
                    for input_field in self.input_fields:
                        if input_field.field.collidepoint(event.pos):
                            input_field.active = True
                            clicked_on_input = True
                            any_input_active = True
                    if not clicked_on_input:
                        any_input_active = False
                # typing
                elif event.type == pygame.KEYDOWN:
                    for input_field in self.input_fields:
                        if input_field.active:
                            if event.key == pygame.K_BACKSPACE:
                                input_field.backspace()
                            elif event.unicode.isdigit():
                                input_field.add(event.unicode)
                elif not any_input_active:
                    for input_field in self.input_fields:
                        input_field.active = False

            self.screen.fill(Color('White'))
            for button in self.buttons:
                button.process()
                button.draw()
            for text in self.texts:
                text.draw()
            for input_field in self.input_fields:
                input_field.draw()
            # static graph border
            pygame.draw.rect(self.screen, Color('Black'),
                             (20, 200, 1160, 580),
                             1)
            pygame.display.flip()
        pygame.quit()
class Text:
    def __init__(self, app: App, text: str, pos: tuple[int, int], **options):
        self.app = app
        self.background = None
        self.x = pos[0]
        self.y = pos[1]
        self.padding_x, self.padding_y = options.get('padding', (0, 0))
        self.change_text(text)
    
    def draw(self):
        self.app.screen.blit(self.img, self.rect)
    
    def change_text(self, text: str) -> None:
        self.text = text
        self.img = self.app.font.render(self.text, True, Color('Black'))
        self.rect = self.img.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.surface = pygame.Surface(
            (self.img.get_width() + self.padding_x * 2, self.img.get_height() + self.padding_y * 2)
        )
        self.padding_rect = pygame.Rect(
            self.x,
            self.y,
            self.img.get_width() + self.padding_x * 2, 
            self.img.get_height() + self.padding_y * 2
        )
        self.padding_rect.topleft = (self.x - self.padding_x, self.y - self.padding_y)

class Button(Text):
    def __init__(self, app: App, text: str, pos: tuple[int, int], **options):
        super().__init__(app, text, pos, **options)
        self.clickable = True
        self.clicked = False
        self.on_click = options.get('on_click', lambda: -1)
        self.states = {
            'normal': "#66ff66",
            'hover': "#99ff99",
            'pressed': "#99ff99",
            'unclickable': "#ff0000"
        }
        self.change_text(text)
        

    def process(self):
        if not self.clickable:
            self.surface.fill(self.states['unclickable'])
        else:
            self.surface.fill(self.states['normal'])
            mouse_pos = pygame.mouse.get_pos()
            if self.padding_rect.collidepoint(mouse_pos):
                self.surface.fill(self.states['hover'])
                # left click, prevent double clicking
                if pygame.mouse.get_pressed(num_buttons=3)[0]:
                    self.surface.fill(self.states['pressed'])
                    if not self.pressed and self.clickable:
                        self.on_click()
                        self.pressed = True
                else:
                    self.pressed = False
    def draw(self):
        self.app.screen.blit(self.surface, (self.x - self.padding_x, self.y - self.padding_y))
        self.app.screen.blit(self.img, self.rect)

class InputField:
    def __init__(self, app: App, width: int, height: int, pos: tuple[int, int]):
        self.app = app
        self.width = width
        self.height = height
        self.x, self.y = pos
        self.field = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = "50"
        self.active = False

    def add(self, text: str) -> None:
        if len(self.text) > 7:
            return
        if self.text == "0":
            self.text = text
        else:
            self.text += text
    
    def backspace(self) -> None:
        if not self.text:
            return
        if len(self.text) == 1:
            self.text = "0"
        else:
            # remove last character
            self.text = self.text[:-1]

    def text(self) -> str:
        return self.text

    def draw(self) -> None:
        pygame.draw.rect(self.app.screen, Color('Gray'), self.field, 2)
        text_surface = self.app.font.render(self.text, True, Color('Black'))
        self.app.screen.blit(text_surface, (self.x + 7, self.y + self.height // 2 - 10))
        
        if self.active:
            pygame.draw.rect(self.app.screen, Color('Red'), self.field, 3)


app = App("Sorting Algorithms Analyzer")
app.run()