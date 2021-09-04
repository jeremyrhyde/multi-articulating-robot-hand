#!/usr/bin/env python3
"""finger.py
   Multiarticulated Hand - Component Finger
   This class focuses on the fingers of the robotic hand excluding thumb, wrist
   motion and sublater motion. Paramters:
      -
      -
   are use to define the finger.
"""
__project__ = 'Multiarticulated Robotic Hand'
__author__ = "Jeremy Hyde"

import os
import sys
import math

from tendon import Tendon

class Finger:

    tendon = {'retraction' : None, 'extension' : None}

    def __init__(self, mp_l, ratio, joints, motor_retraction_port, motor_extension_port):

        # Define phlange structure and parameters
        # Structure - phlanges[name] : {length}
        self.phlanges = {'metacarpal' : {'ratio' : ratio[0], 'length' : ratio[0]*mp_l},
                         'proximal' : {'ratio' : ratio[1], 'length' : ratio[1]*mp_l},
                         'middle' : {'ratio' : ratio[2], 'length' : ratio[2]*mp_l},
                         'distal' : {'ratio' : ratio[3], 'length' : ratio[3]*mp_l}}

        # Define joint structure and parameters
        # Structure - joints[name] : {'angle' : {'min', 'curr', 'max'}, {'radius' : {'retraction', 'extension'}}
        self.joints = joints

        self.tendon['retraction'] = None# Servo(motor_retraction_port, 40)
        self.tendon['extension'] = None #Servo(motor_extension_port , 50)


    def move_MCP_joint_dtheta(self, mcp_dtheta):

        mcp_theta2 = self.MCP_joint['angle']['curr'] + mcp_dtheta

        if self.check_safe_move(self.MCP_joint['angle'], mcp_next_theta): return

        #dl = 2 * math.pow(self.MCP_joint['radius']['retraction'],2) * (math.cos(self.MCP_joint['curr'['angle']]) - math.cos(mcp_theta2))

        #self.actuation['retraction'].move_dl(dl)

    def move_MCP_joint_to_theta(self, mcp_theta2):

        mcp_dtheta = mcp_theta2 - self.MCP_joint['angle']['curr']

        if self.check_safe_move(self.MCP_joint['angle'], mcp_theta2): return

        #dl = 2 * math.pow(self.MCP_joint['radius']['retraction'],2) * (math.cos(self.MCP_joint['curr'['angle']]) - math.cos(mcp_theta2))

        #self.actuation['retraction'].move_dl(dl)

    def move_PIP_DIPs_joint_dtheta(self, pip_dtheta, dip_dtheta):

        pip_theta2 = self.PIP_joint['angle']['curr'] + pip_dtheta
        dip_theta2 = self.DIP_joint['angle']['curr'] + dip_dtheta

        if self.check_safe_move(self.PIP_joint['angle'], pip_theta2): return
        if self.check_safe_move(self.DIP_joint['angle'], dip_theta2): return

        #dl = 2 * math.pow(self.MCP_joint['radius']['retraction'],2) * (math.cos(self.PIP_joint['curr'['angle']]) - math.cos(next_theta))

        #self.actuation['retraction'].move_dl(dl)

    def move_PIP_DIP_joints_to_theta(self, pip_theta2, dip_theta2):

        pip_dtheta = pip_theta2 - self.PIP_joint['angle']['curr']
        dip_dtheta = dip_theta2 - self.DIP_joint['angle']['curr']

        if self.check_safe_move(self.PIP_joint['angle'], pip_theta2): return
        if self.check_safe_move(self.DIP_joint['angle'], dip_theta2): return

        #dl = 2 * math.pow(self.MCP_joint['radius']['retraction'],2) * (math.cos(self.MCP_joint['curr'['angle']]) - math.cos(next_theta))

        #self.actuation['retraction'].move_dl(dl)

    def move_MCP_PIP_DIP_joints_dtheta(self, mcp_dtheta, pip_dtheta, dip_dtheta):

        mcp_theta2 = self.MCP_joint['angle']['curr'] + mcp_dtheta
        pip_theta2 = self.PIP_joint['angle']['curr'] + pip_dtheta
        dip_theta2 = self.DIP_joint['angle']['curr'] + dip_dtheta

        if self.check_safe_move(self.MCP_joint['angle'], mcp_theta2): return
        if self.check_safe_move(self.PIP_joint['angle'], pip_theta2): return
        if self.check_safe_move(self.DIP_joint['angle'], dip_theta2): return

        dl_ret = 0
        dl_ext = 0

        #self.actuation['retraction'].move_dl(dl_ret)
        #self.actuation['retraction'].move_dl(dl_ext)

    def move_MCP_PIP_DIP_joints_to_theta(self, mcp_theta2, pip_theta2, dip_theta2):

        mcp_dtheta = mcp_theta2 - self.MCP_joint['angle']['curr']
        pip_dtheta = pip_theta2 - self.PIP_joint['angle']['curr']
        dip_dtheta = dip_theta2 - self.DIP_joint['angle']['curr']

        if self.check_safe_move(self.MCP_joint['angle'], mcp_theta2): return
        if self.check_safe_move(self.PIP_joint['angle'], pip_theta2): return
        if self.check_safe_move(self.DIP_joint['angle'], dip_theta2): return

        l2_ret = 0
        l2_ext = 0

        #self.actuation['retraction'].move_to(l2_ret)
        #self.actuation['retraction'].move_to(l2_ext)



    # Confirm desired move is within finger's bounds
    def check_safe_move(self, angles, next_angle):
        if next_angle < angles['min'] or next_angle > angles['max']: return False
        else: return True

    def close(self):
        pass

def main():


    metacarpal_phlange_length = 1
    ratio = [1, 2, 3, 4]

    joints = {'MCP' : {'angles' : {'min' : -10, 'curr' : 0, 'max' : 100}, 'radius' : {'retraction' : 10, 'extension' : 10}},
              'PIP' : {'angles' : {'min' : -10, 'curr' : 0, 'max' : 100}, 'radius' : {'retraction' : 10, 'extension' : 10}},
              'DIP' : {'angles' : {'min' : -10, 'curr' : 0, 'max' : 100}, 'radius' : {'retraction' : 10, 'extension' : 10}}}

    motor_retraction_port = 0
    motor_extension_port = 1


    tendon = Finger(metacarpal_phlange_length, ratio, joints, motor_retraction_port, motor_extension_port)


if __name__ == '__main__':
    main()
