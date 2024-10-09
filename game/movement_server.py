import socket
import threading


# 50x50 Map
game_map = [
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     'W', 'W', 'W', 'W', ],
    ['W', 'D', 'D', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'D', 'D',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
     'I', 'I', 'I', 'W', ],
    ['W', 'D', 'D', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'D', 'D',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
     'I', 'I', 'I', 'W', ],
    ['W', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I',
     'I', 'I', 'I', 'W', ],
    ['W', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M',
     'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'M', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'I', 'M', 'M',
     'M', 'M', 'M', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'F', 'F', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'F', 'F', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'F', 'F', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'F', 'F', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'F', 'F', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F', 'F',
     'F', 'F', 'F', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'L', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'D', 'D', 'S', 'S', 'S', 'S', 'S', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'S', 'S', 'S', 'S', 'S', 'S', 'S', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'D', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'G', 'G', 'G', 'G', 'G',
     'G', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'G', 'G', 'G', 'G', 'G',
     'G', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'G',
     'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'G', 'G', 'G', 'G', 'G', 'G', 'G', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D', 'D',
     'D', 'D', 'D', 'W', ],
    ['W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W',
     'W', 'W', 'W', 'W']

]

# Initialize players and their positions
players = {}

# Displaying area size
display_size = 10

# Define ANSI color codes for each player
player_colors = [
    "\033[91m",  # Red
    "\033[92m",  # Green
    "\033[93m",  # Yellow
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
    "\033[96m",  # Cyan
]

# Reset color
reset_color = "\033[0m"


# Update player position
def update_map(player_name, direction):
    player_x, player_y = players[player_name]

    # Movement logic
    if direction == 'W' and player_y > 0:
        player_y -= 1
    elif direction == 'A' and player_x > 0:
        player_x -= 1
    elif direction == 'S' and player_y < len(game_map) - 1:
        player_y += 1
    elif direction == 'D' and player_x < len(game_map[0]) - 1:
        player_x += 1

    players[player_name] = (player_x, player_y)


# Function to display a 10x10 section of the map centered around the player
def display_map(player_name):
    player_x, player_y = players[player_name]

    # Calculate boundaries for the 10x10 area
    start_x = max(0, player_x - display_size // 2)
    end_x = min(len(game_map[0]), player_x + display_size // 2 + 1)
    start_y = max(0, player_y - display_size // 2)
    end_y = min(len(game_map), player_y + display_size // 2 + 1)

    # Extract the section of the map
    temp_map = [row[start_x:end_x] for row in game_map[start_y:end_y]]

    # Add player's color to their position
    player_color = player_colors[list(players.keys()).index(player_name) % len(player_colors)]
    for player, (x, y) in players.items():
        if start_x <= x < end_x and start_y <= y < end_y:
            temp_map[y - start_y][x - start_x] = f"{player_color}█{reset_color}"  # Display colored player symbol

    # Join the map to a string for broadcasting
    return "\n".join([" ".join(row) for row in temp_map])


# Broadcast map to all clients
def broadcast_map():
    for client in clients:
        map_data = "\n".join([display_map(name) for name in players.keys()])
        client.sendall(map_data.encode())


# Handle each client
def handle_client(client, address):
    name = client.recv(1024).decode()

    # Assign initial position
    players[name] = (25, 25)  # Default position in the middle of the map

    # Send map updates
    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break
            update_map(name, data)
            broadcast_map()
        except:
            break

    client.close()
    del players[name]


# Server setup
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('10.100.2.181', 12345))
server_socket.listen()

clients = []


def start_server():
    print("Server started. Waiting for players...")
    while True:
        client, address = server_socket.accept()
        clients.append(client)
        print(f"Player {address} connected.")
        threading.Thread(target=handle_client, args=(client, address)).start()


start_server()
