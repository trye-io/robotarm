import pygame
from PCA9685 import PCA9685

def clamp(x):
    return max(500, min(2500, x))

pygame.init()

FPS = 60
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1080, 720))

gripper_position = 1500
yaw_position = 1500
up_down_position = 1500
forward_backward_postion = 1500

is_left_pressed = False
is_right_pressed = False
is_up_pressed = False
is_down_pressed = False
is_w_pressed = False
is_s_pressed = False
is_a_pressed = False
is_d_pressed = False

is_running = True

pwm = PCA9685(0x40, debug=False)
pwm.setPWMFreq(50)

while is_running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                is_left_pressed = True
            if event.key == pygame.K_RIGHT:
                is_right_pressed = True
            if event.key == pygame.K_UP:
                is_up_pressed = True
            if event.key == pygame.K_DOWN:
                is_down_pressed = True
            if event.key == pygame.K_w:
                is_w_pressed = True
            if event.key == pygame.K_s:
                is_s_pressed = True
            if event.key == pygame.K_a:
                is_a_pressed = True
            if event.key == pygame.K_d:
                is_d_pressed = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                is_left_pressed = False
            if event.key == pygame.K_RIGHT:
                is_right_pressed = False
            if event.key == pygame.K_UP:
                is_up_pressed = False
            if event.key == pygame.K_DOWN:
                is_down_pressed = False
            if event.key == pygame.K_w:
                is_w_pressed = False
            if event.key == pygame.K_s:
                is_s_pressed = False
            if event.key == pygame.K_a:
                is_a_pressed = False
            if event.key == pygame.K_d:
                is_d_pressed = False
    
    if is_left_pressed:
        yaw_position -= 5
    if is_right_pressed:
        yaw_position += 5
    if is_up_pressed:
        up_down_position -= 5
    if is_down_pressed:
        up_down_position += 5
    if is_w_pressed:
        forward_backward_postion -= 5
    if is_s_pressed:
        forward_backward_postion += 5
    if is_a_pressed:
        gripper_position -= 5
    if is_d_pressed:
        gripper_position += 5
    
    pwm.setServoPulse(0, clamp(gripper_position))
    pwm.setServoPulse(1, clamp(yaw_position))
    pwm.setServoPulse(2, clamp(up_down_position))
    pwm.setServoPulse(3, clamp(forward_backward_postion))

    clock.tick(FPS)
    
    