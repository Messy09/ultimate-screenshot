thonpython
import logging
import time
from pathlib import Path
from uuid import uuid4

logger = logging.getLogger("pdf")

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "data" / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

class PDFGenerator:
    def __init__(self, device_profile):
        self.device = device_profile

    def generate(self, url: str):
        logger.info(f"[PDF] Generating PDF for {url} using {self.device['name']}...")

        time.sleep(0.8)
        file_id = str(uuid4())
        fake_path = OUTPUT_DIR / f"{file_id}.pdf"
        fake_path.write_text("FAKE_PDF_DATA")

        return {
            "screenshot_image": f"/preview/{file_id}",
            "content_Type": "application/pdf",
            "linkUrl": url,
            "screenshot_url": f"/download/{file_id}"
        }