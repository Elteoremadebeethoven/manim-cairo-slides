from slides import *

#  ____  _     ___ ____  _____   _ 
# / ___|| |   |_ _|  _ \| ____| / |
# \___ \| |    | || | | |  _|   | |
#  ___) | |___ | || |_| | |___  | |
# |____/|_____|___|____/|_____| |_|
                                 

class Slide1_test1(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        #                    v   TEXT_INDEX, line 1 
        "index_paragraphs": [0], # (LN-1)
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\flushleft",
        # "alignment": "\\flushright",
        # "alignment": "\\centering",
        # "alignment": "\\jusfity",
        "justify_length": 5, # Width of the paragraphs
    }

class Slide1_test2(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        #                    v   TEXT_INDEX
        "index_paragraphs": [0],
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\flushleft",
        "colored_text": [
        #    v  TEXT_INDEX
            (0, [RED, 18, 21]),
            (0, [ORANGE, 87, 92]),
            (0, [ORANGE, 148, 154]),
            # You can add all the lists that are necessary,
            # this method is efficient when the following
            # method does not work.
        ],
    }

class Slide1_test3(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        #                    v   TEXT_INDEX
        "index_paragraphs": [0],
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\flushright",
        "tex_to_color_map": {
            "amet": RED,
            "dolore": ORANGE,
            "ullamco": ORANGE,
            # However, this method can cause problems
            # with punctuation marks, when that happens 
            # use the previous method.
        },
    }
    
# The structure of the animations are as follows:
# 1. Pause before entering, default is 0.1
# 2. Entrance animations
# 3. Pause before leaving
# 4. Exit animations

class Slide1(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [0],
        "test_code": False, # Animation activated
        "alignment": "\\flushleft",
        "tex_to_color_map": {
            "amet": RED,
            "dolore": ORANGE,
            "ullamco": ORANGE,
        },
        # Animation CONFIG
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FadeInFromBlackRectangle",
        "animation_kwargs_in": {
            "run_time": 6
        },
        # Before OUT:
        "pause_before_remove": 2.5,
        # --- Animation OUT CONFIG
        "animation_out": "FadeOutToBlackRectangle",
        "animation_kwargs_out": {
            "run_time": 1.5
        },
    }

#  ____  _     ___ ____  _____   ____  
# / ___|| |   |_ _|  _ \| ____| |___ \ 
# \___ \| |    | || | | |  _|     __) |
#  ___) | |___ | || |_| | |___   / __/ 
# |____/|_____|___|____/|_____| |_____|
                                     
class Slide2_test1(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [1,2], # Lines 2 and 3 of test_script.txt 
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\justify",
        "justify_length": 6,
    }
    
# You can see that in the second
# paragraph the word "deserunt" 
# is divided, for that you can
# add \break in the script, see 
# line 4 of the script.

class Slide2_test1_break_line(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [1,3], # Lines 2 and 4 of test_script.txt 
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\justify",
        "justify_length": 6,
    }
    
# You can also use the coloring methods we saw earlier.

class Slide2_test2(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [1,3], # Lines 2 and 4 of test_script.txt 
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\justify",
        "justify_length": 6,
        "colored_text": [
        #    v  TEXT_INDEX FIRST PARAGRAPH
            (0, [RED, 35, 43]),
            (0, [ORANGE, 78, 85]),
        #    v  TEXT_INDEX SECOND PARAGRAPH
            (1, [TEAL, 33, 40]),
            (1, [PURPLE, 77, 80]),
        ],
    }
    
# Usint tex map

class Slide2_test3(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [1,3], # Lines 2 and 4 of test_script.txt 
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\justify",
        "justify_length": 6,
        "tex_to_color_map": {
            "voluptate": RED,
            "pariatur": ORANGE,
            "proident": TEAL,
            "anim": PURPLE,
        },
    }

# You can also modify each paragraph
# in more detail using the following method.

class Slide2_test4(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [1,3], # Lines 2 and 4 of test_script.txt 
        "test_code": True, # No animation, only show text and subindexes
        "alignment": "\\justify",
        "justify_length": 6,
        "tex_to_color_map": {
            "voluptate": RED,
            "pariatur": ORANGE,
            "proident": TEAL,
            "anim": PURPLE,
        },
        "functions": [
            #               v   n-1 paragraph (paragraph 1)
            lambda mob: mob[0].shift(LEFT * 0.1),
            #               v   n-1 paragraph (paragraph 2)
            lambda mob: mob[1].shift(RIGHT * 0.1 + DOWN * 0.5),
            #               v   n-1 paragraph (paragraph 2)
            lambda mob: mob[1][48:53].scale(1.4).set_color(YELLOW),
            # You can repeat add all the modifications you want.
        ],
    }
    
# Animations with 2 paragraphs
class Slide2(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [1,3], # Lines 2 and 4 of test_script.txt 
        "test_code": False, # Animation activated
        "alignment": "\\justify",
        "justify_length": 6,
        "tex_to_color_map": {
            "voluptate": RED,
            "pariatur": ORANGE,
            "proident": TEAL,
            "anim": PURPLE,
        },
        "functions": [
            lambda mob: mob[0].shift(LEFT * 0.1),
            lambda mob: mob[1].shift(RIGHT * 0.1 + DOWN * 0.5),
            lambda mob: mob[1][48:53].scale(1.4).set_color(YELLOW),
        ],
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "TransformFromPolygon",
        "animation_kwargs_in": {
            # "run_time": 3
        },
        "run_times": [4,5], # 2s for first paragraph, 3s for second paragraph run_time
        # Before OUT:
        "middle_pauses": [2], # Pauses between the appearance of each paragraph
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }
    
#  ____  _ _     _        _____ 
# / ___|| (_) __| | ___  |___ / 
# \___ \| | |/ _` |/ _ \   |_ \ 
#  ___) | | | (_| |  __/  ___) |
# |____/|_|_|\__,_|\___| |____/ 

# The only limitation of this library
# is that you cannot use tex color map
# with formulas, you will have to use
# the first method to color it if that
# is what you want.

class Slide3_test(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,5,6], # Lines 5,6,7 
        #               1st Pargh   2nd pargh    3th pargh
        "text_types": [TextJustify, TexMobject, TextJustify], 
        "test_code": True,
        "alignment": "\\justify",
        "justify_length": 6,
        "colored_text": [
        #    v  TEXT_INDEX / If the text is only 1 character, repeat the number
            (1, [RED, 8, 8]),    # If the text is only 1 character, repeat the number
            (1, [TEAL, 14, 14]), # If the text is only 1 character, repeat the number
        ],
    }

class Slide3(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,5,6], # Lines 5,6,7 
        #               1st Pargh   2nd pargh    3th pargh
        "text_types": [TextJustify, TexMobject, TextJustify], 
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        "colored_text": [
        #    v  TEXT_INDEX
            (1, [RED, 8, 8]),    # If the text is only 1 character, repeat the number
            (1, [TEAL, 14, 14]), # If the text is only 1 character, repeat the number
        ],
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        # "animation_in": "TransformFromPolygon",
        # REMARK: animation_in != animations_in
        # Animations of       1st paragraph        2nd p     3th paragraph
        "animations_in": ["TransformFromPolygon", "Write","TransformFromPolygon"],
        "run_times": [2,3,2], # 2s 1st paragraph, 3s 2nd paragraph, 2s 3th paragraph
        # Before OUT
        "middle_pauses": [2,1], # 2s pause between paragraph 1 and 2, 2s pause between paragraph 2 and 1
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

#     _          _                 _   _                           _       
#    / \   _ __ (_)_ __ ___   __ _| |_(_) ___  _ __  ___          (_)_ __  
#   / _ \ | '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|  _____  | | '_ \ 
#  / ___ \| | | | | | | | | | (_| | |_| | (_) | | | \__ \ |_____| | | | | |
# /_/   \_\_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|___/         |_|_| |_|


class TransformFromPolygonExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4], # Lines 5,6,7 
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "TransformFromPolygon",
        "animations_in_config": [
            {}, # First paragraph with default config
            { # Second paragraph config
                "sides_polygons": it.cycle([3,4]),
                "polygons_colors": it.cycle([ORANGE,PINK])
            },
            { # Third paragraph config
                "sides_polygons": it.cycle([4,6,7]),
                "polygons_colors": it.cycle([YELLOW,PURPLE,WHITE])
            },
        ],
        "run_times": [2,3,2], # 2s 1st paragraph, 3s 2nd paragraph, 2s 3th paragraph
        # Before OUT
        "middle_pauses": [2,1], # 2s pause between paragraph 1 and 2, 2s pause between paragraph 2 and 1
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

class KeyboardExamples_pre_fail(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [7,8], # Lines 8 and 9 <- Start with \tt in the .txt file 
        "test_code": True,
        "alignment": "\\flushleft",
        "justify_length": 6,
    }

# Imagine that we want to align the 2nd line 
# with respect to the first line, for that we 
# can do the following.
class KeyboardExamples_pre(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [7,8], # Lines 8 and 9 <- Start with \tt in the .txt file 
        "test_code": True,
        "alignment": "\\flushleft",
        "justify_length": 6,
        "functions": [lambda mob: mob[1].align_to(mob[0],LEFT)],
    }

class KeyboardExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [7,8], # Lines 8 and 9 <- Start with \tt in the .txt file 
        "test_code": False,
        "alignment": "\\flushleft",
        "justify_length": 6,
        "functions": [lambda mob: mob[1].align_to(mob[0],LEFT)],
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Keyboard",
        # "run_times": [2,3,2], Not run_times in this animation
        # Before OUT
        "middle_pauses": [2], # 2s pause between paragraph 1 and 2, 2s pause between paragraph 2 and 1
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------

class FadeInFromBlackRectangleExamples(SlideScene):
    CONFIG = {
        # This scene has no specific configuration, just the run_time
        "script_name": "test_script",
        "index_paragraphs": [3,4], # Lines 4,5
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FadeInFromBlackRectangle",
        "run_times": [3,2], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


class FadeInFrom3DCameraExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FadeInFrom3DCamera",
        "animations_in_config": [
            {}, # Default config
            { # 2nd paragraph config
                "random_range": [-1,1]
            }, 
            { # 3th paragraph config
                "random_range": [1,3]
            }, 
        ],
        "run_times": [3,2,2], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


class FadeInFrom3DRotateExamples(SlideScene):
    CONFIG = {
        # This scene has no specific configuration, just the run_time
        "script_name": "test_script",
        "index_paragraphs": [4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FadeInFrom3DRotate",
        "run_times": [3], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


class WriteExamples(SlideScene):
    CONFIG = {
        # This scene has no specific configuration, just the run_time
        "script_name": "test_script",
        "index_paragraphs": [4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [3], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

class FadeInExamples(SlideScene):
    CONFIG = {
        # This scene has no specific configuration, just the run_time
        "script_name": "test_script",
        "index_paragraphs": [4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FadeIn",
        "run_times": [3], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }
    
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


class FromOutCameraExamples_defaults(SlideScene):
    CONFIG = {
        # This scene has no specific configuration, just the run_time
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FromOutCamera",
        "run_times": [2], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

class FromOutCameraExamples_custom(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "FromOutCamera",
        "animations_in_config": [
            {"direction": LEFT},
            {"direction": LEFT},
            {"direction": DOWN},
        ],
        "run_times": [2], 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


class ScaleFromBigExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "ScaleFromBig",
        "animations_in_config": [
            {"scale": 1.5},
            {"scale": 2},
            {"scale": 3},
        ],
        "run_times": [4]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# -------------------------------------------------------------------


class ShowHiddenBehindRectanglesExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "ShowHiddenBehindRectangles",
        "animations_in_config": [
            {
                "rectangles_config": {
                    "direction": RIGHT, # RIGHT or LEFT is horizontal
                    "partitions": 11,
                } 
            },
            {
                "rectangles_config": {
                    "direction": RIGHT, # RIGHT or LEFT is horizontal
                    "partitions": 20,
                } 
            },
            {
                "rectangles_config": {
                    "direction": UP, # UP or DOWN is vertical
                    "partitions": 30,
                } 
            },
        ],
        "run_times": [4]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "UnWriteAll",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }
    
#     _          _                 _   _                                       _   
#    / \   _ __ (_)_ __ ___   __ _| |_(_) ___  _ __  ___            ___  _   _| |_ 
#   / _ \ | '_ \| | '_ ` _ \ / _` | __| |/ _ \| '_ \/ __|  _____   / _ \| | | | __|
#  / ___ \| | | | | | | | | | (_| | |_| | (_) | | | \__ \ |_____| | (_) | |_| | |_ 
# /_/   \_\_| |_|_|_| |_| |_|\__,_|\__|_|\___/|_| |_|___/          \___/ \__,_|\__|

# Unlike entry animations, you CANNOT
# apply multiple exit animations for 
# each paragraph, so there is only one kwargs.

class FallExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "Fall",
        "animation_kwargs_out": {
            "run_time": 2
        },
    }

class FadeOutRandomExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "FadeOutRandom",
        "animation_kwargs_out": {
            "run_time": 3
        },
    }

class FadeOutToBlackRectangleExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "FadeOutToBlackRectangle",
        "animation_kwargs_out": {
            "run_time": 3
        },
    }

class FadeOutFrom3DCameraExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "FadeOutFrom3DCamera",
        "animation_kwargs_out": {
            "run_time": 3,
            "random_range": [-1,1] # Default is [-5,5]
        },
    }

class FadeOutFrom3DRotateExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "FadeOutFrom3DRotate",
        "animation_kwargs_out": {
            "run_time": 3,
        },
    }

class ToOutCameraExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "ToOutCamera",
        "animation_kwargs_out": {
            "run_time": 3,
        },
    }

class ScaleToSmallExamples(SlideScene):
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "Write",
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "ScaleToSmall",
        "animation_kwargs_out": {
            "run_time": 3,
        },
    }

class HiddeBehindRectanglesExamples(SlideScene):
    # This animation only works if the animation-in is ShowHiddenBehindRectangles
    CONFIG = {
        "script_name": "test_script",
        "index_paragraphs": [4,4,4],
        "test_code": False,
        "alignment": "\\justify",
        "justify_length": 6,
        # Animations
        # Before start:
        "pause_at_start": 0.1,
        # --- Animation IN CONFIG
        "animation_in": "ShowHiddenBehindRectangles", # <-  Need this
        "run_times": [1]*3, 
        # Before OUT
        "pause_before_remove": 2.5, # Pause after the appearance of all paragraphs
        # --- Animation OUT CONFIG
        "animation_out": "HiddeBehindRectangles",
        "animation_kwargs_out": {
            "run_time": 3,
        },
    }

