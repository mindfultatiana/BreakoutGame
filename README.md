# Breakout Game

A classic breakout/brick breaker game built with Python and Kivy, designed to run on both desktop and Android devices. This project includes Docker containerization for easy Android APK building using Buildozer.

## Features

- **Classic Breakout Gameplay**: Break all the blocks by bouncing a ball off your paddle
- **Touch Controls**: Optimized for mobile devices with intuitive touch controls
- **Colorful Graphics**: Vibrant block colors and smooth animations
- **Cross-Platform**: Runs on desktop and Android devices
- **Game Over/Win Screens**: Modal popups with replay functionality

## Screenshots

*Game in action with colorful blocks and paddle controls*

## Installation & Setup

### Prerequisites

- Docker and Docker Compose
- Git

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/mindfultatiana/BreakoutGame.git
   cd BreakoutGame
   ```

2. **Build and run with Docker**
   ```bash
   docker-compose up --build
   ```

   This will automatically build the Android APK. The process may take 15-30 minutes on first run as it downloads and sets up the Android SDK, NDK, and other dependencies.

3. **Find your APK**
   ```bash
   ls bin/
   ```
   Look for `breakoutgame-0.1-armeabi-v7a-debug.apk`

### Manual Desktop Testing

If you want to test the game on desktop first:

```bash
pip install kivy pillow
python main.py
```

## Game Controls

### Desktop
- **Mouse**: Click and drag to move paddle
- **Keyboard**: Use arrow keys or A/D keys to move paddle

### Mobile/Tablet
- **Touch**: Tap and drag in the bottom half of the screen to move paddle
- The paddle will smoothly follow your finger movement

## Technical Details

### Architecture

- **Framework**: Kivy (Python GUI framework)
- **Build Tool**: Buildozer (Android APK compilation)
- **Containerization**: Docker with Python 3.9 and Java 17
- **Target Platform**: Android (armeabi-v7a architecture)

### File Structure

```
BreakoutGame/
├── main.py              # Main game logic and classes
├── breakout.kv          # Kivy UI layout file
├── buildozer.spec       # Android build configuration
├── Dockerfile           # Container setup for building
├── docker-compose.yml   # Docker orchestration
├── build.sh            # Build script
└── README.md           # This file
```

### Game Classes

- **`Player`**: Paddle widget with touch controls and smooth movement
- **`Ball`**: Game ball with physics and collision detection
- **`Block`**: Destructible blocks with random colors
- **`Game`**: Main game logic, collision handling, and game state
- **`GameEndPopup`**: Modal dialog for game over/win states

### Dependencies

- `kivy==2.1.0` - Main GUI framework
- `pillow` - Image processing
- `pyjnius` - Java/Android integration
- `cython==0.29.33` - Python to C compilation

## Building for Android

The project uses Docker to provide a consistent build environment with all necessary Android development tools.

### Build Configuration

Key settings in `buildozer.spec`:
- **Target API**: Latest Android API
- **Architecture**: armeabi-v7a (32-bit ARM)
- **Permissions**: Internet access
- **Orientation**: Portrait mode
- **Full Screen**: Enabled for immersive gaming

### Customization

To modify the game:

1. **Change app details** in `buildozer.spec`:
   ```ini
   title = Your Game Name
   package.name = yourgamename
   package.domain = com.yourname.yourgame
   ```

2. **Add app icon**: Uncomment and set the icon path:
   ```ini
   icon.filename = %(source.dir)s/data/icon.png
   ```

3. **Add splash screen**: Uncomment and set the presplash path:
   ```ini
   presplash.filename = %(source.dir)s/data/presplash.png
   ```

## Development

### Game Mechanics

- **Ball Physics**: Realistic bouncing with velocity adjustments
- **Collision Detection**: Precise collision handling between ball, paddle, and blocks
- **Difficulty**: Ball speed increases based on paddle hit location
- **Win Condition**: Destroy all blocks
- **Lose Condition**: Ball falls below paddle

### Adding Features

Common enhancements you could add:
- Power-ups (multi-ball, larger paddle, etc.)
- Multiple levels with different block layouts
- Score tracking and high scores
- Sound effects and background music
- Particle effects for block destruction

### Testing

Test on desktop before building APK:
```bash
python main.py
```

For Android testing, install the APK on your device:
```bash
adb install bin/breakoutgame-0.1-armeabi-v7a-debug.apk
```

## Troubleshooting

### Common Build Issues

1. **Docker space issues**: Clean up Docker images periodically
   ```bash
   docker system prune -a
   ```

2. **Build fails**: Check logs in the container
   ```bash
   docker-compose logs
   ```

3. **APK not found**: Ensure build completed successfully
   ```bash
   docker-compose up --build
   ls bin/
   ```

### Performance Issues

- The game runs at 60 FPS by default
- Reduce frame rate in `main.py` if needed: `Clock.schedule_interval(self.update, 1./30.)`
- Large screen devices may need UI scaling adjustments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test on both desktop and Android
5. Submit a pull request

## License

This project is open source. Feel free to use, modify, and distribute as needed.

## Acknowledgments

- Built following Kivy game development tutorials
- Thanks to the Kivy and Buildozer communities for excellent documentation
- Docker containerization inspired by mobile development best practices

---

**Enjoy breaking those blocks!** 🎮