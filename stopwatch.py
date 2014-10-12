import simplegui
import math

# define global variables
time = "0:00.0"
interval = 100
t = 0
attempts = 0
score = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time, a, b, c, d
    a = t / 600
    b = (t - a * 600) / 100
    c = (t - a * 600 - b * 100) / 10
    d = t % 10
    time = str(a) + ":" + str(b) + str(c) + "." + str(d)
    return time
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()
    
def stop_handler():
    global score, attempts, d
    if timer.is_running() == True:
        timer.stop()
        if d == 0:
            score += 1
            attempts += 1
            return score, attempts
        else:
            attempts += 1
            return score, attempts
    else:
        return score, attempts
    
def reset_handler():
    global timer, t, attempts, score
    timer.stop()
    t = 0
    attempts = 0
    score = 0
    timer = simplegui.create_timer(interval, timer_handler)

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    format(t)
    t += 1
    print time

# define draw handler
def draw(canvas):
    canvas.draw_text(format(t), [50, 150], 60, "Red")
    canvas.draw_text(str(score) + "/" + str(attempts), [50, 25], 25, "White")
    
# create frame
frame = simplegui.create_frame("Timer", 300, 300)
frame.add_button("Start", start_handler, 200)
frame.add_button("Stop", stop_handler, 200)
frame.add_button("Reset", reset_handler, 200)

# register event handlers
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval, timer_handler)

# start frame
frame.start()
