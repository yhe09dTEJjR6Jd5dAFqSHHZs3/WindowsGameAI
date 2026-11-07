import sys
sys.dont_write_bytecode = True

import collections
import ctypes as C
import datetime
import hashlib
import hmac
import importlib
import json
import math
import os
from pathlib import Path
import queue
import random
import re
import sqlite3
import stat
import sysconfig
import shutil
import tempfile
import threading
import time
import traceback
import uuid
import urllib.parse
import urllib.request
import zipfile


APP_NAME = "通用鼠标游戏 Agent · 对象学习与规划"
MINIMUM_PYTHON = (3, 10)
WINDOW_GEOMETRY = "1080x780"
WINDOW_MIN_WIDTH = 760
WINDOW_MIN_HEIGHT = 560
UI_FIT_WIDTH_RATIO = 0.92
UI_FIT_HEIGHT_RATIO = 0.84
UI_COMPACT_MIN_WIDTH = 480
UI_COMPACT_MIN_HEIGHT = 420
UI_PREVIEW_LABEL_HEIGHT = 28
UI_PREVIEW_MIN_HEIGHT = 160
UI_METRIC_COLUMNS = 4
UI_LOG_VISIBLE_ROWS = 8
UI_LOG_VISIBLE_COLUMNS = 36
UI_PREVIEW_PLACEHOLDER_MARGIN = 14
UI_METRIC_COMPACT_COLUMNS = 2
UI_COMPACT_METRIC_COUNT = 4
UI_DEMONSTRATION_LOG_INTERVAL = 8
UI_METRIC_COMPACT_WIDTH = 940
UI_PANEL_STACK_WIDTH = 850
UI_METRIC_COMPACT_HEIGHT = 650
UI_FONT_BASE = 10
UI_FONT_TITLE = 19
UI_FONT_METRIC = 17
UI_SPACING_FINE = 3
UI_SPACING_XS = 6
UI_SPACING_SM = 8
UI_SPACING_MD = 12
UI_SPACING_LG = 14
UI_SPACING_SECTION = 20
UI_SPACING_BUTTON = 9
UI_WRAP_HEADER = 840
UI_WRAP_HELP = 820
COORDINATE_CENTER = 0.5
UI_WRAP_HINT = 640
SECONDS_PER_MINUTE = 60
PERCENT_SCALE = 100
UI_TICK_MS = 120
UI_THEME_REFRESH_SECONDS = 2.0
UI_TARGET_DISCOVERY_SECONDS = 0.9
TD_DISCOUNT = 0.82
TD_LEARNING_RATE = 0.30
TD_LEARNING_RATE_DECAY = 0.10
TD_ACTION_WEIGHT = 0.42
TD_TRACE_DEPTH = 5
TD_TRACE_DECAY = 0.60
TD_TRACE_CREDIT = 0.22
TD_TRACE_MIN_PROGRESS = 0.045
TD_REWARD_CEILING = 1.0
KEY_PRESSED_MASK = 0x0001
WH_MOUSE_LL = 14
WM_MOUSEMOVE = 0x0200
WM_LBUTTONDOWN = 0x0201
WM_LBUTTONUP = 0x0202
WM_RBUTTONDOWN = 0x0204
WM_RBUTTONUP = 0x0205
WM_MBUTTONDOWN = 0x0207
WM_MBUTTONUP = 0x0208
WM_MOUSEWHEEL = 0x020A
LLMHF_INJECTED = 0x00000001
VK_LBUTTON = 0x01
VK_RBUTTON = 0x02
VK_MBUTTON = 0x04
OBSERVER_QUEUE_CAPACITY = 1024
OBSERVER_QUEUE_BATCH = 96
OBSERVER_FRAME_HISTORY = 18
OBSERVER_FRAME_MAX_AGE_SECONDS = 1.5
OBSERVER_FRAME_INTERVAL_ACTIVE_SECONDS = 0.13
OBSERVER_FRAME_INTERVAL_IDLE_SECONDS = 0.50
OBSERVER_CAPTURE_EDGE = 384
OBSERVER_ACTIVE_WINDOW_SECONDS = 2.0
OBSERVER_HOOK_MOVE_INTERVAL_SECONDS = 0.06
OBSERVER_HOOK_SILENCE_SECONDS = 1.8
OBSERVER_HOOK_WAIT_SECONDS = 0.018
OBSERVER_WORKER_WAIT_SECONDS = 0.045
OBSERVER_AFTER_ACTION_SECONDS = 0.21
OBSERVER_DRAG_THRESHOLD = 0.026
OBSERVER_MOVE_DISTANCE = 0.055
OBSERVER_MOVE_RECORD_SECONDS = 0.42
OBSERVER_LONG_PRESS_SECONDS = 0.48
OBSERVER_SINGLE_CLICK_TIMEOUT_SECONDS = 0.52
OBSERVER_DOUBLE_CLICK_DISTANCE = 0.028
OBSERVER_ERROR_REPORT_SECONDS = 12.0
DEMONSTRATION_RECENT_LIMIT = 512
DEMONSTRATION_MATCH_LIMIT = 160
DEMONSTRATION_MAX_CANDIDATES = 9
DEMONSTRATION_EXACT_SHAPE_DIFFERENCE = 32
DEMONSTRATION_EXACT_HUE_DIFFERENCE = 80
DEMONSTRATION_COARSE_SHAPE_DIFFERENCE = 23
DEMONSTRATION_COARSE_HUE_DIFFERENCE = 56
DEMONSTRATION_GENERAL_SHAPE_DIFFERENCE = 12
DEMONSTRATION_GENERAL_HUE_DIFFERENCE = 30
DEMONSTRATION_GENERAL_CONTEXT_DISTANCE = 5
DEMONSTRATION_BASE_REPLAY_CHANCE = 0.86
DEMONSTRATION_STAGNATION_DECAY = 0.19
DEMONSTRATION_COUNT_WEIGHT = 0.065
DEMONSTRATION_EFFECT_WEIGHT = 0.12
DEMONSTRATION_REPLAY_WEIGHT = 0.30
DEMONSTRATION_SIMILARITY_WEIGHT = 2.1
DEMONSTRATION_SCENE_BONUS = 0.24
DEMONSTRATION_RANDOM_NOISE = 0.04
DEMONSTRATION_SEQUENCE_SECONDS = 5.0
DEMONSTRATION_SEQUENCE_WEIGHT = 0.44
DEMONSTRATION_SEQUENCE_PRIOR = 2.0
DEMONSTRATION_SEQUENCE_MIN_GOAL_PROGRESS = -0.001
DEMONSTRATION_POLICY_PRIOR_WEIGHT = 0.17
DEMONSTRATION_GENERAL_PRIOR_VISITS = 6.0
DEMONSTRATION_LOCAL_MATCH_WEIGHT = 0.90
DEMONSTRATION_LOCAL_MAX_SHAPE_DISTANCE = 44
DEMONSTRATION_LOCAL_MAX_COLOR_DISTANCE = 100
DEMONSTRATION_FAILURE_PENALTY = 0.65
DEMONSTRATION_EXPECTED_NOOP_PENALTY = 0.25
DEMONSTRATION_LOCAL_PATCH_SCALE = 2.0
DEMONSTRATION_REPLAY_SUCCESS_REWARD = 0.18
DEMONSTRATION_GOAL_REWARD_SHARE = 0.60
DEMONSTRATION_GOAL_PROGRESS_GAIN = 2.7
DEMONSTRATION_GOAL_COMPLETION_DISTANCE = 0.16
DEMONSTRATION_GOAL_COMPLETION_BONUS = 0.12
DEMONSTRATION_PATH_MAX_POINTS = 36
DEMONSTRATION_PATH_MAX_BYTES = 4096
DEMONSTRATION_PATH_MIN_DISTANCE = 0.008
DEMONSTRATION_TRANSFER_GOAL_COUNT = 4
DEMONSTRATION_TRANSFER_GOAL_MIN_EFFECT = 0.01
DEMONSTRATION_TRANSFER_GOAL_MIN_DISTANCE = 0.06
DEMONSTRATION_TRANSFER_GOAL_WEIGHT = 0.75
OBJECT_PATCH_SIDE = 8
OBJECT_PATCH_GRAY_QUANTIZATION = 16
OBJECT_PATCH_RADIUS_X = 0.065
OBJECT_PATCH_RADIUS_Y = 0.09
OBJECT_PATCH_MIN_CONTRAST = 0.80
OBJECT_PATCH_MATCH_THRESHOLD = 0.80
OBJECT_PATCH_RELOCATION_THRESHOLD = 0.85
OBJECT_PATCH_DESTINATION_THRESHOLD = 0.88
OBJECT_PATCH_SIMILARITY_SHAPE_WEIGHT = 1.75
OBJECT_PATCH_SIMILARITY_HUE_WEIGHT = 0.25
OBJECT_PATCH_SIMILARITY_BRIGHTNESS_WEIGHT = 0.16
OBJECT_PATCH_POSITION_WEIGHT = 0.055
OBJECT_PATCH_REFINE_COUNT = 3
OBJECT_PATCH_REFINE_RATIO = 0.5
OBJECT_PATCH_REFINE_STEPS = 4
OBJECT_PATCH_MAX_COARSE_DISTANCE = 12
OBJECT_PATCH_REPLAY_CANDIDATES = 16
OBJECT_PATCH_MATCH_REWARD = 1.25
OBJECT_PATCH_MISMATCH_PENALTY = 0.65
OBJECT_PATCH_APPEARANCE_GRID = 3
OBJECT_PATCH_APPEARANCE_BAND = 1.1
OBJECT_PATCH_APPEARANCE_BRIGHTNESS_LEVELS = 4
OBJECT_PATCH_APPEARANCE_CONTRAST_LEVELS = 4
OBJECT_PATCH_APPEARANCE_HUE_LEVELS = 4
VISUAL_AFFORDANCE_PRIOR_VISITS = 5.0
VISUAL_AFFORDANCE_HUMAN_WEIGHT = 0.62
VISUAL_AFFORDANCE_ACTION_WEIGHT = 0.40
VISUAL_AFFORDANCE_SPOT_WEIGHT = 0.60
MOUSE_PATH_STEP_SECONDS = 0.018
MOUSE_PATH_TIME_EPSILON = 0.001
MODEL_REFRESH_ACTIONS = 6
MODEL_MAX_EDGES = 12000
MODEL_VALUE_ITERATIONS = 18
MODEL_VALUE_TOLERANCE = 0.001
MODEL_VALUE_LIMIT = 1.0
MODEL_DISCOUNT = 0.78
MODEL_HUMAN_CONFIDENCE_PRIOR = 1.8
MODEL_HUMAN_COUNT_WEIGHT = 4.0
MODEL_HUMAN_REWARD = 0.86
MODEL_HUMAN_EFFECT_WEIGHT = 0.30
MODEL_HUMAN_STATIC_FACTOR = 0.55
MODEL_AGENT_REWARD_WEIGHT = 0.10
MODEL_SELF_LOOP_PENALTY = 0.12
MODEL_REGION_WEIGHT = 1.30
MODEL_ACTION_WEIGHT = 1.60
MODEL_MAX_CACHED_GAMES = 16
MODEL_COARSE_BACKOFF_WEIGHT = 0.45
UI_RESTORE_TOPMOST_MS = 420
UI_WRAP_MINIMUM = 180
UI_LOG_LIMIT = 240
COUNTS_REFRESH_SECONDS = 1.5
TARGET_COLUMNS = 4
TARGET_ROWS = 3
TARGET_SALIENCE_WEIGHT = 0.32
TARGET_HISTORY_WEIGHT = 1.15
TARGET_EXPLORATION_WEIGHT = 0.34
TARGET_RECENCY_PENALTY = 0.12
TARGET_JITTER_SPAN = 0.28
TARGET_AIM_BLEND = 0.78
TARGET_AIM_BASE_ENERGY = 8.0
TARGET_PICK_NOISE = 0.018
TARGET_GLOBAL_EXPLORATION = 0.04
DESTINATION_HISTORY_WEIGHT = 1.05
DESTINATION_COARSE_PRIOR_VISITS = 7.0
DESTINATION_SALIENCE_WEIGHT = 0.26
DESTINATION_EXPLORATION_WEIGHT = 0.38
DESTINATION_REPEAT_BONUS = 0.10
DESTINATION_RANDOM_CHANCE = 0.06
POLICY_NO_EFFECT_STEPS = 10
POLICY_STAGNATION_REGION_CHANCE = 0.35
POLICY_STAGNATION_SPOT_CHANCE = 0.28
POLICY_EXPLORATION_BOOST = 0.75
POLICY_SUCCESS_REPEAT_CHANCE = 0.24
TARGET_REPEAT_DECAY = 0.70
TARGET_RECENT_WINDOW = 8
COARSE_CONTEXT_COLUMNS = 3
COARSE_CONTEXT_ROWS = 2
COARSE_CONTEXT_LEVELS = 3
COARSE_CONTEXT_SATURATION_LEVELS = 2
COARSE_ACTION_PRIOR_VISITS = 9.0
COARSE_SPOT_PRIOR_VISITS = 6.0
COARSE_SPOT_WEIGHT = 0.65
REPEAT_EFFECT_THRESHOLD = 0.012
REPEAT_ACTION_BONUS = 0.16
REPEAT_SPOT_BONUS = 0.12
ACTION_PRIOR_WEIGHT = 0.14
ACTION_PRIORS = {"左击": 1.0, "双击": 0.70, "左拖": 0.55, "移动": 0.48, "相对移动": 0.40, "左按相对移动": 0.48, "右按相对移动": 0.32, "左长按": 0.45, "右击": 0.32, "右拖": 0.30, "右长按": 0.26, "中击": 0.22, "上滚": 0.34, "下滚": 0.34}
EVENT_RETENTION_COUNT = 75000
EVENT_PRUNE_INTERVAL = 2048
DB_WAL_PAGES = 256
DB_CACHE_KIB = 8192
BLACKBOX_JSON_INDENT = 2
BLACKBOX_RECENT_EVENT_LIMIT = 512
MIN_FREE_SPACE_BYTES = 128 * 1024 * 1024
MIN_TARGET_DIMENSION = 64
BOUNDS_INSET = 1
SPEED_TIME_FLOOR_SECONDS = 0.001
PREVIEW_ZOOM = 2
VISION_LONG_EDGE = 384
VISION_ADAPTIVE_MIN_EDGE = 112
VISION_RESOLUTION_STEP = 48
VISION_ADAPTIVE_MAX_EDGE = 1024
VISION_MAX_CAPTURE_PIXELS = 768 * 768
VISION_ADAPT_EVERY_STEPS = 8
VISION_PROCESS_BUDGET_LOW_SECONDS = 0.085
VISION_PROCESS_BUDGET_HIGH_SECONDS = 0.24
VISION_COST_EMA_WEIGHT = 0.25
VISION_ACCELERATOR_FAILURE_LIMIT = 3
VISION_MIN_EDGE = 24
VISION_CONTEXT_SAMPLE_BUDGET = 24000
VISION_SALIENCE_SAMPLE_BUDGET = 48000
VISION_DIFFERENCE_SAMPLE_BUDGET = 48000
VISION_COLOR_DIFFERENCE_WEIGHT = 0.36
COLOR_FINGERPRINT_SATURATION_THRESHOLD = 40
FINGERPRINT_BLUE_HUE = 3
ACTION_MOTION_REFERENCE = 0.06
ACTION_MOTION_PRIOR_BONUS = 0.10
ACTION_STILL_PRIOR_BONUS = 0.06
ACTION_MOTION_ACTIONS = frozenset(("移动", "相对移动", "左拖", "右拖", "左按相对移动", "右按相对移动"))
ACTION_DESTINATION_ACTIONS = frozenset(("左拖", "右拖", "左按相对移动", "右按相对移动"))
ACTION_STILL_ACTIONS = frozenset(("左击", "双击", "右击", "中击", "左长按", "右长按"))
GRID_COLUMNS = 6
GRID_ROWS = 4
CONTEXT_COLUMNS = 5
CONTEXT_ROWS = 3
FINGERPRINT_SIDE = 8
CONTEXT_LEVELS = 4
CONTEXT_SATURATION_LEVELS = 3
VISUAL_CHANGE_SCALE = 4.0
VISUAL_QUIET_PENALTY = 0.025
VISUAL_NOVELTY_BONUS = 0.10
VISUAL_SCENE_TRANSITION_BONUS = 0.10
VISUAL_EFFECT_THRESHOLD = 0.004
SPOT_CHANGE_WEIGHT = 0.42
REGION_CHANGE_WEIGHT = 0.36
GLOBAL_CHANGE_WEIGHT = 1.0 - SPOT_CHANGE_WEIGHT - REGION_CHANGE_WEIGHT
BACKGROUND_MOTION_WEIGHT = 0.75
DRAG_DESTINATION_EFFECT_WEIGHT = 0.38
MOTION_SALIENCE_WEIGHT = 2.0
EXPLORATION_STRENGTH = 0.60
GENERALIZATION_STRENGTH = 0.40
GENERALIZATION_PRIOR_VISITS = 7.0
STORE_HISTORY_CACHE_ENTRIES = 32
STORE_HISTORY_CACHE_AGE_STEPS = 4
STATE_RECENT_WINDOW = 12
STATE_CYCLE_PENALTY = 0.12
BACKGROUND_EMA_WEIGHT = 0.18
BACKGROUND_EMA_GUARD_WEIGHT = 0.8
GAME_TITLE_ID_LENGTH = 120
REGION_RECENCY_PENALTY = 0.50
REGION_SALIENCE_WEIGHT = 0.48
REGION_HISTORY_WEIGHT = 1.20
REGION_EXPLORATION_WEIGHT = 0.42
REGION_RANDOM_CHANCE = 0.08
REGION_SCORE_JITTER = 0.018
REGION_PRIOR_VISITS = 7.0
REGION_SUCCESS_RECENCY_FACTOR = 0.15
COLOR_SALIENCE_WEIGHT = 0.27
SATURATION_CHANGE_WEIGHT = 0.20
GAME_ID_LENGTH = 16
SHARED_HOST_EXECUTABLES = frozenset(("chrome.exe", "msedge.exe", "firefox.exe", "opera.exe", "brave.exe", "python.exe", "pythonw.exe", "java.exe", "javaw.exe"))
WINDOW_TITLE_LIMIT = 512
WINDOW_PATH_LIMIT = 32768
WINDOW_CLASS_LIMIT = 256
WINDOW_DISPLAY_NAME_LIMIT = 78
PROCESS_QUERY_LIMITED_INFORMATION = 0x1000
SW_RESTORE = 9
GA_ROOT = 2
RECOVER_WINDOW_EVERY_SECONDS = 0.8
SNAPSHOT_RECHECK_THRESHOLD = 0.0018
ACTION_FEEDBACK_RECHECK_SECONDS = (0.20, 0.38)
DRAG_DURATION_SECONDS = 0.38
LONG_PRESS_SECONDS = 0.9
RELATIVE_MOUSE_REACH = 0.35
RELATIVE_DRAG_TIME_SECONDS = 0.30
RELATIVE_DRAG_STEPS = 12
ACTION_HOLD_DURATIONS = (0.42, LONG_PRESS_SECONDS, 1.65)
ACTION_DRAG_DURATIONS = (0.19, DRAG_DURATION_SECONDS, 0.78)
ACTION_RELATIVE_DRAG_DURATIONS = (0.14, RELATIVE_DRAG_TIME_SECONDS, 0.57)
ACTION_WHEEL_TICKS = (1, 2, 4)
ACTION_PARAMETER_PRIOR_VISITS = 4.0
ACTION_PARAMETER_EXPLORATION = 0.22
ACTION_PARAMETER_DEFAULT_BONUS = 0.075
ACTION_AIM_MIN_REWARD = 0.045
ACTION_AIM_PRIOR_STRENGTH = 0.85
ACTION_AIM_COARSE_WEIGHT = 0.28
ACTION_AIM_MAX_REPLAY = 0.94
ACTION_AIM_EXPLORATION_DECAY = 0.65
ACTION_PLAN_WEIGHT = 0.36
ACTION_PLAN_PRIOR_VISITS = 4.0
ACTION_WHEEL_TICK_INTERVAL_SECONDS = 0.045
CLICK_DURATION_SECONDS = 0.055
CURSOR_POSITION_CHECK_ATTEMPTS = 3
CURSOR_POSITION_CHECK_INTERVAL_SECONDS = 0.01
ACTION_SETTLE_SECONDS = 0.13
SCREEN_HIDE_SETTLE_SECONDS = 0.11
ERROR_RETRY_SECONDS = 0.28
ERROR_REPORT_SECONDS = 10.0
KEYBOARD_POLL_SECONDS = 0.025
REPORT_EVERY_STEPS = 4
DATABASE_BUSY_SECONDS = 3
MILLISECONDS_PER_SECOND = 1000
ERROR_RETRY_MS = round(ERROR_RETRY_SECONDS * MILLISECONDS_PER_SECOND)
BYTES_PER_COLOR_PIXEL = 4
BYTES_PER_RGB_PIXEL = 3
BITS_PER_BYTE = 8
COLOR_MAX = (1 << BITS_PER_BYTE) - 1
COLOR_CHANNEL_RED_WEIGHT = 77
COLOR_CHANNEL_GREEN_WEIGHT = 150
COLOR_CHANNEL_BLUE_WEIGHT = 29
WIN64_POINTER_BYTES = 8
WINERROR_NOT_ENOUGH_MEMORY = 8
WINERROR_OUTOFMEMORY = 14
ABSOLUTE_COORDINATE_MAX = 65535
WHEEL_DELTA = 120
GW_HWNDNEXT = 2
SM_XVIRTUALSCREEN = 76
SM_YVIRTUALSCREEN = 77
SM_CXVIRTUALSCREEN = 78
SM_CYVIRTUALSCREEN = 79
SRCCOPY = 0x00CC0020
CAPTUREBLT = 0x40000000
BI_RGB = 0
DIB_RGB_COLORS = 0
COLORONCOLOR = 3
INPUT_MOUSE = 0
MOUSEEVENTF_MOVE = 0x0001
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004
MOUSEEVENTF_RIGHTDOWN = 0x0008
MOUSEEVENTF_RIGHTUP = 0x0010
MOUSEEVENTF_MIDDLEDOWN = 0x0020
MOUSEEVENTF_MIDDLEUP = 0x0040
MOUSE_BUTTON_RELEASE_FLAGS = MOUSEEVENTF_LEFTUP | MOUSEEVENTF_RIGHTUP | MOUSEEVENTF_MIDDLEUP
MOUSE_BUTTON_DOWN_FLAGS = MOUSEEVENTF_LEFTDOWN | MOUSEEVENTF_RIGHTDOWN | MOUSEEVENTF_MIDDLEDOWN
MOUSEEVENTF_WHEEL = 0x0800
MOUSE_POSITION_REQUIRED_FLAGS = MOUSE_BUTTON_DOWN_FLAGS | MOUSEEVENTF_WHEEL
MOUSEEVENTF_VIRTUALDESK = 0x4000
MOUSEEVENTF_ABSOLUTE = 0x8000
WH_KEYBOARD_LL = 13
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x0104
WM_SYSKEYUP = 0x0105
PM_REMOVE = 0x0001
VK_FIRST = 0x08
VK_CANCEL = 0x03
VK_LAST = 0xFE
KEYBOARD_KEYS = (VK_CANCEL, *range(VK_FIRST, VK_LAST + 1))
KEY_DOWN_MASK = 0x8000
LLKHF_INJECTED = 0x10
KEYBOARD_SHUTDOWN_TIMEOUT_SECONDS = 1.0
DPI_AWARENESS_CONTEXT_PER_MONITOR_V2 = -4
DWM_CLOAKED_ATTRIBUTE = 14
FOLDERID_DESKTOP = "B4BFCC3A-DB2C-424C-B029-7FE99A87C641"
MOUSE_ACTIONS = ("移动", "相对移动", "左击", "右击", "双击", "左拖", "右拖", "左长按", "右长按", "中击", "上滚", "下滚", "左按相对移动", "右按相对移动")
ACTION_PARAMETERS = {
    "左长按": ACTION_HOLD_DURATIONS,
    "右长按": ACTION_HOLD_DURATIONS,
    "左拖": ACTION_DRAG_DURATIONS,
    "右拖": ACTION_DRAG_DURATIONS,
    "左按相对移动": ACTION_RELATIVE_DRAG_DURATIONS,
    "右按相对移动": ACTION_RELATIVE_DRAG_DURATIONS,
    "上滚": ACTION_WHEEL_TICKS,
    "下滚": ACTION_WHEEL_TICKS,
}
UI_LIGHT_BACKGROUND = "#f4f7fb"
UI_LIGHT_FOREGROUND = "#162033"
UI_LIGHT_MUTED = "#5d6c81"
UI_LIGHT_ACCENT = "#2563eb"
UI_LIGHT_CARD = "#ffffff"
UI_LIGHT_BORDER = "#dce4ef"
UI_BACKGROUND = UI_LIGHT_BACKGROUND
UI_FOREGROUND = UI_LIGHT_FOREGROUND
UI_MUTED = UI_LIGHT_MUTED
UI_ACCENT = UI_LIGHT_ACCENT
UI_CARD = UI_LIGHT_CARD
UI_BORDER = UI_LIGHT_BORDER
UI_DARK_BACKGROUND = "#151a24"
UI_DARK_FOREGROUND = "#eaf0fa"
UI_DARK_MUTED = "#a7b5c9"
UI_DARK_ACCENT = "#8ab4ff"
UI_DARK_CARD = "#202938"
UI_DARK_BORDER = "#39465a"
UI_THEME_REGISTRY = r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize"
UI_THEME_VALUE = "AppsUseLightTheme"
WINDOW_IGNORED_CLASSES = frozenset(("Progman", "WorkerW", "Shell_TrayWnd"))
STORAGE_CHECK_SECONDS = 3.0
FALLBACK_CONTEXT_LIMIT = 256
ACCELERATOR_METADATA_URL = "https://pypi.org/pypi/numpy/json"
ACCELERATOR_ARCHIVE_HOST = "files.pythonhosted.org"
ACCELERATOR_NAME = "numpy"
ACCELERATOR_METADATA_MAX_BYTES = 16 * 1024 * 1024
ACCELERATOR_ARCHIVE_MAX_BYTES = 80 * 1024 * 1024
ACCELERATOR_UNPACK_MAX_BYTES = 512 * 1024 * 1024
ACCELERATOR_ARCHIVE_MAX_ENTRIES = 10000
ACCELERATOR_ARCHIVE_MAX_NAME = 1024
ACCELERATOR_ARCHIVE_ENCRYPTED_FLAG = 0x0001
ARCHIVE_UNIX_MODE_SHIFT = 16
ACCELERATOR_TIMEOUT_SECONDS = 8.0
ACCELERATOR_RETRIES = 2
ACCELERATOR_RETRY_SECONDS = 0.8
ACCELERATOR_CHUNK_BYTES = 128 * 1024
ACCELERATOR_PROGRESS_BYTES = 1024 * 1024
ACCELERATOR_DISK_MULTIPLIER = 3
ACCELERATOR_STOP_WAIT_SECONDS = 0.2
ACCELERATOR_METADATA_MARKER = "ready.json"
NUMPY_ACCELERATOR = None
NUMPY_IMPORT_LOCK = threading.RLock()



def utc_stamp():
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


def python_abi():
    tag = "cp" + str(sys.version_info.major) + str(sys.version_info.minor)
    return tag + ("t" if sysconfig.get_config_var("Py_GIL_DISABLED") else "")

def set_system_palette():
    global UI_BACKGROUND, UI_FOREGROUND, UI_MUTED, UI_ACCENT, UI_CARD, UI_BORDER
    try:
        import winreg
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, UI_THEME_REGISTRY) as key:
            dark = winreg.QueryValueEx(key, UI_THEME_VALUE)[0] == 0
    except (OSError, ImportError, ValueError):
        dark = False
    UI_BACKGROUND = UI_DARK_BACKGROUND if dark else UI_LIGHT_BACKGROUND
    UI_FOREGROUND = UI_DARK_FOREGROUND if dark else UI_LIGHT_FOREGROUND
    UI_MUTED = UI_DARK_MUTED if dark else UI_LIGHT_MUTED
    UI_ACCENT = UI_DARK_ACCENT if dark else UI_LIGHT_ACCENT
    UI_CARD = UI_DARK_CARD if dark else UI_LIGHT_CARD
    UI_BORDER = UI_DARK_BORDER if dark else UI_LIGHT_BORDER
    return dark


def object_patch(frame, x, y):
    side = OBJECT_PATCH_SIDE
    count = side * side
    samples = bytearray(count * 2)
    x = min(1.0, max(0.0, x))
    y = min(1.0, max(0.0, y))
    for row in range(side):
        offset_y = ((row + COORDINATE_CENTER) / side - COORDINATE_CENTER) * 2 * OBJECT_PATCH_RADIUS_Y
        py = min(frame.height - 1, max(0, round((y + offset_y) * (frame.height - 1))))
        for column in range(side):
            offset_x = ((column + COORDINATE_CENTER) / side - COORDINATE_CENTER) * 2 * OBJECT_PATCH_RADIUS_X
            px = min(frame.width - 1, max(0, round((x + offset_x) * (frame.width - 1))))
            index = py * frame.width + px
            point = row * side + column
            samples[point] = frame.gray[index] // OBJECT_PATCH_GRAY_QUANTIZATION
            rgb_index = index * BYTES_PER_RGB_PIXEL
            red, green, blue = frame.rgb[rgb_index:rgb_index + BYTES_PER_RGB_PIXEL]
            if max(red, green, blue) - min(red, green, blue) < COLOR_FINGERPRINT_SATURATION_THRESHOLD:
                hue = 0
            elif red >= green and red >= blue:
                hue = 1
            elif green >= red and green >= blue:
                hue = 2
            else:
                hue = FINGERPRINT_BLUE_HUE
            samples[count + point] = hue
    return samples.hex()


def object_patch_contrast(values):
    size = OBJECT_PATCH_SIDE * OBJECT_PATCH_SIDE
    mean = sum(values[:size]) / size
    return sum(abs(value - mean) for value in values[:size]) / size


def object_patch_similarity(first, second):
    size = OBJECT_PATCH_SIDE * OBJECT_PATCH_SIDE
    if len(first) != size * 2 or len(second) != size * 2:
        return 0.0
    mean_first = sum(first[:size]) / size
    mean_second = sum(second[:size]) / size
    shape = sum(abs((first[index] - mean_first) - (second[index] - mean_second))
                for index in range(size)) / (size * (OBJECT_PATCH_GRAY_QUANTIZATION - 1))
    hue = sum(first[size + index] != second[size + index] for index in range(size)) / size
    brightness = abs(mean_first - mean_second) / (OBJECT_PATCH_GRAY_QUANTIZATION - 1)
    return max(0.0, 1.0 - OBJECT_PATCH_SIMILARITY_SHAPE_WEIGHT * shape
               - OBJECT_PATCH_SIMILARITY_HUE_WEIGHT * hue
               - OBJECT_PATCH_SIMILARITY_BRIGHTNESS_WEIGHT * brightness)


def object_appearance(patch):
    try:
        data = bytes.fromhex(patch)
    except (ValueError, TypeError):
        return ""
    side = OBJECT_PATCH_SIDE
    size = side * side
    if len(data) != size * 2:
        return ""
    contrast = object_patch_contrast(data)
    if contrast < OBJECT_PATCH_MIN_CONTRAST:
        return ""
    mean = sum(data[:size]) / size
    levels = []
    grid = OBJECT_PATCH_APPEARANCE_GRID
    for row in range(grid):
        for column in range(grid):
            pixels = [data[py * side + px]
                      for py in range(row * side // grid, (row + 1) * side // grid)
                      for px in range(column * side // grid, (column + 1) * side // grid)]
            value = sum(pixels) / len(pixels)
            levels.append("0" if value < mean - OBJECT_PATCH_APPEARANCE_BAND
                          else "2" if value > mean + OBJECT_PATCH_APPEARANCE_BAND else "1")
    hue_counts = [data[size:].count(hue) for hue in range(OBJECT_PATCH_APPEARANCE_HUE_LEVELS)]
    dominant = max(range(1, OBJECT_PATCH_APPEARANCE_HUE_LEVELS), key=hue_counts.__getitem__)
    if hue_counts[0] >= sum(hue_counts[1:]):
        dominant = 0
    brightness = min(OBJECT_PATCH_APPEARANCE_BRIGHTNESS_LEVELS - 1,
                     int(mean * OBJECT_PATCH_APPEARANCE_BRIGHTNESS_LEVELS / OBJECT_PATCH_GRAY_QUANTIZATION))
    contrast_bucket = min(OBJECT_PATCH_APPEARANCE_CONTRAST_LEVELS - 1, int(contrast))
    return f"{brightness}{contrast_bucket}{dominant}" + "".join(levels)


def position_cell_spot(x, y):
    column = min(GRID_COLUMNS - 1, max(0, int(x * GRID_COLUMNS)))
    row = min(GRID_ROWS - 1, max(0, int(y * GRID_ROWS)))
    fine_column = min(TARGET_COLUMNS - 1, max(0, int((x * GRID_COLUMNS - column) * TARGET_COLUMNS)))
    fine_row = min(TARGET_ROWS - 1, max(0, int((y * GRID_ROWS - row) * TARGET_ROWS)))
    return row * GRID_COLUMNS + column, fine_row * TARGET_COLUMNS + fine_column


def visual_affordance_value(rows, appearance, action):
    n, total, human_n = rows.get((appearance, action), (0, 0.0, 0))
    autonomous = total / (n + VISUAL_AFFORDANCE_PRIOR_VISITS)
    human = VISUAL_AFFORDANCE_HUMAN_WEIGHT * human_n / (human_n + VISUAL_AFFORDANCE_PRIOR_VISITS)
    return max(-TD_REWARD_CEILING, min(TD_REWARD_CEILING, autonomous + human))


class Store:
    def __init__(self, directory):
        self.folder = Path(directory)
        self.folder.mkdir(parents=True, exist_ok=True)
        self.path = self.folder / "experience.sqlite3"
        self.lock = threading.RLock()
        self.db = sqlite3.connect(self.path, timeout=DATABASE_BUSY_SECONDS, check_same_thread=False)
        self.last_error = ""
        self.events_since_prune = 0
        self.last_space_check = 0.0
        self.storage_paused = False
        self.history_cache = collections.OrderedDict()
        self.history_version = 0
        self.demonstration_version = 0
        self.demonstration_cache = {}
        self.model_version = 0
        self.model_cache = collections.OrderedDict()
        try:
            with self.db:
                self.db.execute("PRAGMA journal_mode=WAL")
                self.db.execute("PRAGMA synchronous=NORMAL")
                self.db.execute(f"PRAGMA wal_autocheckpoint={DB_WAL_PAGES}")
                self.db.execute(f"PRAGMA cache_size={-DB_CACHE_KIB}")
                self.db.execute("CREATE TABLE IF NOT EXISTS actions(context TEXT, action TEXT, n INTEGER, total REAL, PRIMARY KEY(context,action))")
                self.db.execute("CREATE TABLE IF NOT EXISTS visits(state TEXT PRIMARY KEY, n INTEGER)")
                self.db.execute("CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY, time TEXT, kind TEXT, payload TEXT)")
                self.db.execute("CREATE TABLE IF NOT EXISTS targets(context TEXT, cell INTEGER, action TEXT, spot INTEGER, n INTEGER, total REAL, PRIMARY KEY(context,cell,action,spot))")
                self.db.execute("CREATE TABLE IF NOT EXISTS destinations(context TEXT, cell INTEGER, action TEXT, dest_cell INTEGER, n INTEGER, total REAL, PRIMARY KEY(context,cell,action,dest_cell))")
                self.db.execute("CREATE TABLE IF NOT EXISTS q_values(context TEXT, cell INTEGER, action TEXT, n INTEGER, value REAL, PRIMARY KEY(context,cell,action))")
                self.db.execute("CREATE TABLE IF NOT EXISTS parameters(game TEXT, action TEXT, variant INTEGER, n INTEGER, total REAL, PRIMARY KEY(game,action,variant))")
                self.db.execute("CREATE TABLE IF NOT EXISTS demonstrations(id INTEGER PRIMARY KEY, game TEXT NOT NULL, context TEXT NOT NULL, coarse TEXT NOT NULL, signature TEXT NOT NULL, cell INTEGER NOT NULL, spot INTEGER NOT NULL, action TEXT NOT NULL, destination INTEGER NOT NULL, variant INTEGER NOT NULL, x REAL NOT NULL, y REAL NOT NULL, to_x REAL NOT NULL, to_y REAL NOT NULL, n INTEGER NOT NULL, effect REAL NOT NULL, replay_n INTEGER NOT NULL DEFAULT 0, replay_effect REAL NOT NULL DEFAULT 0, updated TEXT NOT NULL, UNIQUE(game,signature,cell,spot,action,destination,variant))")
                self.db.execute("CREATE INDEX IF NOT EXISTS demonstrations_game_recent ON demonstrations(game,id DESC)")
                self.db.execute("CREATE INDEX IF NOT EXISTS demonstrations_scene ON demonstrations(game,coarse)")
                self.db.execute("CREATE TABLE IF NOT EXISTS demonstration_sequences(game TEXT NOT NULL, previous_id INTEGER NOT NULL, next_id INTEGER NOT NULL, n INTEGER NOT NULL, PRIMARY KEY(game,previous_id,next_id))")
                self.db.execute("CREATE TABLE IF NOT EXISTS learned_aims(context TEXT NOT NULL, cell INTEGER NOT NULL, spot INTEGER NOT NULL, action TEXT NOT NULL, n INTEGER NOT NULL, strength REAL NOT NULL, weighted_x REAL NOT NULL, weighted_y REAL NOT NULL, PRIMARY KEY(context,cell,spot,action))")
                self.db.execute("CREATE TABLE IF NOT EXISTS visual_affordances(game TEXT NOT NULL, appearance TEXT NOT NULL, action TEXT NOT NULL, n INTEGER NOT NULL DEFAULT 0, total REAL NOT NULL DEFAULT 0, human_n INTEGER NOT NULL DEFAULT 0, PRIMARY KEY(game,appearance,action))")
                self.db.execute("CREATE TABLE IF NOT EXISTS scene_transitions(context TEXT NOT NULL, cell INTEGER NOT NULL, action TEXT NOT NULL, next_context TEXT NOT NULL, n INTEGER NOT NULL, total REAL NOT NULL, PRIMARY KEY(context,cell,action,next_context))")
                self.db.execute("CREATE TABLE IF NOT EXISTS behavioral_transitions(game TEXT NOT NULL, context TEXT NOT NULL, cell INTEGER NOT NULL, action TEXT NOT NULL, next_context TEXT NOT NULL, human_n INTEGER NOT NULL DEFAULT 0, agent_n INTEGER NOT NULL DEFAULT 0, human_effect REAL NOT NULL DEFAULT 0, agent_reward REAL NOT NULL DEFAULT 0, PRIMARY KEY(game,context,cell,action,next_context))")
                self.db.execute("CREATE INDEX IF NOT EXISTS behavioral_transitions_by_game ON behavioral_transitions(game)")
                columns = {entry[1] for entry in self.db.execute("PRAGMA table_info(demonstrations)")}
                for name in ("local_signature", "next_signature", "next_coarse", "next_local_signature", "path", "anchor_patch", "destination_patch"):
                    if name not in columns:
                        self.db.execute(f"ALTER TABLE demonstrations ADD COLUMN {name} TEXT NOT NULL DEFAULT ''")
                if "duration" not in columns:
                    self.db.execute("ALTER TABLE demonstrations ADD COLUMN duration REAL NOT NULL DEFAULT 0")
                if self.db.execute("SELECT 1 FROM behavioral_transitions LIMIT 1").fetchone() is None:
                    self.db.execute(
                        "INSERT INTO behavioral_transitions(game,context,cell,action,next_context,human_n,human_effect) "
                        "SELECT game,coarse,cell,action,next_coarse,SUM(n),SUM(effect) "
                        "FROM demonstrations WHERE coarse<>'' AND next_coarse<>'' "
                        "GROUP BY game,coarse,cell,action,next_coarse"
                    )
                    self.db.execute(
                        "INSERT INTO behavioral_transitions(game,context,cell,action,next_context,agent_n,agent_reward) "
                        "SELECT substr(context,1,instr(context,'-')-1),context,cell,action,next_context,n,total "
                        "FROM scene_transitions WHERE instr(context,'-')>0 "
                        "ON CONFLICT(game,context,cell,action,next_context) "
                        "DO UPDATE SET agent_n=excluded.agent_n,agent_reward=excluded.agent_reward"
                    )
        except Exception:
            self.db.close()
            raise

    def can_record(self):
        current = time.monotonic()
        if current - self.last_space_check >= STORAGE_CHECK_SECONDS:
            self.last_space_check = current
            try:
                self.storage_paused = shutil.disk_usage(self.folder).free < MIN_FREE_SPACE_BYTES
            except OSError:
                self.storage_paused = True
            if self.storage_paused:
                self.last_error = "存储设备剩余空间过低，已暂停写入记录；Agent 仍会继续操作"
        return not self.storage_paused

    def event(self, kind, content):
        try:
            if not self.can_record():
                return
            with self.lock, self.db:
                self.db.execute("INSERT INTO events(time,kind,payload) VALUES(?,?,?)", (utc_stamp(), kind, json.dumps(content, ensure_ascii=False)))
                self.events_since_prune += 1
                if self.events_since_prune >= EVENT_PRUNE_INTERVAL:
                    self.events_since_prune = 0
                    self.db.execute("DELETE FROM events WHERE id < (SELECT MAX(id) FROM events) - ?", (EVENT_RETENTION_COUNT,))
        except Exception as error:
            self.last_error = str(error)

    def history(self, context, coarse_context=None):
        cache_key = (context, coarse_context)
        game = context.rsplit("-", 1)[0]
        with self.lock:
            cached = self.history_cache.get(cache_key)
            if cached is not None and self.history_version - cached[0] <= STORE_HISTORY_CACHE_AGE_STEPS:
                self.history_cache.move_to_end(cache_key)
                data = cached[1]
                return (dict(data[0]), *data[1:])
        prefix = "v2/C/" + context + "/"
        local = {}
        coarse = {}
        global_cells = {}
        global_actions = {}
        with self.lock:
            local_rows = self.db.execute(
                "SELECT context,action,n,total FROM actions WHERE context GLOB ?", (prefix + "*",)
            ).fetchall()
            for key, action, count, total in local_rows:
                suffix = key[len(prefix):]
                if suffix.isdigit():
                    local[(int(suffix), action)] = (count, total)
            if coarse_context is not None:
                coarse_prefix = "v2/B/" + coarse_context + "/"
                coarse_rows = self.db.execute(
                    "SELECT context,action,n,total FROM actions WHERE context GLOB ?", (coarse_prefix + "*",)
                ).fetchall()
                for key, action, count, total in coarse_rows:
                    suffix = key[len(coarse_prefix):]
                    if suffix.isdigit():
                        coarse[(int(suffix), action)] = (count, total)
            general_rows = self.db.execute(
                "SELECT context,action,n,total FROM actions WHERE context GLOB ?", (f"v3/G/{game}/*",)
            ).fetchall()
            for key, action, count, total in general_rows:
                suffix = key[len(f"v3/G/{game}/"):]
                if suffix.isdigit():
                    global_cells[(int(suffix), action)] = (count, total)
            global_rows = self.db.execute(
                "SELECT action,n,total FROM actions WHERE context=?", ("v3/A/" + game,)
            ).fetchall()
            global_actions = {action: (count, total) for action, count, total in global_rows}
            target_rows = self.db.execute(
                "SELECT cell,action,spot,n,total FROM targets WHERE context=?", (context,)
            ).fetchall()
            targets = {(cell, action, spot): (count, total) for cell, action, spot, count, total in target_rows}
            coarse_targets = {}
            if coarse_context is not None:
                target_rows = self.db.execute(
                    "SELECT cell,action,spot,n,total FROM targets WHERE context=?", ("v2/B/" + coarse_context,)
                ).fetchall()
                coarse_targets = {(cell, action, spot): (count, total) for cell, action, spot, count, total in target_rows}
            destination_rows = self.db.execute(
                "SELECT cell,action,dest_cell,n,total FROM destinations WHERE context=?", (context,)
            ).fetchall()
            destinations = {(cell, action, dest): (count, total) for cell, action, dest, count, total in destination_rows}
            coarse_destinations = {}
            if coarse_context is not None:
                destination_rows = self.db.execute(
                    "SELECT cell,action,dest_cell,n,total FROM destinations WHERE context=?", ("v2/B/" + coarse_context,)
                ).fetchall()
                coarse_destinations = {(cell, action, dest): (count, total) for cell, action, dest, count, total in destination_rows}
            values = {}
            if coarse_context is not None:
                value_rows = self.db.execute(
                    "SELECT cell,action,value FROM q_values WHERE context=?", (coarse_context,)
                ).fetchall()
                values = {(cell, action): value for cell, action, value in value_rows}
            parameter_rows = self.db.execute(
                "SELECT action,variant,n,total FROM parameters WHERE game=?", (game,)
            ).fetchall()
            parameters = {(action, variant): (count, total) for action, variant, count, total in parameter_rows}
            aim_rows = self.db.execute(
                "SELECT cell,spot,action,n,strength,weighted_x,weighted_y FROM learned_aims WHERE context=?", (context,)
            ).fetchall()
            aims = {(cell, spot, action): (n, strength, weighted_x, weighted_y)
                    for cell, spot, action, n, strength, weighted_x, weighted_y in aim_rows}
            coarse_aims = {}
            planning = {}
            if coarse_context is not None:
                aim_rows = self.db.execute(
                    "SELECT cell,spot,action,n,strength,weighted_x,weighted_y FROM learned_aims WHERE context=?",
                    ("v2/B/" + coarse_context,),
                ).fetchall()
                coarse_aims = {(cell, spot, action): (n, strength, weighted_x, weighted_y)
                               for cell, spot, action, n, strength, weighted_x, weighted_y in aim_rows}
                transitions = self.db.execute(
                    "SELECT t.cell,t.action,t.next_context,t.n,MAX(v.value) "
                    "FROM scene_transitions AS t LEFT JOIN q_values AS v ON v.context=t.next_context "
                    "WHERE t.context=? GROUP BY t.cell,t.action,t.next_context", (coarse_context,)
                ).fetchall()
                planning_totals = {}
                for cell, action, next_context, count, next_value in transitions:
                    prior_count, prior_total = planning_totals.get((cell, action), (0, 0.0))
                    planning_totals[(cell, action)] = (
                        prior_count + count, prior_total + count * max(0.0, next_value or 0.0)
                    )
                planning = {key: total / (count + ACTION_PLAN_PRIOR_VISITS)
                            for key, (count, total) in planning_totals.items()}
        data = (local, coarse, global_cells, global_actions, targets, coarse_targets,
                destinations, coarse_destinations, values, parameters, aims, coarse_aims, planning)
        with self.lock:
            self.history_cache[cache_key] = (self.history_version, data)
            self.history_cache.move_to_end(cache_key)
            if len(self.history_cache) > STORE_HISTORY_CACHE_ENTRIES:
                self.history_cache.popitem(last=False)
        return (dict(local), *data[1:])

    def record_demonstration(self, game, context, coarse, signature, cell, spot, action, destination, variant, x, y, to_x, to_y, effect, previous_id=None, local_signature="", next_signature="", next_coarse="", next_local_signature="", duration=0.0, path="", next_context="", anchor_patch="", destination_patch="", appearance=""):
        if not self.can_record():
            return False
        with self.lock, self.db:
            self.db.execute(
                "INSERT INTO demonstrations(game,context,coarse,signature,cell,spot,action,destination,variant,x,y,to_x,to_y,n,effect,updated,local_signature,next_signature,next_coarse,next_local_signature,duration,path,anchor_patch,destination_patch) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,1,?,?,?,?,?,?,?,?,?,?) "
                "ON CONFLICT(game,signature,cell,spot,action,destination,variant) DO UPDATE SET "
                "n=demonstrations.n+1,context=excluded.context,coarse=excluded.coarse,updated=excluded.updated,"
                "local_signature=excluded.local_signature,next_signature=excluded.next_signature,"
                "next_coarse=excluded.next_coarse,next_local_signature=excluded.next_local_signature, "
                "duration=(demonstrations.duration*demonstrations.n+excluded.duration)/(demonstrations.n+1), "
                "x=(demonstrations.x*demonstrations.n+excluded.x)/(demonstrations.n+1), "
                "y=(demonstrations.y*demonstrations.n+excluded.y)/(demonstrations.n+1), "
                "to_x=(demonstrations.to_x*demonstrations.n+excluded.to_x)/(demonstrations.n+1), "
                "to_y=(demonstrations.to_y*demonstrations.n+excluded.to_y)/(demonstrations.n+1), "
                "path=CASE WHEN excluded.path<>'' THEN excluded.path ELSE demonstrations.path END, "
                "anchor_patch=CASE WHEN excluded.anchor_patch<>'' THEN excluded.anchor_patch ELSE demonstrations.anchor_patch END, "
                "destination_patch=CASE WHEN excluded.destination_patch<>'' THEN excluded.destination_patch ELSE demonstrations.destination_patch END, "
                "effect=demonstrations.effect+excluded.effect",
                (game, context, coarse, signature, cell, spot, action, destination, variant,
                 x, y, to_x, to_y, min(1.0, max(0.0, effect)), utc_stamp(),
                 local_signature, next_signature, next_coarse, next_local_signature,
                 duration if math.isfinite(duration) and duration > 0.0 else 0.0,
                 path if isinstance(path, str) and len(path) <= DEMONSTRATION_PATH_MAX_BYTES else "",
                 anchor_patch, destination_patch),
            )
            observation_id = self.db.execute(
                "SELECT id FROM demonstrations WHERE game=? AND signature=? AND cell=? AND spot=? AND action=? AND destination=? AND variant=?",
                (game, signature, cell, spot, action, destination, variant),
            ).fetchone()[0]
            if previous_id is not None:
                self.db.execute(
                    "INSERT INTO demonstration_sequences(game,previous_id,next_id,n) VALUES(?,?,?,1) "
                    "ON CONFLICT(game,previous_id,next_id) DO UPDATE SET n=n+1",
                    (game, previous_id, observation_id),
                )
            if coarse and next_coarse:
                self.db.execute(
                    "INSERT INTO behavioral_transitions(game,context,cell,action,next_context,human_n,human_effect) "
                    "VALUES(?,?,?,?,?,1,?) ON CONFLICT(game,context,cell,action,next_context) "
                    "DO UPDATE SET human_n=human_n+1,human_effect=human_effect+excluded.human_effect",
                    (game, coarse, cell, action, next_coarse, min(1.0, max(0.0, effect))),
                )
            if context and next_context:
                self.db.execute(
                    "INSERT INTO behavioral_transitions(game,context,cell,action,next_context,human_n,human_effect) "
                    "VALUES(?,?,?,?,?,1,?) ON CONFLICT(game,context,cell,action,next_context) "
                    "DO UPDATE SET human_n=human_n+1,human_effect=human_effect+excluded.human_effect",
                    (game, context, cell, action, next_context, min(1.0, max(0.0, effect))),
                )
            if appearance:
                self.db.execute(
                    "INSERT INTO visual_affordances(game,appearance,action,human_n) VALUES(?,?,?,1) "
                    "ON CONFLICT(game,appearance,action) DO UPDATE SET human_n=human_n+1",
                    (game, appearance, action),
                )
            self.demonstration_version += 1
            self.demonstration_cache.pop(game, None)
            self.model_version += 1
            self.model_cache.pop(game, None)
        return observation_id

    def demonstration_counts(self):
        with self.lock:
            return self.db.execute("SELECT COALESCE(SUM(n),0), COUNT(*) FROM demonstrations").fetchone()

    def demonstration_examples(self, game, context, coarse):
        with self.lock:
            cached = self.demonstration_cache.get(game)
            if cached is None or cached[0] != self.demonstration_version:
                recent = self.db.execute(
                    "SELECT id,context,coarse,signature,cell,spot,action,destination,variant,x,y,to_x,to_y,n,effect,replay_n,replay_effect,local_signature,next_signature,next_coarse,next_local_signature,duration,path,anchor_patch,destination_patch "
                    "FROM demonstrations WHERE game=? ORDER BY id DESC LIMIT ?",
                    (game, DEMONSTRATION_RECENT_LIMIT),
                ).fetchall()
                priors = self.db.execute(
                    "SELECT cell,action,SUM(n) FROM demonstrations WHERE game=? GROUP BY cell,action",
                    (game,),
                ).fetchall()
                cached = (self.demonstration_version, recent, {(cell, action): count for cell, action, count in priors})
                self.demonstration_cache[game] = cached
            rows = self.db.execute(
                "SELECT id,context,coarse,signature,cell,spot,action,destination,variant,x,y,to_x,to_y,n,effect,replay_n,replay_effect,local_signature,next_signature,next_coarse,next_local_signature,duration,path,anchor_patch,destination_patch "
                "FROM demonstrations WHERE game=? AND (context=? OR coarse=?) ORDER BY CASE WHEN context=? THEN 0 ELSE 1 END, n DESC LIMIT ?",
                (game, context, coarse, context, DEMONSTRATION_MATCH_LIMIT),
            ).fetchall()
            return list(dict.fromkeys(rows + cached[1])), dict(cached[2])

    def appearance_history(self, game, appearances):
        keys = tuple(sorted(set(appearance for appearance in appearances if appearance)))
        if not keys:
            return {}
        placeholders = ",".join("?" for _ in keys)
        with self.lock:
            rows = self.db.execute(
                "SELECT appearance,action,n,total,human_n FROM visual_affordances "
                "WHERE game=? AND appearance IN (" + placeholders + ")",
                (game, *keys),
            ).fetchall()
        return {(appearance, action): (n, total, human_n)
                for appearance, action, n, total, human_n in rows}

    def demonstration_successors(self, game, previous_id):
        if previous_id is None:
            return {}
        with self.lock:
            rows = self.db.execute(
                "SELECT next_id,n FROM demonstration_sequences WHERE game=? AND previous_id=?",
                (game, previous_id),
            ).fetchall()
        return dict(rows)

    def behavioral_plan(self, game, context, exact_context=None):
        def select(plans):
            broad = plans.get(context, {})
            if exact_context is None:
                return dict(broad)
            result = {choice: MODEL_COARSE_BACKOFF_WEIGHT * score
                      for choice, score in broad.items()}
            for choice, score in plans.get(exact_context, {}).items():
                result[choice] = min(MODEL_VALUE_LIMIT,
                                     score + MODEL_COARSE_BACKOFF_WEIGHT * broad.get(choice, 0.0))
            return result
        with self.lock:
            cached = self.model_cache.get(game)
            if cached is not None and self.model_version - cached[0] < MODEL_REFRESH_ACTIONS:
                self.model_cache.move_to_end(game)
                return select(cached[1])
            rows = self.db.execute(
                "SELECT context,cell,action,next_context,human_n,agent_n,human_effect,agent_reward "
                "FROM behavioral_transitions WHERE game=? "
                "ORDER BY human_n DESC,agent_n DESC LIMIT ?",
                (game, MODEL_MAX_EDGES),
            ).fetchall()
            version = self.model_version
        transitions = collections.defaultdict(lambda: collections.defaultdict(list))
        for source, cell, action, destination, human_n, agent_n, human_effect, agent_reward in rows:
            if action not in MOUSE_ACTIONS or not 0 <= cell < GRID_COLUMNS * GRID_ROWS:
                continue
            human_strength = human_n / (human_n + MODEL_HUMAN_CONFIDENCE_PRIOR) if human_n else 0.0
            demonstration_reward = MODEL_HUMAN_REWARD * human_strength
            if human_n:
                demonstration_reward *= 1.0 + MODEL_HUMAN_EFFECT_WEIGHT * human_effect / human_n
                if source == destination and human_effect / human_n <= VISUAL_EFFECT_THRESHOLD:
                    demonstration_reward *= MODEL_HUMAN_STATIC_FACTOR
            autonomous_reward = MODEL_AGENT_REWARD_WEIGHT * agent_reward / agent_n if agent_n else 0.0
            penalty = (MODEL_SELF_LOOP_PENALTY * agent_n / (human_n + agent_n)
                       if source == destination and agent_n else 0.0)
            probability_weight = human_n * MODEL_HUMAN_COUNT_WEIGHT + agent_n
            transitions[source][(cell, action)].append(
                (destination, probability_weight, demonstration_reward + autonomous_reward - penalty)
            )
        values = {}
        for _ in range(MODEL_VALUE_ITERATIONS):
            updated = {}
            maximum_change = 0.0
            for source, actions in transitions.items():
                candidates = []
                for edges in actions.values():
                    total = sum(edge[1] for edge in edges)
                    if total:
                        score = sum(weight * (reward + MODEL_DISCOUNT * values.get(destination, 0.0))
                                    for destination, weight, reward in edges) / total
                        candidates.append(score)
                updated[source] = min(MODEL_VALUE_LIMIT, max(0.0, max(candidates, default=0.0)))
                maximum_change = max(maximum_change, abs(updated[source] - values.get(source, 0.0)))
            values = updated
            if maximum_change <= MODEL_VALUE_TOLERANCE:
                break
        plans = {}
        for source, actions in transitions.items():
            plans[source] = {}
            for choice, edges in actions.items():
                total = sum(edge[1] for edge in edges)
                if total:
                    score = sum(weight * (reward + MODEL_DISCOUNT * values.get(destination, 0.0))
                                for destination, weight, reward in edges) / total
                    plans[source][choice] = min(MODEL_VALUE_LIMIT, max(-MODEL_VALUE_LIMIT, score))
        with self.lock:
            if self.model_version == version:
                self.model_cache[game] = (version, plans)
                self.model_cache.move_to_end(game)
                if len(self.model_cache) > MODEL_MAX_CACHED_GAMES:
                    self.model_cache.popitem(last=False)
        return select(plans)

    def learn(self, context, cell, spot, action, state, effect, coarse_context=None, scene_transition=False, to_cell=None, next_coarse_context=None, cyclic_state=False, variant=None, game_id=None, trace=(), demonstration_id=None, x=None, y=None, goal_feedback=None, next_context=None, appearance=""):
        if not self.can_record():
            raise sqlite3.OperationalError(self.last_error)
        if game_id is None:
            game_id = context.rsplit("-", 1)[0]
        with self.lock, self.db:
            self.db.execute("INSERT INTO visits(state,n) VALUES(?,1) ON CONFLICT(state) DO UPDATE SET n=n+1", (state,))
            visits = self.db.execute("SELECT n FROM visits WHERE state=?", (state,)).fetchone()[0]
            intrinsic_reward = math.tanh(
                effect * VISUAL_CHANGE_SCALE
                + (VISUAL_NOVELTY_BONUS / math.sqrt(visits) if effect > VISUAL_EFFECT_THRESHOLD else -VISUAL_QUIET_PENALTY)
                + (VISUAL_SCENE_TRANSITION_BONUS if scene_transition else 0.0)
                - (STATE_CYCLE_PENALTY if cyclic_state and not scene_transition else 0.0))
            reward = intrinsic_reward if goal_feedback is None else (
                (1.0 - DEMONSTRATION_GOAL_REWARD_SHARE) * intrinsic_reward
                + DEMONSTRATION_GOAL_REWARD_SHARE * goal_feedback
            )
            if appearance:
                self.db.execute(
                    "INSERT INTO visual_affordances(game,appearance,action,n,total) VALUES(?,?,?,1,?) "
                    "ON CONFLICT(game,appearance,action) DO UPDATE SET "
                    "n=n+1,total=total+excluded.total",
                    (game_id, appearance, action, reward),
                )
            keys = [f"v2/C/{context}/{cell}", f"v3/G/{game_id}/{cell}", f"v3/A/{game_id}"]
            if coarse_context is not None:
                keys.append(f"v2/B/{coarse_context}/{cell}")
            for key in keys:
                self.db.execute(
                    "INSERT INTO actions(context,action,n,total) VALUES(?,?,1,?) "
                    "ON CONFLICT(context,action) DO UPDATE SET n=n+1,total=total+excluded.total",
                    (key, action, reward),
                )
            self.db.execute(
                "INSERT INTO targets(context,cell,action,spot,n,total) VALUES(?,?,?,?,1,?) "
                "ON CONFLICT(context,cell,action,spot) DO UPDATE SET n=n+1,total=total+excluded.total",
                (context, cell, action, spot, reward),
            )
            if coarse_context is not None:
                self.db.execute(
                    "INSERT INTO targets(context,cell,action,spot,n,total) VALUES(?,?,?,?,1,?) "
                    "ON CONFLICT(context,cell,action,spot) DO UPDATE SET n=n+1,total=total+excluded.total",
                    ("v2/B/" + coarse_context, cell, action, spot, reward),
                )
            if to_cell is not None and action in ACTION_DESTINATION_ACTIONS:
                keys = [context]
                if coarse_context is not None:
                    keys.append("v2/B/" + coarse_context)
                for key in keys:
                    self.db.execute(
                        "INSERT INTO destinations(context,cell,action,dest_cell,n,total) VALUES(?,?,?,?,1,?) "
                        "ON CONFLICT(context,cell,action,dest_cell) DO UPDATE SET n=n+1,total=total+excluded.total",
                        (key, cell, action, to_cell, reward),
                    )
            if game_id is not None and variant is not None:
                self.db.execute(
                    "INSERT INTO parameters(game,action,variant,n,total) VALUES(?,?,?,1,?) "
                    "ON CONFLICT(game,action,variant) DO UPDATE SET n=n+1,total=total+excluded.total",
                    (game_id, action, variant, reward)
                )
            if coarse_context is not None and next_coarse_context is not None:
                self.db.execute(
                    "INSERT INTO scene_transitions(context,cell,action,next_context,n,total) "
                    "VALUES(?,?,?,?,1,?) ON CONFLICT(context,cell,action,next_context) "
                    "DO UPDATE SET n=n+1,total=total+excluded.total",
                    (coarse_context, cell, action, next_coarse_context, reward),
                )
                self.db.execute(
                    "INSERT INTO behavioral_transitions(game,context,cell,action,next_context,agent_n,agent_reward) "
                    "VALUES(?,?,?,?,?,1,?) ON CONFLICT(game,context,cell,action,next_context) "
                    "DO UPDATE SET agent_n=agent_n+1,agent_reward=agent_reward+excluded.agent_reward",
                    (game_id, coarse_context, cell, action, next_coarse_context, reward),
                )
            if context and next_context:
                self.db.execute(
                    "INSERT INTO behavioral_transitions(game,context,cell,action,next_context,agent_n,agent_reward) "
                    "VALUES(?,?,?,?,?,1,?) ON CONFLICT(game,context,cell,action,next_context) "
                    "DO UPDATE SET agent_n=agent_n+1,agent_reward=agent_reward+excluded.agent_reward",
                    (game_id, context, cell, action, next_context, reward),
                )
            aim_strength = max(0.0, reward - ACTION_AIM_MIN_REWARD)
            if x is not None and y is not None and aim_strength:
                aim_keys = [context]
                if coarse_context is not None:
                    aim_keys.append("v2/B/" + coarse_context)
                for key in aim_keys:
                    self.db.execute(
                        "INSERT INTO learned_aims(context,cell,spot,action,n,strength,weighted_x,weighted_y) "
                        "VALUES(?,?,?,?,1,?,?,?) ON CONFLICT(context,cell,spot,action) "
                        "DO UPDATE SET n=n+1,strength=strength+excluded.strength,"
                        "weighted_x=weighted_x+excluded.weighted_x,weighted_y=weighted_y+excluded.weighted_y",
                        (key, cell, spot, action, aim_strength, aim_strength * x, aim_strength * y),
                    )
            q_value = None
            if coarse_context is not None and next_coarse_context is not None:
                row = self.db.execute(
                    "SELECT n,value FROM q_values WHERE context=? AND cell=? AND action=?",
                    (coarse_context, cell, action)
                ).fetchone()
                count, old_value = row if row else (0, 0.0)
                next_row = self.db.execute(
                    "SELECT MAX(value) FROM q_values WHERE context=?", (next_coarse_context,)
                ).fetchone()
                next_best = max(0.0, next_row[0] or 0.0)
                immediate = min(TD_REWARD_CEILING, max(-TD_REWARD_CEILING, reward))
                target = (1.0 - TD_DISCOUNT) * immediate + TD_DISCOUNT * next_best
                learning_rate = TD_LEARNING_RATE / (1.0 + TD_LEARNING_RATE_DECAY * math.sqrt(count))
                value = min(TD_REWARD_CEILING, max(-TD_REWARD_CEILING, old_value + learning_rate * (target - old_value)))
                q_value = value
                self.db.execute(
                    "INSERT INTO q_values(context,cell,action,n,value) VALUES(?,?,?,1,?) "
                    "ON CONFLICT(context,cell,action) DO UPDATE SET n=n+1,value=excluded.value",
                    (coarse_context, cell, action, value)
                )
            if demonstration_id is not None:
                self.db.execute(
                    "UPDATE demonstrations SET replay_n=replay_n+1,replay_effect=replay_effect+? WHERE id=?",
                    (reward, demonstration_id),
                )
            trace_values = {}
            if trace and scene_transition and not cyclic_state and reward >= TD_TRACE_MIN_PROGRESS:
                for age, (trace_context, trace_cell, trace_action) in enumerate(reversed(tuple(trace)), 1):
                    existing = self.db.execute(
                        "SELECT value FROM q_values WHERE context=? AND cell=? AND action=?",
                        (trace_context, trace_cell, trace_action)
                    ).fetchone()
                    old = existing[0] if existing else 0.0
                    credit = min(TD_REWARD_CEILING, max(-TD_REWARD_CEILING,
                                 old + TD_TRACE_CREDIT * (TD_TRACE_DECAY ** age) * reward * (TD_REWARD_CEILING - old)))
                    self.db.execute(
                        "INSERT INTO q_values(context,cell,action,n,value) VALUES(?,?,?,1,?) "
                        "ON CONFLICT(context,cell,action) DO UPDATE SET n=n+1,value=excluded.value",
                        (trace_context, trace_cell, trace_action, credit)
                    )
                    trace_values[(trace_context, trace_cell, trace_action)] = credit
        with self.lock:
            self.history_version += 1
            if coarse_context is not None and next_coarse_context is not None or context and next_context:
                self.model_version += 1
            if demonstration_id is not None:
                cached = self.demonstration_cache.get(game_id)
                if cached is not None:
                    recent = []
                    for example in cached[1]:
                        if example[0] == demonstration_id:
                            example = (*example[:15], example[15] + 1, example[16] + reward, *example[17:])
                        recent.append(example)
                    self.demonstration_cache[game_id] = (cached[0], recent, cached[2])
            def increment(mapping, key):
                count, total = mapping.get(key, (0, 0.0))
                mapping[key] = count + 1, total + reward
            for (cached_context, cached_coarse), (_, data) in self.history_cache.items():
                local, coarse, general, overall, targets, coarse_targets, destinations, coarse_destinations, values, parameters, aims, coarse_aims, planning = data
                if cached_context.startswith(game_id + "-"):
                    increment(general, (cell, action))
                    increment(overall, action)
                if cached_context == context:
                    increment(local, (cell, action))
                    increment(targets, (cell, action, spot))
                    if to_cell is not None and action in ACTION_DESTINATION_ACTIONS:
                        increment(destinations, (cell, action, to_cell))
                if coarse_context is not None and cached_coarse == coarse_context:
                    increment(coarse, (cell, action))
                    increment(coarse_targets, (cell, action, spot))
                    if to_cell is not None and action in ACTION_DESTINATION_ACTIONS:
                        increment(coarse_destinations, (cell, action, to_cell))
                    if q_value is not None:
                        values[(cell, action)] = q_value
                for (trace_context, trace_cell, trace_action), trace_value in trace_values.items():
                    if cached_coarse == trace_context:
                        values[(trace_cell, trace_action)] = trace_value
                if game_id is not None and variant is not None and cached_context.startswith(game_id + "-"):
                    increment(parameters, (action, variant))
                if aim_strength and x is not None and y is not None:
                    if cached_context == context:
                        n, weight, wx, wy = aims.get((cell, spot, action), (0, 0.0, 0.0, 0.0))
                        aims[(cell, spot, action)] = (n + 1, weight + aim_strength,
                                                      wx + x * aim_strength, wy + y * aim_strength)
                    if coarse_context is not None and cached_coarse == coarse_context:
                        n, weight, wx, wy = coarse_aims.get((cell, spot, action), (0, 0.0, 0.0, 0.0))
                        coarse_aims[(cell, spot, action)] = (n + 1, weight + aim_strength,
                                                             wx + x * aim_strength, wy + y * aim_strength)
        return reward, visits

    def counts(self):
        with self.lock:
            states = self.db.execute("SELECT COUNT(*) FROM visits").fetchone()[0]
            actions = self.db.execute("SELECT COALESCE(SUM(n),0) FROM actions WHERE context='v2/A' OR context GLOB 'v3/A/*'").fetchone()[0]
        return states, actions

    def behavioral_counts(self):
        with self.lock:
            return self.db.execute(
                "SELECT COUNT(*),COALESCE(SUM(human_n),0),COALESCE(SUM(agent_n),0) "
                "FROM behavioral_transitions"
            ).fetchone()

    def export(self, desktop, info, preview):
        snapshot = self.folder / ("snapshot-" + uuid.uuid4().hex + ".sqlite3")
        target = Path(desktop) / ("Agent黑匣子-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + "-" + uuid.uuid4().hex + ".zip")
        partial = target.with_suffix(".zip.part")
        try:
            with self.lock:
                backup = sqlite3.connect(snapshot)
                try:
                    self.db.backup(backup)
                finally:
                    backup.close()
                recent = self.db.execute(
                    "SELECT time,kind,payload FROM events ORDER BY id DESC LIMIT ?",
                    (BLACKBOX_RECENT_EVENT_LIMIT,)
                ).fetchall()
            events = []
            for stamp, kind, payload in reversed(recent):
                try:
                    content = json.loads(payload)
                except (ValueError, TypeError):
                    content = payload
                events.append(json.dumps({"time": stamp, "kind": kind, "payload": content}, ensure_ascii=False) + "\n")
            with zipfile.ZipFile(partial, "w", compression=zipfile.ZIP_DEFLATED) as archive:
                archive.write(snapshot, "experience.sqlite3")
                archive.writestr("runtime.json", json.dumps(info, ensure_ascii=False, indent=BLACKBOX_JSON_INDENT))
                archive.writestr("recent_events.jsonl", "".join(events))
                archive.write(Path(__file__), Path(__file__).name)
                if preview:
                    archive.writestr("last_capture.ppm", preview)
            os.replace(partial, target)
            return target
        finally:
            snapshot.unlink(missing_ok=True)
            partial.unlink(missing_ok=True)

    def close(self):
        with self.lock:
            self.db.close()


class AcceleratorManager:
    def __init__(self, folder, store, events, canceled, generation):
        self.folder = Path(folder)
        self.store = store
        self.events = events
        self.canceled = canceled
        self.generation = generation
        self.package_dir = self.folder / "dependencies" / ("numpy-" + python_abi())

    def report(self, stage, message, percent=None):
        if not self.canceled.is_set():
            self.events.put(("accelerator", (self.generation, stage, message, percent)))
            self.store.event("accelerator", {"stage": stage, "message": message, "percent": percent})

    def load(self, site=None):
        global NUMPY_ACCELERATOR
        if self.canceled.is_set():
            return False
        with NUMPY_IMPORT_LOCK:
            if NUMPY_ACCELERATOR is not None:
                return True
            inserted = False
            if site is not None and str(site) not in sys.path:
                sys.path.insert(0, str(site))
                inserted = True
            try:
                candidate = importlib.import_module(ACCELERATOR_NAME)
                sample = bytes((COLOR_CHANNEL_RED_WEIGHT, COLOR_CHANNEL_GREEN_WEIGHT, COLOR_CHANNEL_BLUE_WEIGHT))
                test = candidate.frombuffer(sample, dtype=candidate.uint8)
                if int(test.sum()) != sum(sample):
                    raise RuntimeError("NumPy 自检失败")
                NUMPY_ACCELERATOR = candidate
                return True
            except Exception:
                if inserted:
                    sys.path.remove(str(site))
                for name in tuple(sys.modules):
                    if name == ACCELERATOR_NAME or name.startswith(ACCELERATOR_NAME + "."):
                        sys.modules.pop(name, None)
                return False

    def metadata(self):
        request = urllib.request.Request(ACCELERATOR_METADATA_URL, headers={"Accept": "application/json", "User-Agent": "MouseGameAgent/1"})
        with urllib.request.urlopen(request, timeout=ACCELERATOR_TIMEOUT_SECONDS) as response:
            if urllib.parse.urlsplit(response.geturl()).hostname != "pypi.org":
                raise OSError("软件包元数据地址不可信")
            raw = response.read(ACCELERATOR_METADATA_MAX_BYTES + 1)
            if len(raw) > ACCELERATOR_METADATA_MAX_BYTES:
                raise OSError("软件包元数据过大")
        metadata = json.loads(raw)
        info = metadata.get("info") if isinstance(metadata, dict) else None
        if not isinstance(info, dict) or info.get("name", "").lower() != ACCELERATOR_NAME:
            raise OSError("软件包元数据格式不正确")
        if not isinstance(metadata.get("releases"), dict):
            raise OSError("软件包版本列表无效")
        return metadata

    def choose_wheel(self, metadata):
        if sys.implementation.name != "cpython":
            raise OSError("没有可匹配的 CPython 加速包；将使用内置视觉处理")
        python_tag = "cp" + str(sys.version_info.major) + str(sys.version_info.minor)
        suffix = "-" + python_tag + "-" + python_abi() + "-win_amd64.whl"
        versions = metadata.get("releases", {})
        candidates = sorted((version for version in versions if re.fullmatch(r"\d+(?:\.\d+)*", version)),
                            key=lambda version: tuple(int(part) for part in version.split(".")), reverse=True)
        for version in candidates:
            files = versions[version]
            if not isinstance(files, list):
                continue
            for file in files:
                if not isinstance(file, dict):
                    continue
                name = file.get("filename", "")
                digests = file.get("digests")
                if not isinstance(name, str) or not isinstance(digests, dict):
                    continue
                sha256 = digests.get("sha256", "")
                size = file.get("size", 0)
                if (name.startswith(ACCELERATOR_NAME + "-" + version + "-")
                        and name.endswith(suffix) and file.get("packagetype") == "bdist_wheel"
                        and not file.get("yanked", False) and isinstance(size, int)
                        and 0 < size <= ACCELERATOR_ARCHIVE_MAX_BYTES
                        and isinstance(sha256, str) and len(sha256) == hashlib.sha256().digest_size * 2
                        and re.fullmatch(r"[0-9a-f]+", sha256)):
                    url = file.get("url", "")
                    if not isinstance(url, str):
                        continue
                    parsed = urllib.parse.urlsplit(url)
                    if parsed.scheme == "https" and parsed.hostname == ACCELERATOR_ARCHIVE_HOST and parsed.path.endswith("/" + name):
                        return version, file
        raise OSError("找不到当前 Python 对应的安全 Windows x64 加速包")

    def download(self, file, destination):
        size = file["size"]
        if shutil.disk_usage(self.folder).free < MIN_FREE_SPACE_BYTES + size * ACCELERATOR_DISK_MULTIPLIER:
            raise OSError("剩余空间不足，跳过可选加速下载")
        request = urllib.request.Request(file["url"], headers={"Accept-Encoding": "identity", "User-Agent": "MouseGameAgent/1"})
        digest = hashlib.sha256()
        received = 0
        last_reported = 0
        with urllib.request.urlopen(request, timeout=ACCELERATOR_TIMEOUT_SECONDS) as response:
            parsed = urllib.parse.urlsplit(response.geturl())
            if parsed.scheme != "https" or parsed.hostname != ACCELERATOR_ARCHIVE_HOST:
                raise OSError("下载跳转到了非官方地址")
            with open(destination, "wb") as stream:
                while not self.canceled.is_set():
                    chunk = response.read(ACCELERATOR_CHUNK_BYTES)
                    if not chunk:
                        break
                    received += len(chunk)
                    if received > size or received > ACCELERATOR_ARCHIVE_MAX_BYTES:
                        raise OSError("下载内容超出官方登记大小")
                    stream.write(chunk)
                    digest.update(chunk)
                    if received - last_reported >= ACCELERATOR_PROGRESS_BYTES:
                        last_reported = received
                        self.report("downloading", f"正在下载视觉加速组件：{received * PERCENT_SCALE // size}%", received * PERCENT_SCALE // size)
        if self.canceled.is_set():
            raise InterruptedError("加速下载已取消")
        if received != size or not hmac.compare_digest(digest.hexdigest(), file["digests"]["sha256"]):
            raise OSError("加速组件大小或 SHA-256 校验不正确")

    def unpack(self, archive_path, site):
        site.mkdir(parents=True, exist_ok=True)
        with zipfile.ZipFile(archive_path) as archive:
            entries = archive.infolist()
            if len(entries) > ACCELERATOR_ARCHIVE_MAX_ENTRIES:
                raise OSError("压缩包文件数过多")
            if sum(info.file_size for info in entries) > ACCELERATOR_UNPACK_MAX_BYTES:
                raise OSError("压缩包解压内容过大")
            for info in entries:
                if self.canceled.is_set():
                    raise InterruptedError("加速下载已取消")
                name = info.filename
                components = name.rstrip("/").split("/")
                top = components[0]
                trusted_top = top in ("numpy", "numpy.libs") or (top.startswith("numpy-") and top.endswith(".dist-info"))
                entry_type = stat.S_IFMT(info.external_attr >> ARCHIVE_UNIX_MODE_SHIFT)
                correct_type = (0, stat.S_IFDIR) if info.is_dir() else (0, stat.S_IFREG)
                if (not trusted_top or any(component in ("", ".", "..") for component in components)
                        or len(name) > ACCELERATOR_ARCHIVE_MAX_NAME or "\\" in name
                        or ":" in name or name.startswith("/") or entry_type not in correct_type
                        or info.flag_bits & ACCELERATOR_ARCHIVE_ENCRYPTED_FLAG):
                    raise OSError("软件包包含不安全文件或路径")
                path = site.joinpath(*components)
                if info.is_dir():
                    path.mkdir(parents=True, exist_ok=True)
                else:
                    path.parent.mkdir(parents=True, exist_ok=True)
                    with archive.open(info) as src, open(path, "wb") as dst:
                        remaining = info.file_size
                        while remaining:
                            if self.canceled.is_set():
                                raise InterruptedError("加速下载已取消")
                            chunk = src.read(min(ACCELERATOR_CHUNK_BYTES, remaining + 1))
                            if not chunk or len(chunk) > remaining:
                                raise OSError("压缩包实际解压大小异常")
                            dst.write(chunk)
                            remaining -= len(chunk)
                        if src.read(1):
                            raise OSError("压缩包内容超出声明大小")
        if not (site / "numpy" / "__init__.py").is_file():
            raise OSError("解压组件不完整")

    def run(self):
        if self.load():
            self.report("ready", "检测到可用的 NumPy，视觉处理已加速")
            return
        try:
            marker = self.package_dir / ACCELERATOR_METADATA_MARKER
            if marker.is_file() and (self.package_dir / "numpy" / "__init__.py").is_file():
                if self.load(self.package_dir):
                    self.report("ready", "已加载所选文件夹内的视觉加速组件")
                    return
                self.report("recovering", "本地加速组件不可用，正在恢复")
            self.report("checking", "一切就绪；后台正在检查可选视觉加速组件")
            metadata = self.metadata()
            version, wheel = self.choose_wheel(metadata)
            self.report("downloading", "已选择匹配的 NumPy " + version + "，开始校验下载", 0)
            self.package_dir.parent.mkdir(parents=True, exist_ok=True)
            for attempt in range(ACCELERATOR_RETRIES):
                if self.canceled.is_set():
                    return
                try:
                    with tempfile.TemporaryDirectory(prefix=".accel-", dir=self.package_dir.parent) as staging:
                        staging = Path(staging)
                        archive_path = staging / wheel["filename"]
                        self.download(wheel, archive_path)
                        site = staging / "site"
                        self.unpack(archive_path, site)
                        (site / ACCELERATOR_METADATA_MARKER).write_text(json.dumps({"name": ACCELERATOR_NAME, "version": version, "sha256": wheel["digests"]["sha256"]}), encoding="utf-8")
                        previous = staging / "previous"
                        if self.package_dir.exists():
                            os.replace(self.package_dir, previous)
                        try:
                            os.replace(site, self.package_dir)
                        except Exception:
                            if previous.exists():
                                os.replace(previous, self.package_dir)
                            raise
                    if self.load(self.package_dir):
                        self.report("ready", "NumPy " + version + " 校验通过，视觉加速已启用")
                    else:
                        self.report("fallback", "NumPy 与当前设备不兼容，已自动使用内置视觉")
                    return
                except (OSError, EOFError, zipfile.BadZipFile, InterruptedError) as error:
                    if self.canceled.is_set():
                        return
                    if attempt + 1 >= ACCELERATOR_RETRIES:
                        raise OSError(str(error)) from error
                    self.canceled.wait(ACCELERATOR_RETRY_SECONDS)
        except Exception as error:
            self.report("fallback", "下载不可用，已使用内置视觉：" + str(error))


class Frame:
    __slots__ = ("width", "height", "gray", "rgb", "bounds")

    def __init__(self, width, height, gray, rgb, bounds=None):
        self.width = width
        self.height = height
        self.gray = gray
        self.rgb = rgb
        self.bounds = bounds if bounds is not None else (0, 0, width, height)

    def ppm(self):
        return f"P6\n{self.width} {self.height}\n{COLOR_MAX}\n".encode("ascii") + self.rgb


def parse_demonstration_path(raw):
    if not isinstance(raw, str) or not raw or len(raw) > DEMONSTRATION_PATH_MAX_BYTES:
        return None
    try:
        points = json.loads(raw)
        if not isinstance(points, list) or not 2 <= len(points) <= DEMONSTRATION_PATH_MAX_POINTS:
            return None
        parsed = []
        for point in points:
            if not isinstance(point, list) or len(point) != 3:
                return None
            fraction, x, y = (float(value) for value in point)
            if (not all(map(math.isfinite, (fraction, x, y))) or not 0.0 <= fraction <= 1.0
                    or not 0.0 <= x <= 1.0 or not 0.0 <= y <= 1.0
                    or parsed and fraction <= parsed[-1][0]):
                return None
            parsed.append((fraction, x, y))
        if parsed[0][0] > MOUSE_PATH_TIME_EPSILON or parsed[-1][0] < 1.0 - MOUSE_PATH_TIME_EPSILON:
            return None
        return parsed
    except (TypeError, ValueError, OverflowError):
        return None


class VisionPolicy:
    def __init__(self, store, game_id="desktop"):
        self.store = store
        self.game_id = game_id
        self.rng = random.Random()
        self.prior = None
        self.last_cell = None
        self.last_context = None
        self.last_action = None
        self.last_effect = 0.0
        self.no_effect_steps = 0
        self.last_spot = None
        self.last_destination = None
        self.recent_spots = collections.deque(maxlen=TARGET_RECENT_WINDOW)
        self.recent_states = collections.deque(maxlen=STATE_RECENT_WINDOW)
        self.recent_decisions = collections.deque(maxlen=TD_TRACE_DEPTH)
        self.last_demonstration_id = None
        self.last_demonstration_duration = None
        self.last_demonstration_path = ""
        self.demonstration_goal = None
        self.last_goal_progress = 0.0
        self.background_ema = None
        self.fallback = collections.OrderedDict()
        self.demonstration_retarget = None
        self.transfer_goals = []

    def context(self, frame):
        levels = []
        colors = []
        stride = max(1, math.ceil(math.sqrt(frame.width * frame.height / VISION_CONTEXT_SAMPLE_BUDGET)))
        numpy = NUMPY_ACCELERATOR
        if numpy is not None:
            gray_values = numpy.frombuffer(frame.gray, dtype=numpy.uint8).reshape(frame.height, frame.width)
            rgb_values = numpy.frombuffer(frame.rgb, dtype=numpy.uint8).reshape(frame.height, frame.width, BYTES_PER_RGB_PIXEL)
        else:
            rgb = frame.rgb
        for row in range(CONTEXT_ROWS):
            y0 = frame.height * row // CONTEXT_ROWS
            y1 = frame.height * (row + 1) // CONTEXT_ROWS
            for column in range(CONTEXT_COLUMNS):
                x0 = frame.width * column // CONTEXT_COLUMNS
                x1 = frame.width * (column + 1) // CONTEXT_COLUMNS
                if numpy is not None:
                    region_gray = gray_values[y0:y1:stride, x0:x1:stride]
                    region_rgb = rgb_values[y0:y1:stride, x0:x1:stride]
                    sample = int(region_gray.sum())
                    saturation = int((region_rgb.max(axis=2).astype(numpy.int16) - region_rgb.min(axis=2)).sum())
                    total = region_gray.size
                else:
                    sample = 0
                    saturation = 0
                    total = 0
                    for y in range(y0, y1, stride):
                        start = y * frame.width
                        for x in range(x0, x1, stride):
                            index = start + x
                            sample += frame.gray[index]
                            offset = index * BYTES_PER_RGB_PIXEL
                            red, green, blue = rgb[offset], rgb[offset + 1], rgb[offset + 2]
                            saturation += max(red, green, blue) - min(red, green, blue)
                            total += 1
                levels.append(min(CONTEXT_LEVELS - 1, sample * CONTEXT_LEVELS // max(1, total * (COLOR_MAX + 1))))
                colors.append(min(CONTEXT_SATURATION_LEVELS - 1, saturation * CONTEXT_SATURATION_LEVELS // max(1, total * (COLOR_MAX + 1))))
        coarse_levels = []
        coarse_colors = []
        for row in range(COARSE_CONTEXT_ROWS):
            for column in range(COARSE_CONTEXT_COLUMNS):
                indices = [r * CONTEXT_COLUMNS + c
                           for r in range(CONTEXT_ROWS) for c in range(CONTEXT_COLUMNS)
                           if r * COARSE_CONTEXT_ROWS // CONTEXT_ROWS == row
                           and c * COARSE_CONTEXT_COLUMNS // CONTEXT_COLUMNS == column]
                average_level = sum(levels[index] for index in indices) / max(1, len(indices))
                average_color = sum(colors[index] for index in indices) / max(1, len(indices))
                coarse_levels.append(str(min(COARSE_CONTEXT_LEVELS - 1, round(average_level * (COARSE_CONTEXT_LEVELS - 1) / max(1, CONTEXT_LEVELS - 1)))))
                coarse_colors.append(str(min(COARSE_CONTEXT_SATURATION_LEVELS - 1, round(average_color * (COARSE_CONTEXT_SATURATION_LEVELS - 1) / max(1, CONTEXT_SATURATION_LEVELS - 1)))))
        exact = self.game_id + "-" + "".join(map(str, levels)) + "".join(map(str, colors))
        coarse = self.game_id + "-" + "".join(coarse_levels) + "".join(coarse_colors)
        return exact, coarse

    def reset_scene(self, game_id=None):
        if game_id is not None:
            self.game_id = game_id
        self.prior = None
        self.last_cell = None
        self.last_context = None
        self.last_action = None
        self.last_effect = 0.0
        self.no_effect_steps = 0
        self.last_spot = None
        self.last_destination = None
        self.recent_spots.clear()
        self.recent_states.clear()
        self.recent_decisions.clear()
        self.last_demonstration_id = None
        self.last_demonstration_duration = None
        self.last_demonstration_path = ""
        self.demonstration_goal = None
        self.last_goal_progress = 0.0
        self.background_ema = None
        self.demonstration_retarget = None
        self.transfer_goals = []

    def fingerprint(self, frame, region=None):
        values = []
        hue_signature = 0
        x0, y0, x1, y1 = region if region is not None else (0, 0, frame.width, frame.height)
        for row in range(FINGERPRINT_SIDE):
            y = min(frame.height - 1, y0 + (row * 2 + 1) * (y1 - y0) // (FINGERPRINT_SIDE * 2))
            for column in range(FINGERPRINT_SIDE):
                x = min(frame.width - 1, x0 + (column * 2 + 1) * (x1 - x0) // (FINGERPRINT_SIDE * 2))
                index = y * frame.width + x
                values.append(frame.gray[index])
                offset = index * BYTES_PER_RGB_PIXEL
                red, green, blue = frame.rgb[offset:offset + BYTES_PER_RGB_PIXEL]
                if max(red, green, blue) - min(red, green, blue) < COLOR_FINGERPRINT_SATURATION_THRESHOLD:
                    hue = 0
                elif red >= green and red >= blue:
                    hue = 1
                elif green >= red and green >= blue:
                    hue = 2
                else:
                    hue = FINGERPRINT_BLUE_HUE
                hue_signature |= hue << (len(values) - 1) * 2
        average = sum(values) / len(values)
        binary = sum((int(value >= average) << index) for index, value in enumerate(values))
        return f"{binary:016x}{hue_signature:032x}"

    def local_fingerprint(self, frame, cell, spot):
        grid_column, grid_row = cell % GRID_COLUMNS, cell // GRID_COLUMNS
        spot_column, spot_row = spot % TARGET_COLUMNS, spot // TARGET_COLUMNS
        center_x = (grid_column + (spot_column + COORDINATE_CENTER) / TARGET_COLUMNS) * frame.width / GRID_COLUMNS
        center_y = (grid_row + (spot_row + COORDINATE_CENTER) / TARGET_ROWS) * frame.height / GRID_ROWS
        half_width = frame.width * DEMONSTRATION_LOCAL_PATCH_SCALE / (GRID_COLUMNS * TARGET_COLUMNS * 2)
        half_height = frame.height * DEMONSTRATION_LOCAL_PATCH_SCALE / (GRID_ROWS * TARGET_ROWS * 2)
        x0 = max(0, min(frame.width - 1, round(center_x - half_width)))
        y0 = max(0, min(frame.height - 1, round(center_y - half_height)))
        x1 = max(x0 + 1, min(frame.width, round(center_x + half_width)))
        y1 = max(y0 + 1, min(frame.height, round(center_y + half_height)))
        return self.fingerprint(frame, (x0, y0, x1, y1))

    def fingerprint_distance(self, first, second):
        if not first or not second or len(first) != len(second):
            return None
        try:
            bits = (int(first[:16], 16) ^ int(second[:16], 16)).bit_count()
            bits += (int(first[16:], 16) ^ int(second[16:], 16)).bit_count()
            return bits / (FINGERPRINT_SIDE * FINGERPRINT_SIDE * (1 + 2))
        except ValueError:
            return None

    def coarse_context_distance(self, first, second):
        try:
            left = first.rsplit("-", 1)[1]
            right = second.rsplit("-", 1)[1]
            if len(left) != len(right):
                return math.inf
            return sum(abs(int(a) - int(b)) for a, b in zip(left, right))
        except (IndexError, ValueError):
            return math.inf

    def salience(self, frame):
        if NUMPY_ACCELERATOR is not None:
            return self.salience_fast(frame, NUMPY_ACCELERATOR)
        area_count = GRID_COLUMNS * GRID_ROWS
        spot_count = TARGET_COLUMNS * TARGET_ROWS
        scores = [0.0] * area_count
        counts = [0] * area_count
        fine_scores = [0.0] * (area_count * spot_count)
        fine_counts = [0] * (area_count * spot_count)
        aim_x = [0.0] * (area_count * spot_count)
        aim_y = [0.0] * (area_count * spot_count)
        aim_weights = [0.0] * (area_count * spot_count)
        last = self.prior
        has_motion = last is not None and (last.width, last.height, last.bounds) == (frame.width, frame.height, frame.bounds)
        values = frame.gray
        rgb = frame.rgb
        width = frame.width
        motion_sum = 0
        sample_count = 0
        stride = max(1, math.ceil(math.sqrt(frame.width * frame.height / VISION_SALIENCE_SAMPLE_BUDGET)))
        for y in range(stride // 2, frame.height, stride):
            row = y * width
            cell_row = min(GRID_ROWS - 1, y * GRID_ROWS // frame.height)
            y0 = cell_row * frame.height // GRID_ROWS
            y1 = (cell_row + 1) * frame.height // GRID_ROWS
            target_row = min(TARGET_ROWS - 1, (y - y0) * TARGET_ROWS // max(1, y1 - y0))
            for x in range(stride // 2, width, stride):
                index = row + x
                cell_column = min(GRID_COLUMNS - 1, x * GRID_COLUMNS // width)
                cell = cell_row * GRID_COLUMNS + cell_column
                x0 = cell_column * width // GRID_COLUMNS
                x1 = (cell_column + 1) * width // GRID_COLUMNS
                target_column = min(TARGET_COLUMNS - 1, (x - x0) * TARGET_COLUMNS // max(1, x1 - x0))
                fine_index = cell * spot_count + target_row * TARGET_COLUMNS + target_column
                value = values[index]
                edge = abs(value - values[index - 1]) if x else 0
                if y:
                    edge += abs(value - values[index - width])
                movement = abs(value - last.gray[index]) if has_motion else 0
                motion_sum += movement
                sample_count += 1
                offset = index * BYTES_PER_RGB_PIXEL
                red, green, blue = rgb[offset], rgb[offset + 1], rgb[offset + 2]
                saturation = max(red, green, blue) - min(red, green, blue)
                saturation_motion = 0
                if has_motion:
                    previous_rgb = last.rgb
                    prior_red, prior_green, prior_blue = previous_rgb[offset], previous_rgb[offset + 1], previous_rgb[offset + 2]
                    saturation_motion = abs(saturation - (max(prior_red, prior_green, prior_blue) - min(prior_red, prior_green, prior_blue)))
                energy = edge + movement * MOTION_SALIENCE_WEIGHT + saturation * COLOR_SALIENCE_WEIGHT + saturation_motion * SATURATION_CHANGE_WEIGHT
                scores[cell] += energy
                counts[cell] += 1
                fine_scores[fine_index] += energy
                fine_counts[fine_index] += 1
                aim_weight = energy + TARGET_AIM_BASE_ENERGY
                aim_x[fine_index] += (x + COORDINATE_CENTER) * aim_weight
                aim_y[fine_index] += (y + COORDINATE_CENTER) * aim_weight
                aim_weights[fine_index] += aim_weight
        typical = sum(scores) / max(1, sum(counts))
        normalized = [score / max(1, count) / max(1.0, typical) for score, count in zip(scores, counts)]
        fine = [score / max(1, count) / max(1.0, typical) for score, count in zip(fine_scores, fine_counts)]
        centers = [(x / max(1.0, weight), y / max(1.0, weight)) for x, y, weight in zip(aim_x, aim_y, aim_weights)]
        motion_level = motion_sum / max(1, sample_count * COLOR_MAX)
        return normalized, fine, centers, motion_level


    def salience_fast(self, frame, numpy):
        width, height = frame.width, frame.height
        stride = max(1, math.ceil(math.sqrt(width * height / VISION_SALIENCE_SAMPLE_BUDGET)))
        xx = numpy.arange(stride // 2, width, stride, dtype=numpy.int32)
        yy = numpy.arange(stride // 2, height, stride, dtype=numpy.int32)
        x, y = numpy.meshgrid(xx, yy)
        gray = numpy.frombuffer(frame.gray, dtype=numpy.uint8).reshape(height, width)
        rgb = numpy.frombuffer(frame.rgb, dtype=numpy.uint8).reshape(height, width, BYTES_PER_RGB_PIXEL)
        values = gray[y, x].astype(numpy.int16)
        edge = numpy.where(x > 0, numpy.abs(values - gray[y, numpy.maximum(0, x - 1)]), 0)
        edge += numpy.where(y > 0, numpy.abs(values - gray[numpy.maximum(0, y - 1), x]), 0)
        old = self.prior
        has_motion = old is not None and (old.width, old.height, old.bounds) == (width, height, frame.bounds)
        movement = numpy.zeros_like(values)
        if has_motion:
            previous_gray = numpy.frombuffer(old.gray, dtype=numpy.uint8).reshape(height, width)
            movement = numpy.abs(values - previous_gray[y, x])
        colors = rgb[y, x]
        saturation = colors.max(axis=2).astype(numpy.int16) - colors.min(axis=2)
        color_movement = numpy.zeros_like(values)
        if has_motion:
            previous_rgb = numpy.frombuffer(old.rgb, dtype=numpy.uint8).reshape(height, width, BYTES_PER_RGB_PIXEL)
            previous_colors = previous_rgb[y, x]
            previous_saturation = previous_colors.max(axis=2).astype(numpy.int16) - previous_colors.min(axis=2)
            color_movement = numpy.abs(saturation - previous_saturation)
        energy = (edge + movement * MOTION_SALIENCE_WEIGHT
                  + saturation * COLOR_SALIENCE_WEIGHT + color_movement * SATURATION_CHANGE_WEIGHT)
        cell_col = numpy.minimum(GRID_COLUMNS - 1, x * GRID_COLUMNS // width)
        cell_row = numpy.minimum(GRID_ROWS - 1, y * GRID_ROWS // height)
        cell = cell_row * GRID_COLUMNS + cell_col
        x0 = cell_col * width // GRID_COLUMNS
        x1 = (cell_col + 1) * width // GRID_COLUMNS
        y0 = cell_row * height // GRID_ROWS
        y1 = (cell_row + 1) * height // GRID_ROWS
        fine_col = numpy.minimum(TARGET_COLUMNS - 1, (x - x0) * TARGET_COLUMNS // numpy.maximum(1, x1 - x0))
        fine_row = numpy.minimum(TARGET_ROWS - 1, (y - y0) * TARGET_ROWS // numpy.maximum(1, y1 - y0))
        spot_count = TARGET_COLUMNS * TARGET_ROWS
        fine_cell = cell * spot_count + fine_row * TARGET_COLUMNS + fine_col
        cell_count = GRID_COLUMNS * GRID_ROWS
        cell_sum = numpy.bincount(cell.ravel(), weights=energy.ravel(), minlength=cell_count)
        count = numpy.bincount(cell.ravel(), minlength=cell_count)
        fine_sum = numpy.bincount(fine_cell.ravel(), weights=energy.ravel(), minlength=cell_count * spot_count)
        fine_count = numpy.bincount(fine_cell.ravel(), minlength=cell_count * spot_count)
        weights = energy + TARGET_AIM_BASE_ENERGY
        aim_x = numpy.bincount(fine_cell.ravel(), weights=((x + COORDINATE_CENTER) * weights).ravel(), minlength=cell_count * spot_count)
        aim_y = numpy.bincount(fine_cell.ravel(), weights=((y + COORDINATE_CENTER) * weights).ravel(), minlength=cell_count * spot_count)
        aim_sum = numpy.bincount(fine_cell.ravel(), weights=weights.ravel(), minlength=cell_count * spot_count)
        typical = float(cell_sum.sum() / max(1, int(count.sum())))
        normalized = (cell_sum / numpy.maximum(1, count) / max(1.0, typical)).tolist()
        fine = (fine_sum / numpy.maximum(1, fine_count) / max(1.0, typical)).tolist()
        centers = list(zip((aim_x / numpy.maximum(1.0, aim_sum)).tolist(), (aim_y / numpy.maximum(1.0, aim_sum)).tolist()))
        motion_level = float(movement.sum()) / max(1, int(movement.size) * COLOR_MAX)
        return normalized, fine, centers, motion_level

    def coordinates(self, cell, spot, frame, centers=None):
        column, row = cell % GRID_COLUMNS, cell // GRID_COLUMNS
        x0 = column * frame.width // GRID_COLUMNS
        x1 = (column + 1) * frame.width // GRID_COLUMNS
        y0 = row * frame.height // GRID_ROWS
        y1 = (row + 1) * frame.height // GRID_ROWS
        spot_column, spot_row = spot % TARGET_COLUMNS, spot // TARGET_COLUMNS
        horizontal = self.rng.uniform(-TARGET_JITTER_SPAN, TARGET_JITTER_SPAN)
        vertical = self.rng.uniform(-TARGET_JITTER_SPAN, TARGET_JITTER_SPAN)
        x = (x0 + (spot_column + COORDINATE_CENTER + horizontal / 2) * (x1 - x0) / TARGET_COLUMNS) / frame.width
        y = (y0 + (spot_row + COORDINATE_CENTER + vertical / 2) * (y1 - y0) / TARGET_ROWS) / frame.height
        if centers:
            aim_x, aim_y = centers[cell * TARGET_COLUMNS * TARGET_ROWS + spot]
            x += (aim_x / frame.width - (x0 + (spot_column + COORDINATE_CENTER) * (x1 - x0) / TARGET_COLUMNS) / frame.width) * TARGET_AIM_BLEND
            y += (aim_y / frame.height - (y0 + (spot_row + COORDINATE_CENTER) * (y1 - y0) / TARGET_ROWS) / frame.height) * TARGET_AIM_BLEND
        return min(1.0, max(0.0, x)), min(1.0, max(0.0, y))

    def locate_object(self, frame, patch, original_x, original_y, cache):
        try:
            reference = bytes.fromhex(patch)
        except (TypeError, ValueError):
            return None
        if (len(reference) != OBJECT_PATCH_SIDE * OBJECT_PATCH_SIDE * 2
                or object_patch_contrast(reference) < OBJECT_PATCH_MIN_CONTRAST):
            return None
        candidates = []
        columns = GRID_COLUMNS * TARGET_COLUMNS
        rows = GRID_ROWS * TARGET_ROWS

        def evaluate(x, y):
            x = min(1.0, max(0.0, x))
            y = min(1.0, max(0.0, y))
            point = (x, y)
            found = cache.get(point)
            if found is None:
                found = bytes.fromhex(object_patch(frame, x, y))
                cache[point] = found
            similarity = object_patch_similarity(reference, found)
            distance = math.hypot(x - original_x, y - original_y)
            rank = similarity - OBJECT_PATCH_POSITION_WEIGHT * distance
            candidate = (rank, similarity, x, y)
            candidates.append(candidate)
            return candidate

        evaluate(original_x, original_y)
        for row in range(rows):
            for column in range(columns):
                evaluate((column + COORDINATE_CENTER) / columns,
                         (row + COORDINATE_CENTER) / rows)
        candidates.sort(reverse=True)
        best_locations = candidates[:OBJECT_PATCH_REFINE_COUNT]
        for start in best_locations:
            current = start
            width_step = OBJECT_PATCH_REFINE_RATIO / columns
            height_step = OBJECT_PATCH_REFINE_RATIO / rows
            for _ in range(OBJECT_PATCH_REFINE_STEPS):
                local = [current]
                for delta_y in (-height_step, 0.0, height_step):
                    for delta_x in (-width_step, 0.0, width_step):
                        if delta_x or delta_y:
                            local.append(evaluate(current[2] + delta_x, current[3] + delta_y))
                current = max(local)
                width_step *= COORDINATE_CENTER
                height_step *= COORDINATE_CENTER
        best = max(candidates)
        if best[1] < OBJECT_PATCH_MATCH_THRESHOLD:
            return None
        return best[2], best[3], best[1]

    def choose_demonstration(self, frame, context, coarse_context):
        self.demonstration_retarget = None
        self.transfer_goals = []
        try:
            rows, priors = self.store.demonstration_examples(self.game_id, context, coarse_context)
        except sqlite3.Error as error:
            self.store.last_error = str(error)
            return None, {}
        if not rows:
            return None, priors
        try:
            successors = self.store.demonstration_successors(self.game_id, self.last_demonstration_id)
        except sqlite3.Error:
            successors = {}
        fingerprint = self.fingerprint(frame)
        visual = int(fingerprint[:16], 16)
        color = int(fingerprint[16:], 16)
        proposed = []
        for example in rows:
            (example_id, exact, coarse, signature, cell, spot, action, destination, variant,
             x, y, to_x, to_y, count, effect, replay_n, replay_effect,
             local_signature, next_signature, next_coarse, next_local_signature, duration,
             path, anchor_patch, destination_patch) = example
            if action not in MOUSE_ACTIONS or not 0 <= cell < GRID_COLUMNS * GRID_ROWS:
                continue
            try:
                shape_distance = (visual ^ int(signature[:16], 16)).bit_count()
                color_distance = (color ^ int(signature[16:], 16)).bit_count()
            except ValueError:
                continue
            if exact == context:
                global_match = (shape_distance <= DEMONSTRATION_EXACT_SHAPE_DIFFERENCE
                                and color_distance <= DEMONSTRATION_EXACT_HUE_DIFFERENCE)
                scene_bonus = DEMONSTRATION_SCENE_BONUS
            elif coarse == coarse_context:
                global_match = (shape_distance <= DEMONSTRATION_COARSE_SHAPE_DIFFERENCE
                                and color_distance <= DEMONSTRATION_COARSE_HUE_DIFFERENCE)
                scene_bonus = DEMONSTRATION_SCENE_BONUS / 2
            else:
                global_match = (shape_distance <= DEMONSTRATION_GENERAL_SHAPE_DIFFERENCE
                                and color_distance <= DEMONSTRATION_GENERAL_HUE_DIFFERENCE
                                and self.coarse_context_distance(coarse, coarse_context)
                                <= DEMONSTRATION_GENERAL_CONTEXT_DISTANCE)
                scene_bonus = 0.0
            if next_signature and signature != next_signature and next_signature == fingerprint:
                continue
            if not global_match and (not anchor_patch or
                    self.coarse_context_distance(coarse, coarse_context) > OBJECT_PATCH_MAX_COARSE_DISTANCE
                    and example_id not in successors):
                continue
            shape_similarity = max(0.0, 1.0 - shape_distance / (FINGERPRINT_SIDE * FINGERPRINT_SIDE))
            color_similarity = max(0.0, 1.0 - color_distance / (FINGERPRINT_SIDE * FINGERPRINT_SIDE * 2))
            similarity = shape_similarity * color_similarity
            mean_effect = effect / max(1, count)
            replay_quality = replay_effect / replay_n if replay_n else 0.0
            score = (similarity * DEMONSTRATION_SIMILARITY_WEIGHT + scene_bonus
                     + DEMONSTRATION_COUNT_WEIGHT * math.log1p(count)
                     + DEMONSTRATION_EFFECT_WEIGHT * mean_effect
                     + DEMONSTRATION_REPLAY_WEIGHT * replay_quality
                     + DEMONSTRATION_SEQUENCE_WEIGHT * successors.get(example_id, 0)
                     / (successors.get(example_id, 0) + DEMONSTRATION_SEQUENCE_PRIOR)
                     + self.rng.random() * DEMONSTRATION_RANDOM_NOISE)
            if not global_match:
                score -= OBJECT_PATCH_MISMATCH_PENALTY
            if replay_n:
                score -= DEMONSTRATION_FAILURE_PENALTY * max(
                    0.0, DEMONSTRATION_REPLAY_SUCCESS_REWARD - replay_quality)
            if next_signature and next_signature == fingerprint and next_coarse == coarse_context:
                score -= DEMONSTRATION_EXPECTED_NOOP_PENALTY
            proposed.append((score, example, global_match))
        if not proposed:
            return None, priors
        proposed.sort(reverse=True, key=lambda item: item[0])
        seen_goals = set()
        for _, example, global_match in proposed:
            outcome = example[18]
            if (not global_match or not outcome or outcome in seen_goals
                    or example[14] / max(1, example[13]) < DEMONSTRATION_TRANSFER_GOAL_MIN_EFFECT):
                continue
            distance = self.fingerprint_distance(fingerprint, outcome)
            if distance is None or distance < DEMONSTRATION_TRANSFER_GOAL_MIN_DISTANCE:
                continue
            seen_goals.add(outcome)
            self.transfer_goals.append(outcome)
            if len(self.transfer_goals) >= DEMONSTRATION_TRANSFER_GOAL_COUNT:
                break
        cache = {}
        matched = []
        for score, example, global_match in proposed[:OBJECT_PATCH_REPLAY_CANDIDATES]:
            (example_id, exact, coarse, signature, cell, spot, action, destination, variant,
             x, y, to_x, to_y, count, effect, replay_n, replay_effect,
             local_signature, next_signature, next_coarse, next_local_signature, duration,
             path, anchor_patch, destination_patch) = example
            target = None
            if anchor_patch:
                target = self.locate_object(frame, anchor_patch, x, y, cache)
                if target is None and not global_match:
                    continue
                if target is not None:
                    score += OBJECT_PATCH_MATCH_REWARD * target[2]
            if target is None:
                if local_signature:
                    current_local = self.local_fingerprint(frame, cell, spot)
                    try:
                        local_shape = (int(current_local[:16], 16) ^ int(local_signature[:16], 16)).bit_count()
                        local_color = (int(current_local[16:], 16) ^ int(local_signature[16:], 16)).bit_count()
                    except ValueError:
                        continue
                    if (local_shape > DEMONSTRATION_LOCAL_MAX_SHAPE_DISTANCE
                            or local_color > DEMONSTRATION_LOCAL_MAX_COLOR_DISTANCE):
                        continue
                    local_similarity = (1.0 - local_shape / (FINGERPRINT_SIDE * FINGERPRINT_SIDE))
                    local_similarity *= 1.0 - local_color / (FINGERPRINT_SIDE * FINGERPRINT_SIDE * 2)
                    score += DEMONSTRATION_LOCAL_MATCH_WEIGHT * local_similarity
                selected = (x, y, to_x, to_y)
            else:
                current_x, current_y, confidence = target
                if confidence < OBJECT_PATCH_RELOCATION_THRESHOLD and global_match:
                    current_x, current_y = x, y
                delta_x, delta_y = current_x - x, current_y - y
                destination_x = min(1.0, max(0.0, to_x + delta_x))
                destination_y = min(1.0, max(0.0, to_y + delta_y))
                if action in ACTION_DESTINATION_ACTIONS and destination_patch:
                    destination_match = self.locate_object(frame, destination_patch,
                                                           to_x, to_y, cache)
                    if destination_match and destination_match[2] >= OBJECT_PATCH_DESTINATION_THRESHOLD:
                        destination_x, destination_y = destination_match[:2]
                selected = (current_x, current_y, destination_x, destination_y)
            matched.append((score, example, selected))
        if not matched:
            return None, priors
        matched.sort(reverse=True, key=lambda item: item[0])
        options = matched[:DEMONSTRATION_MAX_CANDIDATES]
        chance = DEMONSTRATION_BASE_REPLAY_CHANCE / (
            1.0 + self.no_effect_steps * DEMONSTRATION_STAGNATION_DECAY)
        if self.rng.random() >= chance:
            return None, priors
        weights = [math.exp(score - options[0][0]) for score, _, _ in options]
        _, selected_example, selected_coordinates = self.rng.choices(options, weights=weights, k=1)[0]
        self.demonstration_retarget = selected_coordinates
        return selected_example, priors

    def pick(self, frame):
        context, coarse_context = self.context(frame)
        salient, fine, centers, motion_level = self.salience(frame)
        motion_strength = min(1.0, motion_level / ACTION_MOTION_REFERENCE)
        example, demonstrated_actions = self.choose_demonstration(frame, context, coarse_context)
        if example is not None:
            (demonstration_id, _, _, _, cell, spot, action, destination, variant,
             x, y, to_x, to_y, _, _, _, _, _, expected_signature, _, expected_local, duration, path, anchor_patch, destination_patch) = example
            if self.demonstration_retarget is not None:
                x, y, to_x, to_y = self.demonstration_retarget
                cell, spot = position_cell_spot(x, y)
                destination = position_cell_spot(to_x, to_y)[0] if action in ACTION_DESTINATION_ACTIONS else cell
            x = min(1.0, max(0.0, x))
            y = min(1.0, max(0.0, y))
            to_x = min(1.0, max(0.0, to_x))
            to_y = min(1.0, max(0.0, to_y))
            self.last_demonstration_id = demonstration_id
            self.last_demonstration_duration = duration if duration > 0.0 else None
            self.last_demonstration_path = path
            self.demonstration_goal = (demonstration_id, expected_signature, expected_local, cell, spot)
            self.last_destination = destination if destination >= 0 else cell
            self.last_cell = cell
            self.last_spot = spot
            self.last_context = context
            self.last_action = action
            self.recent_spots.append((cell, spot))
            valid_variant = (variant if action in ACTION_PARAMETERS
                             and 0 <= variant < len(ACTION_PARAMETERS[action]) else None)
            return (context, coarse_context, cell, spot, action, x, y, to_x, to_y,
                    self.last_destination, valid_variant, demonstration_id)
        self.last_demonstration_id = None
        self.last_demonstration_duration = None
        self.last_demonstration_path = ""
        self.demonstration_goal = None
        try:
            (local, coarse, general, action_history, targets, coarse_targets, destinations,
             coarse_destinations, q_values, parameters, aims, coarse_aims, planning) = self.store.history(context, coarse_context)
            behavioral_plan = self.store.behavioral_plan(self.game_id, coarse_context, context)
            for key, (count, total) in self.fallback.get(context, {}).items():
                persisted_count, persisted_total = local.get(key, (0, 0.0))
                local[key] = (persisted_count + count, persisted_total + total)
        except sqlite3.Error as error:
            self.store.last_error = str(error)
            (local, coarse, general, action_history, targets, coarse_targets, destinations,
             coarse_destinations, q_values, parameters, aims, coarse_aims, planning) = (
                self.fallback.get(context, {}), {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}
            )
            behavioral_plan = {}
        exploration = min(1.0, self.no_effect_steps / POLICY_NO_EFFECT_STEPS)
        region_visits = [sum(local.get((region, candidate), (0, 0))[0] for candidate in MOUSE_ACTIONS)
                         for region in range(GRID_COLUMNS * GRID_ROWS)]
        total_region_visits = sum(region_visits)
        total_demonstrations = sum(demonstrated_actions.values())
        region_scores = []
        for region, intensity in enumerate(salient):
            best_estimate = 0.0
            for candidate in MOUSE_ACTIONS:
                n, total = local.get((region, candidate), (0, 0.0))
                coarse_n, coarse_total = coarse.get((region, candidate), (0, 0.0))
                general_n, general_total = general.get((region, candidate), (0, 0.0))
                overall_n, overall_total = action_history.get(candidate, (0, 0.0))
                prior = (coarse_total / coarse_n if coarse_n else
                         general_total / general_n if general_n else
                         overall_total / overall_n if overall_n else 0.0)
                estimate = (total + REGION_PRIOR_VISITS * prior) / (n + REGION_PRIOR_VISITS)
                estimate += TD_ACTION_WEIGHT * q_values.get((region, candidate), 0.0)
                estimate += ACTION_PLAN_WEIGHT * planning.get((region, candidate), 0.0)
                estimate += MODEL_REGION_WEIGHT * behavioral_plan.get((region, candidate), 0.0)
                best_estimate = max(best_estimate, estimate)
            score = REGION_HISTORY_WEIGHT * best_estimate
            if total_demonstrations:
                score += DEMONSTRATION_POLICY_PRIOR_WEIGHT * sum(demonstrated_actions.get((region, a), 0) for a in MOUSE_ACTIONS) / total_demonstrations
            score += REGION_SALIENCE_WEIGHT * math.sqrt(max(0.0, intensity))
            score += REGION_EXPLORATION_WEIGHT * (1.0 + exploration * POLICY_EXPLORATION_BOOST) * math.sqrt(
                math.log(total_region_visits + len(salient) + 1) / (region_visits[region] + 1))
            if self.last_cell == region:
                repeat_factor = REGION_SUCCESS_RECENCY_FACTOR if self.last_effect >= REPEAT_EFFECT_THRESHOLD else 1.0
                score -= REGION_RECENCY_PENALTY * repeat_factor
            region_scores.append(score + self.rng.random() * REGION_SCORE_JITTER)
        if self.rng.random() < REGION_RANDOM_CHANCE + exploration * POLICY_STAGNATION_REGION_CHANCE:
            cell = self.rng.randrange(len(region_scores))
        else:
            cell = max(range(len(region_scores)), key=region_scores.__getitem__)
        spot_count = TARGET_COLUMNS * TARGET_ROWS
        spot_appearances = []
        for candidate_spot in range(spot_count):
            column = cell % GRID_COLUMNS
            row = cell // GRID_COLUMNS
            fine_column = candidate_spot % TARGET_COLUMNS
            fine_row = candidate_spot // TARGET_COLUMNS
            aim_x = (column + (fine_column + COORDINATE_CENTER) / TARGET_COLUMNS) / GRID_COLUMNS
            aim_y = (row + (fine_row + COORDINATE_CENTER) / TARGET_ROWS) / GRID_ROWS
            if centers:
                center_x, center_y = centers[cell * spot_count + candidate_spot]
                aim_x += (center_x / frame.width - aim_x) * TARGET_AIM_BLEND
                aim_y += (center_y / frame.height - aim_y) * TARGET_AIM_BLEND
            spot_appearances.append(object_appearance(object_patch(frame, aim_x, aim_y)))
        try:
            appearance_history = self.store.appearance_history(self.game_id, spot_appearances)
        except sqlite3.Error as error:
            self.store.last_error = str(error)
            appearance_history = {}
        tries = sum(local.get((cell, action), (0, 0))[0] for action in MOUSE_ACTIONS)
        candidates = []
        for action in MOUSE_ACTIONS:
            local_n, local_total = local.get((cell, action), (0, 0.0))
            coarse_n, coarse_total = coarse.get((cell, action), (0, 0.0))
            general_n, general_total = general.get((cell, action), (0, 0.0))
            overall_n, overall_total = action_history.get(action, (0, 0.0))
            local_average = local_total / local_n if local_n else 0.0
            global_average = general_total / general_n if general_n else (overall_total / overall_n if overall_n else 0.0)
            coarse_confidence = coarse_n / (coarse_n + COARSE_ACTION_PRIOR_VISITS) if coarse_n else 0.0
            coarse_average = coarse_total / coarse_n if coarse_n else global_average
            general_estimate = coarse_confidence * coarse_average + (1 - coarse_confidence) * global_average
            confidence = local_n / (local_n + GENERALIZATION_PRIOR_VISITS * GENERALIZATION_STRENGTH) if local_n else 0.0
            estimate = confidence * local_average + (1 - confidence) * general_estimate
            explore = EXPLORATION_STRENGTH * (1.0 + exploration * POLICY_EXPLORATION_BOOST) * math.sqrt(math.log(tries + len(MOUSE_ACTIONS) + 1) / (local_n + 1))
            prior = ACTION_PRIOR_WEIGHT * ACTION_PRIORS[action] / math.sqrt(local_n + 1)
            if total_demonstrations:
                human_count = demonstrated_actions.get((cell, action), 0)
                prior += DEMONSTRATION_POLICY_PRIOR_WEIGHT * math.sqrt(human_count / (total_demonstrations + DEMONSTRATION_GENERAL_PRIOR_VISITS))
            if action in ACTION_MOTION_ACTIONS:
                prior += ACTION_MOTION_PRIOR_BONUS * motion_strength / math.sqrt(local_n + 1)
            elif action in ACTION_STILL_ACTIONS:
                prior += ACTION_STILL_PRIOR_BONUS * (1.0 - motion_strength) / math.sqrt(local_n + 1)
            repetition = (REPEAT_ACTION_BONUS if self.last_context == context and self.last_cell == cell
                          and self.last_action == action and self.last_effect >= REPEAT_EFFECT_THRESHOLD else 0.0)
            long_term = TD_ACTION_WEIGHT * q_values.get((cell, action), 0.0)
            future = ACTION_PLAN_WEIGHT * planning.get((cell, action), 0.0)
            behavioral_future = MODEL_ACTION_WEIGHT * behavioral_plan.get((cell, action), 0.0)
            affordance = max((visual_affordance_value(appearance_history, key, action)
                              for key in spot_appearances if key), default=0.0)
            candidates.append((estimate + long_term + future + behavioral_future + explore + prior
                               + repetition + VISUAL_AFFORDANCE_ACTION_WEIGHT * affordance
                               + self.rng.random() * VISUAL_EFFECT_THRESHOLD, action))
        action = max(candidates)[1]
        total_target_tries = sum(targets.get((cell, action, spot), (0, 0))[0]
                                + coarse_targets.get((cell, action, spot), (0, 0))[0] * COARSE_SPOT_WEIGHT
                                for spot in range(spot_count))
        spot_scores = []
        for spot in range(spot_count):
            count, total = targets.get((cell, action, spot), (0, 0.0))
            coarse_count, coarse_total = coarse_targets.get((cell, action, spot), (0, 0.0))
            coarse_mean = coarse_total / coarse_count if coarse_count else 0.0
            confidence = count / (count + COARSE_SPOT_PRIOR_VISITS) if count else 0.0
            mean = confidence * (total / count if count else 0.0) + (1 - confidence) * coarse_mean * COARSE_SPOT_WEIGHT
            intensity = max(0.0, fine[cell * spot_count + spot])
            score = TARGET_HISTORY_WEIGHT * mean + TARGET_SALIENCE_WEIGHT * math.sqrt(intensity)
            appearance = spot_appearances[spot]
            if appearance:
                score += VISUAL_AFFORDANCE_SPOT_WEIGHT * visual_affordance_value(
                    appearance_history, appearance, action)
            score += TARGET_EXPLORATION_WEIGHT * (1.0 + exploration * POLICY_EXPLORATION_BOOST) * math.sqrt(math.log(total_target_tries + spot_count + 1) / (count + 1))
            for age, recently in enumerate(reversed(self.recent_spots)):
                if recently == (cell, spot):
                    repeated_success = self.last_context == context and self.last_effect >= REPEAT_EFFECT_THRESHOLD
                    score += (REPEAT_SPOT_BONUS if repeated_success and age == 0 else -TARGET_RECENCY_PENALTY) * (TARGET_REPEAT_DECAY ** age)
            score += self.rng.random() * TARGET_PICK_NOISE
            spot_scores.append(score)
        if self.rng.random() < TARGET_GLOBAL_EXPLORATION + exploration * POLICY_STAGNATION_SPOT_CHANCE:
            spot = self.rng.randrange(spot_count)
        else:
            spot = max(range(spot_count), key=spot_scores.__getitem__)
        if (not exploration and self.last_context == context and self.last_effect >= REPEAT_EFFECT_THRESHOLD
                and self.last_cell is not None and self.last_spot is not None
                and self.rng.random() < POLICY_SUCCESS_REPEAT_CHANCE):
            cell, spot, action = self.last_cell, self.last_spot, self.last_action
        x, y = self.coordinates(cell, spot, frame, centers)
        aim_key = (cell, spot, action)
        local_aim = aims.get(aim_key, (0, 0.0, 0.0, 0.0))
        general_aim = coarse_aims.get(aim_key, (0, 0.0, 0.0, 0.0))
        precise_strength = local_aim[1] + general_aim[1] * ACTION_AIM_COARSE_WEIGHT
        if precise_strength > 0.0:
            learned_x = (local_aim[2] + general_aim[2] * ACTION_AIM_COARSE_WEIGHT) / precise_strength
            learned_y = (local_aim[3] + general_aim[3] * ACTION_AIM_COARSE_WEIGHT) / precise_strength
            confidence = min(ACTION_AIM_MAX_REPLAY, precise_strength / (precise_strength + ACTION_AIM_PRIOR_STRENGTH))
            confidence *= 1.0 - exploration * ACTION_AIM_EXPLORATION_DECAY
            x = min(1.0, max(0.0, x * (1.0 - confidence) + learned_x * confidence))
            y = min(1.0, max(0.0, y * (1.0 - confidence) + learned_y * confidence))
        other = cell
        to_x, to_y = x, y
        if action in ACTION_DESTINATION_ACTIONS:
            destination_count = GRID_COLUMNS * GRID_ROWS
            total_destination_tries = sum(destinations.get((cell, action, candidate), (0, 0.0))[0] for candidate in range(destination_count))
            destination_scores = []
            for candidate in range(destination_count):
                count, total = destinations.get((cell, action, candidate), (0, 0.0))
                coarse_n, coarse_total = coarse_destinations.get((cell, action, candidate), (0, 0.0))
                confidence = count / (count + DESTINATION_COARSE_PRIOR_VISITS) if count else 0.0
                coarse_mean = coarse_total / coarse_n if coarse_n else 0.0
                estimate = confidence * (total / count if count else 0.0) + (1.0 - confidence) * coarse_mean
                score = DESTINATION_HISTORY_WEIGHT * estimate
                score += DESTINATION_SALIENCE_WEIGHT * math.sqrt(max(0.0, salient[candidate]))
                score += DESTINATION_EXPLORATION_WEIGHT * (1.0 + exploration * POLICY_EXPLORATION_BOOST) * math.sqrt(math.log(total_destination_tries + destination_count + 1) / (count + 1))
                if (candidate == self.last_destination and self.last_action == action
                        and self.last_context == context and self.last_effect >= REPEAT_EFFECT_THRESHOLD):
                    score += DESTINATION_REPEAT_BONUS
                destination_scores.append(score + self.rng.random() * TARGET_PICK_NOISE)
            if self.rng.random() < DESTINATION_RANDOM_CHANCE + exploration * POLICY_STAGNATION_REGION_CHANCE:
                other = self.rng.randrange(destination_count)
            else:
                other = max(range(destination_count), key=destination_scores.__getitem__)
            other_spot = max(range(spot_count), key=lambda index: fine[other * spot_count + index] + self.rng.random() * TARGET_PICK_NOISE)
            to_x, to_y = self.coordinates(other, other_spot, frame, centers)
        variant = None
        choices = ACTION_PARAMETERS.get(action)
        if choices:
            total_count = sum(parameters.get((action, index), (0, 0.0))[0] for index in range(len(choices)))
            scores = []
            for index in range(len(choices)):
                count, total = parameters.get((action, index), (0, 0.0))
                estimate = (total / count) * count / (count + ACTION_PARAMETER_PRIOR_VISITS) if count else 0.0
                explore = ACTION_PARAMETER_EXPLORATION * (1.0 + exploration * POLICY_EXPLORATION_BOOST)
                explore *= math.sqrt(math.log(total_count + len(choices) + 1) / (count + 1))
                default = ACTION_PARAMETER_DEFAULT_BONUS if index == len(choices) // 2 else 0.0
                scores.append(estimate + explore + default + self.rng.random() * TARGET_PICK_NOISE)
            variant = max(range(len(choices)), key=scores.__getitem__)
        self.last_destination = other
        self.last_cell = cell
        self.last_spot = spot
        self.last_context = context
        self.last_action = action
        self.recent_spots.append((cell, spot))
        return context, coarse_context, cell, spot, action, x, y, to_x, to_y, other, variant, None

    def difference(self, first, second, cell=None, spot=None):
        if first is None or second is None or (first.width, first.height, first.bounds) != (second.width, second.height, second.bounds):
            return 0.0
        x0, y0, x1, y1 = 0, 0, first.width, first.height
        if cell is not None:
            column = cell % GRID_COLUMNS
            row = cell // GRID_COLUMNS
            x0 = column * first.width // GRID_COLUMNS
            x1 = (column + 1) * first.width // GRID_COLUMNS
            y0 = row * first.height // GRID_ROWS
            y1 = (row + 1) * first.height // GRID_ROWS
            if spot is not None:
                sub_column = spot % TARGET_COLUMNS
                sub_row = spot // TARGET_COLUMNS
                left, top = x0, y0
                area_width, area_height = x1 - x0, y1 - y0
                x0 = left + sub_column * area_width // TARGET_COLUMNS
                x1 = left + (sub_column + 1) * area_width // TARGET_COLUMNS
                y0 = top + sub_row * area_height // TARGET_ROWS
                y1 = top + (sub_row + 1) * area_height // TARGET_ROWS
        stride = max(1, math.ceil(math.sqrt((x1 - x0) * (y1 - y0) / VISION_DIFFERENCE_SAMPLE_BUDGET)))
        numpy = NUMPY_ACCELERATOR
        if numpy is not None:
            width, height = first.width, first.height
            gray_before = numpy.frombuffer(first.gray, dtype=numpy.uint8).reshape(height, width)[y0:y1:stride, x0:x1:stride].astype(numpy.int16)
            gray_after = numpy.frombuffer(second.gray, dtype=numpy.uint8).reshape(height, width)[y0:y1:stride, x0:x1:stride].astype(numpy.int16)
            rgb_before = numpy.frombuffer(first.rgb, dtype=numpy.uint8).reshape(height, width, BYTES_PER_RGB_PIXEL)[y0:y1:stride, x0:x1:stride].astype(numpy.int16)
            rgb_after = numpy.frombuffer(second.rgb, dtype=numpy.uint8).reshape(height, width, BYTES_PER_RGB_PIXEL)[y0:y1:stride, x0:x1:stride].astype(numpy.int16)
            return float(((1.0 - VISION_COLOR_DIFFERENCE_WEIGHT) * numpy.abs(gray_before - gray_after).mean()
                          + VISION_COLOR_DIFFERENCE_WEIGHT * numpy.abs(rgb_before - rgb_after).mean()) / COLOR_MAX)
        brightness, color, count = 0, 0, 0
        first_gray, second_gray = first.gray, second.gray
        first_rgb, second_rgb = first.rgb, second.rgb
        for y in range(y0, y1, stride):
            start = y * first.width
            for x in range(x0, x1, stride):
                index = start + x
                brightness += abs(first_gray[index] - second_gray[index])
                offset = index * BYTES_PER_RGB_PIXEL
                color += (abs(first_rgb[offset] - second_rgb[offset])
                          + abs(first_rgb[offset + 1] - second_rgb[offset + 1])
                          + abs(first_rgb[offset + 2] - second_rgb[offset + 2]))
                count += 1
        return ((1.0 - VISION_COLOR_DIFFERENCE_WEIGHT) * brightness
                + VISION_COLOR_DIFFERENCE_WEIGHT * color / BYTES_PER_RGB_PIXEL) / max(1, count * COLOR_MAX)

    def update(self, context, cell, spot, action, before, after, background, coarse_context=None, to_cell=None, variant=None, to_x=None, to_y=None, demonstration_id=None, x=None, y=None):
        global_effect = self.difference(before, after)
        local_effect = self.difference(before, after, cell)
        spot_effect = self.difference(before, after, cell, spot)
        measured_effect = SPOT_CHANGE_WEIGHT * spot_effect + REGION_CHANGE_WEIGHT * local_effect + GLOBAL_CHANGE_WEIGHT * global_effect
        if action in ACTION_DESTINATION_ACTIONS and to_cell is not None:
            destination_effect = self.difference(before, after, to_cell)
            if to_x is not None and to_y is not None:
                destination_column = to_cell % GRID_COLUMNS
                destination_row = to_cell // GRID_COLUMNS
                left = destination_column / GRID_COLUMNS
                top = destination_row / GRID_ROWS
                local_x = min(1.0 - BOUNDS_INSET / max(1, before.width), max(0.0, to_x))
                local_y = min(1.0 - BOUNDS_INSET / max(1, before.height), max(0.0, to_y))
                column = min(TARGET_COLUMNS - 1, max(0, int((local_x - left) * GRID_COLUMNS * TARGET_COLUMNS)))
                row = min(TARGET_ROWS - 1, max(0, int((local_y - top) * GRID_ROWS * TARGET_ROWS)))
                destination_spot = row * TARGET_COLUMNS + column
                destination_effect = max(destination_effect, self.difference(before, after, to_cell, destination_spot))
            measured_effect = (1.0 - DRAG_DESTINATION_EFFECT_WEIGHT) * measured_effect + DRAG_DESTINATION_EFFECT_WEIGHT * destination_effect
        guarded_background = max(background, (self.background_ema or 0.0) * BACKGROUND_EMA_GUARD_WEIGHT)
        effect = max(0.0, measured_effect - guarded_background * BACKGROUND_MOTION_WEIGHT)
        self.background_ema = background if self.background_ema is None else (1.0 - BACKGROUND_EMA_WEIGHT) * self.background_ema + BACKGROUND_EMA_WEIGHT * background
        next_context, next_coarse_context = self.context(after)
        scene_transition = bool(coarse_context and effect >= VISUAL_EFFECT_THRESHOLD and coarse_context != next_coarse_context)
        fingerprint = self.fingerprint(after)
        cyclic_state = (next_coarse_context, fingerprint) in self.recent_states and effect >= VISUAL_EFFECT_THRESHOLD
        goal_feedback = None
        self.last_goal_progress = 0.0
        if demonstration_id is not None and self.demonstration_goal is not None:
            expected_id, expected_signature, expected_local, goal_cell, goal_spot = self.demonstration_goal
            if demonstration_id == expected_id:
                comparisons = []
                if expected_signature:
                    before_global = self.fingerprint_distance(self.fingerprint(before), expected_signature)
                    after_global = self.fingerprint_distance(fingerprint, expected_signature)
                    if before_global is not None and after_global is not None:
                        comparisons.append((before_global, after_global))
                if expected_local:
                    before_local = self.fingerprint_distance(self.local_fingerprint(before, goal_cell, goal_spot), expected_local)
                    after_local = self.fingerprint_distance(self.local_fingerprint(after, goal_cell, goal_spot), expected_local)
                    if before_local is not None and after_local is not None:
                        comparisons.append((before_local, after_local))
                if comparisons:
                    before_distance = sum(pair[0] for pair in comparisons) / len(comparisons)
                    after_distance = sum(pair[1] for pair in comparisons) / len(comparisons)
                    self.last_goal_progress = before_distance - after_distance
                    goal_feedback = max(-TD_REWARD_CEILING, min(TD_REWARD_CEILING,
                        self.last_goal_progress * DEMONSTRATION_GOAL_PROGRESS_GAIN
                        + (DEMONSTRATION_GOAL_COMPLETION_BONUS if
                           after_distance <= DEMONSTRATION_GOAL_COMPLETION_DISTANCE < before_distance else 0.0)))
        if demonstration_id is None and self.transfer_goals:
            initial_signature = self.fingerprint(before)
            possible_goals = []
            for outcome in self.transfer_goals:
                starting_distance = self.fingerprint_distance(initial_signature, outcome)
                ending_distance = self.fingerprint_distance(fingerprint, outcome)
                if (starting_distance is not None and ending_distance is not None
                        and starting_distance >= DEMONSTRATION_TRANSFER_GOAL_MIN_DISTANCE):
                    possible_goals.append((starting_distance, ending_distance))
            if possible_goals:
                starting_distance, ending_distance = min(possible_goals)
                self.last_goal_progress = starting_distance - ending_distance
                goal_feedback = max(-TD_REWARD_CEILING, min(TD_REWARD_CEILING,
                    self.last_goal_progress * DEMONSTRATION_GOAL_PROGRESS_GAIN
                    * DEMONSTRATION_TRANSFER_GOAL_WEIGHT))
        try:
            appearance = object_appearance(object_patch(before, x, y)) if x is not None and y is not None else ""
            reward, visits = self.store.learn(context, cell, spot, action, self.game_id + "/" + fingerprint, effect, coarse_context, scene_transition, to_cell, next_coarse_context, cyclic_state, variant, self.game_id, self.recent_decisions, demonstration_id, x, y, goal_feedback, next_context, appearance)
        except sqlite3.Error as error:
            self.store.last_error = str(error)
            reward, visits = effect, 0
            fallback = self.fallback.setdefault(context, {})
            count, total = fallback.get((cell, action), (0, 0.0))
            fallback[(cell, action)] = count + 1, total + reward
            self.fallback.move_to_end(context)
            if len(self.fallback) > FALLBACK_CONTEXT_LIMIT:
                self.fallback.popitem(last=False)
        if scene_transition:
            self.recent_decisions.clear()
        elif coarse_context is not None:
            self.recent_decisions.append((coarse_context, cell, action))
        if (demonstration_id is not None and goal_feedback is not None
                and self.last_goal_progress < DEMONSTRATION_SEQUENCE_MIN_GOAL_PROGRESS):
            self.last_demonstration_id = None
        self.recent_states.append((next_coarse_context, fingerprint))
        self.prior = after
        self.last_effect = effect
        self.no_effect_steps = self.no_effect_steps + 1 if effect < VISUAL_EFFECT_THRESHOLD or cyclic_state and not scene_transition else 0
        return reward, effect, visits


class MouseInput(C.Structure):
    _fields_ = [("dx", C.c_int32), ("dy", C.c_int32), ("mouseData", C.c_uint32), ("dwFlags", C.c_uint32), ("time", C.c_uint32), ("dwExtraInfo", C.c_size_t)]


class InputUnion(C.Union):
    _fields_ = [("mi", MouseInput)]


class Input(C.Structure):
    _anonymous_ = ("value",)
    _fields_ = [("type", C.c_uint32), ("value", InputUnion)]


class BitmapHeader(C.Structure):
    _fields_ = [("biSize", C.c_uint32), ("biWidth", C.c_int32), ("biHeight", C.c_int32), ("biPlanes", C.c_uint16), ("biBitCount", C.c_uint16), ("biCompression", C.c_uint32), ("biSizeImage", C.c_uint32), ("biXPelsPerMeter", C.c_int32), ("biYPelsPerMeter", C.c_int32), ("biClrUsed", C.c_uint32), ("biClrImportant", C.c_uint32)]


class KeyboardHookData(C.Structure):
    _fields_ = [("vkCode", C.c_uint32), ("scanCode", C.c_uint32), ("flags", C.c_uint32), ("time", C.c_uint32), ("extra", C.c_size_t)]


class WinPoint(C.Structure):
    _fields_ = [("x", C.c_int32), ("y", C.c_int32)]


class WinRect(C.Structure):
    _fields_ = [("left", C.c_int32), ("top", C.c_int32), ("right", C.c_int32), ("bottom", C.c_int32)]


class MouseHookData(C.Structure):
    _fields_ = [("pt", WinPoint), ("mouseData", C.c_uint32), ("flags", C.c_uint32), ("time", C.c_uint32), ("extra", C.c_size_t)]


class WinMessage(C.Structure):
    _fields_ = [("hwnd", C.c_void_p), ("message", C.c_uint32), ("wParam", C.c_size_t), ("lParam", C.c_ssize_t), ("time", C.c_uint32), ("pt", WinPoint), ("lPrivate", C.c_uint32)]


class Native:
    def __init__(self):
        self.user = C.WinDLL("user32", use_last_error=True)
        self.gdi = C.WinDLL("gdi32", use_last_error=True)
        self.kernel = C.WinDLL("kernel32", use_last_error=True)
        self.shell = C.WinDLL("shell32", use_last_error=True)
        self.ole = C.WinDLL("ole32", use_last_error=True)
        self.dwm = C.WinDLL("dwmapi", use_last_error=True)
        self.hook_type = C.WINFUNCTYPE(C.c_ssize_t, C.c_int, C.c_size_t, C.c_ssize_t)
        self.window_enum_type = C.WINFUNCTYPE(C.c_int, C.c_void_p, C.c_ssize_t)
        signatures = (
            (self.user, "GetSystemMetrics", C.c_int, [C.c_int]),
            (self.user, "GetCursorPos", C.c_int, [C.POINTER(WinPoint)]),
            (self.user, "GetForegroundWindow", C.c_void_p, []),
            (self.user, "EnumWindows", C.c_int, [self.window_enum_type, C.c_ssize_t]),
            (self.user, "GetWindow", C.c_void_p, [C.c_void_p, C.c_uint]),
            (self.user, "GetAncestor", C.c_void_p, [C.c_void_p, C.c_uint]),
            (self.user, "GetWindowTextLengthW", C.c_int, [C.c_void_p]),
            (self.user, "GetWindowTextW", C.c_int, [C.c_void_p, C.c_wchar_p, C.c_int]),
            (self.user, "GetClassNameW", C.c_int, [C.c_void_p, C.c_wchar_p, C.c_int]),
            (self.user, "GetWindowThreadProcessId", C.c_uint32, [C.c_void_p, C.POINTER(C.c_uint32)]),
            (self.user, "GetClientRect", C.c_int, [C.c_void_p, C.POINTER(WinRect)]),
            (self.user, "ClientToScreen", C.c_int, [C.c_void_p, C.POINTER(WinPoint)]),
            (self.user, "IsWindowVisible", C.c_int, [C.c_void_p]),
            (self.user, "IsIconic", C.c_int, [C.c_void_p]),
            (self.user, "IsWindow", C.c_int, [C.c_void_p]),
            (self.user, "ShowWindow", C.c_int, [C.c_void_p, C.c_int]),
            (self.user, "SetForegroundWindow", C.c_int, [C.c_void_p]),
            (self.user, "GetDC", C.c_void_p, [C.c_void_p]),
            (self.user, "ReleaseDC", C.c_int, [C.c_void_p, C.c_void_p]),
            (self.user, "SendInput", C.c_uint, [C.c_uint, C.POINTER(Input), C.c_int]),
            (self.user, "GetAsyncKeyState", C.c_short, [C.c_int]),
            (self.user, "GetDoubleClickTime", C.c_uint, []),
            (self.user, "SetWindowsHookExW", C.c_void_p, [C.c_int, self.hook_type, C.c_void_p, C.c_uint]),
            (self.user, "CallNextHookEx", C.c_ssize_t, [C.c_void_p, C.c_int, C.c_size_t, C.c_ssize_t]),
            (self.user, "UnhookWindowsHookEx", C.c_int, [C.c_void_p]),
            (self.user, "PeekMessageW", C.c_int, [C.POINTER(WinMessage), C.c_void_p, C.c_uint, C.c_uint, C.c_uint]),
            (self.user, "TranslateMessage", C.c_int, [C.POINTER(WinMessage)]),
            (self.user, "DispatchMessageW", C.c_ssize_t, [C.POINTER(WinMessage)]),
            (self.user, "SetProcessDpiAwarenessContext", C.c_int, [C.c_void_p]),
            (self.gdi, "CreateCompatibleDC", C.c_void_p, [C.c_void_p]),
            (self.gdi, "CreateCompatibleBitmap", C.c_void_p, [C.c_void_p, C.c_int, C.c_int]),
            (self.gdi, "SelectObject", C.c_void_p, [C.c_void_p, C.c_void_p]),
            (self.gdi, "DeleteObject", C.c_int, [C.c_void_p]),
            (self.gdi, "DeleteDC", C.c_int, [C.c_void_p]),
            (self.gdi, "SetStretchBltMode", C.c_int, [C.c_void_p, C.c_int]),
            (self.gdi, "StretchBlt", C.c_int, [C.c_void_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_void_p, C.c_int, C.c_int, C.c_int, C.c_int, C.c_uint32]),
            (self.gdi, "GetDIBits", C.c_int, [C.c_void_p, C.c_void_p, C.c_uint, C.c_uint, C.c_void_p, C.POINTER(BitmapHeader), C.c_uint]),
            (self.kernel, "GetModuleHandleW", C.c_void_p, [C.c_wchar_p]),
            (self.kernel, "OpenProcess", C.c_void_p, [C.c_uint32, C.c_int, C.c_uint32]),
            (self.kernel, "QueryFullProcessImageNameW", C.c_int, [C.c_void_p, C.c_uint32, C.c_wchar_p, C.POINTER(C.c_uint32)]),
            (self.kernel, "CloseHandle", C.c_int, [C.c_void_p]),
            (self.shell, "SHGetKnownFolderPath", C.c_long, [C.c_void_p, C.c_uint32, C.c_void_p, C.POINTER(C.c_void_p)]),
            (self.ole, "CoTaskMemFree", None, [C.c_void_p]),
        )
        for library, name, returns, arguments in signatures:
            function = getattr(library, name)
            function.restype = returns
            function.argtypes = arguments
        self.dwm.DwmGetWindowAttribute.restype = C.c_long
        self.dwm.DwmGetWindowAttribute.argtypes = [C.c_void_p, C.c_uint32, C.c_void_p, C.c_uint32]
        self.user.SetProcessDpiAwarenessContext(C.c_void_p(DPI_AWARENESS_CONTEXT_PER_MONITOR_V2))
        self.double_click_time = self.user.GetDoubleClickTime() / MILLISECONDS_PER_SECOND
        self.io_lock = threading.RLock()
        self.held = set()
        self.active_target_window = None
        self.active_target_owner = None

    def bounds(self):
        return tuple(self.user.GetSystemMetrics(metric) for metric in (SM_XVIRTUALSCREEN, SM_YVIRTUALSCREEN, SM_CXVIRTUALSCREEN, SM_CYVIRTUALSCREEN))

    def desktop(self):
        guid = C.create_string_buffer(uuid.UUID(FOLDERID_DESKTOP).bytes_le)
        output = C.c_void_p()
        status = self.shell.SHGetKnownFolderPath(C.cast(guid, C.c_void_p), 0, None, C.byref(output))
        if status < 0 or not output.value:
            raise OSError("无法定位 Windows 桌面文件夹", status)
        try:
            return Path(C.wstring_at(output))
        finally:
            self.ole.CoTaskMemFree(output)

    def window_bounds(self, hwnd):
        if not hwnd or not self.user.IsWindow(hwnd) or not self.user.IsWindowVisible(hwnd) or self.user.IsIconic(hwnd):
            return None
        cloaked = C.c_uint32()
        if self.dwm.DwmGetWindowAttribute(hwnd, DWM_CLOAKED_ATTRIBUTE, C.byref(cloaked), C.sizeof(cloaked)) == 0 and cloaked.value:
            return None
        process = C.c_uint32()
        self.user.GetWindowThreadProcessId(hwnd, C.byref(process))
        if process.value == os.getpid():
            return None
        rectangle = WinRect()
        origin = WinPoint()
        if not self.user.GetClientRect(hwnd, C.byref(rectangle)) or not self.user.ClientToScreen(hwnd, C.byref(origin)):
            return None
        width = rectangle.right - rectangle.left
        height = rectangle.bottom - rectangle.top
        if width < MIN_TARGET_DIMENSION or height < MIN_TARGET_DIMENSION:
            return None
        virtual_x, virtual_y, virtual_w, virtual_h = self.bounds()
        left = max(origin.x, virtual_x)
        top = max(origin.y, virtual_y)
        right = min(origin.x + width, virtual_x + virtual_w)
        bottom = min(origin.y + height, virtual_y + virtual_h)
        if right - left < MIN_TARGET_DIMENSION or bottom - top < MIN_TARGET_DIMENSION:
            return None
        return left, top, right - left, bottom - top

    def window_owner(self, hwnd):
        if not hwnd or not self.user.IsWindow(hwnd):
            return None
        process = C.c_uint32()
        self.user.GetWindowThreadProcessId(hwnd, C.byref(process))
        return process.value, self.window_class(hwnd)

    def window_caption(self, hwnd):
        if not hwnd:
            return ""
        length = min(WINDOW_TITLE_LIMIT, max(1, self.user.GetWindowTextLengthW(hwnd) + 1))
        buffer = C.create_unicode_buffer(length)
        self.user.GetWindowTextW(hwnd, buffer, length)
        return buffer.value

    def window_class(self, hwnd):
        buffer = C.create_unicode_buffer(WINDOW_CLASS_LIMIT)
        self.user.GetClassNameW(hwnd, buffer, WINDOW_CLASS_LIMIT)
        return buffer.value

    def windows(self):
        result = []
        def visit(hwnd, argument):
            if self.window_bounds(hwnd) is not None and self.window_class(hwnd) not in WINDOW_IGNORED_CLASSES:
                caption = self.window_caption(hwnd) or self.window_class(hwnd)
                if caption:
                    result.append((hwnd, caption))
            return True
        callback = self.window_enum_type(visit)
        self.user.EnumWindows(callback, 0)
        return result

    def window_by_game_id(self, identity, owner=None):
        fallback = None
        if identity:
            for hwnd, caption in self.windows():
                if self.game_id(hwnd) == identity:
                    return hwnd, self.window_bounds(hwnd)
                if owner is not None and self.window_owner(hwnd) == owner:
                    fallback = hwnd
        return (fallback, self.window_bounds(fallback)) if fallback else (None, None)

    def game_id(self, hwnd):
        if not hwnd:
            return "desktop"
        process = C.c_uint32()
        self.user.GetWindowThreadProcessId(hwnd, C.byref(process))
        executable = ""
        handle = self.kernel.OpenProcess(PROCESS_QUERY_LIMITED_INFORMATION, False, process.value)
        if handle:
            try:
                buffer = C.create_unicode_buffer(WINDOW_PATH_LIMIT)
                length = C.c_uint32(WINDOW_PATH_LIMIT)
                if self.kernel.QueryFullProcessImageNameW(handle, 0, buffer, C.byref(length)):
                    executable = str(Path(buffer.value)).lower()
            finally:
                self.kernel.CloseHandle(handle)
        caption = re.sub(r"\d+", "#", self.window_caption(hwnd).casefold().strip())[:GAME_TITLE_ID_LENGTH]
        if executable and Path(executable).name not in SHARED_HOST_EXECUTABLES:
            identity = (executable, self.window_class(hwnd))
        else:
            identity = (executable, self.window_class(hwnd), caption)
        return hashlib.sha256(repr(identity).encode("utf-8")).hexdigest()[:GAME_ID_LENGTH]

    def foreground_window(self, own_hwnd=None):
        handle = self.user.GetForegroundWindow()
        if own_hwnd:
            top = self.user.GetAncestor(own_hwnd, GA_ROOT)
            if top and (not handle or handle == top):
                handle = self.user.GetWindow(top, GW_HWNDNEXT)
        candidates = set()
        while handle and handle not in candidates:
            candidates.add(handle)
            area = self.window_bounds(handle)
            if area is not None and self.window_class(handle) not in WINDOW_IGNORED_CLASSES:
                return handle, area
            handle = self.user.GetWindow(handle, GW_HWNDNEXT)
        return None, None

    def target_is_foreground(self, hwnd):
        foreground = self.user.GetForegroundWindow()
        if not hwnd or not foreground:
            return False
        return bool(foreground == hwnd or self.user.GetAncestor(foreground, GA_ROOT) == self.user.GetAncestor(hwnd, GA_ROOT))

    def activate_window(self, hwnd):
        if hwnd and self.user.IsWindow(hwnd):
            if self.user.IsIconic(hwnd):
                self.user.ShowWindow(hwnd, SW_RESTORE)
            if not self.target_is_foreground(hwnd):
                self.user.SetForegroundWindow(hwnd)
            return self.target_is_foreground(hwnd)
        return False

    def capture(self, area=None, long_edge=VISION_LONG_EDGE):
        x, y, screen_width, screen_height = area if area is not None else self.bounds()
        if min(screen_width, screen_height) <= 0:
            raise OSError("屏幕当前不可捕获")
        ratio = min(1.0, min(long_edge, VISION_ADAPTIVE_MAX_EDGE) / max(screen_width, screen_height))
        ratio = min(ratio, math.sqrt(VISION_MAX_CAPTURE_PIXELS / (screen_width * screen_height)))
        width = min(screen_width, max(VISION_MIN_EDGE, round(screen_width * ratio)))
        height = min(screen_height, max(VISION_MIN_EDGE, round(screen_height * ratio)))
        screen = self.user.GetDC(None)
        memory = None
        bitmap = None
        selected = None
        try:
            if not screen:
                raise C.WinError(C.get_last_error())
            memory = self.gdi.CreateCompatibleDC(screen)
            if not memory:
                raise C.WinError(C.get_last_error())
            bitmap = self.gdi.CreateCompatibleBitmap(screen, width, height)
            if not bitmap:
                raise C.WinError(C.get_last_error())
            selected = self.gdi.SelectObject(memory, bitmap)
            if not selected or selected == C.c_void_p(-1).value:
                raise C.WinError(C.get_last_error())
            self.gdi.SetStretchBltMode(memory, COLORONCOLOR)
            if not self.gdi.StretchBlt(memory, 0, 0, width, height, screen, x, y, screen_width, screen_height, SRCCOPY | CAPTUREBLT):
                if not self.gdi.StretchBlt(memory, 0, 0, width, height, screen, x, y, screen_width, screen_height, SRCCOPY):
                    raise C.WinError(C.get_last_error())
            self.gdi.SelectObject(memory, selected)
            selected = None
            header = BitmapHeader()
            header.biSize = C.sizeof(header)
            header.biWidth = width
            header.biHeight = -height
            header.biPlanes = 1
            header.biBitCount = BITS_PER_BYTE * BYTES_PER_COLOR_PIXEL
            header.biCompression = BI_RGB
            pixels = C.create_string_buffer(width * height * BYTES_PER_COLOR_PIXEL)
            if self.gdi.GetDIBits(memory, bitmap, 0, height, pixels, C.byref(header), DIB_RGB_COLORS) != height:
                raise C.WinError(C.get_last_error())
            raw = pixels.raw
            numpy = NUMPY_ACCELERATOR
            if numpy is not None:
                bgra = numpy.frombuffer(raw, dtype=numpy.uint8).reshape(-1, BYTES_PER_COLOR_PIXEL)
                pixels = bgra[:, (2, 1, 0)]
                values = pixels.astype(numpy.uint16)
                gray = ((values[:, 0] * COLOR_CHANNEL_RED_WEIGHT
                         + values[:, 1] * COLOR_CHANNEL_GREEN_WEIGHT
                         + values[:, 2] * COLOR_CHANNEL_BLUE_WEIGHT) >> BITS_PER_BYTE).astype(numpy.uint8).tobytes()
                rgb = pixels.tobytes()
            else:
                rgb = bytearray(width * height * BYTES_PER_RGB_PIXEL)
                rgb[0::BYTES_PER_RGB_PIXEL] = raw[2::BYTES_PER_COLOR_PIXEL]
                rgb[1::BYTES_PER_RGB_PIXEL] = raw[1::BYTES_PER_COLOR_PIXEL]
                rgb[2::BYTES_PER_RGB_PIXEL] = raw[0::BYTES_PER_COLOR_PIXEL]
                gray = bytearray((rgb[i] * COLOR_CHANNEL_RED_WEIGHT + rgb[i + 1] * COLOR_CHANNEL_GREEN_WEIGHT + rgb[i + 2] * COLOR_CHANNEL_BLUE_WEIGHT) >> BITS_PER_BYTE for i in range(0, len(rgb), BYTES_PER_RGB_PIXEL))
                rgb = bytes(rgb)
            return Frame(width, height, gray, rgb, (x, y, screen_width, screen_height))
        finally:
            if selected and memory:
                self.gdi.SelectObject(memory, selected)
            if bitmap:
                self.gdi.DeleteObject(bitmap)
            if memory:
                self.gdi.DeleteDC(memory)
            if screen:
                self.user.ReleaseDC(None, screen)

    def send(self, flags, x=0, y=0, data=0):
        if (self.active_target_window and self.active_target_owner is not None
                and not flags & MOUSE_BUTTON_RELEASE_FLAGS
                and self.window_owner(self.active_target_window) != self.active_target_owner):
            raise OSError("目标窗口所属进程已变化，阻止误操作其他程序")
        if self.active_target_window and not flags & MOUSE_BUTTON_RELEASE_FLAGS and not self.target_is_foreground(self.active_target_window):
            raise OSError("目标窗口已失去前台焦点，已阻止鼠标误操作")
        if self.active_target_window and (flags & MOUSE_POSITION_REQUIRED_FLAGS or
                                          flags & MOUSEEVENTF_MOVE and not flags & MOUSEEVENTF_ABSOLUTE):
            area = self.window_bounds(self.active_target_window)
            if area is None:
                raise OSError("目标游戏窗口已经不可用，正在自动恢复")
            left, top, width, height = area
            point = WinPoint()
            for attempt in range(CURSOR_POSITION_CHECK_ATTEMPTS):
                if not self.user.GetCursorPos(C.byref(point)):
                    raise OSError("无法确认目标游戏内的鼠标位置，正在自动恢复")
                if left <= point.x < left + width and top <= point.y < top + height:
                    break
                if attempt + 1 < CURSOR_POSITION_CHECK_ATTEMPTS:
                    time.sleep(CURSOR_POSITION_CHECK_INTERVAL_SECONDS)
            else:
                raise OSError("鼠标位于游戏窗口外，已避免误点击其他程序")
            if flags & MOUSEEVENTF_MOVE and not flags & MOUSEEVENTF_ABSOLUTE:
                x = max(left - point.x, min(left + width - BOUNDS_INSET - point.x, x))
                y = max(top - point.y, min(top + height - BOUNDS_INSET - point.y, y))
        packet = Input()
        packet.type = INPUT_MOUSE
        packet.mi = MouseInput(x, y, data & C.c_uint32(-1).value, flags, 0, 0)
        if self.user.SendInput(1, C.byref(packet), C.sizeof(packet)) != 1:
            raise OSError(f"Windows 拒绝模拟鼠标输入（Win32 错误 {C.get_last_error()}）：权限、受保护桌面或游戏输入限制")

    def move(self, x, y, stop, area=None):
        if stop.is_set():
            return
        virtual_x, virtual_y, virtual_w, virtual_h = self.bounds()
        if self.active_target_window:
            area = self.window_bounds(self.active_target_window)
            if area is None:
                raise OSError("目标游戏窗口已不可用，已阻止鼠标越界")
        left, top, width, height = area if area is not None else (virtual_x, virtual_y, virtual_w, virtual_h)
        pixel_x = left + min(1.0, max(0.0, x)) * max(0, width - BOUNDS_INSET)
        pixel_y = top + min(1.0, max(0.0, y)) * max(0, height - BOUNDS_INSET)
        absolute_x = round((pixel_x - virtual_x) * ABSOLUTE_COORDINATE_MAX / max(1, virtual_w - BOUNDS_INSET))
        absolute_y = round((pixel_y - virtual_y) * ABSOLUTE_COORDINATE_MAX / max(1, virtual_h - BOUNDS_INSET))
        absolute_x = min(ABSOLUTE_COORDINATE_MAX, max(0, absolute_x))
        absolute_y = min(ABSOLUTE_COORDINATE_MAX, max(0, absolute_y))
        with self.io_lock:
            if not stop.is_set():
                self.send(MOUSEEVENTF_MOVE | MOUSEEVENTF_ABSOLUTE | MOUSEEVENTF_VIRTUALDESK, absolute_x, absolute_y)

    def move_relative(self, x, y, stop, area=None):
        if stop.is_set():
            return
        if self.active_target_window:
            area = self.window_bounds(self.active_target_window)
            if area is None:
                raise OSError("目标游戏窗口已不可用，已阻止鼠标越界")
        _, _, width, height = area if area is not None else self.bounds()
        dx = round((x - COORDINATE_CENTER) * width * RELATIVE_MOUSE_REACH)
        dy = round((y - COORDINATE_CENTER) * height * RELATIVE_MOUSE_REACH)
        with self.io_lock:
            if not stop.is_set():
                self.send(MOUSEEVENTF_MOVE, dx, dy)

    def press(self, down, up, duration, stop):
        with self.io_lock:
            if stop.is_set():
                return
            self.held.add(up)
            try:
                self.send(down)
            except Exception:
                self.held.discard(up)
                raise
        try:
            stop.wait(duration)
        finally:
            with self.io_lock:
                if up in self.held:
                    self.send(up)
                    self.held.discard(up)

    def release(self):
        with self.io_lock:
            first_error = None
            for up in tuple(self.held):
                try:
                    self.send(up)
                    self.held.discard(up)
                except OSError as error:
                    if first_error is None:
                        first_error = error
            if first_error:
                raise first_error

    def relative_drag(self, name, x, y, to_x, to_y, stop, area=None, duration=RELATIVE_DRAG_TIME_SECONDS):
        if stop.is_set():
            return
        self.move(x, y, stop, area)
        if stop.is_set():
            return
        _, _, width, height = area if area is not None else self.bounds()
        dx = round((to_x - x) * width * RELATIVE_MOUSE_REACH)
        dy = round((to_y - y) * height * RELATIVE_MOUSE_REACH)
        down, up = ((MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP) if name == "左按相对移动" else (MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP))
        with self.io_lock:
            if stop.is_set():
                return
            self.held.add(up)
            try:
                self.send(down)
            except Exception:
                self.held.discard(up)
                raise
        try:
            prior_x, prior_y = 0, 0
            for step in range(RELATIVE_DRAG_STEPS):
                if stop.is_set():
                    break
                next_x = round(dx * (step + 1) / RELATIVE_DRAG_STEPS)
                next_y = round(dy * (step + 1) / RELATIVE_DRAG_STEPS)
                with self.io_lock:
                    if not stop.is_set():
                        self.send(MOUSEEVENTF_MOVE, next_x - prior_x, next_y - prior_y)
                prior_x, prior_y = next_x, next_y
                stop.wait(duration / RELATIVE_DRAG_STEPS)
        finally:
            self.release()

    def drag_trajectory(self, name, points, x, y, to_x, to_y, stop, area, duration):
        down, up = ((MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP)
                    if name == "左拖" else (MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP))
        self.move(x, y, stop, area)
        if stop.is_set():
            return
        start_point = points[0]
        end_point = points[-1]
        timeline = []
        for fraction, px, py in points:
            offset_x = (x - start_point[1]) * (1.0 - fraction) + (to_x - end_point[1]) * fraction
            offset_y = (y - start_point[2]) * (1.0 - fraction) + (to_y - end_point[2]) * fraction
            timeline.append((fraction, min(1.0, max(0.0, px + offset_x)),
                             min(1.0, max(0.0, py + offset_y))))
        with self.io_lock:
            if stop.is_set():
                return
            self.held.add(up)
            try:
                self.send(down)
            except Exception:
                self.held.discard(up)
                raise
        try:
            started = time.monotonic()
            segment = 0
            while not stop.is_set():
                elapsed = min(1.0, (time.monotonic() - started) / max(MOUSE_PATH_STEP_SECONDS, duration))
                while segment + 1 < len(timeline) - 1 and elapsed >= timeline[segment + 1][0]:
                    segment += 1
                if elapsed >= 1.0:
                    self.move(to_x, to_y, stop, area)
                    break
                first, second = timeline[segment], timeline[segment + 1]
                blend = min(1.0, max(0.0, (elapsed - first[0]) / max(MOUSE_PATH_TIME_EPSILON, second[0] - first[0])))
                self.move(first[1] + (second[1] - first[1]) * blend,
                          first[2] + (second[2] - first[2]) * blend, stop, area)
                stop.wait(MOUSE_PATH_STEP_SECONDS)
        finally:
            self.release()

    def action(self, name, x, y, to_x, to_y, stop, area=None, variant=None, duration_override=None, path=""):
        if name not in MOUSE_ACTIONS:
            raise ValueError("不支持的鼠标动作：" + str(name))
        parameter = ACTION_PARAMETERS[name][variant] if variant is not None and name in ACTION_PARAMETERS else None
        if (duration_override is not None and name in ACTION_PARAMETERS
                and name not in ("上滚", "下滚") and math.isfinite(duration_override)
                and duration_override > 0.0):
            parameter = duration_override
        if name in ("左按相对移动", "右按相对移动"):
            self.relative_drag(name, x, y, to_x, to_y, stop, area,
                               duration=parameter if parameter is not None else RELATIVE_DRAG_TIME_SECONDS)
            return
        if name == "相对移动":
            self.move_relative(x, y, stop, area)
            return
        self.move(x, y, stop, area)
        if stop.is_set():
            return
        if name == "移动":
            stop.wait(ACTION_SETTLE_SECONDS)
        elif name == "上滚" or name == "下滚":
            for tick in range(parameter if parameter is not None else ACTION_WHEEL_TICKS[0]):
                with self.io_lock:
                    if not stop.is_set():
                        self.send(MOUSEEVENTF_WHEEL, data=WHEEL_DELTA if name == "上滚" else -WHEEL_DELTA)
                if tick + 1 < (parameter if parameter is not None else ACTION_WHEEL_TICKS[0]):
                    stop.wait(ACTION_WHEEL_TICK_INTERVAL_SECONDS)
        elif name == "左长按" or name == "右长按":
            down, up = ((MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP) if name == "左长按" else (MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP))
            self.press(down, up, parameter if parameter is not None else LONG_PRESS_SECONDS, stop)
        elif name == "左拖" or name == "右拖":
            demonstrated_path = parse_demonstration_path(path)
            if demonstrated_path is not None:
                self.drag_trajectory(name, demonstrated_path, x, y, to_x, to_y, stop, area,
                                     parameter if parameter is not None else DRAG_DURATION_SECONDS)
                return
            down, up = ((MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP) if name == "左拖" else (MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP))
            with self.io_lock:
                if stop.is_set():
                    return
                self.held.add(up)
                try:
                    self.send(down)
                except Exception:
                    self.held.discard(up)
                    raise
            try:
                start = time.monotonic()
                while not stop.is_set():
                    fraction = min(1.0, (time.monotonic() - start) / (parameter if parameter is not None else DRAG_DURATION_SECONDS))
                    self.move(x + (to_x - x) * fraction, y + (to_y - y) * fraction, stop, area)
                    if fraction >= 1.0:
                        break
                    stop.wait(KEYBOARD_POLL_SECONDS)
            finally:
                self.release()
        else:
            down, up = {
                "右击": (MOUSEEVENTF_RIGHTDOWN, MOUSEEVENTF_RIGHTUP),
                "中击": (MOUSEEVENTF_MIDDLEDOWN, MOUSEEVENTF_MIDDLEUP),
            }.get(name, (MOUSEEVENTF_LEFTDOWN, MOUSEEVENTF_LEFTUP))
            self.press(down, up, CLICK_DURATION_SECONDS, stop)
            if name == "双击" and not stop.wait(min(ACTION_SETTLE_SECONDS, self.double_click_time / 2)):
                self.press(down, up, CLICK_DURATION_SECONDS, stop)


class KeyboardGuard:
    def __init__(self, native, stop):
        self.native = native
        self.stop = stop
        self.armed = threading.Event()
        self.ready = threading.Event()
        self.close_event = threading.Event()
        self.error = ""
        self.lock = threading.RLock()
        self.pressed = set()
        self.thread = threading.Thread(target=self.run, daemon=True, name="keyboard-stop-guard")
        self.thread.start()

    def run(self):
        user = self.native.user
        def callback(code, message, data):
            if code >= 0 and message in (WM_KEYDOWN, WM_SYSKEYDOWN, WM_KEYUP, WM_SYSKEYUP) and self.armed.is_set():
                record = C.cast(data, C.POINTER(KeyboardHookData)).contents
                if not record.flags & LLKHF_INJECTED:
                    with self.lock:
                        if message in (WM_KEYUP, WM_SYSKEYUP):
                            self.pressed.discard(record.vkCode)
                        elif record.vkCode not in self.pressed:
                            self.stop.set()
                            self.pressed.add(record.vkCode)
            return user.CallNextHookEx(None, code, message, data)
        self.callback = self.native.hook_type(callback)
        hook = user.SetWindowsHookExW(WH_KEYBOARD_LL, self.callback, self.native.kernel.GetModuleHandleW(None), 0)
        if not hook:
            self.error = "低级键盘钩子不可用，已使用系统按键轮询作为备选"
        self.ready.set()
        message = WinMessage()
        try:
            while not self.close_event.is_set():
                while user.PeekMessageW(C.byref(message), None, 0, 0, PM_REMOVE):
                    user.TranslateMessage(C.byref(message))
                    user.DispatchMessageW(C.byref(message))
                if self.armed.is_set():
                    with self.lock:
                        for key in KEYBOARD_KEYS:
                            state = user.GetAsyncKeyState(key)
                            if state & KEY_DOWN_MASK:
                                if key not in self.pressed:
                                    self.stop.set()
                                self.pressed.add(key)
                            else:
                                self.pressed.discard(key)
                                if not hook and state & KEY_PRESSED_MASK:
                                    self.stop.set()
                self.close_event.wait(KEYBOARD_POLL_SECONDS)
        finally:
            if hook:
                user.UnhookWindowsHookEx(hook)

    def arm(self, reset_stop=True):
        with self.lock:
            self.pressed = {key for key in KEYBOARD_KEYS if self.native.user.GetAsyncKeyState(key) & KEY_DOWN_MASK}
            if reset_stop:
                self.stop.clear()
            self.armed.set()



class PassiveMouseObserver:
    def __init__(self, app):
        self.app = app
        self.native = app.native
        self.enabled = threading.Event()
        self.closing = threading.Event()
        self.hook_ready = threading.Event()
        self.hook_installed = False
        self.hook_error = ""
        self.generation = 0
        self.queue = queue.Queue(maxsize=OBSERVER_QUEUE_CAPACITY)
        self.samples = collections.deque(maxlen=OBSERVER_FRAME_HISTORY)
        self.pressed = {}
        self.pending_click = None
        self.pending = []
        self.window = None
        self.area = None
        self.game = ""
        self.policy = VisionPolicy(None)
        self.last_sample = 0.0
        self.last_input = 0.0
        self.last_hook_move = 0.0
        self.last_hook_input = 0.0
        self.last_user_move = 0.0
        self.last_move_point = None
        self.last_observation_id = None
        self.last_observation_time = 0.0
        self.last_error_report = 0.0
        self.last_error = ""
        self.poll_buttons = {}
        self.poll_position = None
        self.total = 0
        self.hook_thread = threading.Thread(target=self.run_hook, name="mouse-observation-hook", daemon=True)
        self.worker_thread = threading.Thread(target=self.run_worker, name="passive-human-learning", daemon=True)
        self.hook_thread.start()
        self.worker_thread.start()

    def activate(self, value):
        self.enabled.clear()
        self.generation += 1
        if value and not self.closing.is_set():
            self.enabled.set()

    def active(self):
        return (self.enabled.is_set() and not self.closing.is_set()
                and not self.app.running and not self.app.preparing and self.app.store is not None)

    def enqueue(self, now, message, x, y, data, hwnd):
        if not self.active():
            return
        if message == WM_MOUSEMOVE:
            if now - self.last_hook_move < OBSERVER_HOOK_MOVE_INTERVAL_SECONDS:
                return
            self.last_hook_move = now
        try:
            self.queue.put_nowait((self.generation, now, message, x, y, data, hwnd))
        except queue.Full:
            pass

    def run_hook(self):
        try:
            self.install_hook()
        except Exception as error:
            self.hook_installed = False
            self.hook_error = "鼠标观察钩子发生异常，已自动使用输入轮询：" + str(error)
            self.hook_ready.set()
            self.report_error(error)

    def install_hook(self):
        user = self.native.user
        def callback(code, message, data):
            try:
                if code >= 0 and self.active():
                    event = C.cast(data, C.POINTER(MouseHookData)).contents
                    if not event.flags & LLMHF_INJECTED:
                        now = time.monotonic()
                        self.last_hook_input = now
                        self.enqueue(now, message, event.pt.x, event.pt.y,
                                     event.mouseData, user.GetForegroundWindow())
            except Exception:
                pass
            return user.CallNextHookEx(None, code, message, data)
        self.callback = self.native.hook_type(callback)
        hook = user.SetWindowsHookExW(WH_MOUSE_LL, self.callback, self.native.kernel.GetModuleHandleW(None), 0)
        self.hook_installed = bool(hook)
        if not hook:
            self.hook_error = "鼠标系统钩子不可用，将使用鼠标按钮与位置轮询；此模式无法捕获滚轮"
        self.hook_ready.set()
        message = WinMessage()
        try:
            while not self.closing.is_set():
                while user.PeekMessageW(C.byref(message), None, 0, 0, PM_REMOVE):
                    user.TranslateMessage(C.byref(message))
                    user.DispatchMessageW(C.byref(message))
                self.closing.wait(OBSERVER_HOOK_WAIT_SECONDS)
        finally:
            if hook:
                user.UnhookWindowsHookEx(hook)

    def poll_input(self):
        if not self.active():
            return
        point = WinPoint()
        if not self.native.user.GetCursorPos(C.byref(point)):
            return
        now = time.monotonic()
        hwnd = self.native.user.GetForegroundWindow()
        states = {
            VK_LBUTTON: bool(self.native.user.GetAsyncKeyState(VK_LBUTTON) & KEY_DOWN_MASK),
            VK_RBUTTON: bool(self.native.user.GetAsyncKeyState(VK_RBUTTON) & KEY_DOWN_MASK),
            VK_MBUTTON: bool(self.native.user.GetAsyncKeyState(VK_MBUTTON) & KEY_DOWN_MASK),
        }
        messages = {
            VK_LBUTTON: (WM_LBUTTONDOWN, WM_LBUTTONUP),
            VK_RBUTTON: (WM_RBUTTONDOWN, WM_RBUTTONUP),
            VK_MBUTTON: (WM_MBUTTONDOWN, WM_MBUTTONUP),
        }
        if self.poll_position != (point.x, point.y):
            self.enqueue(now, WM_MOUSEMOVE, point.x, point.y, 0, hwnd)
            self.poll_position = (point.x, point.y)
        for key, state in states.items():
            previous = self.poll_buttons.get(key, state)
            if state != previous:
                self.enqueue(now, messages[key][0 if state else 1], point.x, point.y, 0, hwnd)
            self.poll_buttons[key] = state

    def reset_window(self, hwnd=None, area=None):
        self.samples.clear()
        self.pressed.clear()
        self.pending.clear()
        self.pending_click = None
        self.window = hwnd
        self.area = area
        self.game = self.native.game_id(hwnd) if hwnd else ""
        self.policy.game_id = self.game
        self.last_sample = 0.0
        self.last_input = 0.0
        self.last_user_move = 0.0
        self.last_move_point = None
        self.last_observation_id = None
        self.last_observation_time = 0.0

    def before_for(self, when):
        for captured, hwnd, area, frame in reversed(self.samples):
            if (hwnd == self.window and area == self.area and captured <= when
                    and when - captured <= OBSERVER_FRAME_MAX_AGE_SECONDS):
                return frame
        return None

    def inside(self, x, y):
        if not self.area:
            return False
        left, top, width, height = self.area
        return left <= x < left + width and top <= y < top + height

    def normalized(self, x, y):
        left, top, width, height = self.area
        return (min(1.0, max(0.0, (x - left) / max(1, width - BOUNDS_INSET))),
                min(1.0, max(0.0, (y - top) / max(1, height - BOUNDS_INSET))))

    def cell_spot(self, x, y):
        return position_cell_spot(x, y)

    def recorded_path(self, points, start, end):
        if len(points) < 2 or end <= start:
            return ""
        if len(points) > DEMONSTRATION_PATH_MAX_POINTS:
            points = [points[round(index * (len(points) - 1) / (DEMONSTRATION_PATH_MAX_POINTS - 1))]
                      for index in range(DEMONSTRATION_PATH_MAX_POINTS)]
        output = []
        for when, px, py in points:
            if not self.inside(px, py):
                return ""
            x, y = self.normalized(px, py)
            fraction = min(1.0, max(0.0, (when - start) / (end - start)))
            if output and fraction <= output[-1][0]:
                continue
            output.append([round(fraction, 4), round(x, 5), round(y, 5)])
        if len(output) < 2:
            return ""
        output[0][0] = 0.0
        output[-1][0] = 1.0
        encoded = json.dumps(output, separators=(",", ":"))
        return encoded if len(encoded) <= DEMONSTRATION_PATH_MAX_BYTES else ""

    def submit(self, start, action, sx, sy, ex, ey, now, variant=-1, duration=0.0, path=""):
        if start is None or not self.inside(sx, sy) or not self.inside(ex, ey):
            return
        frame, identity, bounds = start
        if identity != self.game or bounds != self.area or frame is None:
            return
        self.pending.append((now + OBSERVER_AFTER_ACTION_SECONDS, start, action, sx, sy, ex, ey, variant, duration, path))

    def finish_click(self):
        if self.pending_click is not None:
            start, action, sx, sy, ex, ey, timestamp = self.pending_click
            self.submit(start, action, sx, sy, ex, ey, timestamp)
            self.pending_click = None

    def accept(self, entry):
        generation, now, message, x, y, data, hwnd = entry
        if generation != self.generation or hwnd != self.window or not self.inside(x, y):
            return
        self.last_input = now
        down_actions = {WM_LBUTTONDOWN: "左", WM_RBUTTONDOWN: "右", WM_MBUTTONDOWN: "中"}
        up_actions = {WM_LBUTTONUP: "左", WM_RBUTTONUP: "右", WM_MBUTTONUP: "中"}
        if message in down_actions:
            button = down_actions[message]
            frame = self.before_for(now)
            if frame is not None:
                self.pressed[button] = (now, x, y, (frame, self.game, self.area), [(now, x, y)])
        elif message in up_actions:
            button = up_actions[message]
            pressed = self.pressed.pop(button, None)
            if pressed is None:
                return
            started, sx, sy, start, trajectory = pressed
            left, top, width, height = self.area
            distance = math.hypot((x - sx) / max(1, width), (y - sy) / max(1, height))
            duration = now - started
            if button in ("左", "右") and distance >= OBSERVER_DRAG_THRESHOLD:
                self.finish_click()
                action = button + "拖"
                if action in ACTION_PARAMETERS:
                    variant = min(range(len(ACTION_PARAMETERS[action])),
                                  key=lambda index: abs(ACTION_PARAMETERS[action][index] - duration))
                else:
                    variant = -1
                trajectory.append((now, x, y))
                path = self.recorded_path(trajectory, started, now)
                self.submit(start, action, sx, sy, x, y, now, variant, duration, path)
            elif button in ("左", "右") and duration >= OBSERVER_LONG_PRESS_SECONDS:
                self.finish_click()
                action = button + "长按"
                variant = min(range(len(ACTION_PARAMETERS[action])),
                              key=lambda index: abs(ACTION_PARAMETERS[action][index] - duration))
                self.submit(start, action, sx, sy, x, y, now, variant, duration)
            else:
                action = button + "击"
                if (button == "左" and self.pending_click is not None
                        and self.pending_click[1] == "左击"
                        and now - self.pending_click[6] <= self.native.double_click_time
                        and math.hypot((sx - self.pending_click[2]) / max(1, width),
                                       (sy - self.pending_click[3]) / max(1, height)) <= OBSERVER_DOUBLE_CLICK_DISTANCE):
                    first = self.pending_click
                    self.pending_click = None
                    self.submit(first[0], "双击", first[2], first[3], x, y, now)
                elif button == "左":
                    self.finish_click()
                    self.pending_click = (start, action, sx, sy, x, y, now)
                else:
                    self.finish_click()
                    self.submit(start, action, sx, sy, x, y, now)
        elif message == WM_MOUSEWHEEL:
            frame = self.before_for(now)
            if frame is None:
                return
            delta = C.c_int16(data >> (BITS_PER_BYTE * 2)).value
            if not delta:
                return
            action = "上滚" if delta > 0 else "下滚"
            variant = min(range(len(ACTION_WHEEL_TICKS)),
                          key=lambda index: abs(ACTION_WHEEL_TICKS[index] - abs(delta) / WHEEL_DELTA))
            self.finish_click()
            self.submit((frame, self.game, self.area), action, x, y, x, y, now, variant)
        elif message == WM_MOUSEMOVE:
            if self.pressed:
                left, top, width, height = self.area
                for pressed in self.pressed.values():
                    points = pressed[4]
                    if (math.hypot((x - points[-1][1]) / max(1, width),
                                   (y - points[-1][2]) / max(1, height)) >= DEMONSTRATION_PATH_MIN_DISTANCE):
                        points.append((now, x, y))
                        if len(points) >= DEMONSTRATION_PATH_MAX_POINTS:
                            points[:] = points[::2]
            else:
                if self.last_move_point is None:
                    self.last_move_point = (x, y)
                    return
                left, top, width, height = self.area
                distance = math.hypot((x - self.last_move_point[0]) / max(1, width),
                                      (y - self.last_move_point[1]) / max(1, height))
                if (now - self.last_user_move >= OBSERVER_MOVE_RECORD_SECONDS
                        and distance >= OBSERVER_MOVE_DISTANCE):
                    frame = self.before_for(now)
                    if frame is not None:
                        self.finish_click()
                        self.submit((frame, self.game, self.area), "移动", x, y, x, y, now)
                        self.last_user_move = now
                        self.last_move_point = (x, y)

    def process_pending(self, now):
        if not self.pending:
            return
        ready = [item for item in self.pending if item[0] <= now]
        if not ready:
            return
        self.pending = [item for item in self.pending if item[0] > now]
        if not self.active() or self.window != self.native.user.GetForegroundWindow():
            return
        if self.area != self.native.window_bounds(self.window):
            return
        try:
            after = self.native.capture(self.area, OBSERVER_CAPTURE_EDGE)
        except OSError:
            return
        for deadline, start, action, sx, sy, ex, ey, variant, duration, path in ready:
            if not self.active():
                return
            before, game, bounds = start
            if game != self.game or bounds != after.bounds:
                continue
            x, y = self.normalized(sx, sy)
            to_x, to_y = self.normalized(ex, ey)
            cell, spot = self.cell_spot(x, y)
            destination = self.cell_spot(to_x, to_y)[0] if action in ACTION_DESTINATION_ACTIONS else -1
            try:
                context, coarse = self.policy.context(before)
                signature = self.policy.fingerprint(before)
                local_signature = self.policy.local_fingerprint(before, cell, spot)
                next_signature = self.policy.fingerprint(after)
                next_local_signature = self.policy.local_fingerprint(after, cell, spot)
                next_context, next_coarse = self.policy.context(after)
                effect = self.policy.difference(before, after)
                anchor_patch = object_patch(before, x, y)
                destination_patch = (object_patch(before, to_x, to_y)
                                     if action in ACTION_DESTINATION_ACTIONS else "")
                appearance = object_appearance(anchor_patch)
                store = self.app.store
                previous_id = (self.last_observation_id if deadline - self.last_observation_time <= DEMONSTRATION_SEQUENCE_SECONDS else None)
                observation_id = (store.record_demonstration(
                    game, context, coarse, signature, cell, spot, action, destination, variant,
                    x, y, to_x, to_y, effect, previous_id,
                    local_signature, next_signature, next_coarse, next_local_signature, duration, path,
                    next_context, anchor_patch, destination_patch, appearance
                ) if store is not None else None)
                if observation_id:
                    self.last_observation_id = observation_id
                    self.last_observation_time = deadline
                    self.total += 1
                    self.app.events.put(("observation", (self.total, action)))
            except (sqlite3.Error, OSError, ValueError, MemoryError) as error:
                self.report_error(error)

    def report_error(self, error):
        now = time.monotonic()
        message = str(error)
        if message != self.last_error or now - self.last_error_report > OBSERVER_ERROR_REPORT_SECONDS:
            self.last_error = message
            self.last_error_report = now
            self.app.events.put(("observer_error", message))

    def run_worker(self):
        generation = -1
        while not self.closing.is_set():
            try:
                if not self.active():
                    generation = -1
                    self.closing.wait(OBSERVER_WORKER_WAIT_SECONDS)
                    continue
                if self.generation != generation:
                    generation = self.generation
                    self.reset_window()
                    while True:
                        try:
                            self.queue.get_nowait()
                        except queue.Empty:
                            break
                if (self.hook_ready.is_set() and
                        (not self.hook_installed or time.monotonic() - self.last_hook_input > OBSERVER_HOOK_SILENCE_SECONDS)):
                    self.poll_input()
                hwnd = self.native.user.GetForegroundWindow()
                area = self.native.window_bounds(hwnd)
                if area is None:
                    if self.window is not None:
                        self.reset_window()
                    self.closing.wait(OBSERVER_WORKER_WAIT_SECONDS)
                    continue
                if hwnd != self.window or area != self.area:
                    self.reset_window(hwnd, area)
                now = time.monotonic()
                capture_interval = (OBSERVER_FRAME_INTERVAL_ACTIVE_SECONDS
                                    if now - self.last_input < OBSERVER_ACTIVE_WINDOW_SECONDS
                                    else OBSERVER_FRAME_INTERVAL_IDLE_SECONDS)
                if now - self.last_sample >= capture_interval:
                    frame = self.native.capture(area, OBSERVER_CAPTURE_EDGE)
                    self.samples.append((time.monotonic(), hwnd, area, frame))
                    self.last_sample = time.monotonic()
                for _ in range(OBSERVER_QUEUE_BATCH):
                    try:
                        entry = self.queue.get_nowait()
                    except queue.Empty:
                        break
                    self.accept(entry)
                now = time.monotonic()
                if self.pending_click is not None:
                    if now - self.pending_click[6] >= max(self.native.double_click_time, OBSERVER_SINGLE_CLICK_TIMEOUT_SECONDS):
                        self.finish_click()
                self.process_pending(now)
            except Exception as error:
                self.report_error(error)
                self.reset_window()
            self.closing.wait(OBSERVER_WORKER_WAIT_SECONDS)

    def close(self):
        self.activate(False)
        self.closing.set()
        self.hook_thread.join(timeout=KEYBOARD_SHUTDOWN_TIMEOUT_SECONDS)
        self.worker_thread.join(timeout=KEYBOARD_SHUTDOWN_TIMEOUT_SECONDS)


class Application:
    def __init__(self, root, native, tk, ttk, dialogs):
        self.root, self.native, self.tk, self.ttk, self.dialogs = root, native, tk, ttk, dialogs
        self.stop = threading.Event()
        self.stop.set()
        self.events = queue.SimpleQueue()
        self.store = None
        self.worker = None
        self.export_worker = None
        self.accelerator_worker = None
        self.accelerator_cancel = threading.Event()
        self.accelerator_generation = 0
        self.accelerator_status = "未检查"
        self.guard = KeyboardGuard(native, self.stop)
        self.guard_restart_pending = False
        self.running = False
        self.preparing = False
        self.steps = 0
        self.base_steps = 0
        self.reward = 0.0
        self.effect = 0.0
        self.visits = 0
        self.no_effect_steps = 0
        self.last_action = "—"
        self.vision_edge = VISION_LONG_EDGE
        self.vision_cost = None
        self.last_error = ""
        self.last_frame = None
        self.preview_image = None
        self.preview_source = None
        self.started_at = None
        self.log_lines = 0
        self.pending_after_ids = set()
        self.last_counts_check = 0.0
        self.last_theme_check = time.monotonic()
        self.last_target_preview_check = 0.0
        self.last_target_preview = None
        self.dark_mode = UI_BACKGROUND == UI_DARK_BACKGROUND
        self.folder = tk.StringVar(value="尚未选择文件夹")
        self.download_percent = tk.DoubleVar(value=0.0)
        self.last_external_window = None
        self.last_external_identity = None
        self.selected_game_id = None
        self.last_target = None
        self.last_target_caption = ""
        self.last_selection = None
        self.initial_target_window = None
        self.initial_target_area = None
        self.root_hwnd = None
        self.status = tk.StringVar(value="请选择文件夹；选定之前不会创建数据文件")
        self.target_text = tk.StringVar(value="自动目标：等待识别游戏窗口")
        self.step_text = tk.StringVar(value="0")
        self.reward_text = tk.StringVar(value="0.0000")
        self.no_effect_text = tk.StringVar(value="0")
        self.action_text = tk.StringVar(value="—")
        self.states_text = tk.StringVar(value="0")
        self.demonstration_text = tk.StringVar(value="0")
        self.vision_text = tk.StringVar(value=str(VISION_LONG_EDGE))
        self.runtime_text = tk.StringVar(value="00:00")
        self.rate_text = tk.StringVar(value="0.0/分")
        self.create_ui()
        self.observer = PassiveMouseObserver(self)
        root.protocol("WM_DELETE_WINDOW", self.close)
        root.report_callback_exception = self.ui_error
        self.schedule(UI_TICK_MS, self.tick)
        self.root.after_idle(self.select_folder)

    def schedule(self, milliseconds, callback):
        token = None
        def invoke():
            self.pending_after_ids.discard(token)
            callback()
        token = self.root.after(milliseconds, invoke)
        self.pending_after_ids.add(token)
        return token

    def apply_styles(self):
        styles = self.styles
        styles.configure("TFrame", background=UI_BACKGROUND)
        styles.configure("Card.TFrame", background=UI_CARD, relief="solid", bordercolor=UI_BORDER)
        styles.configure("TLabel", background=UI_BACKGROUND, foreground=UI_FOREGROUND, font=("Microsoft YaHei UI", UI_FONT_BASE))
        styles.configure("Muted.TLabel", foreground=UI_MUTED)
        styles.configure("Heading.TLabel", font=("Microsoft YaHei UI", UI_FONT_TITLE, "bold"), foreground=UI_FOREGROUND)
        styles.configure("Metric.TLabel", font=("Segoe UI", UI_FONT_METRIC, "bold"), foreground=UI_ACCENT, background=UI_CARD)
        styles.configure("Card.TLabel", background=UI_CARD)
        styles.configure("CardMuted.TLabel", background=UI_CARD, foreground=UI_MUTED)
        styles.configure("TButton", padding=(UI_SPACING_MD, UI_SPACING_BUTTON), font=("Microsoft YaHei UI", UI_FONT_BASE), background=UI_CARD, foreground=UI_FOREGROUND)
        styles.map("TButton", background=[("active", UI_BORDER)])
        styles.configure("Primary.TButton", background=UI_ACCENT, foreground=UI_DARK_BACKGROUND if self.dark_mode else UI_CARD)
        styles.map("Primary.TButton", background=[("active", UI_ACCENT), ("disabled", UI_BORDER)], foreground=[("disabled", UI_MUTED)])
        styles.configure("TLabelframe", background=UI_BACKGROUND, foreground=UI_FOREGROUND)
        styles.configure("TLabelframe.Label", background=UI_BACKGROUND, foreground=UI_FOREGROUND)

    def refresh_theme(self):
        now = time.monotonic()
        if now - self.last_theme_check < UI_THEME_REFRESH_SECONDS:
            return
        self.last_theme_check = now
        dark = set_system_palette()
        if dark == self.dark_mode:
            return
        self.dark_mode = dark
        self.root.configure(background=UI_BACKGROUND)
        self.apply_styles()
        self.preview_canvas.configure(background=UI_CARD)
        self.log_view.configure(background=UI_CARD, foreground=UI_FOREGROUND, insertbackground=UI_FOREGROUND, selectbackground=UI_ACCENT)
        self.draw_preview()

    def create_ui(self):
        root, ttk = self.root, self.ttk
        root.title(APP_NAME)
        wanted_width, wanted_height = (int(value) for value in WINDOW_GEOMETRY.split("x"))
        width = max(1, min(wanted_width, root.winfo_screenwidth(), max(UI_COMPACT_MIN_WIDTH, round(root.winfo_screenwidth() * UI_FIT_WIDTH_RATIO))))
        height = max(1, min(wanted_height, root.winfo_screenheight(), max(UI_COMPACT_MIN_HEIGHT, round(root.winfo_screenheight() * UI_FIT_HEIGHT_RATIO))))
        root.geometry(f"{width}x{height}")
        root.minsize(min(WINDOW_MIN_WIDTH, width), min(WINDOW_MIN_HEIGHT, height))
        root.configure(background=UI_BACKGROUND)
        self.styles = ttk.Style(root)
        self.styles.theme_use("clam")
        self.apply_styles()
        body = ttk.Frame(root, padding=UI_SPACING_LG)
        body.pack(fill="both", expand=True)
        self.wrap_labels = []
        self.last_responsive_layout = None
        body.bind("<Configure>", self.responsive_layout)
        ttk.Label(body, text=APP_NAME, style="Heading.TLabel").pack(anchor="w")
        self.wrapped_label(body, text="单文件 · 离线可运行 · 智能下载 · 对象定位与鼠标示范 · 外观迁移学习 · 状态规划 · 任意键停止", style="Muted.TLabel", wraplength=UI_WRAP_HEADER).pack(anchor="w", pady=(UI_SPACING_FINE, UI_SPACING_XS))
        self.wrapped_label(body, textvariable=self.status, wraplength=UI_WRAP_HEADER).pack(anchor="w", pady=(0, UI_SPACING_SM))
        self.download_bar = ttk.Progressbar(body, mode="determinate", maximum=PERCENT_SCALE, variable=self.download_percent)
        folder_row = ttk.Frame(body)
        self.folder_row = folder_row
        folder_row.pack(fill="x", pady=(0, UI_SPACING_SM))
        folder_row.bind("<Configure>", self.fit_text)
        ttk.Label(folder_row, text="数据目录：", style="Muted.TLabel").pack(side="left")
        self.wrapped_label(folder_row, textvariable=self.folder, wraplength=UI_WRAP_HINT).pack(side="left", fill="x", expand=True)
        self.folder_button = ttk.Button(folder_row, text="选择文件夹", command=self.select_folder)
        self.folder_button.pack(side="right")
        self.wrapped_label(body, textvariable=self.target_text, style="Muted.TLabel", wraplength=UI_WRAP_HEADER).pack(anchor="w", pady=(0, UI_SPACING_SM))
        metrics = ttk.Frame(body)
        metrics.pack(fill="x", pady=(0, UI_SPACING_XS))
        for column in range(UI_METRIC_COLUMNS):
            metrics.grid_columnconfigure(column, weight=1, uniform="metric")
        self.metrics = metrics
        self.metric_tiles = []
        for index, (heading, variable) in enumerate((("累计操作", self.step_text), ("用户示范", self.demonstration_text), ("最近动作", self.action_text), ("累计场景", self.states_text), ("视觉奖励", self.reward_text), ("连续无效", self.no_effect_text), ("视觉长边", self.vision_text), ("运行时间", self.runtime_text), ("操作速率", self.rate_text))):
            tile = ttk.Frame(metrics, padding=UI_SPACING_SM, style="Card.TFrame")
            self.metric_tiles.append(tile)
            tile.grid(row=index // UI_METRIC_COLUMNS, column=index % UI_METRIC_COLUMNS, sticky="nsew", padx=UI_SPACING_FINE, pady=UI_SPACING_FINE)
            ttk.Label(tile, text=heading, style="CardMuted.TLabel").pack(anchor="w")
            ttk.Label(tile, textvariable=variable, style="Metric.TLabel").pack(anchor="w")
        controls = ttk.Frame(body)
        controls.pack(fill="x", pady=(UI_SPACING_SM, UI_SPACING_XS))
        self.start_button = ttk.Button(controls, text="启动", style="Primary.TButton", command=self.start, state="disabled")
        self.start_button.pack(side="left", fill="x", expand=True, padx=(0, UI_SPACING_SM))
        self.blackbox_button = ttk.Button(controls, text="黑匣子", command=self.blackbox, state="disabled")
        self.blackbox_button.pack(side="right")
        self.wrapped_label(body, text="选择文件夹 → 在前台游戏窗口被动学习你的鼠标示范及操作结果（不保存原始示范画面）→ 点击启动后隐藏界面，Agent 结合视觉对象位置、示范轨迹、跨场景操作经验和状态转换自行操作 → 按任意键停止；黑匣子仅在点击后导出。", style="Muted.TLabel", wraplength=UI_WRAP_HELP).pack(anchor="w", pady=(0, UI_SPACING_SM))
        panels = ttk.Frame(body)
        panels.pack(fill="both", expand=True)
        panels.grid_columnconfigure(0, weight=1, uniform="panel")
        panels.grid_columnconfigure(1, weight=1, uniform="panel")
        panels.grid_rowconfigure(0, weight=1)
        self.panels = panels
        photo_box = ttk.LabelFrame(panels, text="最近采样画面")
        self.photo_box = photo_box
        photo_box.grid(row=0, column=0, sticky="nsew", padx=(0, UI_SPACING_XS))
        self.preview_canvas = self.tk.Canvas(photo_box, bg=UI_CARD, highlightthickness=0, height=UI_PREVIEW_MIN_HEIGHT)
        self.preview_canvas.pack(fill="both", expand=True, padx=UI_SPACING_SM, pady=UI_SPACING_SM)
        self.preview_canvas.bind("<Configure>", self.draw_preview)
        records = ttk.LabelFrame(panels, text="运行记录（最新）")
        self.records_box = records
        records.grid(row=0, column=1, sticky="nsew", padx=(UI_SPACING_XS, 0))
        self.log_view = self.tk.Text(records, wrap="word", state="disabled", height=UI_LOG_VISIBLE_ROWS, width=UI_LOG_VISIBLE_COLUMNS, bg=UI_CARD, fg=UI_FOREGROUND, relief="flat", padx=UI_SPACING_SM, pady=UI_SPACING_SM, font=("Consolas", UI_FONT_BASE), cursor="arrow")
        self.log_view.pack(fill="both", expand=True, padx=UI_SPACING_XS, pady=UI_SPACING_XS)
        self.draw_preview()
        self.root.after_idle(self.responsive_layout)
        self.log("控制台已创建；等待选择文件夹")

    def wrapped_label(self, parent, **kwargs):
        label = self.ttk.Label(parent, **kwargs)
        self.wrap_labels.append(label)
        return label

    def fit_text(self, event=None):
        for label in self.wrap_labels:
            if not label.winfo_exists():
                continue
            width = max(UI_WRAP_MINIMUM, label.master.winfo_width() - UI_SPACING_SECTION - UI_SPACING_MD)
            if int(label.cget("wraplength")) != width:
                label.configure(wraplength=width)


    def responsive_layout(self, event=None):
        self.fit_text()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        compact = height < UI_METRIC_COMPACT_HEIGHT
        columns = UI_METRIC_COMPACT_COLUMNS if width < UI_METRIC_COMPACT_WIDTH else UI_METRIC_COLUMNS
        stack = width < UI_PANEL_STACK_WIDTH
        layout = (compact, columns, stack)
        if layout == self.last_responsive_layout:
            return
        self.last_responsive_layout = layout
        for tile in self.metric_tiles:
            tile.grid_forget()
        for column in range(UI_METRIC_COLUMNS):
            self.metrics.grid_columnconfigure(column, weight=int(column < columns))
        for index, tile in enumerate(self.metric_tiles[:UI_COMPACT_METRIC_COUNT] if compact else self.metric_tiles):
            tile.grid(row=index // columns, column=index % columns, sticky="nsew", padx=UI_SPACING_FINE, pady=UI_SPACING_FINE)
        self.photo_box.grid_forget()
        self.records_box.grid_forget()
        if stack:
            self.panels.grid_columnconfigure(0, weight=1)
            self.panels.grid_columnconfigure(1, weight=0)
            self.panels.grid_rowconfigure(0, weight=1)
            self.panels.grid_rowconfigure(1, weight=1)
            self.photo_box.grid(row=0, column=0, sticky="nsew", pady=(0, UI_SPACING_XS))
            self.records_box.grid(row=1, column=0, sticky="nsew", pady=(UI_SPACING_XS, 0))
        else:
            self.panels.grid_columnconfigure(0, weight=1)
            self.panels.grid_columnconfigure(1, weight=1)
            self.panels.grid_rowconfigure(0, weight=1)
            self.panels.grid_rowconfigure(1, weight=0)
            self.photo_box.grid(row=0, column=0, sticky="nsew", padx=(0, UI_SPACING_XS))
            self.records_box.grid(row=0, column=1, sticky="nsew", padx=(UI_SPACING_XS, 0))

    def log(self, message):
        self.log_view.configure(state="normal")
        self.log_view.insert("end", datetime.datetime.now().strftime("%H:%M:%S") + "  " + message + "\n")
        self.log_lines += 1
        if self.log_lines > UI_LOG_LIMIT:
            self.log_view.delete("1.0", "2.0")
            self.log_lines -= 1
        self.log_view.see("end")
        self.log_view.configure(state="disabled")

    def ui_error(self, kind, value, tb):
        self.last_error = "".join(traceback.format_exception(kind, value, tb))
        self.status.set("界面异常：" + str(value))
        self.log("界面异常：" + str(value))
        if self.store:
            self.store.event("ui_error", self.last_error)

    def select_folder(self):
        if self.running or self.preparing or self.any_background_worker():
            return
        self.observer.activate(False)
        initial = self.folder.get() if self.store else str(Path.home())
        location = self.dialogs.askdirectory(parent=self.root, initialdir=initial, title="选择 Agent 数据存储文件夹")
        if not location:
            if self.store:
                self.observer.activate(True)
            if not self.store:
                self.status.set("请选择文件夹后再启动；尚未写入任何数据文件")
            return
        self.preparing = True
        self.folder_button.configure(state="disabled")
        self.start_button.configure(state="disabled")
        self.blackbox_button.configure(state="disabled")
        self.status.set("正在初始化所选文件夹…")
        threading.Thread(target=self.prepare, args=(location,), daemon=True, name="storage-init").start()

    def prepare(self, directory):
        store = None
        try:
            store = Store(directory)
            store.event("open", {"python": sys.version, "bounds": self.native.bounds()})
            self.events.put(("store_ready", (store, directory)))
        except Exception as error:
            if store is not None:
                store.close()
            self.events.put(("store_failed", str(error)))

    def any_background_worker(self):
        return self.export_worker is not None and self.export_worker.is_alive()

    def find_target(self):
        recent = self.last_external_window
        if recent:
            area = self.native.window_bounds(recent)
            if area is not None and self.last_external_identity == (
                    self.native.window_owner(recent), self.native.game_id(recent)):
                return recent, area
        return self.native.foreground_window(self.root.winfo_id())

    def start(self):
        if self.running or self.preparing or self.any_background_worker() or not self.store or not self.guard.ready.is_set() or not self.guard.thread.is_alive():
            return
        self.last_error = ""
        try:
            self.base_steps = self.store.counts()[1]
        except sqlite3.Error as error:
            self.last_error = str(error)
            self.base_steps = 0
        self.steps = 0
        self.reward = 0.0
        self.effect = 0.0
        self.visits = 0
        self.no_effect_steps = 0
        self.last_action = "—"
        self.vision_edge = VISION_LONG_EDGE
        self.vision_cost = None
        self.vision_text.set(str(self.vision_edge))
        self.rate_text.set("0.0/分")
        self.last_frame = None
        self.preview_image = None
        self.preview_source = None
        self.last_target = None
        self.last_target_caption = ""
        self.last_selection = None
        self.draw_preview()
        self.reward_text.set("0.0000")
        self.no_effect_text.set("0")
        self.action_text.set("—")
        self.started_at = time.monotonic()
        self.running = True
        self.observer.activate(False)
        self.start_button.configure(state="disabled")
        self.folder_button.configure(state="disabled")
        self.blackbox_button.configure(state="disabled")
        self.root_hwnd = self.root.winfo_id()
        try:
            self.initial_target_window, self.initial_target_area = self.find_target()
            self.selected_game_id = self.native.game_id(self.initial_target_window) if self.initial_target_window else None
        except Exception:
            self.last_error = traceback.format_exc()
            self.initial_target_window, self.initial_target_area = None, None
            self.selected_game_id = None
        self.guard.arm()
        self.root.withdraw()
        self.root.update_idletasks()
        if self.initial_target_window is not None:
            try:
                self.native.activate_window(self.initial_target_window)
            except Exception as error:
                self.log("游戏窗口激活暂不可用，Agent 将自动恢复：" + str(error))
        self.status.set("Agent 运行中；按任意键停止")
        try:
            self.worker = threading.Thread(target=self.run_agent, daemon=True, name="mouse-game-agent")
            self.worker.start()
        except Exception as error:
            self.stop.set()
            self.guard.armed.clear()
            self.running = False
            self.observer.activate(True)
            self.started_at = None
            self.root.deiconify()
            self.start_button.configure(state="normal")
            self.folder_button.configure(state="normal")
            self.blackbox_button.configure(state="normal")
            self.status.set("无法启动 Agent：" + str(error))
            self.log("Agent 启动失败：" + str(error))

    def run_agent(self):
        try:
            while not self.stop.is_set():
                try:
                    self.agent_session()
                except Exception:
                    self.last_error = traceback.format_exc()
                    self.events.put(("agent_error", "Agent 运行循环发生异常，自动恢复：" + self.last_error.splitlines()[-1]))
                    if self.store:
                        self.store.event("session_restart", self.last_error)
                    try:
                        self.native.release()
                    except Exception:
                        if self.store:
                            self.store.event("release_error", traceback.format_exc())
                    self.stop.wait(ERROR_RETRY_SECONDS)
        finally:
            self.native.active_target_window = None
            self.native.active_target_owner = None
            try:
                self.native.release()
            except Exception:
                self.last_error = traceback.format_exc()
                if self.store:
                    self.store.event("release_error", self.last_error)
            if self.store:
                self.store.event("stop", {"steps": self.steps, "keyboard_stop": self.stop.is_set()})
            self.events.put(("agent_finished", self.steps))

    def agent_session(self):
        global NUMPY_ACCELERATOR
        policy = VisionPolicy(self.store)
        previous = None
        vision_failures = 0
        last_reported_error = ""
        last_error_report = 0.0
        area = self.initial_target_area
        window = self.initial_target_window
        window_owner = self.native.window_owner(window) if window else None
        last_known_owner = window_owner
        last_target_check = 0.0
        try:
            self.stop.wait(SCREEN_HIDE_SETTLE_SECONDS)
            try:
                if window is None:
                    if self.selected_game_id:
                        window, area = self.native.window_by_game_id(self.selected_game_id)
                    else:
                        window, area = self.native.foreground_window(self.root_hwnd)
                if window is not None:
                    self.native.activate_window(window)
                    area = self.native.window_bounds(window) or area
                    policy.reset_scene(self.native.game_id(window))
                    self.selected_game_id = policy.game_id
                    self.last_target_caption = self.native.window_caption(window)
                    window_owner = self.native.window_owner(window)
                    last_known_owner = window_owner
                self.last_target = area
                self.events.put(("target_info", (self.last_target_caption, area)))
                self.store.event("start", {"time": utc_stamp(), "monitor_bounds": self.native.bounds(), "window_bounds": area, "game_id": policy.game_id, "window_title": self.last_target_caption, "mouse_only": True})
            except Exception:
                self.last_error = traceback.format_exc()
                self.store.event("initialization_error", self.last_error)
                self.events.put(("agent_error", self.last_error.splitlines()[-1]))
            while not self.stop.is_set():
                started = time.monotonic()
                vision_stage = False
                try:
                    if window is not None and started - last_target_check >= RECOVER_WINDOW_EVERY_SECONDS:
                        last_target_check = started
                        if self.native.window_owner(window) != window_owner:
                            window, area, window_owner = None, None, None
                            last_target_check = 0.0
                            self.native.active_target_window = None
                            self.native.active_target_owner = None
                    if window is not None:
                        refreshed = self.native.window_bounds(window)
                        if refreshed is None:
                            self.native.activate_window(window)
                            refreshed = self.native.window_bounds(window)
                            if refreshed is None:
                                window, area, window_owner = None, None, None
                        if refreshed is not None:
                            if area != refreshed:
                                policy.prior = None
                                policy.background_ema = None
                                previous = None
                            area = refreshed
                            self.last_target = refreshed
                            if not self.native.activate_window(window):
                                raise OSError("目标窗口暂时无法取得前台焦点，自动重试以避免误点其他窗口")
                    if window is None and started - last_target_check >= RECOVER_WINDOW_EVERY_SECONDS:
                        last_target_check = started
                        if self.selected_game_id:
                            window, area = self.native.window_by_game_id(self.selected_game_id, last_known_owner)
                        else:
                            window, area = self.native.foreground_window(self.root_hwnd)
                        if window is not None:
                            self.native.activate_window(window)
                            window_owner = self.native.window_owner(window)
                            last_known_owner = window_owner
                            policy.reset_scene(self.native.game_id(window))
                            previous = None
                            self.selected_game_id = policy.game_id
                            self.last_target_caption = self.native.window_caption(window)
                            self.events.put(("target_info", (self.last_target_caption, area)))
                    if window is None:
                        raise OSError("目标游戏窗口暂时不可用，持续尝试重新定位")
                    self.last_target = area
                    vision_started = time.monotonic()
                    vision_stage = True
                    before = self.native.capture(area, self.vision_edge)
                    context, coarse_context, cell, spot, action, x, y, to_x, to_y, to_cell, variant, demonstration_id = policy.pick(before)
                    decision_cost = time.monotonic() - vision_started
                    background = (SPOT_CHANGE_WEIGHT * policy.difference(previous, before, cell, spot)
                                  + REGION_CHANGE_WEIGHT * policy.difference(previous, before, cell)
                                  + GLOBAL_CHANGE_WEIGHT * policy.difference(previous, before))
                    if not self.native.target_is_foreground(window):
                        raise OSError("游戏失去前台焦点，正在重新获取以防止误点其他程序")
                    if self.native.window_bounds(window) != before.bounds:
                        raise OSError("游戏窗口在分析画面后发生变化，重新捕获以避免错误操作")
                    self.native.active_target_window = window
                    self.native.active_target_owner = window_owner
                    vision_stage = False
                    try:
                        self.native.action(action, x, y, to_x, to_y, self.stop, before.bounds,
                                           variant, policy.last_demonstration_duration if demonstration_id is not None else None,
                                           policy.last_demonstration_path if demonstration_id is not None else "")
                    finally:
                        self.native.active_target_window = None
                        self.native.active_target_owner = None
                    if self.stop.wait(ACTION_SETTLE_SECONDS):
                        break
                    response_started = time.monotonic()
                    vision_stage = True
                    if not self.native.target_is_foreground(window) or self.native.window_bounds(window) != before.bounds:
                        raise OSError("目标窗口焦点或尺寸变化，丢弃本次反馈")
                    after = self.native.capture(before.bounds, self.vision_edge)
                    response_cost = time.monotonic() - response_started
                    for delay in ACTION_FEEDBACK_RECHECK_SECONDS:
                        if policy.difference(before, after) >= SNAPSHOT_RECHECK_THRESHOLD:
                            break
                        if self.stop.wait(delay):
                            return
                        if not self.native.target_is_foreground(window) or self.native.window_bounds(window) != before.bounds:
                            raise OSError("目标窗口焦点或尺寸变化，丢弃本次反馈")
                        response_started = time.monotonic()
                        after = self.native.capture(before.bounds, self.vision_edge)
                        response_cost += time.monotonic() - response_started
                    if self.stop.is_set():
                        return
                    if (not self.native.target_is_foreground(window)
                            or self.native.window_bounds(window) != before.bounds
                            or (window_owner is not None and self.native.window_owner(window) != window_owner)):
                        raise OSError("反馈截图不再属于选定游戏窗口，已避免错误学习")
                    learning_started = time.monotonic()
                    score, effect, visits = policy.update(context, cell, spot, action, before, after, background, coarse_context, to_cell, variant, to_x, to_y, demonstration_id, x, y)
                    vision_stage = False
                    vision_failures = 0
                    vision_cost = decision_cost + response_cost + time.monotonic() - learning_started
                    self.vision_cost = (vision_cost if self.vision_cost is None else
                                        (1 - VISION_COST_EMA_WEIGHT) * self.vision_cost + VISION_COST_EMA_WEIGHT * vision_cost)
                    previous = after
                    self.reward = score
                    self.effect = effect
                    self.visits = visits
                    self.no_effect_steps = policy.no_effect_steps
                    self.steps += 1
                    actual_parameter = (policy.last_demonstration_duration if demonstration_id is not None
                                        and policy.last_demonstration_duration is not None
                                        and action not in ("上滚", "下滚") else
                                        ACTION_PARAMETERS[action][variant] if variant is not None else None)
                    self.last_action = action if actual_parameter is None else f"{action}({actual_parameter:g})"
                    if demonstration_id is not None:
                        self.last_action = "示范·" + self.last_action
                    self.last_frame = after
                    self.last_selection = (x, y, to_x, to_y, action)
                    self.store.event("action", {"index": self.steps, "context": context, "coarse_context": coarse_context, "cell": cell, "spot": spot, "action": action, "parameter": actual_parameter, "from": [x, y], "to": [to_x, to_y], "destination_cell": to_cell if action in ACTION_DESTINATION_ACTIONS else None, "bounds": before.bounds, "visual_effect": effect, "visual_reward": score, "demonstration_id": demonstration_id, "demonstration_goal_progress": policy.last_goal_progress if demonstration_id is not None else None, "state_visits": visits, "elapsed": time.monotonic() - started, "vision_long_edge": self.vision_edge})
                    if self.steps % VISION_ADAPT_EVERY_STEPS == 0:
                        maximum = min(VISION_ADAPTIVE_MAX_EDGE, max(VISION_ADAPTIVE_MIN_EDGE, max(before.bounds[2:])))
                        if self.vision_cost < VISION_PROCESS_BUDGET_LOW_SECONDS:
                            updated = min(maximum, self.vision_edge + VISION_RESOLUTION_STEP)
                        elif self.vision_cost > VISION_PROCESS_BUDGET_HIGH_SECONDS:
                            updated = max(VISION_ADAPTIVE_MIN_EDGE, self.vision_edge - VISION_RESOLUTION_STEP)
                        else:
                            updated = self.vision_edge
                        if updated != self.vision_edge:
                            self.vision_edge = updated
                            policy.prior = None
                            policy.background_ema = None
                            previous = None
                            self.events.put(("vision_resolution", updated))
                    if self.steps % REPORT_EVERY_STEPS == 0:
                        self.events.put(("stats", (self.steps, score, self.last_action, effect, self.no_effect_steps)))
                except Exception as error:
                    self.last_error = traceback.format_exc()
                    error_kind = self.last_error.splitlines()[-1]
                    vision_failures = vision_failures + 1 if vision_stage else 0
                    if vision_failures >= VISION_ACCELERATOR_FAILURE_LIMIT and NUMPY_ACCELERATOR is not None:
                        NUMPY_ACCELERATOR = None
                        self.accelerator_status = "fallback · 视觉加速异常，已切换内置处理"
                        self.events.put(("agent_error", self.accelerator_status))
                        vision_failures = 0
                    if isinstance(error, MemoryError) or getattr(error, "winerror", None) in (WINERROR_NOT_ENOUGH_MEMORY, WINERROR_OUTOFMEMORY):
                        self.vision_edge = max(VISION_MIN_EDGE, self.vision_edge // 2)
                        self.events.put(("vision_resolution", self.vision_edge))
                    now = time.monotonic()
                    if error_kind != last_reported_error or now - last_error_report >= ERROR_REPORT_SECONDS:
                        self.store.event("recoverable_error", self.last_error)
                        self.events.put(("agent_error", error_kind))
                        last_reported_error, last_error_report = error_kind, now
                    policy.prior = None
                    policy.background_ema = None
                    previous = None
                    try:
                        self.native.release()
                    except Exception:
                        self.store.event("release_error", traceback.format_exc())
                    self.stop.wait(ERROR_RETRY_SECONDS)
        finally:
            self.native.active_target_window = None
            self.native.active_target_owner = None

    def lower_topmost(self):
        if self.root.winfo_exists():
            self.root.attributes("-topmost", False)

    def show_preview(self):
        if self.last_frame is None:
            return
        try:
            self.preview_source = self.tk.PhotoImage(data=self.last_frame.ppm(), format="PPM")
            self.draw_preview()
        except Exception as error:
            self.log("预览不可用：" + str(error))

    def draw_preview(self, event=None):
        canvas = self.preview_canvas
        canvas.delete("all")
        if self.preview_source is None or self.last_frame is None:
            canvas.create_text(UI_PREVIEW_PLACEHOLDER_MARGIN, UI_PREVIEW_PLACEHOLDER_MARGIN, text="最近采样画面在停止后显示", fill=UI_MUTED, anchor="nw")
            return
        source = self.preview_source
        available_width = max(1, canvas.winfo_width())
        available_height = max(1, canvas.winfo_height() - UI_PREVIEW_LABEL_HEIGHT)
        scale = min(available_width / source.width(), available_height / source.height())
        if scale >= PREVIEW_ZOOM:
            self.preview_image = source.zoom(PREVIEW_ZOOM)
        elif scale >= 1:
            self.preview_image = source
        else:
            self.preview_image = source.subsample(max(1, math.ceil(1 / scale)))
        width = self.preview_image.width()
        height = self.preview_image.height()
        x0 = max(0, (canvas.winfo_width() - width) // 2)
        y0 = max(0, (available_height - height) // 2)
        canvas.create_image(x0, y0, image=self.preview_image, anchor="nw")
        if self.last_selection is not None:
            x, y, to_x, to_y, action = self.last_selection
            p_x = x0 + round(x * width)
            p_y = y0 + round(y * height)
            if action in ACTION_DESTINATION_ACTIONS:
                p_to_x = x0 + round(to_x * width)
                p_to_y = y0 + round(to_y * height)
                canvas.create_line(p_x, p_y, p_to_x, p_to_y, fill=UI_ACCENT, width=PREVIEW_ZOOM, arrow="last")
            canvas.create_oval(p_x - PREVIEW_ZOOM, p_y - PREVIEW_ZOOM, p_x + PREVIEW_ZOOM, p_y + PREVIEW_ZOOM, outline=UI_ACCENT, width=PREVIEW_ZOOM)
            canvas.create_text(x0, available_height, text="最后动作：" + action, fill=UI_MUTED, anchor="nw")

    def blackbox(self):
        if self.running or not self.store or self.any_background_worker():
            return
        info = {"created": utc_stamp(), "python": sys.version, "platform": sys.platform, "steps": self.steps, "reward": self.reward, "visual_effect": self.effect, "no_effect_steps": self.no_effect_steps, "last_action": self.last_action, "last_selection": self.last_selection, "last_state_visits": self.visits, "vision_long_edge": self.vision_edge, "vision_process_seconds": self.vision_cost, "last_error": self.last_error, "database_error": self.store.last_error, "accelerator": self.accelerator_status, "bounds": self.native.bounds(), "target_bounds": self.last_target, "target_caption": self.last_target_caption, "policy": "仅使用鼠标的视觉交互、按游戏隔离的在线学习、对象外观重定位及鼠标示范复用、外观条件化操作迁移、完整拖拽轨迹回放、人类示范驱动的状态转换规划、分层探索、TD 学习、动态采样与异常恢复；视觉变化和示范相似度均不等于游戏胜利；未使用第三方 AI 模型"}
        manifest = Path(self.folder.get()) / "dependencies" / ("numpy-" + python_abi()) / ACCELERATOR_METADATA_MARKER
        if manifest.is_file():
            try:
                info["accelerator_manifest"] = json.loads(manifest.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                info["accelerator_manifest"] = "无法读取"
        try:
            info["human_demonstrations"] = self.store.demonstration_counts()[0]
            edges, human, autonomous = self.store.behavioral_counts()
            info["transition_model"] = {"edges": edges, "human_transition_updates_across_resolutions": human, "autonomous_transition_updates_across_resolutions": autonomous}
        except sqlite3.Error as error:
            info["learning_counts_error"] = str(error)
        info["mouse_observation_hook"] = "enabled" if self.observer.hook_installed else self.observer.hook_error
        preview = self.last_frame.ppm() if self.last_frame else None
        self.blackbox_button.configure(state="disabled")
        self.start_button.configure(state="disabled")
        self.folder_button.configure(state="disabled")
        self.status.set("正在生成黑匣子…")
        store = self.store
        def worker():
            try:
                target = store.export(self.native.desktop(), info, preview)
                message = "黑匣子已保存到桌面：" + str(target)
            except Exception as error:
                message = "黑匣子导出失败：" + str(error)
            self.events.put(("export_finished", message))
        self.export_worker = threading.Thread(target=worker, daemon=True, name="blackbox-export")
        self.export_worker.start()

    def tick(self):
        try:
            self.tick_body()
        except Exception:
            try:
                self.ui_error(*sys.exc_info())
            except Exception:
                pass
        finally:
            try:
                if self.root.winfo_exists():
                    self.schedule(UI_TICK_MS, self.tick)
            except Exception:
                pass

    def update_target_preview(self):
        hwnd = self.last_external_window
        if not hwnd or self.native.window_bounds(hwnd) is None:
            hwnd, _ = self.native.foreground_window(self.root.winfo_id())
        area = self.native.window_bounds(hwnd)
        if area is None:
            target = "自动目标：等待可用的游戏窗口"
        else:
            caption = self.native.window_caption(hwnd) or self.native.window_class(hwnd)
            target = "自动目标：" + caption[:WINDOW_DISPLAY_NAME_LIMIT] + " · " + str(area)
        if target != self.last_target_preview:
            self.last_target_preview = target
            self.target_text.set(target)

    def tick_body(self):
        self.refresh_theme()
        if not self.running:
            candidate = self.native.user.GetForegroundWindow()
            if candidate and self.native.window_bounds(candidate) is not None and self.native.window_class(candidate) not in WINDOW_IGNORED_CLASSES:
                if candidate != self.last_external_window:
                    self.last_external_identity = (self.native.window_owner(candidate), self.native.game_id(candidate))
                self.last_external_window = candidate
            current = time.monotonic()
            if current - self.last_target_preview_check >= UI_TARGET_DISCOVERY_SECONDS:
                self.last_target_preview_check = current
                try:
                    self.update_target_preview()
                except OSError as error:
                    self.log("目标窗口识别暂不可用：" + str(error))
        if not self.guard.thread.is_alive() and (not self.running or not self.stop.is_set()):
            if self.running:
                try:
                    for key in KEYBOARD_KEYS:
                        if self.native.user.GetAsyncKeyState(key) & (KEY_DOWN_MASK | KEY_PRESSED_MASK):
                            self.stop.set()
                            break
                except Exception:
                    pass
            if not self.running or not self.stop.is_set():
                self.guard = KeyboardGuard(self.native, self.stop)
                self.guard_restart_pending = self.running
                self.log("键盘停止监听线程已重新建立")
        if self.guard_restart_pending and self.guard.ready.is_set() and self.guard.thread.is_alive():
            if not self.stop.is_set():
                self.guard.arm(reset_stop=False)
            self.guard_restart_pending = False
        processed = 0
        while processed < UI_LOG_LIMIT:
            try:
                kind, content = self.events.get_nowait()
            except queue.Empty:
                break
            processed += 1
            if kind == "store_ready":
                store, directory = content
                prior = self.store
                self.store = store
                if prior is not None:
                    prior.close()
                self.folder.set(directory)
                self.preparing = False
                self.base_steps = 0
                self.steps = 0
                self.reward = 0.0
                self.effect = 0.0
                self.visits = 0
                self.no_effect_steps = 0
                self.last_action = "—"
                self.last_frame = None
                self.last_selection = None
                self.preview_source = None
                self.preview_image = None
                self.step_text.set("0")
                self.reward_text.set("0.0000")
                self.action_text.set("—")
                self.no_effect_text.set("0")
                self.runtime_text.set("00:00")
                self.rate_text.set("0.0/分")
                self.draw_preview()
                self.last_counts_check = 0.0
                try:
                    self.demonstration_text.set(str(store.demonstration_counts()[0]))
                except sqlite3.Error:
                    self.demonstration_text.set("0")
                self.observer.activate(True)
                self.status.set("一切就绪" + (" · " + self.guard.error if self.guard.error else "") + " · 后台检查视觉加速")
                self.log("数据目录就绪：" + directory)
                self.accelerator_cancel.set()
                self.download_bar.pack_forget()
                self.download_percent.set(0.0)
                self.accelerator_cancel = threading.Event()
                self.accelerator_generation += 1
                manager = AcceleratorManager(directory, store, self.events, self.accelerator_cancel, self.accelerator_generation)
                self.accelerator_worker = threading.Thread(target=manager.run, daemon=True, name="smart-download")
                self.accelerator_worker.start()
            elif kind == "store_failed":
                self.observer.activate(self.store is not None)
                self.preparing = False
                self.status.set("文件夹无法使用，请重新选择：" + content)
                self.log("数据目录初始化失败：" + content)
            elif kind == "accelerator":
                generation, stage, message, percent = content
                if generation == self.accelerator_generation:
                    self.accelerator_status = stage + " · " + message
                    if stage == "downloading":
                        self.download_percent.set(percent if percent is not None else 0)
                        if not self.download_bar.winfo_manager():
                            self.download_bar.pack(fill="x", pady=(0, UI_SPACING_XS), before=self.folder_row)
                    elif self.download_bar.winfo_manager():
                        self.download_bar.pack_forget()
                    if stage in ("ready", "fallback"):
                        if not self.running and not self.preparing:
                            self.status.set("一切就绪 · " + message)
                        self.log(message)
                    elif stage in ("checking", "recovering"):
                        self.log(message)
                    elif stage == "downloading" and not self.running and not self.preparing:
                        self.status.set("一切就绪 · " + message)
            elif kind == "observation":
                count, action = content
                try:
                    self.demonstration_text.set(str(self.store.demonstration_counts()[0]))
                except sqlite3.Error:
                    self.demonstration_text.set(str(count))
                if count % UI_DEMONSTRATION_LOG_INTERVAL == 0:
                    self.log(f"被动学习：已观察 {count} 次用户鼠标示范；最近动作 {action}")
            elif kind == "observer_error":
                self.log("用户示范观察异常，持续尝试恢复：" + content)
            elif kind == "stats":
                self.step_text.set(str(self.base_steps + content[0]))
                self.reward_text.set(f"{content[1]:+.4f}")
                self.action_text.set(content[2])
                self.no_effect_text.set(str(content[4]))
                self.log(f"操作 {content[0]} · {content[2]} · 奖励 {content[1]:+.4f} · 变化 {content[3]:.4f} · 连续无效 {content[4]}")
            elif kind == "vision_resolution":
                self.vision_text.set(str(content))
            elif kind == "target_info":
                caption, area = content
                self.target_text.set("自动目标：" + (caption if caption else "等待可用窗口") + " · " + (str(area) if area else "尚未定位"))
            elif kind == "agent_error":
                self.log("Agent 自动恢复：" + content)
            elif kind == "agent_finished":
                if not self.stop.is_set():
                    self.log("Agent 线程意外退出，正在自动重建运行线程")
                    try:
                        self.worker = threading.Thread(target=self.run_agent, daemon=True, name="mouse-game-agent-recovery")
                        self.worker.start()
                    except Exception as error:
                        self.last_error = traceback.format_exc()
                        self.events.put(("agent_error", "无法恢复 Agent 线程：" + str(error)))
                        self.schedule(ERROR_RETRY_MS, self.recover_agent_worker)
                    continue
                self.last_counts_check = 0.0
                self.running = False
                self.observer.activate(True)
                self.guard_restart_pending = False
                self.guard.armed.clear()
                if self.root.state() == "withdrawn":
                    self.root.deiconify()
                    self.root.lift()
                    self.root.attributes("-topmost", True)
                    self.schedule(UI_RESTORE_TOPMOST_MS, self.lower_topmost)
                self.step_text.set(str(self.base_steps + self.steps))
                self.reward_text.set(f"{self.reward:+.4f}")
                self.action_text.set(self.last_action)
                self.no_effect_text.set(str(self.no_effect_steps))
                self.show_preview()
                if self.started_at is not None:
                    elapsed = int(time.monotonic() - self.started_at)
                    self.runtime_text.set(f"{elapsed // SECONDS_PER_MINUTE:02d}:{elapsed % SECONDS_PER_MINUTE:02d}")
                    self.started_at = None
                self.status.set(f"已停止 · 本次 {self.steps} 次操作 · 最新视觉奖励 {self.reward:+.4f}")
                self.log("已停止；鼠标已释放；目标窗口：" + (self.last_target_caption or "未定位"))
            elif kind == "export_finished":
                self.status.set(content)
                self.log(content)
        ready = self.store is not None and not self.preparing and self.guard.ready.is_set() and self.guard.thread.is_alive()
        can_control = not self.running and not self.preparing and not self.any_background_worker()
        self.start_button.configure(state="normal" if ready and can_control else "disabled")
        self.blackbox_button.configure(state="normal" if self.store is not None and can_control else "disabled")
        self.folder_button.configure(state="normal" if can_control else "disabled")
        if self.store is not None and not self.running and not self.preparing and not self.guard.ready.is_set():
            self.status.set("等待键盘停止监听准备完成…")
        if self.store is not None and not self.running and not self.guard.thread.is_alive():
            self.start_button.configure(state="disabled")
            self.status.set("键盘停止监听不可用，无法启动 Agent")
        if self.started_at is not None:
            elapsed = time.monotonic() - self.started_at
            elapsed_seconds = int(elapsed)
            self.runtime_text.set(f"{elapsed_seconds // SECONDS_PER_MINUTE:02d}:{elapsed_seconds % SECONDS_PER_MINUTE:02d}")
            self.rate_text.set(f"{self.steps * SECONDS_PER_MINUTE / max(SPEED_TIME_FLOOR_SECONDS, elapsed):.1f}/分")
        if self.store is not None and not self.running and time.monotonic() - self.last_counts_check >= COUNTS_REFRESH_SECONDS:
            self.last_counts_check = time.monotonic()
            try:
                states, total = self.store.counts()
                self.states_text.set(str(states))
                self.step_text.set(str(max(total, self.base_steps + self.steps)))
            except sqlite3.Error as error:
                self.log("读取统计失败：" + str(error))

    def recover_agent_worker(self):
        if self.running and not self.stop.is_set() and (self.worker is None or not self.worker.is_alive()):
            try:
                self.worker = threading.Thread(target=self.run_agent, daemon=True, name="mouse-game-agent-recovery")
                self.worker.start()
                self.log("Agent 自动运行恢复成功")
            except Exception as error:
                self.log("Agent 运行恢复重试：" + str(error))
                self.schedule(ERROR_RETRY_MS, self.recover_agent_worker)

    def close(self):
        if self.running:
            return
        if self.preparing or self.any_background_worker():
            self.status.set("正在完成选定文件夹中的存储操作后关闭…")
            self.schedule(UI_TICK_MS, self.close)
            return
        self.observer.close()
        self.accelerator_cancel.set()
        if self.accelerator_worker is not None and self.accelerator_worker.is_alive():
            self.accelerator_worker.join(timeout=ACCELERATOR_STOP_WAIT_SECONDS)
        self.guard.close_event.set()
        self.guard.thread.join(timeout=KEYBOARD_SHUTDOWN_TIMEOUT_SECONDS)
        if self.store:
            self.store.close()
        for token in tuple(self.pending_after_ids):
            try:
                self.root.after_cancel(token)
            except self.tk.TclError:
                pass
        self.pending_after_ids.clear()
        self.root.destroy()



def main():
    if sys.platform != "win32" or C.sizeof(C.c_void_p) != WIN64_POINTER_BYTES:
        raise SystemExit("此文件需要 Windows 11 x64 与 64 位 Python。")
    if sys.version_info < MINIMUM_PYTHON:
        raise SystemExit("请使用 Python 3.10 或更新的 64 位版本。")
    try:
        import tkinter as tk
        from tkinter import filedialog, ttk
        set_system_palette()
        native = Native()
        root = tk.Tk()
        Application(root, native, tk, ttk, filedialog)
        root.mainloop()
    except Exception:
        C.windll.user32.MessageBoxW(None, traceback.format_exc(), APP_NAME, 0)


if __name__ == "__main__":
    main()
