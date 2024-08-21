"""Constants for librelink."""

from logging import Logger, getLogger
from typing import Final

LOGGER: Logger = getLogger(__package__)

NAME: Final = "LibreLink"
DOMAIN: Final = "librelink"
VERSION: Final = "1.2.3"
ATTRIBUTION: Final = "Data provided by https://libreview.com"
LOGIN_URL: Final = "/llu/auth/login"
CONNECTION_URL: Final = "/llu/connections"
BASE_URL_LIST: Final = {
    "Global": "https://api.libreview.io",
    "Latin America": "https://api-la.libreview.io",
}
PRODUCT: Final = "llu.ios"
VERSION_APP: Final = "4.11.0"
GLUCOSE_VALUE_ICON: Final = "mdi:diabetes"
GLUCOSE_TREND_ICON: Final = {
    1: "mdi:arrow-down-bold-box",
    2: "mdi:arrow-bottom-right-bold-box",
    3: "mdi:arrow-right-bold-box",
    4: "mdi:arrow-top-right-bold-box",
    5: "mdi:arrow-up-bold-box",
}
GLUCOSE_TREND_MESSAGE: Final = {
    1: "Decreasing fast",
    2: "Decreasing",
    3: "Stable",
    4: "Increasing",
    5: "Increasing fast",
}

CONF_PATIENT_ID: Final = "patient_id"

REFRESH_RATE_MIN: Final = 1
API_TIME_OUT_SECONDS: Final = 20
