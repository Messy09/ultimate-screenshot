thonpython
import json
import logging
from pathlib import Path

from capture.screenshot import ScreenshotCapturer
from capture.video_recorder import VideoRecorder
from capture.pdf_generator import PDFGenerator
from emulation.device_profiles import get_device_profile
from utils.cookies import apply_cookies
from utils.scroll import auto_scroll
from utils.timers import wait_for_load

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("runner")

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

def load_inputs():
    sample_path = DATA_DIR / "sample_inputs.json"
    with open(sample_path, "r") as f:
        return json.load(f)

def main():
    logger.info("Starting Ultimate Screenshot task...")

    inputs = load_inputs()
    results = []

    for item in inputs:
        url = item.get("url")
        device = item.get("device", "desktop")
        output_type = item.get("type", "screenshot")

        logger.info(f"Processing URL: {url}")

        device_profile = get_device_profile(device)
        wait_for_load(1.0)

        if item.get("cookies"):
            apply_cookies(item["cookies"])

        auto_scroll(steps=3, delay=0.2)

        if output_type == "screenshot":
            capturer = ScreenshotCapturer(device_profile)
            result = capturer.capture(url)

        elif output_type == "video":
            recorder = VideoRecorder(device_profile)
            result = recorder.record(url)

        elif output_type == "pdf":
            pdf_gen = PDFGenerator(device_profile)
            result = pdf_gen.generate(url)

        else:
            raise ValueError(f"Unknown type: {output_type}")

        results.append(result)

    output_path = DATA_DIR / "sample_outputs.json"
    with open(output_path, "w") as f:
        json.dump(results, f, indent=4)

    logger.info("Capture process completed successfully.")

if __name__ == "__main__":
    main()