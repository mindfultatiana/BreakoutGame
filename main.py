from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.properties import (ListProperty, NumericProperty, 
                           ObjectProperty, StringProperty)
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform as kivy_platform
from kivy.graphics import Color, Rectangle, Ellipse
import random

__version__ = '0.1'  # Used later during Android compilation

class Player(Widget):
    position = NumericProperty(0.5)
    
    def __init__(self, **kwargs):
        super(Player, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)  # White color
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics, size=self.update_graphics)
        self.touch_active = False
        self.target_position = 0.5
    
    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
    
    def on_touch_down(self, touch):
        if self.parent and touch.y < self.parent.height * 0.5:
            self.touch_active = True
            # Convert touch x to relative position (0.0 to 1.0)
            relative_x = touch.x / self.parent.width
            # Center the paddle on the touch point
            paddle_width = 0.1  # size_hint x value
            self.target_position = relative_x - (paddle_width / 2)
            return True
        return False
    
    def on_touch_move(self, touch):
        if self.touch_active and self.parent:
            # Convert touch x to relative position (0.0 to 1.0)
            relative_x = touch.x / self.parent.width
            # Center the paddle on the touch point
            paddle_width = 0.1  # size_hint x value
            self.target_position = relative_x - (paddle_width / 2)
            return True
        return False
    
    def on_touch_up(self, touch):
        self.touch_active = False
        return True
    
    def update(self, dt):
        if self.touch_active:
            # Move towards target position smoothly
            diff = self.target_position - self.position
            # Adjust speed - higher value = faster response
            move_speed = 8.0
            self.position += diff * move_speed * dt
        
        # Calculate proper bounds accounting for paddle width
        paddle_width = 0.1  # This matches the size_hint x value
        min_pos = 0.0  # Left edge of screen
        max_pos = 1.0 - paddle_width  # Right edge minus paddle width
        
        # Keep player within proper bounds
        self.position = max(min_pos, min(max_pos, self.position))
        
        # Also clamp target position to prevent issues
        self.target_position = max(min_pos, min(max_pos, self.target_position))

class Ball(Widget):
    pos_hint_x = NumericProperty(0.5)
    pos_hint_y = NumericProperty(0.3)
    velocity = ListProperty([0.1, 0.5])
    
    def __init__(self, **kwargs):
        super(Ball, self).__init__(**kwargs)
        with self.canvas:
            Color(1, 1, 1, 1)  # White color
            self.ellipse = Ellipse(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics, size=self.update_graphics)
    
    def update_graphics(self, *args):
        self.ellipse.pos = self.pos
        self.ellipse.size = self.size
    
    def update(self, dt):
        self.pos_hint_x += self.velocity[0] * dt
        self.pos_hint_y += self.velocity[1] * dt
        
        # Bounce from right wall
        if self.right > self.parent.right:
            self.velocity[0] = -1 * abs(self.velocity[0])
        # Bounce from left wall
        if self.x < self.parent.x:
            self.velocity[0] = abs(self.velocity[0])
        # Bounce from top wall
        if self.top > self.parent.top:
            self.velocity[1] = -1 * abs(self.velocity[1])
        # Lose at bottom
        if self.y < self.parent.y:
            self.parent.lose()
        
        self.bounce_from_player(self.parent.player)
        self.parent.destroy_blocks(self)
    
    def bounce_from_player(self, player):
        if self.collide_widget(player):
            self.velocity[1] = abs(self.velocity[1])
            # Add some horizontal velocity based on where ball hits paddle
            self.velocity[0] += (
                0.1 * ((self.center_x - player.center_x) / player.width))

class Block(Widget):
    colour = ListProperty([1, 0, 0, 1])
    
    def __init__(self, **kwargs):
        super(Block, self).__init__(**kwargs)
        # More vibrant colors that should show up better
        colors = [
            [1.0, 0.5, 0.0, 1.0],    # Orange
            [0.0, 0.8, 0.0, 1.0],    # Green
            [0.0, 0.5, 1.0, 1.0],    # Blue
            [1.0, 0.0, 0.5, 1.0],    # Pink
            [0.8, 0.0, 0.8, 1.0],    # Purple
            [1.0, 1.0, 0.0, 1.0],    # Yellow
        ]
        self.colour = random.choice(colors)
        
        with self.canvas:
            Color(*self.colour)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_graphics, size=self.update_graphics)
    
    def update_graphics(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class GameEndPopup(ModalView):
    message = StringProperty()
    game = ObjectProperty()

class Game(FloatLayout):
    blocks = ListProperty([])
    player = ObjectProperty()
    ball = ObjectProperty()
    
    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        
        # Set black background
        with self.canvas.before:
            Color(0, 0, 0, 1)  # Black background
            self.bg_rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Create player and ball
        self.player = Player(size_hint=(0.1, 0.05), pos_hint={'x': 0.45, 'y': 0.05})
        self.ball = Ball(size_hint=(0.03, 0.03), pos_hint={'x': 0.485, 'y': 0.3})
        
        self.add_widget(self.player)
        self.add_widget(self.ball)
    
    def on_touch_down(self, touch):
        # Let the player handle all touches in the bottom half
        if touch.y < self.height * 0.5:
            return self.player.on_touch_down(touch)
        return False
    
    def on_touch_move(self, touch):
        # Let the player handle touch movement
        return self.player.on_touch_move(touch)
    
    def on_touch_up(self, touch):
        # Let the player handle touch release
        return self.player.on_touch_up(touch)
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def setup_blocks(self):
        for block in self.blocks:
            self.remove_widget(block)
        self.blocks = []
        
        for y_jump in range(5):
            for x_jump in range(10):
                block = Block(
                    size_hint=(0.08, 0.06),
                    pos_hint={
                        'x': 0.05 + 0.09*x_jump,
                        'y': 0.6 + 0.08*y_jump
                    }
                )
                self.blocks.append(block)
                self.add_widget(block)
    
    def update(self, dt):
        self.ball.update(dt)
        self.player.update(dt)
        
        # Update positions based on pos_hint
        self.player.pos_hint = {'x': self.player.position, 'y': 0.05}
        self.ball.pos_hint = {'x': self.ball.pos_hint_x, 'y': self.ball.pos_hint_y}
    
    def start(self, *args):
        Clock.schedule_interval(self.update, 1./60.)
    
    def stop(self):
        Clock.unschedule(self.update)
    
    def reset(self):
        for block in self.blocks:
            self.remove_widget(block)
        self.blocks = []
        self.setup_blocks()
        self.ball.velocity = [random.uniform(-0.3, 0.3), 0.5]
        self.ball.pos_hint_x = 0.5
        self.ball.pos_hint_y = 0.3
        self.player.position = 0.5
    
    def lose(self):
        self.stop()
        GameEndPopup(
            message='[color=#ff0000]You lose![/color]',
            game=self).open()
    
    def win(self):
        self.stop()
        GameEndPopup(
            message='[color=#00ff00]You win![/color]',
            game=self).open()
    
    def destroy_blocks(self, ball):
        for i, block in enumerate(self.blocks):
            if ball.collide_widget(block):
                # Calculate overlap to determine bounce direction
                y_overlap = (
                    ball.top - block.y if ball.velocity[1] > 0
                    else block.top - ball.y) / block.height
                x_overlap = (
                    ball.right - block.x if ball.velocity[0] > 0
                    else block.right - ball.x) / block.width
                
                if x_overlap < y_overlap:
                    ball.velocity[0] *= -1
                else:
                    ball.velocity[1] *= -1
                
                self.remove_widget(block)
                self.blocks.pop(i)
                
                if len(self.blocks) == 0:
                    self.win()
                return  # Only remove at most 1 block per frame

class BreakoutApp(App):
    def build(self):
        g = Game()
        g.reset()
        Clock.schedule_once(g.start, 0)
        return g

if __name__ == '__main__':
    BreakoutApp().run()