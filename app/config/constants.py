# -------------------------
# EMERGENCY KEYWORDS
# -------------------------

EMERGENCY_KEYWORDS = [
    "chest pain",
    "shortness of breath",
    "stroke",
    "heart attack",
    "unconscious",
    "severe bleeding",
    "difficulty breathing",
    "seizure"
]

# -------------------------
# MEDICAL DEPARTMENTS
# -------------------------

MEDICAL_DEPARTMENTS = [
    "General Medicine",
    "Cardiology",
    "Neurology",
    "Pulmonology",
    "Orthopedics",
    "Dermatology",
    "ENT",
    "Emergency Medicine"
]

# -------------------------
# SUPPORTED FILE TYPES
# -------------------------

SUPPORTED_IMAGE_TYPES = [
    ".jpg",
    ".jpeg",
    ".png"
]

SUPPORTED_AUDIO_TYPES = [
    ".wav",
    ".mp3",
    ".m4a"
]

SUPPORTED_DOCUMENT_TYPES = [
    ".pdf"
]

# -------------------------
# RAG SETTINGS
# -------------------------

DEFAULT_TOP_K = 5

DEFAULT_RERANK_K = 3

CHUNK_SIZE = 500

CHUNK_OVERLAP = 100

# -------------------------
# AI RESPONSE SETTINGS
# -------------------------

MAX_RESPONSE_TOKENS = 2048

DEFAULT_TEMPERATURE = 0.2

# -------------------------
# ALERT LEVELS
# -------------------------

ALERT_LEVELS = [
    "LOW",
    "MEDIUM",
    "HIGH",
    "CRITICAL"
]