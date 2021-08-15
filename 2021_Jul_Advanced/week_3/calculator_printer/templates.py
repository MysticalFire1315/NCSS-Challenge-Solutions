DASH = ' dash '
RIGHT = ' space|'
LEFT = '|space '
BOTH = '|space|'
NONE = ' space '

seven_segment_display_template = {
  0: [
    DASH,  #  -  #
    BOTH,  # | | #
    NONE,  #     #
    BOTH,  # | | #
    DASH   #  -  #
  ],

  1: [
    NONE,  #     #
    RIGHT, #   | #
    NONE,  #     #
    RIGHT, #   | #
    NONE   #     #
  ],

  2: [
    DASH,  #  -  #
    RIGHT, #   | #
    DASH,  #  -  #
    LEFT,  # |   #
    DASH   #  -  #
  ],

  3: [
    DASH,  #  -  #
    RIGHT, #   | #
    DASH,  #  -  #
    RIGHT, #   | #
    DASH   #  -  #
  ],

  4: [
    NONE,  #     #
    BOTH,  # | | #
    DASH,  #  -  #
    RIGHT, #   | #
    NONE   #     #
  ],

  5: [
    DASH,  #  -  #
    LEFT,  # |   #
    DASH,  #  -  #
    RIGHT, #   | #
    DASH   #  -  #
  ],

  6: [
    DASH,  #  -  #
    LEFT,  # |   #
    DASH,  #  -  #
    BOTH,  # | | #
    DASH   #  -  #
  ],

  7: [
    DASH,  #  -  #
    RIGHT, #   | #
    NONE,  #     #
    RIGHT, #   | #
    NONE   #     #
  ],

  8: [
    DASH,  #  -  #
    BOTH,  # | | #
    DASH,  #  -  #
    BOTH,  # | | #
    DASH   #  -  #
  ],

  9: [
    DASH,  #  -  #
    BOTH,  # | | #
    DASH,  #  -  #
    RIGHT, #   | #
    DASH   #  -  #
  ]
}