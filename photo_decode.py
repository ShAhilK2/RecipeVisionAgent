import base64
import mimetypes
from dotenv import load_dotenv
from pathlib import Path
from tkinter import TclError, Tk, filedialog
from typing import Optional

from langchain.messages import HumanMessage


load_dotenv()


def choose_image_file() -> Path:
    """Open a local file picker when no image path is passed on the command line."""

    root = None
    filename = ""

    try:
        root = Tk()
        root.withdraw()

        filename = filedialog.askopenfilename(
            title="Select an image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.webp"),
                ("All Files", "*.*")
            ]
        )

    except TclError:
        filename = input("Image path: ").strip().strip("'").strip('"')

    finally:
        if root is not None:
            root.destroy()

    if not filename:
        raise SystemExit("No Image Selected")

    return Path(filename).expanduser()


def image_to_data_url(image_path: Path) -> str:
    """Convert an image file to a data URL."""

    image_path = image_path.expanduser().resolve()

    if not image_path.is_file():
        raise ValueError(f"Image file not found: {image_path}")

    mime_type, _ = mimetypes.guess_type(str(image_path))

    if mime_type is None:
        mime_type = "application/octet-stream"

    if not mime_type.startswith("image/"):
        raise ValueError(f"Selected file is not an image: {image_path}")

    img_b64 = base64.b64encode(
        image_path.read_bytes()
    ).decode("utf-8")

    return f"data:{mime_type};base64,{img_b64}"


def build_image_message(
    image_path: Path,
    prompt: Optional[str] = None
) -> HumanMessage:
    """Build a message with an image."""

    return HumanMessage(
        content=[
            {
                "type": "text",
                "text": prompt if prompt is not None else ""
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": image_to_data_url(image_path)
                }
            }
        ]
    )

