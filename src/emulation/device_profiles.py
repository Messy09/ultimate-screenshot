thonpython
DEVICES = {
    "desktop": {
        "name": "Desktop 1080p",
        "width": 1920,
        "height": 1080,
        "user_agent": "Mozilla/5.0 Desktop"
    },
    "iphone": {
        "name": "iPhone 14",
        "width": 390,
        "height": 844,
        "user_agent": "Mozilla/5.0 iPhone"
    },
    "android": {
        "name": "Pixel 7",
        "width": 412,
        "height": 915,
        "user_agent": "Mozilla/5.0 Android"
    }
}

def get_device_profile(name: str):
    return DEVICES.get(name, DEVICES["desktop"])