import json
from pathlib import Path

def get_session_path():
    return Path.home() / ".desfr" / "session.json"

def save_session(file_path):
    session_path = get_session_path()

    session_path.parent.mkdir(parents=True, exist_ok=True)

    session_data = {
        "active_file": str(Path(file_path).resolve())
    }

    with session_path.open("w", encoding="utf-8") as f:
        json.dump(session_data, f, indent=4)

def load_session():
    session_path = get_session_path()

    if not session_path.exists():
        return None

    try:
        with session_path.open("r", encoding="utf-8") as f:

            session_data = json.load(f)

            if not isinstance(session_data, dict):
                return None

            active_file = session_data.get("active_file")

            if not isinstance(active_file, str) or not active_file.strip():
                return None

            return active_file

    except (json.JSONDecodeError, OSError):
            return None

def clear_session():
    session_path = get_session_path()

    if session_path.exists():
        session_path.unlink()