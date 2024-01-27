####################################################
#   UNIVERSAL IMPORTS USED THROUGHOUT THE MODULE   #
####################################################



import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

sns.set_style('darkgrid')

# install ffmpeg
import cv2  # Import Open-CV

from scipy.ndimage import zoom  # Used For Up-Sampling (.csv) Data


import tkinter as tk
from tkinter import filedialog



# Import the Thesis' Football-Related + Pitch Vizualisation Functions Module

import Thesis_Football_Viz_Functions as TFVFs











####################################################
#  UNIVERSAL VARIABLES USED THROUGHOUT THE MODULE  #
####################################################



# Game/Match-Time/Clock - Related Columns

Match_Clock = "T"

New_Integer_Match_Minute_Clock = "Match_Minute_Clock"

New_Float_Match_Seconds_Clock = "Match_Seconds_Clock"

New_String_Match_Full_Clock = "Match_Clock"

First_Or_Second_Half = "Section"   # 1.0 = 1st-Half  /  2.0 = 2nd-Half

Team_Currently_In_Possession_of_Ball = "BallPossesion"   # {1.0 = Home Team; 2.0 = Away Team}




# Ball-Related Columns

Ball_In_Play_Or_Not_Status = "BallStatus"   # Current Status of the Ball - i.e. Whether the Ball Is In Movement/Play Or Not {0.0 = Game/Match Is Paused; 1.0 = Game/Match Is Running}

Ball_Coordinates_Tracking_Data_Columns = ['X', 'Y', 'Z']

Ball_X_Coordinates_Tracking_Data_Column = "X"
Ball_Y_Coordinates_Tracking_Data_Column = "Y"
Ball_Height_Tracking_Data_Column = "Z"

Ball_Velocity_Components_Tracking_Data_Columns = ['V_xBall', 'V_yBall', 'V_zBall']

Ball_Velocity_Component_X_Tracking_Data_Columns = ['V_xBall']
Ball_Velocity_Component_Y_Tracking_Data_Columns = ['V_yBall']
Ball_Velocity_Component_Z_Tracking_Data_Columns = ['V_zBall']

Ball_Speed_Tracking_Data_Column_Original = "S"

Ball_Speed_Tracking_Data_Column = "SpeedBall"

Ball_2D_Coordinates_Velocities_and_Speed_Tracking_Data_Columns = ['X', 'Y', 'Z',
                                                                  'V_xBall', 'V_yBall', 'V_zBall',
                                                                  "SpeedBall"]


Ball_Acceleration_Components_Tracking_Data_Columns = ['Acc_xBall', 'Acc_yBall', 'Acc_zBall']

Ball_Acceleration_Component_X_Tracking_Data_Columns = ['Acc_xBall']
Ball_Acceleration_Component_Y_Tracking_Data_Columns = ['Acc_yBall']
Ball_Acceleration_Component_Z_Tracking_Data_Columns = ['Acc_zBall']

Ball_Acceleration_Magnitude_Tracking_Data_Column = "Acc_MagnitudeBall"

Ball_2D_Coordinates_Velocities_Accelerations_and_Magnitudes_Tracking_Data_Columns = ['X', 'Y',
                                                                                     'V_xBall', 'V_yBall',
                                                                                     "SpeedBall",
                                                                                     'Acc_xBall', 'Acc_yBall',
                                                                                     "Acc_MagnitudeBall"]


Ball_3D_Coordinates_Velocities_Accelerations_and_Magnitudes_Tracking_Data_Columns = ['X', 'Y', 'Z',
                                                                                     'V_xBall', 'V_yBall', 'V_zBall',
                                                                                     "SpeedBall",
                                                                                     'Acc_xBall', 'Acc_yBall', 'Acc_zBall',
                                                                                     "Acc_MagnitudeBall"]

Ball_Visible_In_Broadcast_Tracking_Data_Column = "Visable"




# Home-Team Related Columns

Home_Team_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 
                                               'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11']

Home_Team_X_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11']
Home_Team_Y_Coordinates_Tracking_Data_Columns = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11']

Home_Team_GK_X_Coordinates_Tracking_Data_Columns = "X1"
Home_Team_GK_Y_Coordinates_Tracking_Data_Columns = "Y1"

Home_Team_Speeds_Tracking_Data_Columns_Original = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11']

Home_Team_GK_Speed_Tracking_Data_Columns_Original = "S1"

Home_Team_Velocity_Components_Tracking_Data_Columns = ['V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11',
                                                       'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11']

Home_Team_Velocity_Component_X_Tracking_Data_Columns = ['V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11']
Home_Team_Velocity_Component_Y_Tracking_Data_Columns = ['V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11']

Home_Team_GK_Velocity_Component_X_Tracking_Data_Columns = "V_x1"
Home_Team_GK_Velocity_Component_Y_Tracking_Data_Columns = "V_y1"


Home_Team_Speeds_Tracking_Data_Columns = ["Speed1", "Speed2", "Speed3", "Speed4", "Speed5", "Speed6", "Speed7", "Speed8", "Speed9", "Speed10", "Speed11"]

Home_Team_GK_Speed_Tracking_Data_Columns = "Speed1"


Home_Team_2D_Coordinates_Velocities_and_Speeds_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
                                                                        'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                                        'V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11',
                                                                        'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11',
                                                                        "Speed1", "Speed2", "Speed3", "Speed4", "Speed5", "Speed6", "Speed7", "Speed8", "Speed9", "Speed10", "Speed11"]



Home_Team_Acceleration_Components_Tracking_Data_Columns = ['Acc_x1', 'Acc_x2', 'Acc_x3', 'Acc_x4', 'Acc_x5', 'Acc_x6', 'Acc_x7', 'Acc_x8', 'Acc_x9', 'Acc_x10', 'Acc_x11',
                                                           'Acc_y1', 'Acc_y2', 'Acc_y3', 'Acc_y4', 'Acc_y5', 'Acc_y6', 'Acc_y7', 'Acc_y8', 'Acc_y9', 'Acc_y10', 'Acc_y11']

Home_Team_Acceleration_Component_X_Tracking_Data_Columns = ['Acc_x1', 'Acc_x2', 'Acc_x3', 'Acc_x4', 'Acc_x5', 'Acc_x6', 'Acc_x7', 'Acc_x8', 'Acc_x9', 'Acc_x10', 'Acc_x11']
Home_Team_Acceleration_Component_Y_Tracking_Data_Columns = ['Acc_y1', 'Acc_y2', 'Acc_y3', 'Acc_y4', 'Acc_y5', 'Acc_y6', 'Acc_y7', 'Acc_y8', 'Acc_y9', 'Acc_y10', 'Acc_y11']

Home_Team_GK_Acceleration_Component_X_Tracking_Data_Columns = "Acc_x1"
Home_Team_GK_Acceleration_Component_Y_Tracking_Data_Columns = "Acc_y1"


Home_Team_Acceleration_Magnitudes_Tracking_Data_Columns_V2 = ["Acc_Magnitude1", "Acc_Magnitude2", "Acc_Magnitude3", "Acc_Magnitude4", "Acc_Magnitude5", "Acc_Magnitude6", "Acc_Magnitude7", "Acc_Magnitude8", "Acc_Magnitude9", "Acc_Magnitude10", "Acc_Magnitude11"]

Home_Team_GK_Acceleration_Magnitude_Tracking_Data_Columns_V2 = "Acc_Magnitude1"


Home_Team_2D_Coordinates_Velocities_Accelerations_and_Magnitudes_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
                                                                                          'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                                                          'V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11',
                                                                                          'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11',
                                                                                          "Speed1", "Speed2", "Speed3", "Speed4", "Speed5", "Speed6", "Speed7", "Speed8", "Speed9", "Speed10", "Speed11",
                                                                                          'Acc_x1', 'Acc_x2', 'Acc_x3', 'Acc_x4', 'Acc_x5', 'Acc_x6', 'Acc_x7', 'Acc_x8', 'Acc_x9', 'Acc_x10', 'Acc_x11',
                                                                                          'Acc_y1', 'Acc_y2', 'Acc_y3', 'Acc_y4', 'Acc_y5', 'Acc_y6', 'Acc_y7', 'Acc_y8', 'Acc_y9', 'Acc_y10', 'Acc_y11',
                                                                                          "Acc_Magnitude1", "Acc_Magnitude2", "Acc_Magnitude3", "Acc_Magnitude4", "Acc_Magnitude5", "Acc_Magnitude6", "Acc_Magnitude7", "Acc_Magnitude8", "Acc_Magnitude9", "Acc_Magnitude10", "Acc_Magnitude11"]



Home_Team_Players_Visible_In_Broadcast_Tracking_Data_Columns = ['Visable1', 'Visable2', 'Visable3', 'Visable4', 'Visable5', 'Visable6', 'Visable7', 'Visable8', 'Visable9', 'Visable10', 'Visable11']

Home_Team_GK_Visible_In_Broadcast_Tracking_Data_Columns = "Visable1"




# Away-Team Related Columns

Away_Team_Coordinates_Tracking_Data_Columns = ['X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 
                                               'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22']

Away_Team_X_Coordinates_Tracking_Data_Columns = ['X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22']
Away_Team_Y_Coordinates_Tracking_Data_Columns = ['Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22']

Away_Team_GK_X_Coordinates_Tracking_Data_Columns = "X12"
Away_Team_GK_Y_Coordinates_Tracking_Data_Columns = "Y12"

Away_Team_Speeds_Tracking_Data_Columns_Original = ['S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22']

Away_Team_GK_Speed_Tracking_Data_Columns_Original = "S12"

Away_Team_Velocity_Components_Tracking_Data_Columns = ['V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22',
                                                       'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22']

Away_Team_Velocity_Component_X_Tracking_Data_Columns = ['V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22']
Away_Team_Velocity_Component_Y_Tracking_Data_Columns = ['V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22']

Away_Team_GK_Velocity_Component_X_Tracking_Data_Columns = "V_x12"
Away_Team_GK_Velocity_Component_Y_Tracking_Data_Columns = "V_y12"


Away_Team_Speeds_Tracking_Data_Columns = ["Speed12", "Speed13", "Speed14", "Speed15", "Speed16", "Speed17", "Speed18", "Speed19", "Speed20", "Speed21", "Speed22"]

Away_Team_GK_Speed_Tracking_Data_Columns = "Speed12"


Away_Team_2D_Coordinates_Velocities_and_Speeds_Tracking_Data_Columns = ['X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22',
                                                                        'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                                        'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22',
                                                                        'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22',
                                                                        "Speed12", "Speed13", "Speed14", "Speed15", "Speed16", "Speed17", "Speed18", "Speed19", "Speed20", "Speed21", "Speed22"]


Away_Team_Acceleration_Components_Tracking_Data_Columns = ['Acc_x12', 'Acc_x13', 'Acc_x14', 'Acc_x15', 'Acc_x16', 'Acc_x17', 'Acc_x18', 'Acc_x19', 'Acc_x20', 'Acc_x21', 'Acc_x22',
                                                           'Acc_y12', 'Acc_y13', 'Acc_y14', 'Acc_y15', 'Acc_y16', 'Acc_y17', 'Acc_y18', 'Acc_y19', 'Acc_y20', 'Acc_y21', 'Acc_y22']

Away_Team_Acceleration_Component_X_Tracking_Data_Columns = ['Acc_x12', 'Acc_x13', 'Acc_x14', 'Acc_x15', 'Acc_x16', 'Acc_x17', 'Acc_x18', 'Acc_x19', 'Acc_x20', 'Acc_x21', 'Acc_x22']
Away_Team_Acceleration_Component_Y_Tracking_Data_Columns = ['Acc_y12', 'Acc_y13', 'Acc_y14', 'Acc_y15', 'Acc_y16', 'Acc_y17', 'Acc_y18', 'Acc_y19', 'Acc_y20', 'Acc_y21', 'Acc_y22']

Away_Team_GK_Acceleration_Component_X_Tracking_Data_Columns = "Acc_x12"
Away_Team_GK_Acceleration_Component_Y_Tracking_Data_Columns = "Acc_y12"


Away_Team_Acceleration_Magnitudes_Tracking_Data_Columns_V2 = ["Acc_Magnitude12", "Acc_Magnitude13", "Acc_Magnitude14", "Acc_Magnitude15", "Acc_Magnitude16", "Acc_Magnitude17", "Acc_Magnitude18", "Acc_Magnitude19", "Acc_Magnitude20", "Acc_Magnitude21", "Acc_Magnitude22"]

Away_Team_GK_Acceleration_Magnitude_Tracking_Data_Columns_V2 = "Acc_Magnitude12"


Away_Team_2D_Coordinates_Velocities_Accelerations_and_Magnitudes_Tracking_Data_Columns = ['X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22',
                                                                                          'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                                                          'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22',
                                                                                          'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22',
                                                                                          "Speed12", "Speed13", "Speed14", "Speed15", "Speed16", "Speed17", "Speed18", "Speed19", "Speed20", "Speed21", "Speed22",
                                                                                          'Acc_x12', 'Acc_x13', 'Acc_x14', 'Acc_x15', 'Acc_x16', 'Acc_x17', 'Acc_x18', 'Acc_x19', 'Acc_x20', 'Acc_x21', 'Acc_x22',
                                                                                          'Acc_y12', 'Acc_y13', 'Acc_y14', 'Acc_y15', 'Acc_y16', 'Acc_y17', 'Acc_y18', 'Acc_y19', 'Acc_y20', 'Acc_y21', 'Acc_y22',
                                                                                          "Acc_Magnitude12", "Acc_Magnitude13", "Acc_Magnitude14", "Acc_Magnitude15", "Acc_Magnitude16", "Acc_Magnitude17", "Acc_Magnitude18", "Acc_Magnitude19", "Acc_Magnitude20", "Acc_Magnitude21", "Acc_Magnitude22"]


Away_Team_Players_Visible_In_Broadcast_Tracking_Data_Columns = ['Visable12', 'Visable13', 'Visable14', 'Visable15', 'Visable16', 'Visable17', 'Visable18', 'Visable19', 'Visable20', 'Visable21', 'Visable22']

Away_Team_GK_Visible_In_Broadcast_Tracking_Data_Columns = "Visable12"





# All-Players General Columns

All_Players_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22']

All_Players_and_Ball_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                          'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                          'X', 'Y', 'Z']

All_Players_and_Ball_2D_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                             'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                             'X', 'Y']

All_Players_X_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22']
All_Players_Y_Coordinates_Tracking_Data_Columns = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22']

All_Players_and_Ball_X_Coordinates_Tracking_Data_Columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11', 'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22',
                                                            'X']
All_Players_and_Ball_Y_Coordinates_Tracking_Data_Columns = ['Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11', 'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                            'Y']

All_Players_Velocity_Components_Tracking_Data_Columns = ['V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11', 'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11',
                                                         'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22', 'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22']

All_Players_Velocity_Component_X_Tracking_Data_Columns = ['V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11', 'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22']
All_Players_Velocity_Component_Y_Tracking_Data_Columns = ['V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11', 'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22']


All_Players_Speeds_Tracking_Data_Columns_Original = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11',
                                                     'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22']

All_Players_and_Ball_Speeds_Tracking_Data_Columns_Original = ['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11',
                                                              'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21', 'S22',
                                                              'S']

All_Players_Speeds_Tracking_Data_Columns = ["Speed1", "Speed2", "Speed3", "Speed4", "Speed5", "Speed6", "Speed7", "Speed8", "Speed9", "Speed10", "Speed11",
                                            "Speed12", "Speed13", "Speed14", "Speed15", "Speed16", "Speed17", "Speed18", "Speed19", "Speed20", "Speed21", "Speed22"]


All_Players_and_Ball_2D_Coordinates_Velocities_and_Speeds_Tracking_Data_Columns = ['X', 'Y',
                                                                                   'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
                                                                                   'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                                                   'V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11',
                                                                                   'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11',
                                                                                   "Speed1", "Speed2", "Speed3", "Speed4", "Speed5", "Speed6", "Speed7", "Speed8", "Speed9", "Speed10", "Speed11",
                                                                                   'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22',
                                                                                   'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                                                   'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22',
                                                                                   'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22',
                                                                                   "Speed12", "Speed13", "Speed14", "Speed15", "Speed16", "Speed17", "Speed18", "Speed19", "Speed20", "Speed21", "Speed22"]




All_Players_Acceleration_Components_Tracking_Data_Columns = ['Acc_x1', 'Acc_x2', 'Acc_x3', 'Acc_x4', 'Acc_x5', 'Acc_x6', 'Acc_x7', 'Acc_x8', 'Acc_x9', 'Acc_x10', 'Acc_x11', 'Acc_y1', 'Acc_y2', 'Acc_y3', 'Acc_y4', 'Acc_y5', 'Acc_y6', 'Acc_y7', 'Acc_y8', 'Acc_y9', 'Acc_y10', 'Acc_y11',
                                                             'Acc_x12', 'Acc_x13', 'Acc_x14', 'Acc_x15', 'Acc_x16', 'Acc_x17', 'Acc_x18', 'Acc_x19', 'Acc_x20', 'Acc_x21', 'Acc_x22', 'Acc_y12', 'Acc_y13', 'Acc_y14', 'Acc_y15', 'Acc_y16', 'Acc_y17', 'Acc_y18', 'Acc_y19', 'Acc_y20', 'Acc_y21', 'Acc_y22']

All_Players_Acceleration_Component_X_Tracking_Data_Columns = ['Acc_x1', 'Acc_x2', 'Acc_x3', 'Acc_x4', 'Acc_x5', 'Acc_x6', 'Acc_x7', 'Acc_x8', 'Acc_x9', 'Acc_x10', 'Acc_x11', 'Acc_x12', 'Acc_x13', 'Acc_x14', 'Acc_x15', 'Acc_x16', 'Acc_x17', 'Acc_x18', 'Acc_x19', 'Acc_x20', 'Acc_x21', 'Acc_x22']
All_Players_Acceleration_Component_Y_Tracking_Data_Columns = ['Acc_y1', 'Acc_y2', 'Acc_y3', 'Acc_y4', 'Acc_y5', 'Acc_y6', 'Acc_y7', 'Acc_y8', 'Acc_y9', 'Acc_y10', 'Acc_y11', 'Acc_y12', 'Acc_y13', 'Acc_y14', 'Acc_y15', 'Acc_y16', 'Acc_y17', 'Acc_y18', 'Acc_y19', 'Acc_y20', 'Acc_y21', 'Acc_y22']

All_Players_Acceleration_Magnitudes_Tracking_Data_Columns = ["Acc_Magnitude1", "Acc_Magnitude2", "Acc_Magnitude3", "Acc_Magnitude4", "Acc_Magnitude5", "Acc_Magnitude6", "Acc_Magnitude7", "Acc_Magnitude8", "Acc_Magnitude9", "Acc_Magnitude10", "Acc_Magnitude11",
                                                             "Acc_Magnitude12", "Acc_Magnitude13", "Acc_Magnitude14", "Acc_Magnitude15", "Acc_Magnitude16", "Acc_Magnitude17", "Acc_Magnitude18", "Acc_Magnitude19", "Acc_Magnitude20", "Acc_Magnitude21", "Acc_Magnitude22"]


All_Players_and_Ball_2D_Coordinates_Velocities_and_Magnitudes_Tracking_Data_Columns = ['X', 'Y',
                                                                                       'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
                                                                                       'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                                                       'V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11',
                                                                                       'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11',
                                                                                       "Speed1", "Speed2", "Speed3", "Speed4", "Speed5", "Speed6", "Speed7", "Speed8", "Speed9", "Speed10", "Speed11",
                                                                                       'Acc_x1', 'Acc_x2', 'Acc_x3', 'Acc_x4', 'Acc_x5', 'Acc_x6', 'Acc_x7', 'Acc_x8', 'Acc_x9', 'Acc_x10', 'Acc_x11',
                                                                                       'Acc_y1', 'Acc_y2', 'Acc_y3', 'Acc_y4', 'Acc_y5', 'Acc_y6', 'Acc_y7', 'Acc_y8', 'Acc_y9', 'Acc_y10', 'Acc_y11',
                                                                                       "Acc_Magnitude1", "Acc_Magnitude2", "Acc_Magnitude3", "Acc_Magnitude4", "Acc_Magnitude5", "Acc_Magnitude6", "Acc_Magnitude7", "Acc_Magnitude8", "Acc_Magnitude9", "Acc_Magnitude10", "Acc_Magnitude11",
                                                                                       'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22',
                                                                                       'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                                                       'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22',
                                                                                       'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22',
                                                                                       "Speed12", "Speed13", "Speed14", "Speed15", "Speed16", "Speed17", "Speed18", "Speed19", "Speed20", "Speed21", "Speed22",
                                                                                       'Acc_x12', 'Acc_x13', 'Acc_x14', 'Acc_x15', 'Acc_x16', 'Acc_x17', 'Acc_x18', 'Acc_x19', 'Acc_x20', 'Acc_x21', 'Acc_x22',
                                                                                       'Acc_y12', 'Acc_y13', 'Acc_y14', 'Acc_y15', 'Acc_y16', 'Acc_y17', 'Acc_y18', 'Acc_y19', 'Acc_y20', 'Acc_y21', 'Acc_y22',
                                                                                       "Acc_Magnitude12", "Acc_Magnitude13", "Acc_Magnitude14", "Acc_Magnitude15", "Acc_Magnitude16", "Acc_Magnitude17", "Acc_Magnitude18", "Acc_Magnitude19", "Acc_Magnitude20", "Acc_Magnitude21", "Acc_Magnitude22"]


All_Players_Visible_In_Broadcast_Tracking_Data_Columns = ['Visable1', 'Visable2', 'Visable3', 'Visable4', 'Visable5', 'Visable6', 'Visable7', 'Visable8', 'Visable9', 'Visable10', 'Visable11',
                                                          'Visable12', 'Visable13', 'Visable14', 'Visable15', 'Visable16', 'Visable17', 'Visable18', 'Visable19', 'Visable20', 'Visable21', 'Visable22']

All_Players_and_Ball_Visible_In_Broadcast_Tracking_Data_Columns = ['Visable1', 'Visable2', 'Visable3', 'Visable4', 'Visable5', 'Visable6', 'Visable7', 'Visable8', 'Visable9', 'Visable10', 'Visable11',
                                                                   'Visable12', 'Visable13', 'Visable14', 'Visable15', 'Visable16', 'Visable17', 'Visable18', 'Visable19', 'Visable20', 'Visable21', 'Visable22',
                                                                   'Visable']











####################################################
#         READ POSSESSIONS DATA FUNCTION           #
####################################################



def Read_Possessions_Dataset( original_possessions_dataset = False, all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns = False, all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns = False, possessions_of_shots_and_goals_only_with_nextgoal_related_columns = False, possessions_of_shots_and_goals_only_without_nextgoal_related_columns = False ):
    """
    Function That Reads-In the Specified Possessions' & Targets' Dataset
        
    At Least 1 of the Parameters MUST Be Set To `True` !!
    
    Input: original_possessions_dataset = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: possessions_of_shots_and_goals_only_with_nextgoal_related_columns = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: possessions_of_shots_and_goals_only_without_nextgoal_related_columns = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    
    Output: possessions_df = Specified Possessions' & Targets' Dataset
    """
    
    if original_possessions_dataset == True:
        
        print('\n',
              "Loading & Reading-In the Original Version of the Possessions' & Targets' Dataset",
              '\n')
    
    
        possessions_df = pd.read_parquet("Possessions_and_Targets.parquet", engine = "auto")
    
    
        
        # Dimensions of the Original Version of the Possessions' & Targets' Dataset

        print(f"Dimensions of the Original Version of the Possessions' & Targets' Dataset = {possessions_df.shape}", '\n')
    
    
    
    
    if all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included (With the `nextgoal`-Related Columns Present)",
              '\n')
    
    
        possessions_df = pd.read_parquet("Possessions_and_Targets_With_Shots_and_Goals_Added_and_With_NextGoal_Related_Columns.parquet", engine = "auto")
    
    
        
        # Dimensions of the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included (With the `nextgoal`-Related Columns Present)

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included (With the `nextgoal`-Related Columns Present) = {possessions_df.shape}", '\n')
    
    
    
    
    if all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included (Without the `nextgoal`-Related Columns Present)",
              '\n')
    
    
        possessions_df = pd.read_parquet("Possessions_and_Targets_With_Shots_and_Goals_Added_and_Without_NextGoal_Related_Columns.parquet", engine = "auto")
    
    
        
        # Dimensions of the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included (Without the `nextgoal`-Related Columns Present)

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included (Without the `nextgoal`-Related Columns Present) = {possessions_df.shape}", '\n')
    
    
    
    
    if possessions_of_shots_and_goals_only_with_nextgoal_related_columns == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present)",
              '\n')
    
    
        possessions_df = pd.read_parquet("Possessions_and_Targets_of_Shots_and_Goals_Only_With_NextGoal_Related_Columns.parquet", engine = "auto")
    
    
        
        # Dimensions of the  Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present)

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present) = {possessions_df.shape}", '\n')
        
        
        
    
    if possessions_of_shots_and_goals_only_without_nextgoal_related_columns == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present)",
              '\n')
    
    
        possessions_df = pd.read_parquet("Possessions_and_Targets_of_Shots_and_Goals_Only_Without_NextGoal_Related_Columns.parquet", engine = "auto")
    
    
        
        # Dimensions of the  Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present)

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present) = {possessions_df.shape}", '\n')
    
    
    
    
    
    return possessions_df











##################################################
#         PITCH VIZUALISATION FUNCTION           #
##################################################



def Plot_Soccer_Pitch( metric_unit = "cm", pitch_color = "green", style_of_the_goals = "entire_goal", linewidth = 2, markersize = 20 ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Plots a Soccer Pitch
    
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
    Input: linewidth = Width of Lines; Default == 2
    Input: markersize = Size of Markers (Ex: Penalty Spot, Centre Spot, Posts); Default == 20
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    fig, ax = plt.subplots(figsize = (12, 8))  # Create a Figure & Axis Object
    
    # Decide What Color the Pitch Should Be; Default --> Green
    
    if pitch_color == 'green':
        
        ax.set_facecolor('mediumseagreen')
        lc = 'whitesmoke'  # Line Color
        pc = 'w'  # 'Spots' Color
        
    elif pitch_color == 'white':
        
        lc = 'k'
        pc = 'k'
        
    
    # ALL DIMENSIONS IN [cm] or [m]
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
        Border_Dimensions = (300, 300)  # Include a Border Around the Playing Area of the Pitch With a Width of 300 cm
    
        Cm_Per_Yard = 91.44  # Unit Conversion From Yards To Centimeters [cm]
    
    
        # Soccer Pitch Dimensions Typically Defined In Yards, So Need To Convert To Centimeters [cm]
        
        Goal_Line_Width = 8 * Cm_Per_Yard
        
        Box_Width = 20 * Cm_Per_Yard
        
        Box_Length = 6 * Cm_Per_Yard
        
        Area_Width = 44 * Cm_Per_Yard
        
        Area_Length = 18 * Cm_Per_Yard
        
        Penalty_Spot = 12 * Cm_Per_Yard
        
        Corner_Radius = 1 * Cm_Per_Yard
        
        D_Length = 8 * Cm_Per_Yard
        
        D_Radius = 10 * Cm_Per_Yard
        
        D_Position = 12 * Cm_Per_Yard
        
        Centre_Circle_Radius = 10 * Cm_Per_Yard
        
        
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
        Border_Dimensions = (3, 3)  # Include a Border Around the Playing Area of the Pitch With a Width of 3 m
    
        M_Per_Yard = 0.9144  # Unit Conversion From Yards To Meters [m]
    
    
        # Soccer Pitch Dimensions Typically Defined In Yards, So Need To Convert To Centimeters [cm]
        
        Goal_Line_Width = 8 * M_Per_Yard
        
        Box_Width = 20 * M_Per_Yard
        
        Box_Length = 6 * M_Per_Yard
        
        Area_Width = 44 * M_Per_Yard
        
        Area_Length = 18 * M_Per_Yard
        
        Penalty_Spot = 12 * M_Per_Yard
        
        Corner_Radius = 1 * M_Per_Yard
        
        D_Length = 8 * M_Per_Yard
        
        D_Radius = 10 * M_Per_Yard
        
        D_Position = 12 * M_Per_Yard
        
        Centre_Circle_Radius = 10 * M_Per_Yard
    
    
    
    Half_Pitch_Length = Pitch_Dimensions[0] / 2. # length of half pitch
    
    Half_Pitch_Width = Pitch_Dimensions[1] / 2. # width of half pitch
    
    Signs = [-1, 1]
    
    
    
    # Plot Half-Way Line & Center Circle
    
    ax.plot([0, 0], [-Half_Pitch_Width, Half_Pitch_Width], lc, linewidth = linewidth)
    
    ax.scatter(0.0, 0.0, marker = 'o', facecolor = lc, linewidth = 0, s = markersize)
    
    y = np.linspace(-1, 1, 50) * Centre_Circle_Radius
    x = np.sqrt(Centre_Circle_Radius**2 - y**2)
    
    ax.plot(x, y, lc, linewidth = linewidth)
    
    ax.plot(-x, y, lc, linewidth = linewidth)
    
    
    for Sign in Signs:  # Plots Each Line Seperately
        
        # Plot Border Boundary Around the Playing Pitch
        
        ax.plot([-(Half_Pitch_Length + Border_Dimensions[0]), Half_Pitch_Length + Border_Dimensions[0]], [Sign*(Half_Pitch_Width + Border_Dimensions[1]), Sign*(Half_Pitch_Width + Border_Dimensions[1])], "k", linewidth = linewidth)
        ax.plot([Sign*(Half_Pitch_Length + Border_Dimensions[0]), Sign*(Half_Pitch_Length + Border_Dimensions[0])], [-(Half_Pitch_Width + Border_Dimensions[1]), (Half_Pitch_Width + Border_Dimensions[1])], "k", linewidth = linewidth)
        
        
        # Plot Playing Pitch Boundary
        
        ax.plot([-Half_Pitch_Length, Half_Pitch_Length], [Sign*Half_Pitch_Width, Sign*Half_Pitch_Width], lc, linewidth = linewidth)
        ax.plot([Sign*Half_Pitch_Length, Sign*Half_Pitch_Length], [-Half_Pitch_Width, Half_Pitch_Width], lc, linewidth = linewidth)
        
        
        # Goal Posts & Line
        
        if style_of_the_goals == "entire_goal":
            
            if metric_unit == "cm":
        
                ax.plot([Sign*(Half_Pitch_Length + Goal_Line_Width/3.25), Sign*(Half_Pitch_Length + Goal_Line_Width/3.25)], [-Goal_Line_Width/2, Goal_Line_Width/2], pc, markersize = 6*markersize/20, linewidth = linewidth*1.5)
                ax.plot([(Sign*Half_Pitch_Length + Sign*110) + 100, (Sign*Half_Pitch_Length + Sign*120) - 100], [Goal_Line_Width/2, Goal_Line_Width/2], pc, markersize = 6*markersize/20, linewidth = linewidth*1.5)
                ax.plot([(Sign*Half_Pitch_Length + Sign*110) + 100, (Sign*Half_Pitch_Length + Sign*120) - 100], [-Goal_Line_Width/2, -Goal_Line_Width/2], pc, markersize = 6*markersize/20, linewidth = linewidth*1.5)
                
            if metric_unit == "m":
                
                ax.plot([Sign*(Half_Pitch_Length + Goal_Line_Width/3.25), Sign*(Half_Pitch_Length + Goal_Line_Width/3.25)], [-Goal_Line_Width/2, Goal_Line_Width/2], pc, markersize = 6*markersize/20, linewidth = linewidth*1.5)
                ax.plot([(Sign*Half_Pitch_Length + Sign*1.1) + 1, (Sign*Half_Pitch_Length + Sign*1.2) - 1], [Goal_Line_Width/2, Goal_Line_Width/2], pc, markersize = 6*markersize/20, linewidth = linewidth*1.5)
                ax.plot([(Sign*Half_Pitch_Length + Sign*1.1) + 1, (Sign*Half_Pitch_Length + Sign*1.2) - 1], [-Goal_Line_Width/2, -Goal_Line_Width/2], pc, markersize = 6*markersize/20, linewidth = linewidth*1.5)
            
        if style_of_the_goals == "only_squared_posts":
        
            ax.plot([Sign*Half_Pitch_Length, Sign*Half_Pitch_Length], [-Goal_Line_Width/2, Goal_Line_Width/2], pc+'s', markersize = 6*markersize/20, linewidth = linewidth)
        
        
        # 6-Yard Box = GK's Small Box
        
        ax.plot([Sign*Half_Pitch_Length, Sign*Half_Pitch_Length - Sign*Box_Length], [Box_Width/2, Box_Width/2], lc, linewidth = linewidth)
        ax.plot([Sign*Half_Pitch_Length, Sign*Half_Pitch_Length - Sign*Box_Length], [-Box_Width/2, -Box_Width/2], lc, linewidth = linewidth)
        ax.plot([Sign*Half_Pitch_Length - Sign*Box_Length, Sign*Half_Pitch_Length - Sign*Box_Length], [-Box_Width/2, Box_Width/2], lc, linewidth = linewidth)
        
        
        # Penalty Area/Box
        
        ax.plot([Sign*Half_Pitch_Length, Sign*Half_Pitch_Length - Sign*Area_Length], [Area_Width/2, Area_Width/2], lc, linewidth = linewidth)
        ax.plot([Sign*Half_Pitch_Length, Sign*Half_Pitch_Length - Sign*Area_Length], [-Area_Width/2, -Area_Width/2], lc, linewidth = linewidth)
        ax.plot([Sign*Half_Pitch_Length - Sign*Area_Length, Sign*Half_Pitch_Length - Sign*Area_Length], [-Area_Width/2, Area_Width/2], lc, linewidth = linewidth)
        
        
        # Penalty Spot
        
        ax.scatter(Sign*Half_Pitch_Length - Sign*Penalty_Spot, 0.0, marker = 'o', facecolor = lc, linewidth = 0, s = markersize)
        
        
        # Corner Flags
        
        y = np.linspace(0, 1, 50) * Corner_Radius
        x = np.sqrt(Corner_Radius**2 - y**2)
        
        ax.plot(Sign*Half_Pitch_Length - Sign*x, -Half_Pitch_Width + y, lc, linewidth = linewidth)
        ax.plot(Sign*Half_Pitch_Length - Sign*x, Half_Pitch_Width - y, lc, linewidth = linewidth)
        
        
        # Draw the D (Outside the Main Box)
        
        y = np.linspace(-1, 1, 50) * D_Length  # D_Length Is the Chord of the Circle That Defines the D
        x = np.sqrt(D_Radius**2 - y**2) + D_Position
        
        ax.plot(Sign*Half_Pitch_Length - Sign*x, y, lc, linewidth = linewidth)
        
        
    # Remove Axis Labels & Ticks
    
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    
    ax.set_xticks([])
    ax.set_yticks([])
    
    
    # Set Axis Limits
    
    xmax = Pitch_Dimensions[0]/2 + Border_Dimensions[0]
    ymax = Pitch_Dimensions[1]/2 + Border_Dimensions[1]
    
    ax.set_xlim([-xmax, xmax])
    ax.set_ylim([-ymax, ymax])
    
    ax.set_axisbelow(True)
    
    
    
    
    return fig, ax











###################################################
#                 EDA FUNCTIONS                   #
###################################################



def Correlation_Heat_Map_Between_Features(df, dataset_string_name, figure_size = (14, 12)):
    """
    Function That Displays a Correlation Heat-Map Between the Features of the Specified Dataset/DataFrame
    
    Input: df = DataFrame We Want To Inspect
    Input: dataset_string_name = String of the Name of the DataFrame
    Input: figure_size = Size of the Figure In Inches As a Tuple -->  "(Width, Height)"
    
    Output: Correlation Heat-Map Between the Features of the Specified Dataset/DataFrame
    """
    
    Mask = np.zeros_like(df.corr(numeric_only = True))

    Mask[np.triu_indices_from(Mask)] = True



    with sns.axes_style("white"):

        fig, axis = plt.subplots(figsize = figure_size)

        axis = sns.heatmap(data = df.corr(numeric_only = True), mask = Mask, cmap = 'coolwarm', cbar = True, vmax = 1.0, vmin = -1.0, square = True, linewidth = 0.5)


    plt.title('Correlation Heat-Map Between Features', fontsize = 14)



    plt.savefig(f'EDA_Figures/Correlation_Heat-Map_Between_Features--In_the_{dataset_string_name}_Dataset.png')

    plt.show()











###################################################
#      PLAYERS' INFO. DATA-RELATED FUNCTIONS      #
###################################################



def Read_Players_Info_Dataset( original_players_info_dataset = False, reduced_players_info_dataset = False ):
    """
    Function That Reads-In the Specified Players' Info. Dataset
        
    At Least 1 of the Parameters MUST Be Set To `True` !!
    
    Input: original_players_info_dataset = Boolean Value, That States Whether This Should Be the Version of the Players' Info. Dataset To Be Read-In
    Input: reduced_players_info_dataset = Boolean Value, That States Whether This Should Be the Version of the Players' Info. Dataset To Be Read-In
        
    Output: players_info_df = Specified Players' Info. Dataset
    """
    
    if original_players_info_dataset == True:
        
        print('\n',
              "Loading & Reading-In the Original Version of the Players' Info. Dataset",
              '\n')
    
    
        players_info_df = pd.read_parquet(f"Players_Info.parquet", engine = "auto")
    
    
        
        # Dimensions of the Original Version of the Players' Info. Dataset

        print(f"Dimensions of the Original Version of the Players' Info. Dataset = {players_info_df.shape}", '\n')
    
    
    
    
    if reduced_players_info_dataset == True:
        
        print('\n',
              "Loading & Reading-In the Reduced Version of the Players' Info. Dataset",
              '\n')
    
    
        players_info_df = pd.read_parquet(f"Players_Info_Reduced.parquet", engine = "auto")
    
    
        
        # Dimensions of the Reduced Version of the Players' Info. Dataset

        print(f"Dimensions of the Reduced Version of the Players' Info. Dataset = {players_info_df.shape}", '\n')
    
    
    
    
    return players_info_df











###################################################
#  POSSESSIONS & TARGETS' DATA-RELATED FUNCTIONS  #
###################################################



def Read_Possessions_Dataset( original_possessions_dataset = False, all_possessions_with_shots_and_goals = False, possessions_with_shots_and_goals_only_with_nextgoal_related_columns = False, possessions_with_shots_and_goals_only_without_nextgoal_related_columns = False ):
    """
    Function That Reads-In the Specified Possessions' & Targets' Dataset
        
    At Least 1 of the Parameters MUST Be Set To `True` !!
    
    Input: original_possessions_dataset = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: all_possessions_with_shots_and_goals = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: possessions_with_shots_and_goals_only_with_nextgoal_related_columns = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    Input: possessions_with_shots_and_goals_only_without_nextgoal_related_columns = Boolean Value, That States Whether This Should Be the Version of the Possessions' Dataset To Be Read-In
    
    Output: possessions_df = Specified Possessions' & Targets' Dataset
    """
    
    if original_possessions_dataset == True:
        
        print('\n',
              "Loading & Reading-In the Original Version of the Possessions' & Targets' Dataset",
              '\n')
    
    
        possessions_df = pd.read_parquet(f"Possessions_and_Targets.parquet", engine = "auto")
    
    
        
        # Dimensions of the Original Version of the Possessions' & Targets' Dataset

        print(f"Dimensions of the Original Version of the Possessions' & Targets' Dataset = {possessions_df.shape}", '\n')
    
    
    
    
    if all_possessions_with_shots_and_goals == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included",
              '\n')
    
    
        possessions_df = pd.read_parquet(f"Possessions_and_Targets_With_Shots_and_Goals.parquet", engine = "auto")
    
    
        
        # Dimensions of the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which All Possessions Are Present, With Shots + Goals Indications Included = {possessions_df.shape}", '\n')
    
    
    
    
    if possessions_with_shots_and_goals_only_with_nextgoal_related_columns == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present)",
              '\n')
    
    
        possessions_df = pd.read_parquet(f"Possessions_and_Targets_of_Shots_and_Goals_Only_With_NextGoal_Related_Columns.parquet", engine = "auto")
    
    
        
        # Dimensions of the  Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present)

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present) = {possessions_df.shape}", '\n')
        
        
        
    
    if possessions_with_shots_and_goals_only_without_nextgoal_related_columns == True:
        
        print('\n',
              "Loading & Reading-In the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present)",
              '\n')
    
    
        possessions_df = pd.read_parquet(f"Possessions_and_Targets_of_Shots_and_Goals_Only_Without_NextGoal_Related_Columns.parquet", engine = "auto")
    
    
        
        # Dimensions of the  Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present)

        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present) = {possessions_df.shape}", '\n')
    
    
    
    
    
    return possessions_df











###################################################
#        TRACKING DATA-RELATED FUNCTIONS          #
###################################################



def Read_Final_Version_Match_Tracking_Data(match_num = None):
    """
    Function That Reads the Final Version of the Tracking Data of the Specified Football Match Number `match_num`
    
    Input: match_num = Integer Number Representing the "match_num_Final.parquet" File Containing the Tracking Data of That Football Match
    
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the "match_num_Final.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    match_num = int(input("For Which Match Would You Like To Load & Read Its Respective Tracking Data? -- NOTE: Must Choose a Number In the Range [0, 360]  -->  "))
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data For Match #{match_num + 1}",
          '\n')
    
    
    Tracking_Data_Folder = "Tracking Data/"    
    
    Final_Match_Tracking_Data_df = pd.read_parquet(f"{Tracking_Data_Folder}{match_num}_Final.parquet", engine = "auto")
    
    
    
    
    # Dimensions of the Dataset of the Final Version of the Tracking Data For Match `match_num`

    print(f"Dimensions of the Dataset of the Final Version of the Tracking Data For Match #{match_num + 1} = {Final_Match_Tracking_Data_df.shape}", '\n')
    
    
    return Final_Match_Tracking_Data_df










def To_Single_Playing_Direction( match_tracking_data_df ):
    '''
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Flips the (X- & Y-)Coordinates In the 2nd-Half So That Each Team Always Shoots In the Same Direction Throughout the Match.
    
    Input: match_tracking_data_df = DataFrame of the Match Tracking Data We Want To Inspect
    
    Output: Match_Tracking_Data_Playing_In_One_Same_Direction_All_Match_Long_df = DataFrame of the Match Tracking Data, Where All the (X- & Y-)Coordinates In the 2nd-Half Are Flipped So That Each Team Always Shoots In the Same Direction Throughout the Match
    '''
    
    
    Match_Tracking_Data_Playing_In_One_Same_Direction_All_Match_Long_df = match_tracking_data_df.copy()
    
    First_Or_Second_Half = "Section"   # 1.0 = 1st-Half  /  2.0 = 2nd-Half
    
    Second_Half_Index = Match_Tracking_Data_Playing_In_One_Same_Direction_All_Match_Long_df[First_Or_Second_Half].idxmax(0)
    
    
    
    All_Players_and_Ball_2D_Coordinates_and_Velocities_Tracking_Data_Columns = ['X', 'Y',
                                                                                'V_xBall', 'V_yBall',
                                                                                'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8', 'X9', 'X10', 'X11',
                                                                                'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8', 'Y9', 'Y10', 'Y11',
                                                                                'V_x1', 'V_x2', 'V_x3', 'V_x4', 'V_x5', 'V_x6', 'V_x7', 'V_x8', 'V_x9', 'V_x10', 'V_x11',
                                                                                'V_y1', 'V_y2', 'V_y3', 'V_y4', 'V_y5', 'V_y6', 'V_y7', 'V_y8', 'V_y9', 'V_y10', 'V_y11',
                                                                                'X12', 'X13', 'X14', 'X15', 'X16', 'X17', 'X18', 'X19', 'X20', 'X21', 'X22',
                                                                                'Y12', 'Y13', 'Y14', 'Y15', 'Y16', 'Y17', 'Y18', 'Y19', 'Y20', 'Y21', 'Y22',
                                                                                'V_x12', 'V_x13', 'V_x14', 'V_x15', 'V_x16', 'V_x17', 'V_x18', 'V_x19', 'V_x20', 'V_x21', 'V_x22',
                                                                                'V_y12', 'V_y13', 'V_y14', 'V_y15', 'V_y16', 'V_y17', 'V_y18', 'V_y19', 'V_y20', 'V_y21', 'V_y22']
        
    
    Match_Tracking_Data_Playing_In_One_Same_Direction_All_Match_Long_df.loc[Second_Half_Index : , All_Players_and_Ball_2D_Coordinates_and_Velocities_Tracking_Data_Columns] *= -1
        
        
        
        
    return Match_Tracking_Data_Playing_In_One_Same_Direction_All_Match_Long_df










def Find_Team_GoalKeeper_Column_Name( home_team = False, away_team = False ):
    '''
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Outputs the Home or Away Team's Goalkeeper Column Name In the `match_tracking_data_df` Based On the Specified Team.
    
    Input: home_team = Boolean Value, Where == `True` If the Team Is the Home Team, == `False` Otherwise  -->  Default == `False`
    Input: away_team = Boolean Value, Where == `True` If the Team Is the Away Team, == `False` Otherwise  -->  Default == `False`
        
    Output: String --> The Column Name Representing the Specified Team's Goalkeeper's X-Coordinate
    '''
    
    
    if home_team == True:
        
        return "X1"
    
    elif away_team == True:
        
        return "X12"
    
    else:
        
        return "1 of the Parameters, Either `home_team` or `away_team` Must Be Set To `True`"
    









def Find_Team_GoalKeeper_Kit_Number( home_team = False, away_team = False ):
    '''
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Outputs the Home or Away Team's Goalkeeper Kit Number In the `match_tracking_data_df` Based On the Specified Team.
    
    Input: home_team = Boolean Value, Where == `True` If the Team Is the Home Team, == `False` Otherwise  -->  Default == `False`
    Input: away_team = Boolean Value, Where == `True` If the Team Is the Away Team, == `False` Otherwise  -->  Default == `False`
        
    Output: String --> Integer of the GK's Kit Number
    '''
    
    
    if home_team == True:
        
        return "1"
    
    elif away_team == True:
        
        return "12"
    
    else:
        
        return "1 of the Parameters, Either `home_team` or `away_team` Must Be Set To `True`"
    









def Find_Playing_Direction_of_Team( match_tracking_data_df, home_team = False, away_team = False ):
    '''
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Finds the Direction of Play For the Specified Team
    
    Input: match_tracking_data_df = DataFrame of the Match Tracking Data We Want To Inspect
    Input: home_team = Boolean Value, Where == `True` If the Team Is the Home Team, == `False` Otherwise  -->  Default == `False`
    Input: away_team = Boolean Value, Where == `True` If the Team Is the Away Team, == `False` Otherwise  -->  Default == `False` 
    
    Output: String --> Stating the Direction of Play For the Specified Team
    '''    
    
    
    GK_X_Coordinate_Column = TFVFs.Find_Team_GoalKeeper_Column_Name(home_team = home_team, away_team = away_team)
    
    
    
    if ( GK_X_Coordinate_Column == "X1" ) & ( -(np.sign(match_tracking_data_df.iloc[0][GK_X_Coordinate_Column])) == +1 ):      # +ve is left --> right
    
        print("Home Team Plays (Attacks) From Left --> Right", '\n')
        
        return 1   # 1 == Home Team Plays: Left --> Right
    
    
    if ( GK_X_Coordinate_Column == "X1" ) & ( -(np.sign(match_tracking_data_df.iloc[0][GK_X_Coordinate_Column])) == -1 ):      # -ve is right --> left
    
        print("Home Team Plays (Attacks) From Right --> Left", '\n')
        
        return -1   # -1 == Home Team Plays: Right --> Left
    
    
    
    
    if ( GK_X_Coordinate_Column == "X12" ) & ( -(np.sign(match_tracking_data_df.iloc[0][GK_X_Coordinate_Column])) == +1 ):      # +ve is left --> right
    
        print("Away Team Plays (Attacks) From Left --> Right", '\n')
        
        return 1   # 1 == Away Team Plays: Left --> Right
    
    
    if ( GK_X_Coordinate_Column == "X12" ) & ( -(np.sign(match_tracking_data_df.iloc[0][GK_X_Coordinate_Column])) == -1 ):      # -ve is right --> left
    
        print("Away Team Plays (Attacks) From Right --> Left", '\n')
        
        return -1   # -1 == Away Team Plays: Right --> Left
    
    
    
    else:
        
        return "1 of the Parameters, Either `home_team` or `away_team` Must Be Set To `True`"










def Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row, verbose = True):
    '''
    Function That Finds the Direction of Play For Both Teams
    
    Input: home_team_tracking_data_row = Row (i.e. Instant) of the Home Team's Tracking Data DataFrame
    
    Output: String --> Stating the Direction of Play For Both Teams
    '''    
    
    if ( -(np.sign(home_team_tracking_data_row["X1"])) == +1 ):    # {+1 = Left --> Right; -1 = Right --> Left}

        if verbose == True:
            
            print("Home Team Plays (Attacks) From Left --> Right  /  Away Team Plays (Attacks) From Right --> Left")
            
        
        return 1
    
    
    
    if ( -(np.sign(home_team_tracking_data_row["X1"])) == -1 ):    # {+1 = Left --> Right; -1 = Right --> Left}

        if verbose == True:
            
            print("Home Team Plays (Attacks) From Right --> Left  /  Away Team Plays (Attacks) From Left --> Right")
        
        
        return -1
    
    
    
    

    
    
    
    
    
def Plot_Single_Match_Frame( home_team_tracking_data_row, away_team_tracking_data_row, ball_tracking_data_row, team_colors = ('b', 'r'), home_team_players_color_and_style = "bo", away_team_players_color_and_style = "ro", ball_color_and_style = "ko", include_player_velocities = True, include_ball_velocity = False, player_marker_size = 10, player_alpha = 0.7, display_players_currently_in_possession = True, match_encoded_id = None, frame_number = None, show_kit_numbers = False, kit_numbers_on_player_or_next_to_player = "next to player", figax = None, metric_unit = "cm", pitch_color = "green", style_of_the_goals = "entire_goal" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Plots a Single Frame of Match Tracking Data (Player Positions & Ball) On a Soccer Pitch
    
    Input: home_team_tracking_data_row = Row (i.e. Instant) of the Home Team's Tracking Data DataFrame
    Input: away_team_tracking_data_row = Row of the Away Team's Tracking Data DataFrame
    Input: ball_tracking_data_row = Row of the Ball's (3D) Tracking Data DataFrame
    Input: team_colors = Tuple Containing the Team Colors of the Home & Away Teams; Default == ('b', 'r')  -->  'b' (Blue, Home Team) & 'r' (Red, Away Team)
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: include_player_velocities = Boolean Value, That Determines Whether Player Velocities Are Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: include_ball_velocity = Boolean Value, That Determines Whether the Ball's Velocity Is Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: player_alpha = Alpha (Transparency) Coefficient of Players' Markers; Default == 0.7
    Input: display_players_currently_in_possession = Boolean Value, Stating Whether the Video-Clip Should Include & Display An Indication of the Player Currently In Possession of the Ball, By Adding a Yellow/Golden Ring Around the Player's Marker; Default == True
    Input: match_encoded_id = Integer Value, Indicating the Encoded Match ID (≡ Match# - 1)  --  Ex: Match# = 84  -->  Match ID ≡ `match_encoded_id` = 83; `match_encoded_id` Only Has An Argument Passed To It IF --> `display_players_currently_in_possession = True`
    Input: frame_number = Frame # Which We Specifically Want To Visualize; `frame_number` Only Has An Argument Passed To It IF --> `display_players_currently_in_possession = True`
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: kit_numbers_on_player_or_next_to_player = String That Determines Whether the Players' Kit Numbers Should Be Shown On the Players' Marker Or Next To It; Options  -->  {"next to player", "on player"}; Default == "next to player"
    Input: figax = Tuple of the Form `(fig, ax)`, That Can Be Used To Pass In the `(fig, ax)` Objects of a Previously Generated Pitch; Set To `(fig, ax)` To Re-Use An Existing/Old Pitch (With Data On It Or Not), Or None (the Default) To Generate a New Pitch Plot
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    if figax is None:  # Create a New Pitch
        
        fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
        
    else: # Overlay On a Previously Generated Pitch
        
        fig, ax = figax  # Unpack Specified Tuple Argument of the Parameter
        
    
    
    if display_players_currently_in_possession == True:
    
        Possessions_df = TFVFs.Read_Possessions_Dataset( all_possessions_with_shots_and_goals = True )
                        
        Possessions_of_Current_Match_df = Possessions_df[Possessions_df["MatchId"] == match_encoded_id]
        
        Frames_At_Which_Possession_Starts_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["frames"].values.astype(int)
                        
        Possession_Durations_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["duration"].values.astype(int)
        
        Players_Currently_In_Possession_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["players"].values.astype(int)
    
    
    
    # Plot Home & Away Teams In Order
    
    for Team, Color in zip( [home_team_tracking_data_row, away_team_tracking_data_row], team_colors ):
        
        X_Columns = [c for c in Team.keys() if c[0] == 'X']  # Column Name For Players' X-Coordinate Positions
        Y_Columns = [c for c in Team.keys() if c[0] == 'Y']  # Column Name For Players' Y-Coordinate Positions
        
        
        
        
        if display_players_currently_in_possession == False:
            
            ax.plot( Team[X_Columns], Team[Y_Columns], Color+'o', markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
            
            
            
        if display_players_currently_in_possession == True:
                        
            ax.plot( Team[X_Columns], Team[Y_Columns], Color+'o', markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                
            for Frames_At_Which_Possession_Starts_series_Value, Possession_Durations_series_Value, Players_Currently_In_Possession_series_Value in zip(Frames_At_Which_Possession_Starts_series_Values, Possession_Durations_series_Values, Players_Currently_In_Possession_series_Values):
        
                if frame_number in range(Frames_At_Which_Possession_Starts_series_Value, (Frames_At_Which_Possession_Starts_series_Value + Possession_Durations_series_Value) + 1):
        
                    Player_Currently_In_Possession_X_Coordinate_Column_Name = "X" + str(Players_Currently_In_Possession_series_Value)
                    Player_Currently_In_Possession_Y_Coordinate_Column_Name = "Y" + str(Players_Currently_In_Possession_series_Value)
                
                
                
                    if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Home_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Home_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                        ax.plot( home_team_tracking_data_row[Player_Currently_In_Possession_X_Coordinate_Column_Name], home_team_tracking_data_row[Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                            home_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                        
                
                    if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Away_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Away_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                        ax.plot( away_team_tracking_data_row[Player_Currently_In_Possession_X_Coordinate_Column_Name], away_team_tracking_data_row[Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                            away_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                        
            
        
        
        
        if show_kit_numbers == True:
            
            if metric_unit == "cm":
                
                if kit_numbers_on_player_or_next_to_player == "next to player":
            
                    [ ax.text( Team[x]+75, Team[y]+75, "".join(list(x)[1 : ]), fontsize = 10, color = Color  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                if kit_numbers_on_player_or_next_to_player == "on player":
            
                    [ ax.text( Team[x]-50, Team[y]-50, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                
            if metric_unit == "m":
                
                if kit_numbers_on_player_or_next_to_player == "next to player":
            
                    [ ax.text( Team[x]+2, Team[y]+2, "".join(list(x)[1 : ]), fontsize = 10, color = Color  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                if kit_numbers_on_player_or_next_to_player == "on player":
            
                    [ ax.text( Team[x]-1.5, Team[y]-1.5, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                
                
                
        if include_player_velocities == True:
            
            Vx_Columns = [c for c in Team.keys() if c[ : 3] == 'V_x']  # Column Name For Players' Velocity Component In the X-Direction
            Vy_Columns = [c for c in Team.keys() if c[ : 3] == 'V_y']  # Column Name For Players' Velocity Component In the Y-Direction
            
            
            if metric_unit == "cm":
                
                ax.quiver( Team[X_Columns].values.astype(np.float64), Team[Y_Columns].values.astype(np.float64),
                           Team[Vx_Columns].values.astype(np.float64), Team[Vy_Columns].values.astype(np.float64),
                           color = Color, scale_units = 'inches', scale = 1000, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
                
                
            if metric_unit == "m":
                
                ax.quiver( Team[X_Columns].values.astype(np.float64), Team[Y_Columns].values.astype(np.float64),
                           Team[Vx_Columns].values.astype(np.float64), Team[Vy_Columns].values.astype(np.float64),
                           color = Color, scale_units = 'inches', scale = 10, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
            
            
        
    # Plot the Ball
    
    # Since Some -ve Values Have Been Spotted For the Ball's Height ("Z"), Which Is Not Possible:
    # Check if There Are Values < 0 In Column "Z" (i.e. Height of the Ball) --> Convert -ve Values Into Their Respective Absolute Values, & the Original Values That Are >= 0 Are Retained
    
    if (ball_tracking_data_row["Z"] < 0).any():
        
        ball_tracking_data_row["Z"] = np.abs(ball_tracking_data_row["Z"])

    
    ax.plot( ball_tracking_data_row["X"], ball_tracking_data_row["Y"], 'ko', markersize = np.log(ball_tracking_data_row["Z"]), alpha = 1.0, linewidth = 0 )
    
    
    
    if include_ball_velocity == True:
            
            
        if metric_unit == "cm":
            
            ax.quiver( ball_tracking_data_row["X"], ball_tracking_data_row["Y"],
                       ball_tracking_data_row["V_xBall"], ball_tracking_data_row["V_yBall"],
                       color = "k", scale_units = 'inches', scale = 1000, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
            
            
            
        if metric_unit == "m":
            
            # ax.quiver( ball_tracking_data_row["X"], ball_tracking_data_row["Y"],
            #            ball_tracking_data_row["V_xBall"], ball_tracking_data_row["V_yBall"],
            #            color = "k", scale_units = 'inches', scale = 10, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
            
            
            ax.quiver( ball_tracking_data_row["X"], ball_tracking_data_row["Y"],
                       0, 0,
                       color = "k", scale_units = 'inches', scale = 10, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
    
    
    
    
    return fig, ax










def Plot_Players_and_Ball_Trajectories( match_tracking_data_df, start_frame, end_frame, home_team_players, away_team_players, home_team_players_color_and_style = "b.", away_team_players_color_and_style = "r.", ball_color_and_style = "k.", player_marker_size = 1, show_kit_numbers = True, figax = None, metric_unit = "cm", pitch_color = "green", style_of_the_goals = "entire_goal" ):
    """
    Function That Plots the Players' + Ball's Trajectories Accross the Pitch
    
    Input: match_tracking_data_df = DataFrame of the Match Tracking Data
    Input: start_frame = Starting Frame # (Frame In Which the Trajectory Starts)
    Input: end_frame = Ending Frame # (Frame In Which the Trajectory Ends)
    Input: home_team_players = List of Player #s (Integers) For the Home Team
    Input: away_team_players = List of Player #s (Integers) For the Away Team
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: figax = Tuple of the Form `(fig, ax)`, That Can Be Used To Pass In the `(fig, ax)` Objects of a Previously Generated Pitch; Set To `(fig, ax)` To Re-Use An Existing/Old Pitch (With Data On It Or Not), Or None (the Default) To Generate a New Pitch Plot
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    if figax is None:  # Create a New Pitch
        
        fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
        
    else: # Overlay On a Previously Generated Pitch
        
        fig, ax = figax  # Unpack Specified Tuple Argument of the Parameter
        
    
    
    # Plot the Ball's Trajectory
    
    # Since Some -ve Values Have Been Spotted For the Ball's Height ("Z"), Which Is Not Possible:
    # Check if There Are Values < 0 In Column "Z" (i.e. Height of the Ball) --> Convert -ve Values Into Their Respective Absolute Values, & the Original Values That Are >= 0 Are Retained
    
    if (match_tracking_data_df["Z"] < 0).any():
        
        match_tracking_data_df["Z"] = np.abs(match_tracking_data_df["Z"])

    
    for Frame in range(start_frame, end_frame + 1):
        
        ax.plot( match_tracking_data_df.loc[Frame, "X"], match_tracking_data_df.loc[Frame, "Y"],
                 ball_color_and_style, markersize = np.log( match_tracking_data_df.loc[Frame , "Z"] ) )
    
    
    if show_kit_numbers == True:
    
        ax.annotate("Ball", (match_tracking_data_df.loc[end_frame, "X"] - 200, match_tracking_data_df.loc[end_frame, "Y"] + 50),
                    color = ball_color_and_style[0], size = 10)
    
    
    
    # Plot Home Team Players' Trajectories
    
    for Home_Team_Player_Number in home_team_players:

        ax.plot( match_tracking_data_df.loc[start_frame : end_frame, f"X{Home_Team_Player_Number}"], match_tracking_data_df.loc[start_frame : end_frame, f"Y{Home_Team_Player_Number}"],
                home_team_players_color_and_style, markersize = player_marker_size )
        
        
        if show_kit_numbers == True:
    
            ax.annotate( f"{Home_Team_Player_Number}", (match_tracking_data_df.loc[end_frame, f"X{Home_Team_Player_Number}"] + 50, match_tracking_data_df.loc[end_frame, f"Y{Home_Team_Player_Number}"] + 50),
                        color = home_team_players_color_and_style[0], size = 10 )

    
    
    
    
    # Plot Away Team Players' Trajectories
    
    for Away_Team_Player_Number in away_team_players:

        ax.plot( match_tracking_data_df.loc[start_frame : end_frame, f"X{Away_Team_Player_Number}"], match_tracking_data_df.loc[start_frame : end_frame, f"Y{Away_Team_Player_Number}"],
                away_team_players_color_and_style, markersize = player_marker_size )
        
        
        if show_kit_numbers == True:
    
            ax.annotate( f"{Away_Team_Player_Number}", (match_tracking_data_df.loc[end_frame, f"X{Away_Team_Player_Number}"] + 50, match_tracking_data_df.loc[end_frame, f"Y{Away_Team_Player_Number}"] + 50),
                        color = away_team_players_color_and_style[0], size = 10 )
            
            
    
    
    return fig, ax









    
def Save_Match_Possession_VideoClip( start_frame, end_frame, frames_per_second, home_team_tracking_data_df, away_team_tracking_data_df, ball_tracking_data_df, home_team_players_color_and_style = "bo", away_team_players_color_and_style = "ro", ball_color_and_style = "ko", include_players_trajectories = False, include_ball_trajectory = False, include_player_velocities = True, player_marker_size = 10, player_alpha = 0.7, display_players_currently_in_possession = True, match_encoded_id = None, show_kit_numbers = True, kit_numbers_on_player_or_next_to_player = "next to player", figax = None, metric_unit = "cm", pitch_color = "green", style_of_the_goals = "entire_goal", file_path = "Shots', Goals' & Possessions' Movies", file_name = "Match_Possession_Test_Clip" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Generates a Movie From Match Tracking Data, Saving It As An `.mp4` File In the Path `file_path` Directory With File Name `file_name`
    
    Input: start_frame = Starting Frame # (Frame In Which the Trajectory Starts)
    Input: end_frame = Ending Frame # (Frame In Which the Trajectory Ends)
    Input: frames_per_second = # Frames Per Second (Frequency) To Assume When Generating the Movie; Default == 25
    Input: home_team_tracking_data_df = Home Team's Tracking Data DataFrame - Movie Will Be Created From All Rows In the DataFrame
    Input: away_team_tracking_data_df = Away Team's Tracking Data DataFrame - The Indices of This DataFrame MUST ≡ Indices From the `home_team_tracking_data_df` DataFrame
    Input: ball_tracking_data_df = Ball's Tracking Data DataFrame
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: include_players_trajectories = Boolean Value, That Determines Whether To Include & Visualise the Players' Trajectories, Or To Only Visualise Them As Single Points
    Input: include_ball_trajectory = Boolean Value, That Determines Whether To Include & Visualise the Ball's Trajectory, Or To Only Visualise It As a Single Point
    Input: include_player_velocities = Boolean Value, That Determines Whether Player Velocities Are Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: player_alpha = Alpha (Transparency) Coefficient of Players' Markers; Default == 0.7
    Input: display_players_currently_in_possession = Boolean Value, Stating Whether the Video-Clip Should Include & Display An Indication of the Player Currently In Possession of the Ball, By Adding a Yellow/Golden Ring Around the Player's Marker; Default == True
    Input: match_encoded_id = Integer Value, Indicating the Encoded Match ID (≡ Match# - 1)  --  Ex: Match# = 84  -->  Match ID ≡ `match_encoded_id` = 83
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: kit_numbers_on_player_or_next_to_player = String That Determines Whether the Players' Kit Numbers Should Be Shown On the Players' Marker Or Next To It; Options  -->  {"next to player", "on player"}; Default == "next to player"
    Input: figax = Tuple of the Form `(fig, ax)`, That Can Be Used To Pass In the `(fig, ax)` Objects of a Previously Generated Pitch; Set To `(fig, ax)` To Re-Use An Existing/Old Pitch (With Data On It Or Not), Or None (the Default) To Generate a New Pitch Plot
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
    Input: file_path = Directory To Save the Movie In; Default == "Shots', Goals' & Possessions' Movies"
    Input: file_name = Movie's File-Name; Default == "Match_Possession_Test_Clip"
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    # Set Figure & Movie Settings
    
    FFMpegWriter = animation.writers["ffmpeg"]
    
    MetaData = dict( title = file_name, artist = "Hertha BSC Broadcast Tracking Data Video-Clip", comment = "Matplotlib" )
    
    Writer = FFMpegWriter(fps = frames_per_second, metadata = MetaData)
    
    File_Name = file_path + '/' +  file_name + '.mp4'   # Directory Path + File-Name
    
    
    # Create Soccer Pitch
    
    if figax is None:  # Create a New Pitch
        
        fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
        
    else: # Overlay On a Previously Generated Pitch
        
        fig, ax = figax  # Unpack Specified Tuple Argument of the Parameter
        
    fig.set_tight_layout(True)
    
    
    # Generate Movie
    
    print("Generating Video-Clip... \n \n", end = '')
    
    Team_Colors = (home_team_players_color_and_style, away_team_players_color_and_style)
    
    
    
    if display_players_currently_in_possession == True:
    
        Possessions_df = TFVFs.Read_Possessions_Dataset( all_possessions_with_shots_and_goals = True )
                        
        Possessions_of_Current_Match_df = Possessions_df[Possessions_df["MatchId"] == match_encoded_id]
        
        Frames_At_Which_Possession_Starts_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["frames"].values.astype(int)
                        
        Possession_Durations_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["duration"].values.astype(int)
        
        Players_Currently_In_Possession_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["players"].values.astype(int)
    
    
    
    with Writer.saving(fig, File_Name, 100):
        
        for Frame in range(start_frame, end_frame + 1):
            
            Figure_Objects = []   # This Is Used To Collect Up All the Axis Objects So That They Can Be Deleted After Each Iteration
            
            
            # Plot Home & Away Teams In Order
    
            for Team, Color in zip( [home_team_tracking_data_df.loc[Frame], away_team_tracking_data_df.loc[Frame]], Team_Colors ):
        
                X_Columns = [c for c in Team.keys() if c[0] == 'X']  # Column Name For Players' X-Coordinate Positions
                Y_Columns = [c for c in Team.keys() if c[0] == 'Y']  # Column Name For Players' Y-Coordinate Positions
        
                
                if include_players_trajectories == False:
                    
                    if display_players_currently_in_possession == False:
                        
                    
                        Objects, = ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                        Figure_Objects.append(Objects)
                
                
                
                
                    if display_players_currently_in_possession == True:
                        
                        
                        Objects, = ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                        Figure_Objects.append(Objects)
                
                
                
                        for Frames_At_Which_Possession_Starts_series_Value, Possession_Durations_series_Value, Players_Currently_In_Possession_series_Value in zip(Frames_At_Which_Possession_Starts_series_Values, Possession_Durations_series_Values, Players_Currently_In_Possession_series_Values):
        
                            if Frame in range(Frames_At_Which_Possession_Starts_series_Value, (Frames_At_Which_Possession_Starts_series_Value + Possession_Durations_series_Value) + 1):
        
                                Player_Currently_In_Possession_X_Coordinate_Column_Name = "X" + str(Players_Currently_In_Possession_series_Value)
                                Player_Currently_In_Possession_Y_Coordinate_Column_Name = "Y" + str(Players_Currently_In_Possession_series_Value)
                
                
                
                                if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Home_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Home_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                                    Objects, = ax.plot( home_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_X_Coordinate_Column_Name], home_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                                        home_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                                    Figure_Objects.append(Objects)
                
                
                
                
                                if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Away_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Away_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                                    Objects, = ax.plot( away_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_X_Coordinate_Column_Name], away_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                                        away_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                                    Figure_Objects.append(Objects)
                
                
                
                
                if include_players_trajectories == True:
            
                    ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = 3, alpha = player_alpha )  # Plot Players' Positions
                
                
                
                if show_kit_numbers == True:
            
                    if metric_unit == "cm":
                    
                        if kit_numbers_on_player_or_next_to_player == "next to player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]+75, Team[y]+75, "".join(list(x)[1 : ]), fontsize = 10, color = Color[0]  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List
                    
                
                        if kit_numbers_on_player_or_next_to_player == "on player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]-50, Team[y]-50, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List            
                        
                
                        for Kit_Number in Kit_Numbers_List:
                        
                            Figure_Objects.append(Kit_Number)
                
                
                    
                    if metric_unit == "m":
                        
                        if kit_numbers_on_player_or_next_to_player == "next to player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]+2, Team[y]+2, "".join(list(x)[1 : ]), fontsize = 10, color = Color[0]  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List
                    
                    
                        if kit_numbers_on_player_or_next_to_player == "on player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]-1.5, Team[y]-1.5, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List                    
                    
                
                        for Kit_Number in Kit_Numbers_List:
                        
                            Figure_Objects.append(Kit_Number)
                
                
        
        
                if include_player_velocities == True:
            
                    Vx_Columns = [c for c in Team.keys() if c[ : 3] == 'V_x']  # Column Name For Players' Velocity Component In the X-Direction
                    Vy_Columns = [c for c in Team.keys() if c[ : 3] == 'V_y']  # Column Name For Players' Velocity Component In the Y-Direction
            
            
                    Objects =  ax.quiver( Team[X_Columns].values.astype(np.float64), Team[Y_Columns].values.astype(np.float64),
                                          Team[Vx_Columns].values.astype(np.float64), Team[Vy_Columns].values.astype(np.float64),
                                          color = Color[0], scale_units = 'inches', scale = 1000, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
            
                    
                
                    Figure_Objects.append(Objects)
            
            
            
            
            
            # Plot the Ball
    
            # Since Some -ve Values Have Been Spotted For the Ball's Height ("Z"), Which Is Not Possible:
            # Check if There Are Values < 0 In Column "Z" (i.e. Height of the Ball) --> Convert -ve Values Into Their Respective Absolute Values, & the Original Values That Are >= 0 Are Retained
    
            if (ball_tracking_data_df.loc[Frame, "Z"] < 0).any():
        
                ball_tracking_data_df.loc[Frame, "Z"] = np.abs(ball_tracking_data_df.loc[Frame, "Z"])
            
            
            
            if include_ball_trajectory == False:
        
                Objects, = ax.plot( ball_tracking_data_df.loc[Frame, "X"], ball_tracking_data_df.loc[Frame, "Y"],
                                    ball_color_and_style, markersize = np.log(ball_tracking_data_df.loc[Frame, "Z"]), alpha = 1.0, linewidth = 0 )
                    
                Figure_Objects.append(Objects)
                
                
                
            if include_ball_trajectory == True:
                
                ax.plot( ball_tracking_data_df.loc[Frame, "X"], ball_tracking_data_df.loc[Frame, "Y"],
                         ball_color_and_style, markersize = np.log(ball_tracking_data_df.loc[Frame, "Z"]), alpha = 1.0, linewidth = 0 )
            
            
            
            
            # Include Match Time At the Top
            
            Frame_Minute =  int( (Frame / frames_per_second) / 60 )
            
            Frame_Second =  ( ((Frame / frames_per_second) / 60) - Frame_Minute ) * 60
            
            Match_Time_String = f"{Frame_Minute}:{Frame_Second:1.2f}"
            
            
            if metric_unit == "cm":
        
                Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
            
                Objects = ax.text( -350, Pitch_Dimensions[1]/2 + 100, Match_Time_String, fontsize = 14 )
                
            
            if metric_unit == "m":
        
                Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
            
                Objects = ax.text( -3.5, Pitch_Dimensions[1]/2 + 1, Match_Time_String, fontsize = 14 )
            
            
            
            
            Figure_Objects.append(Objects)
            
            Writer.grab_frame()
            
            
            # Delete all axis objects (other than pitch lines) in preperation for next frame
            
            for Figure_Object in Figure_Objects:
                
                Figure_Object.remove()

                
    
    print("\033[91m\033[1m\033[4m FINISHED \033[0m")
    
    plt.clf()
    
    plt.close(fig)
    

    
    
    
    
    
    
    
    
def Play_Match_Possession_VideoClip(file_name, directory = "Shots', Goals' & Possessions' Movies", fps = 25):
    """
    Function That Loads & Plays a Video-Clip of the Generated Match Tracking Data, Saved In the Directory `directory` As An `.mp4` File With File-Name `file_name`
    
    Input: file_name = String of the Name of the `.mp4` File of the Generated Match Tracking Data --> MUST Include ".mp4" At the End of the String
    Input: directory = String of the Directory Path Where the Generated Match Tracking Data `.mp4` Is Saved In; Default == "Shots', Goals' & Possessions' Movies"
    Input: fps = Integer Indicating the Frame Rate (i.e. #Frames Per Second / Frame Frequency); Default == 25
    
    Output: Video-Clip of the Generated Match Tracking Data On a New Window, With the Following Functionalities:
                                                                                                                 - Video-Clip Does Not Reproduce Until the "p" Key Is Pressed On the Keyboard
                                                                                                                 - If Press "s" On the Keyboard, the Video-Clip Pauses
                                                                                                                 - If Press "p" On the Keyboard When the Video-Clip Is Paused, It Keeps Playing the Video-Clip At the Specified FPS
                                                                                                                 - If Press the Spacebar On the Keyboard, the Video-Clip Starts Being Reproduced Frame-By-Frame
                                                                                                                 - If Press "r" On the Keyboard, the Video-Clip Restarts/Replays From the Start/Beginning
                                                                                                                 - If Press "q" On the Keyboard, It Exits the Video-Clip & Closes Down the Emerging Window (ONLY Way of Closing Down the Window - Not Even Clicking On the Red Cross)
    """
    
    # Open the Video-Clip File
    
    Directory = directory
    
    File_Path = Directory + "/" + file_name
    
    
    Window_Name = file_name
    
    cv2.namedWindow(Window_Name, cv2.WINDOW_AUTOSIZE)

    Video = cv2.VideoCapture(File_Path)
    

    # Check If Video-Clip Opened Successfully
    
    if not Video.isOpened():
        
        print(f"Error Opening the Video-Clip File {file_name}")
        

    # Get the Frame Rate (i.e. #Frames Per Second / Frame Frequency) of the Video-Clip
    
    FPS = fps
    
    
    # Calculate the Delay For a Frame --> We Subtract 1 [ms] To Compensate For the Time It Takes To Execute Other Instructions In the Loop
    
    Delay = int(1000 / FPS) - 1
    

    # Default Value For the Variable That Controls the Playback
    
    Playback = False
    

    while Video.isOpened():
        
        # Read a Frame
        
        Ret, Frame = Video.read()
        

        if not Ret:
            
            # We Have Run Out of Frames (i.e. the Video-Clip Has Finished) --> Wait For User's Input Via Pressing a Keyboard Key
            
            Key = cv2.waitKey(0)
            
        
        else:
            
            # Display the Frame In a Window
            
            cv2.imshow(Window_Name, Frame)
            

            # If Playback Is Enabled --> Wait For the Calculated Delay To Create a Playback Effect
            # If Not --> Wait Indefinitely For User's Input Via Pressing a Keyboard Key
            
            Key = cv2.waitKey(Delay if Playback else 0)
            

        # Check For Keyboard Keys To Control Playback
        
        if Key == ord('p'):
            
            Playback = not Playback  # Toggle Playback
            
        
        elif Key == ord('s'):
            
            Playback = False  # Pause the Video-Clip
            
        
        elif Key == ord(' '):
            
            Playback = False  # Stop Playback To Advance the Playback Frame By Frame
            
            
        elif Key == ord('r'):
            
            Video.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart the Video-Clip, By Re-Setting the Video To Frame With Index = 0 (i.e. the 1st Frame)
            
        
        elif Key == ord('q'):
            
            break  # Quit the Video-Clip Player
            

    # Release the Video-Clip File & Close All Windows When Done So
    
    
    Video.release()
    
    cv2.destroyAllWindows()
    
    
    
    

    
    
    
    
    
def Plot_Static_Shots_On_Pitch( shots_to_plot = "both", num_shots = "all", ball_color_and_style = "ko", scored_shot_edgecolor = "yellow", non_scored_shot_edgecolor = "red", show_ball_height = True, figax = None, metric_unit = "cm", pitch_color = "green", style_of_the_goals = "entire_goal", save_plot_locally = False ):
    """
    Function That Plots (Static) Shots On a Soccer Pitch, Using Match Ball's Tracking Data
    
    Input: shots_to_plot = String Stating the Type of Shots To Plot, Either Only Scored Shots (Goals), Non-Scored Shots (Non-Goals), or Both;  Options == {"goals", "non-goals", "both"};  Default == "both"
    Input: num_shots = Integer Number of Shots To Be Visualized In the Plot; If `num_shots = None`, All Shots Will Be Visualized; If `num_shots = int`, the First `int` Number of Shots In the Tracking Data Will Be Visualized;  Default == None
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted;  Default == "ko"
    Input: scored_shot_edgecolor = String Stating the Edge-Color (`markeredgecolor`) To Assign & Display On the Ball's Marker When It Represents a Scored Shot;  Default == "yellow"
    Input: non_scored_shot_edgecolor = String Stating the Edge-Color (`markeredgecolor`) To Assign & Display On the Ball's Marker When It Represents a Non-Scored Shot;  Default == "red"
    Input: show_ball_height = Boolean Statement On Whether To Show & Visualize the Height of the Ball, Reflected On the Ball's Marker Size (the Heigher the Ball From the Ground, the Larger the Ball's Marker) or Not;  Default == True
    Input: figax = Tuple of the Form `(fig, ax)`, That Can Be Used To Pass In the `(fig, ax)` Objects of a Previously Generated Pitch; Set To `(fig, ax)` To Re-Use An Existing/Old Pitch (With Data On It Or Not), Or None (the Default) To Generate a New Pitch Plot
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
    Input: save_plot_locally = Boolean Statement On Whether To Save the Created Plot or Not Locally In the Laptop Using a `tkinter` File-Explorer/Dialog;  Default == False
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    if figax is None:  # Create a New Pitch
        
        fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
        
    else: # Overlay On a Previously Generated Pitch
        
        fig, ax = figax  # Unpack Specified Tuple Argument of the Parameter



    
    # Initialize Tkinter + Hide the Main Window
    
    Root = tk.Tk()   # Initialize Tkinter
    
    Root.withdraw()   # Hide the Main Window
    

    # Open File-Dialog/Explorer To Select a `.parquet` File
    
    File_Path = filedialog.askopenfilename( title = f"Select the Desired Un-Preprocessed Tracking Data `.parquet` File", filetypes = [ ("Parquet Files", "*.parquet") ] )
    
    if not File_Path:  # If No Appropriate File Is Selected
        
        print("No File Was Selected")
        
        return None
    
    
    Relevant_Columns = [ "X", "Y", "Z", "Will_Be_a_Goal" ]
    
    Ball_Tracking_Data = pd.read_parquet( File_Path, engine = "auto", columns = Relevant_Columns )
        
    
    
    
    # Plot the Ball
    
    # Since Some -ve Values Have Been Spotted For the Ball's Height ("Z"), Which Is Not Possible:
    # Check if There Are Values < 0 In Column "Z" (i.e. Height of the Ball) --> Convert -ve Values Into Their Respective Absolute Values, & the Original Values That Are >= 0 Are Retained
    
    Ball_Tracking_Data["Z"] = Ball_Tracking_Data["Z"].apply( lambda z: abs(z) if z < 0 else z )


    
    # Filter Shot-Type Based On `shots_to_plot`
    
    if shots_to_plot != "both":
        
        Goal_Filter_Value = 1.0 if shots_to_plot == "goals" else 0.0
        
        Ball_Tracking_Data = Ball_Tracking_Data[ Ball_Tracking_Data["Will_Be_a_Goal"] == Goal_Filter_Value ]
        
        
        
    # Limit the #Shots If `num_shots` Is Specified
    
    if num_shots != "all" and isinstance(num_shots, int):
        
        Ball_Tracking_Data = Ball_Tracking_Data.head(num_shots)
                



    # Plot Each Shot
    
    for Index, df_Row in Ball_Tracking_Data.iterrows():
        
        Ball_Edge_Color = scored_shot_edgecolor if df_Row["Will_Be_a_Goal"] == 1.0 else non_scored_shot_edgecolor

        
        if show_ball_height == True:
        
            Ball_Marker_Size = np.log( df_Row["Z"] ) if df_Row["Z"] > 0 else 1  # Avoid ln(0) or ln(-ve)

        else:

            Ball_Marker_Size = 6   # Constant Marker Size If `show_ball_height` == False

        
        
        ax.plot( df_Row["X"], df_Row["Y"], ball_color_and_style, markersize = Ball_Marker_Size, markeredgecolor = Ball_Edge_Color, markeredgewidth = 1.65, alpha = 1.0, linewidth = 0 )
        


    
    if save_plot_locally == True:   # Save the Created Plot Locally
        
        save_path = filedialog.asksaveasfilename( defaultextension = ".png", filetypes = [ ("PNG Files", "*.png"), ("All Files", "*.*") ] )
        
        if save_path:
            
            fig.savefig(save_path)
    
    
    
    
    return fig, ax











###################################################
#        PITCH CONTROL-RELATED FUNCTIONS          #
###################################################



"""
Calculating a Pitch Control Surface

Pitch Control (At a Given Location On the Field) = The Probability That a Team Will Gain Possession If the Ball Is Moved To That Location On the Pitch 


Methdology Described In:

--> "Quantifying Pitch Control" By William Spearman, 2016

--> "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017

--> "Beyond Expected Goals" By William Spearman, 2018

--> William Spearman's Master-Class In Pitch Control: https://www.youtube.com/watch?v=X9PrwPyolyU&list=PLedeYskZY0vBOdQ6Uc9eZjZ2-nz1JT3R7&index=26&ab_channel=FriendsofTracking


Functions
----------

Generate_Pitch_Control_Surface_For_Event() --> Evaluates Pitch Control Surface Over the Entire Field At the Moment of the Given Event (Determined By the Index of the Event Passed As An Input)

Calculate_Pitch_Control_Surface_At_Target() --> Calculates the Pitch Control Probability For the Attacking & Defending Teams At a Specified Target Position On the Ball


Classes
---------

The 'Player' class collects and stores trajectory information for each Player required by the Pitch Control calculations



    Methods
    --------
    
    __init__()
    
    Get_Position()
    
    Get_Velocity()
    
    Simple_Time_To_Intercept()
    
    Probability_Intercepting_Ball()
    
"""




def Default_Pitch_Control_Model_Parameters( metric_unit = "cm", time_to_control_veto = 3 ):
    """
    Inspiration From @author:
                              1) Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
                              2) "Quantifying Pitch Control" By William Spearman, 2016
                              
                              3) "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017

                              3) "Beyond Expected Goals" By William Spearman, 2018
                              
                              4) William Spearman's Master-Class In Pitch Control: https://www.youtube.com/watch?v=X9PrwPyolyU&list=PLedeYskZY0vBOdQ6Uc9eZjZ2-nz1JT3R7&index=26&ab_channel=FriendsofTracking
    
    
    
    Function That Returns the Default Parameters That Defines & Evaluates the Pitch Control Model
    
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: time_to_control_veto = If the Probability That Another Team Or Player Can Get To the Ball + Control It Is Less Than 10**{-time_to_control_veto} --> Ignore That Player
    
    Output: Pitch_Control_model_params = Dictionary of Parameters Required To Determine & Calculate the Pitch Control Model    
    """
    
    # Key Parameters For the Pitch Control Model, As Described In "Beyond Expected Goals" By William Spearman, 2018
    
    Pitch_Control_model_params = {}
    
    
    # Pitch Control Model Parameters
    
    
    if metric_unit == "cm":
        
        Pitch_Control_model_params['Max_Player_Speed'] = 500   # Max Players' Speed [cm/s]
        
        Pitch_Control_model_params['Max_Player_Acceleration'] = 700   # Max Players' Acceleration [cm/s^2]  -->  NOT Used In This Implementation
        
        Pitch_Control_model_params['Avg_Ball_Speed'] = 1500   # Average Ball Travel Speed [cm/s]
        
    
    
    
    if metric_unit == "m":
    
        Pitch_Control_model_params['Max_Player_Speed'] = 5   # Max Players' Speed [m/s]
    
        Pitch_Control_model_params['Max_Player_Acceleration'] = 7   # Max Players' Acceleration [m/s^2]  -->  NOT Used In This Implementation
        
        Pitch_Control_model_params['Avg_Ball_Speed'] = 15   # Average Ball Travel Speed [m/s]
    
    
    
        
    
    Pitch_Control_model_params['Reaction_Time'] = 0.7   # Time Taken [s] For Player To React & Change Direction/Trajectory --> Roughly Determined As Speed_max/Acc_max
    
    Pitch_Control_model_params['Time-To-Intercept_SD'] = 0.45   # Standard Deviation (SD) of the Time-To-Intercept's Sigmoid Function --> (See Eq.4 & Fig.2 In "Physics-Based Modeling of Pass Probabilities in Soccer", Spearman 2017)
                                                                # ≡ Uncertainty In Time That It Takes a Player To Intercept the Ball --> (See Table 1 In "Beyond Expected Goals", Spearman 2018)
    
    
    Pitch_Control_model_params['κ_Defensive_Advantage'] =  1   # κ (Kappa) Parameter = the Advantage Defending Players Have Over Attacking Players To Control the Ball
                                                                  # --> (See Table 1 In "Beyond Expected Goals", Spearman 2018): In the Paper κ = 1.72, BUT I Decided To Set κ = 1 So That Attacking & Defending Players Have the Same Ball Control Probability
    
    Pitch_Control_model_params['λ_Attacking_Team'] = 4.3   # λ_Attacking_Team = Ball Control Parameter (For the Attacking Team/Players)
                                                           # ⇒ Inversely Proportional (∝) To the Avg. Time It Takes a (Attacking) Player To Control the Ball --> (See Table 1 In "Beyond Expected Goals", Spearman 2018)
    
    Pitch_Control_model_params['λ_Defending_Team'] = 4.3 * Pitch_Control_model_params['κ_Defensive_Advantage']   # λ_Defending_Team = Ball Control Parameter (For the Defending Team/Players)
    
    Pitch_Control_model_params['λ_GK'] = 3*Pitch_Control_model_params['λ_Defending_Team']   # Factor of 3 Ensures That Anything Near the GK Is Likely To Be Claimed By the GK
                                                                                            # Make GK Much Faster, To Control the Ball --> Because They Can Catch It With Their Hands Within the Box, So They Have Got This Extra Advantage Over Field Players
    
    
    
    
    # Numerical Parameters For Pitch Control Model's Evaluation
    
    Pitch_Control_model_params['Integration_dt'] = 0.04   # Integration Time-Step (dt) ≡ FPS' (Frames Per Second's) Frequency = 0.04s == 4ms
    
    Pitch_Control_model_params['Max_Integration_Time_Lapse'] = 10   # Max Time-Lapse [s] Within the Integral ≡ Upper Limit On Integral Time Boundary
    
    Pitch_Control_model_params['Pitch_Control_Model_Convergence_Tolerance'] = 0.01   # Assume Convergence (i.e. That the Pitch Control Model Converges) When PPCF > 0.99 At a Given Location/Position On the Pitch
                                                                                                                                       # PPCF = Potential Pitch Control Field
                                                                                     # Specifies How Close To 1 the Total Probability Must Be For the Integration To Be Considered As Converged
    
    
    # The Following Are 'Short-Cut' Parameters
    # i.e. We Do Not Need To Calculate the PPCF Explicitly When a Player Has a Sufficient Head-Start --> A Sufficient Head-Start = When the a Player Arrives At the Target Location At Least `time_to_control` Seconds [s] Before the Next Player Does
    
    Pitch_Control_model_params['Time_To_Control_Ball_Attacking_Team'] = ( time_to_control_veto * np.log(10) ) * ( ( np.sqrt(3) * ( Pitch_Control_model_params['Time-To-Intercept_SD'] / np.pi ) ) + 1/Pitch_Control_model_params['λ_Attacking_Team'] )
    
    Pitch_Control_model_params['Time_To_Control_Ball_Defending_Team'] = ( time_to_control_veto * np.log(10) ) * ( ( np.sqrt(3) * ( Pitch_Control_model_params['Time-To-Intercept_SD'] / np.pi ) ) + 1/Pitch_Control_model_params['λ_Defending_Team'] )
    
    
    
    
    return Pitch_Control_model_params










class Player( object ):
    """
    Inspiration From @author: 
                              1) Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
                              2) "Quantifying Pitch Control" By William Spearman, 2016
                              
                              3) "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017

                              3) "Beyond Expected Goals" By William Spearman, 2018
                              
                              4) William Spearman's Master-Class In Pitch Control: https://www.youtube.com/watch?v=X9PrwPyolyU&list=PLedeYskZY0vBOdQ6Uc9eZjZ2-nz1JT3R7&index=26&ab_channel=FriendsofTracking
    
    
    Class That Defines a Player Object That Stores --> Position, Velocity, Time-To-Intercept + Pitch Control Contributions For a Player   
    """
    
    # Player Object Holds Position, Velocity, Time-To-Intercept + Pitch Control Contributions For Each Player
    
    def __init__( self, team_name, team_tracking_data_row, player_kit_number, GK_kit_number, Pitch_Control_model_params ):
        """
        __init__ (Initialization) Parameters ≡ Parameters Automatically Executed When the `Player()` Class Is Instanciated:
    
        Input: team_name = String of the Team's Name; Options  -->  {"Home", "Away"}
        Input: team_tracking_data_row = Row (i.e. Instant) of the `team_name` Team's Tracking Data DataFrame
        Input: player_kit_number = Player's Kit Number
        Input: GK_kit_number = GKs' Kit Numbers
        Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
        """
        
        self.Team_Name = team_name
        
        
        self.Kit_Number = player_kit_number
        self.is_GK = self.Kit_Number == GK_kit_number
        
        
        self.V_Max = Pitch_Control_model_params['Max_Player_Speed']   # Players' Max Speed In [cm/s]; Could Be Individualised
        self.Reaction_Time = Pitch_Control_model_params['Reaction_Time']   # Players' Reaction Time In [s]; Could Be Individualised
        
        self.Time_To_Intercept_SD = Pitch_Control_model_params['Time-To-Intercept_SD']   # Standard Deviation (SD) of the Time-To-Intercept's Sigmoid Function --> (See Eq.4 & Fig.2 In "Physics-Based Modeling of Pass Probabilities in Soccer", Spearman 2017)
                                                                                         # ≡ Uncertainty In Time That It Takes a Player To Intercept the Ball --> (See Table 1 In "Beyond Expected Goals", Spearman 2018)
        self.λ_Attacking_Team = Pitch_Control_model_params['λ_Attacking_Team']   # λ_Attacking_Team = Ball Control Parameter (For the Attacking Team/Players)
                                                                                 # ⇒ Inversely Proportional (∝) To the Avg. Time It Takes a (Attacking) Player To Control the Ball --> (See Table 1 In "Beyond Expected Goals", Spearman 2018)
        self.λ_Defending_Team = Pitch_Control_model_params['λ_GK'] if self.is_GK else Pitch_Control_model_params['λ_Defending_Team']   # λ_Defending_Team = Ball Control Parameter (For the Defending Team/Players) ⇒ Inversely Proportional (∝) To the Avg. Time It Takes a (Defending) Player To Control the Ball --> (See Table 1 In "Beyond Expected Goals", Spearman 2018)
                                                                                                                                       # Factor of 3 Ensures That Anything Near the GK Is Likely To Be Claimed By the GK
        
        self.Get_Position( team_tracking_data_row = team_tracking_data_row )
        self.Get_Velocity( team_tracking_data_row = team_tracking_data_row )
        
        self.PPCF = 0   # PPCF ≡ Potential Pitch Control Field  -  Initialise This For Later Calculations
        
        
        
        
    def Get_Position( self, team_tracking_data_row ):
        """
        Function (Method) That Extracts the Position of Players
        
        Input: self = 
        Input: team_tracking_data_row = Row (i.e. Instant) of the `team_name` Team's Tracking Data DataFrame
        
        Output: self.Position = Position of Players
        """
        
        self.Position = np.array( [ team_tracking_data_row["X" + self.Kit_Number], team_tracking_data_row["Y" + self.Kit_Number] ] )
        
                
        return self.Position
    
        
        
        
    def Get_Velocity( self, team_tracking_data_row ):
        """
        Function (Method) That Extracts the Velocity of Players
        
        Input: self = 
        Input: team_tracking_data_row = Row (i.e. Instant) of the `team_name` Team's Tracking Data DataFrame
        
        Output: self.Velocity = Velocity of Players
        """
        
        self.Velocity = np.array( [ team_tracking_data_row["V_x" + self.Kit_Number], team_tracking_data_row["V_y" + self.Kit_Number] ] )
        
        
        return self.Velocity
        
            
            
            
    
    def Simple_Time_To_Intercept( self, final_target_position ):
        """
        Function (Method) That Calculates the Time Taken For a Player To Get To Target Position (`final_target_position`) Given Current Position
        
        Input: self = 
        Input: final_target_position = Final Target Position/Location On the Pitch
        
        Output: self.Time_To_Intercept = Time Taken To Intercept & Have Control of the Ball
        """
        
        self.PPCF = 0   # PPCF ≡ Potential Pitch Control Field  -  Initialise This For Later Calculations
        
        
        # Time-To-Intercept Assumes That the Player Continues Moving At Current Velocity For Reaction-Time (`self.Reaction_Time`) [s] & Then Runs At Full Speed To the Target Position/Location
        
        Reaction_Time_Distance = self.Position + (self.Velocity * self.Reaction_Time)
        
        self.Time_To_Intercept = self.Reaction_Time + ( np.linalg.norm(final_target_position - Reaction_Time_Distance) / self.V_Max )
        
        
        return self.Time_To_Intercept
    
    
    
    

    def Probability_Intercepting_Ball( self, Ball_Controlled_At_Timestamp ):
        """
        Function (Method) That Calculates the Probability That a Player Will Have the Ball Controlled At Time `Ball_Controlled_At_Timestamp` Given Their Expected `Time_To_Intercept`
        Calculation Uses Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer", Spearman 2017
        
        Input: self = 
        Input: Ball_Controlled_At_Timestamp = Time (Timestamp) Value At Which a Player Will Have the Ball Controlled ≡ `T` In Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer", Spearman 2017
        
        Output: Probability_Intercepting_Ball = Probability of a Player Arriving At Target Position/Location At Time 'Ball_Controlled_At_Timestamp' Given Their Expected `self.Time_To_Intercept` (Time of Arrival), As Described In Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer", Spearman 2017
        """
        
        # Probability of a Player Arriving At Target Location/Position At Time `Ball_Controlled_At_Timestamp` ≡ 'T', Given Their Expected `self.Time_To_Intercept` (Time of Arrival), As Described In Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer", Spearman 2017
        
        Probability_Intercepting_Ball = 1 / ( 1 + np.exp( - ( np.pi * (Ball_Controlled_At_Timestamp - self.Time_To_Intercept) ) / ( np.sqrt(3.0) * self.Time_To_Intercept_SD ) ) )
        
        
        return Probability_Intercepting_Ball
    
    
    
    
    
    
    
    
    

def Initialize_Players( team_name, team_tracking_data_row, GK_kit_number, Pitch_Control_model_params ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Initializes the Players Object, By Outputting a List of Player Objects For the Team At a Given Instant
    
    Input: team_name = String of the Team's Name; Options  -->  {"Home", "Away"}
    Input: team_tracking_data_row = Row (i.e. Instant) of the `team_name` Team's Tracking Data DataFrame
    Input: GK_kit_number = GKs' Kit Numbers
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    
    Output: Team_Players_Objects_List = List of Player Objects For the Team At a Given Instant
    """    
    
    # Get Player IDs
    
    if team_name == "Home":
        
        Player_IDs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
        
        
    if team_name == "Away":
        
        Player_IDs = ["12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
    
    
    # Create List of Player Objects
    
    Team_Players_Objects_List = []
    
    
    for Player_ID in Player_IDs:
        
        
        # Create a Player Object For `Player_ID`
        
        Team_Player = TFVFs.Player( team_name = team_name, team_tracking_data_row = team_tracking_data_row, player_kit_number = Player_ID, GK_kit_number = GK_kit_number, Pitch_Control_model_params = Pitch_Control_model_params )
        
        Team_Players_Objects_List.append(Team_Player)
                    
    
    
    
    return Team_Players_Objects_List










def Check_OffSides( attacking_players, defending_players, ball_starting_position, GK_kit_numbers, verbose = True, metric_unit = "cm" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Checks Whether Any of the Attacking Players Are On Off-Side (Allowing For a `Tolerance` Margin of Error)
        Off-Side Players Are Removed From the `attacking_players` List & Ignored In the Pitch Control Calculation
    
    Input: attacking_players = List of `Player()` Objects (See `Player()` Class Above) For the Players On the Attacking Team (Team In Possession)
    Input: defending_players = List of `Player()` Objects (See `Player()` Class Above) For the Players On the Defending Team
    Input: ball_starting_position = Current Position/Location of the Ball (Start Position For a Pass); If `ball_starting_position == np.NaN`, Function Will Assume That the Ball Is Already At the Target Position/Location
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: verbose = Boolean Value, Determining How Detailed Should the Function Be; Default == False; If `verbose = True` --> Prints a Message Each Time a Player Is Found To Be Offside
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
            
    Output: Attacking_Players = List of `Player()` Objects For the Players On the Attacking Team With Off-Side Players Removed
    """
    
    # Find Kit Number of Defending GoalKeeper (Just To Establish Attack Direction)
    
    Defending_GK_Kit_Number = GK_kit_numbers[1] if attacking_players[0].Team_Name == "Home" else GK_kit_numbers[0]
    
    
    # Make Sure Defending GoalKeeper Is Actually On the Field!
    
    assert Defending_GK_Kit_Number in [Player.Kit_Number for Player in defending_players], "Defending GK Kit Number Has Not Been Found In `defending players` List of Players"
    
    
    # Get GoalKeeper `Player()` Object
    
    Defending_GK = [Player for Player in defending_players if Player.Kit_Number == Defending_GK_Kit_Number][0]
    
    
    # Use (Defending GoalKeeper x Position/Location) To Figure Out Which Half of the Pitch He Is Defending In (-1 == Left Goal / +1 == Right Goal)
    
    Defending_Half_of_the_Pitch = np.sign(Defending_GK.Position[0])  # Value Either  = -1  Or  = 1
    
    
    # Find the X-Position of the 2nd-Deepest Defeending Player - Including the GK (i.e. the Last Defender Before the GK)
    
    Second_Deepest_Defender_X = sorted( [Defending_Half_of_the_Pitch*Player.Position[0] for Player in defending_players], reverse = True )[1]
    
    
    
    if metric_unit == "cm":
        
        # A `Tolerance` Parameter That Allows a Player To Be Very Marginally Off-Side (Up To `Tolerance` [cm]) Without Being Flagged Off-Side
        
        Tolerance = 20   # 20 [cm]
        
        
        # Define Off-Side Line As Being the Maximum of `Second_Deepest_Defender_X`, `ball position` & the Half-Way Line (i.e. Line of the Center of the Pitch)
        
        OffSide_Line = max(Second_Deepest_Defender_X, Defending_Half_of_the_Pitch*ball_starting_position[0], 0.0) + Tolerance
        
        
    if metric_unit == "m":
        
        # A `Tolerance` Parameter That Allows a Player To Be Very Marginally Off-Side (Up To `Tolerance` [m]) Without Being Flagged Off-Side
        
        Tolerance = 0.2   # 0.2 [m]
        
        
        # Define Off-Side Line As Being the Maximum of `Second_Deepest_Defender_X`, `ball position` & the Half-Way Line (i.e. Line of the Center of the Pitch)
        
        OffSide_Line = max(Second_Deepest_Defender_X, Defending_Half_of_the_Pitch*ball_starting_position[0], 0.0) + Tolerance
        
    
    
    # Any Attacking Players With X-Position Greater Than the Off-Side Line Are Flagged Off-Side
    
    if verbose == True:
        
        for Player in attacking_players:
            
            if Player.Position[0]*Defending_Half_of_the_Pitch > OffSide_Line:
                
                print(f"Player {Player.Kit_Number} In {Player.Team_Name} Team Is Off-Side")
                
    
    Attacking_Players = [Player for Player in attacking_players if Player.Position[0]*Defending_Half_of_the_Pitch <= OffSide_Line]
    
    
    
    
    return Attacking_Players










def Calculate_Pitch_Control_Surface_At_Target( target_position, attacking_players, defending_players, ball_starting_position, Pitch_Control_model_params ):
    """
    Inspiration From @author:
                              1) Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
                              2) "Quantifying Pitch Control" By William Spearman, 2016
                              
                              3) "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017

                              3) "Beyond Expected Goals" By William Spearman, 2018
                              
                              4) William Spearman's Master-Class In Pitch Control: https://www.youtube.com/watch?v=X9PrwPyolyU&list=PLedeYskZY0vBOdQ6Uc9eZjZ2-nz1JT3R7&index=26&ab_channel=FriendsofTracking
    
    
    Function That Calculates the Pitch Control (Surface) Probability For the Attacking & Defending Teams At a Specified Target Position/Location of the Ball On the Pitch
    
    Input: target_position = Numpy Array of Size/Dimensions = 2, Containing the (x, y) Positions of the Position On the Pitch To Evaluate Pitch Control (Surface)
    Input: attacking_players = List of `Player()` Objects (See `Player()` Class Above) For the Players On the Attacking Team (Team In Possession)
    Input: defending_players = List of `Player()` Objects (See `Player()` Class Above) For the Players On the Defending Team
    Input: ball_starting_position = Current Position/Location of the Ball (Start Position For a Pass); If `ball_starting_position == np.NaN`, Function Will Assume That the Ball Is Already At the Target Position/Location
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
        
    Output: PPCF_Attacking_Team = Pitch Control Probability For the Attacking Team
    Output: PPCF_Defending_Team = Pitch Control Probability For the Defending Team ( 1 - PPCF_Attacking_Team - PPCF_Defending_Team  <  Pitch_Control_model_params['Pitch_Control_Model_Convergence_Tolerance'] )
    """
    
    # Calculate Ball Travel Time From Starting Position To End/Target Position/Location
    
    if ball_starting_position is None or any(np.isnan(ball_starting_position)):   # If `ball_starting_position == None` Or `ball_starting_position == np.NaN`, Function Will Assume That the Ball Is Already At the Target Position/Location
        
        Ball_Travel_Time = 0.0
        
    
    else:
        
        # Ball Travel Time Is Distance To Target Position/Location From Current Ball Position, Divided By Assumed Average Ball Speed
        
        Ball_Travel_Time = np.linalg.norm( target_position - ball_starting_position ) / Pitch_Control_model_params['Avg_Ball_Speed']
        
    
    
    # 1st Get the Expected Arrival Time of 'Nearest' Attacking Player (Nearest Also Dependent On Current Velocity)
    
    τ_Min_Attacking_Team = np.nanmin( [Player.Simple_Time_To_Intercept(final_target_position = target_position) for Player in attacking_players] )
    τ_Min_Defending_Team = np.nanmin( [Player.Simple_Time_To_Intercept(final_target_position = target_position) for Player in defending_players] )
    
    
    
    # Check Whether We Actually Need To Solve Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017
    
    if ( τ_Min_Attacking_Team - max(Ball_Travel_Time, τ_Min_Defending_Team) ) >= Pitch_Control_model_params['Time_To_Control_Ball_Defending_Team']:
        
        # If Defending Team Can Arrive Significantly Before Attacking Team --> No Need To Solve Pitch Control Model, i.e. No Need To Solve Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017
        
        return 0, 1   # i.e. Assign Probabilty of Intercepting the Ball of = 0 For Attacking Team & of = 1 For Defending Team
    
    
    elif ( τ_Min_Defending_Team - max(Ball_Travel_Time, τ_Min_Attacking_Team) ) >= Pitch_Control_model_params['Time_To_Control_Ball_Attacking_Team']:
        
        # If Attacking Team Can Arrive Significantly Before Defending Team --> No Need To Solve Pitch Control Model, i.e. No Need To Solve Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017
        
        return 1, 0   # i.e. Assign Probabilty of Intercepting the Ball of = 1 For Attacking Team & of = 0 For Defending Team
    
    
    ######################################
    
    # elif (ball_starting_position[2] >= 180) & (ball_vertical_velocity >= 55) & (ball_speed >= 550):
    
        # Add Code & Conditions So That the Pitch Control Model Is Capable of Taking Into Account the Height of the Ball & It's Vertical Velocity (V_z)
        
        # return 0.5   # Assume In These Situations That the Ball Is In Dispute & That Any Team Player Could Eventually Control It
    
    ######################################
    
    
    else:
        
        # Solve Pitch Control Model By Integrating Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017
        
        # 1st Remove Any Player That Is Far (In Time) From the Target Position/Location
        
        Attacking_Players = [Player for Player in attacking_players if ( Player.Time_To_Intercept - τ_Min_Attacking_Team ) < Pitch_Control_model_params['Time_To_Control_Ball_Attacking_Team'] ]
        Defending_Players = [Player for Player in defending_players if ( Player.Time_To_Intercept - τ_Min_Defending_Team ) < Pitch_Control_model_params['Time_To_Control_Ball_Defending_Team'] ]
        
        
        # Set Up Integration Arrays
        
        dT_array = np.arange( (Ball_Travel_Time - Pitch_Control_model_params['Integration_dt']), (Ball_Travel_Time + Pitch_Control_model_params['Max_Integration_Time_Lapse']), Pitch_Control_model_params['Integration_dt'] )
        
        PPCF_Attacking_Team = np.zeros_like( dT_array )
        PPCF_Defending_Team = np.zeros_like( dT_array )
        
        
        # Integration Eq.3 In "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017 --> Until Convergence Occurs Or Convergence's Tolerance Limit (`Pitch_Control_model_params['Pitch_Control_Model_Convergence_Tolerance'] = 0.01`) Hits
        
        Total_Pitch_Control_Probability = 0.0    #  == PPCF_Defending_Team[i] + PPCF_Attacking_Team[i]
        
        i = 1   # Iteration Number
        
        
        while ( 1 - Total_Pitch_Control_Probability ) > Pitch_Control_model_params['Pitch_Control_Model_Convergence_Tolerance'] and i < dT_array.size:
            
            
            T = dT_array[i]
            
            
            
            for Player in Attacking_Players:
                
                # Calculate Ball Control Probablity For 'Player' In Time Interval  (T + dt)  -->  Eq.3 In "Beyond Expected Goals" By William Spearman, 2018
                
                dPPCF_dT = (1 - PPCF_Attacking_Team[i-1] - PPCF_Defending_Team[i-1]) * Player.Probability_Intercepting_Ball( Ball_Controlled_At_Timestamp = T ) * Player.λ_Attacking_Team
                
                
                # Make Sure It's > 0
                
                assert dPPCF_dT >= 0, "Invalid Attacking Player Probability (`Calculate_Pitch_Control_Surface_At_Target()`)"
                
                
                Player.PPCF += dPPCF_dT * Pitch_Control_model_params['Integration_dt']   # Total Contribution From Individual Player
                
                PPCF_Attacking_Team[i] += Player.PPCF   # Add To Sum Over Players In the Attacking Team (Remembering Array Element Is 0 At the Start of Each Integration Iteration)
                
            
            
            for Player in Defending_Players:
                
                # Calculate Ball Control Probablity For 'Player' In Time Interval  (T + dt)  -->  Eq.3 In "Beyond Expected Goals" By William Spearman, 2018
                
                dPPCF_dT = (1 - PPCF_Attacking_Team[i-1] - PPCF_Defending_Team[i-1]) * Player.Probability_Intercepting_Ball( Ball_Controlled_At_Timestamp = T ) * Player.λ_Defending_Team
                
                
                # Make Sure It's > 0
                
                assert dPPCF_dT >= 0, "Invalid Defending Player Probability (`Calculate_Pitch_Control_Surface_At_Target()`)"
                
                
                Player.PPCF += dPPCF_dT * Pitch_Control_model_params['Integration_dt']   # Total Contribution From Individual Player
                
                PPCF_Defending_Team[i] += Player.PPCF   # Add To Sum Over Players In the Defending Team (Remembering Array Element Is 0 At the Start of Each Integration Iteration)
                
            
            
            Total_Pitch_Control_Probability = PPCF_Defending_Team[i] + PPCF_Attacking_Team[i]
            
            i += 1
            
        
        
        if i >= dT_array.size:
            
            # If the Total Probability `Total_Pitch_Control_Probability` Is Not Close To 1, Even After the Max Number of Iterations of the While Loop, Then the Function Prints the Following Warning Message:
            # This Indicates That the Calculated Pitch Control Probabilities May Not Be Accurate, Because They Do Not Add Up To 1 As Expected
            
            print(f"Integration Failed To Converge: {Total_Pitch_Control_Probability:.3f}", "\n")
            
        
        return PPCF_Attacking_Team[i-1], PPCF_Defending_Team[i-1]













def Generate_Pitch_Control_Surface_For_Single_Match_Frame( frame_number, team_in_possession_of_ball_series, home_team_tracking_data_row, away_team_tracking_data_row, ball_tracking_data_row, GK_kit_numbers, Pitch_Control_model_params, metric_unit = "cm", number_grid_cells_x = 50, include_offsides = True ):
    """
    Inspiration From @author:
                              1) Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
                              2) "Quantifying Pitch Control" By William Spearman, 2016
                              
                              3) "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017

                              3) "Beyond Expected Goals" By William Spearman, 2018
                              
                              4) William Spearman's Master-Class In Pitch Control: https://www.youtube.com/watch?v=X9PrwPyolyU&list=PLedeYskZY0vBOdQ6Uc9eZjZ2-nz1JT3R7&index=26&ab_channel=FriendsofTracking
    
    
    Function That Generates Pitch Control Surface Map & Evaluates the Pitch Control Surface Over the Entire Pitch At the Moment of the Given Event (Determined By the Index of the Event Passed As An Input `event_id`)
    
    Input: frame_number = Frame # (Number), i.e. Specified Instant of the Match (≡ Match Tracking DataFrames' Index)
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: home_team_tracking_data_row = Row (i.e. Instant) of the Home Team's Tracking Data DataFrame
    Input: away_team_tracking_data_row = Row of the Away Team's Tracking Data DataFrame
    Input: ball_tracking_data_row = Row of the Ball's Tracking Data DataFrame
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: number_grid_cells_x = Integer Number of Pixels In the Grid (In the X-Direction) That Covers the Surface of the Pitch; If `metric_unit = "cm"`  -->  Default == 50   /   If `metric_unit = "m"`  -->  Default == 50
                                 `number_grid_cells_y` --> Will Be Calculated Based On `number_grid_cells_x` & the `Pitch_Dimensions`
    Input: include_offsides = Boolean Value, Staing Whether Off-Sides Rules Are Taken Into Consideration In the Pitch Control Model Calculations. If `include_offsides = True`  -->  Find & Remove Off-Side Attacking Players From the Calculation; Default == True
        
    Output: PPCF_Attacking_Team = Pitch Control Surface ( Dimensions = (`number_grid_cells_x`, `number_grid_cells_y`) ) Containing Pitch Control Probability For the Attacking Team
                                  Surface For the Defending Team `PPCF_Defending_Team = 1 - PPCF_Attacking_Team`
    Output: Grid_Cells_Positions_x = Positions of the Pixels In the X-Direction (Field Length)
    Output: Grid_Cells_Positions_y = Positions of the Pixels In the Y-Direction (Field Width)
    """
    
    # Get the Details of the Specified Frame #/Given Instant of the Match (Team In Possession, Ball's Starting Position)
    
    if team_in_possession_of_ball_series.loc[frame_number] == 1.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
    if team_in_possession_of_ball_series.loc[frame_number] == 2.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Away"
        
        
        
    Ball_Starting_Position = np.array( [ball_tracking_data_row["X"], ball_tracking_data_row["Y"]] )
    
    
    
    
    # Break the Pitch Down Into a Grid of Pixels/Cells
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
        
        
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
    
    
    number_grid_cells_y = int( ( number_grid_cells_x * Pitch_Dimensions[1] ) / Pitch_Dimensions[0] )
    
    dx = Pitch_Dimensions[0] / number_grid_cells_x
    dy = Pitch_Dimensions[1] / number_grid_cells_y
    
    Grid_Cells_Positions_x = ( np.arange(number_grid_cells_x) * dx ) - ( Pitch_Dimensions[0] / 2 ) + ( dx / 2 )
    Grid_Cells_Positions_y = ( np.arange(number_grid_cells_y) * dy ) - ( Pitch_Dimensions[1] / 2 ) + ( dy / 2 )
    
    
    # Initialize Pitch Control Grids For Attacking & Defending Teams
    
    PPCF_Attacking_Team = np.zeros( shape = ( len(Grid_Cells_Positions_y), len(Grid_Cells_Positions_x) ) )
    PPCF_Defending_Team = np.zeros( shape = ( len(Grid_Cells_Positions_y), len(Grid_Cells_Positions_x) ) )
    
    
    # Initialize Player Positions & Velocities For Pitch Control Calculations (So That We're Not Repeating This At Each Grid Cell Position)
    
    if Team_In_Possesion_At_Starting_Frame_Number == 'Home':
        
        Attacking_Players = TFVFs.Initialize_Players( team_name = 'Home', team_tracking_data_row = home_team_tracking_data_row, GK_kit_number = GK_kit_numbers[0], Pitch_Control_model_params = Pitch_Control_model_params )
        Defending_Players = TFVFs.Initialize_Players( team_name = 'Away', team_tracking_data_row = away_team_tracking_data_row, GK_kit_number = GK_kit_numbers[1], Pitch_Control_model_params = Pitch_Control_model_params )
        
    
    elif Team_In_Possesion_At_Starting_Frame_Number == 'Away':
        
        Defending_Players = TFVFs.Initialize_Players( team_name = 'Home', team_tracking_data_row = home_team_tracking_data_row, GK_kit_number = GK_kit_numbers[0], Pitch_Control_model_params = Pitch_Control_model_params )
        Attacking_Players = TFVFs.Initialize_Players( team_name = 'Away', team_tracking_data_row = away_team_tracking_data_row, GK_kit_number = GK_kit_numbers[1], Pitch_Control_model_params = Pitch_Control_model_params )
        
    
    else:
        
        assert False, "Team In Possession MUST Be Either 'Home' Or 'Away'"
        
        
    
    # Find Any Attacking Players That Are Off-Side & Remove Them From the Pitch Control Calculation
    
    if include_offsides == True:
        
        Attacking_Players = TFVFs.Check_OffSides( attacking_players = Attacking_Players, defending_players = Defending_Players, ball_starting_position = Ball_Starting_Position, GK_kit_numbers = GK_kit_numbers,
                                                  verbose = True, metric_unit = metric_unit )
        
        
        
    # Calculate Pitch Control Model At Each Location On the Pitch
    
    for i in range( len(Grid_Cells_Positions_y) ):    # Shouldn't It Be the Pther Way Around??? -->  for i in range( len(Grid_Cells_Positions_x) ):   &    for j in range( len(Grid_Cells_Positions_y) ):   ???
        
        for j in range( len(Grid_Cells_Positions_x) ):
            
            Target_Position = np.array( [Grid_Cells_Positions_x[j], Grid_Cells_Positions_y[i]] )
            
            PPCF_Attacking_Team[i, j], PPCF_Defending_Team[i, j] = TFVFs.Calculate_Pitch_Control_Surface_At_Target( target_position = Target_Position,
                                                                                                                    attacking_players = Attacking_Players, defending_players = Defending_Players,
                                                                                                                    ball_starting_position = Ball_Starting_Position,
                                                                                                                    Pitch_Control_model_params = Pitch_Control_model_params )
            
    
    
    # Check Probabilitiy Sums Within Convergence
    
    Check_Probability_Sum = np.sum( PPCF_Attacking_Team + PPCF_Defending_Team ) / float(number_grid_cells_y * number_grid_cells_x)
    
    assert (1 - Check_Probability_Sum) < Pitch_Control_model_params['Pitch_Control_Model_Convergence_Tolerance'], f"`Check_Probability_Sum` Failed: {1 - Check_Probability_Sum:.3f}"
    
    
    
    
    return PPCF_Attacking_Team, Grid_Cells_Positions_x, Grid_Cells_Positions_y










def Plot_Pitch_Control_For_Single_Match_Frame( frame_number, home_team_tracking_data_row, away_team_tracking_data_row, ball_tracking_data_row, team_in_possession_of_ball_series, PPCF_attacking_team, Pitch_Control_surface_alpha = 0.45, team_colors = ('b', 'r'), home_team_players_color_and_style = "bo", away_team_players_color_and_style = "ro", ball_color_and_style = "ko", include_player_velocities = True, include_ball_velocity = False, player_marker_size = 10, player_alpha = 0.7, display_players_currently_in_possession = True, match_encoded_id = None, show_kit_numbers = False, kit_numbers_on_player_or_next_to_player = "next to player", metric_unit = "cm", pitch_color = "white", style_of_the_goals = "entire_goal" ):
    """
    Inspiration From @author:
                              1) Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
                              2) "Quantifying Pitch Control" By William Spearman, 2016
                              
                              3) "Physics-Based Modeling of Pass Probabilities in Soccer" By William Spearman, 2017

                              3) "Beyond Expected Goals" By William Spearman, 2018
                              
                              4) William Spearman's Master-Class In Pitch Control: https://www.youtube.com/watch?v=X9PrwPyolyU&list=PLedeYskZY0vBOdQ6Uc9eZjZ2-nz1JT3R7&index=26&ab_channel=FriendsofTracking
    
    
    Function That Plots the Pitch Control Surface At the Specified Match Frame/Instant - Players' + Ball's Positions (& Velocities) Are Overlaid
    
    Input: frame_number = Frame # (Number), i.e. Specified Instant of the Match (≡ Match Tracking DataFrames' Index)
    Input: home_team_tracking_data_row = Row (i.e. Instant) of the Home Team's Tracking Data DataFrame
    Input: away_team_tracking_data_row = Row of the Away Team's Tracking Data DataFrame
    Input: ball_tracking_data_row = Row of the Ball's Tracking Data DataFrame
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: PPCF_attacking_team = Pitch Control Surface ( Dimensions = (`number_grid_cells_x`, `number_grid_cells_y`) ) Containing Pitch Control Probability For the Attacking Team ( As Returned By the Output of the `Generate_Pitch_Control_Surface_For_Event()` Function )
                                 Surface For the Defending Team `PPCF_Defending_Team = 1 - PPCF_Attacking_Team`
    Input: Pitch_Control_surface_alpha = Alpha (Transparency) Coefficient of the Pitch Control Model's Surface; Default == 0.5
    Input: team_colors = Tuple Containing the Team Colors of the Home & Away Teams; Default == ('b', 'r')  -->  'b' (Blue, Home Team) & 'r' (Red, Away Team)
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: include_player_velocities = Boolean Value, That Determines Whether Player Velocities Are Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: include_ball_velocity = Boolean Value, That Determines Whether the Ball's Velocity Is Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: player_alpha = Alpha (Transparency) Coefficient of Players' Markers; Default == 0.7
    Input: display_players_currently_in_possession = Boolean Value, Stating Whether the Video-Clip Should Include & Display An Indication of the Player Currently In Possession of the Ball, By Adding a Yellow/Golden Ring Around the Player's Marker; Default == True
    Input: match_encoded_id = Integer Value, Indicating the Encoded Match ID (≡ Match# - 1)  --  Ex: Match# = 84  -->  Match ID ≡ `match_encoded_id` = 83; `match_encoded_id` Only Has An Argument Passed To It IF --> `display_players_currently_in_possession = True`
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: kit_numbers_on_player_or_next_to_player = String That Determines Whether the Players' Kit Numbers Should Be Shown On the Players' Marker Or Next To It; Options  -->  {"next to player", "on player"}; Default == "next to player"
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
        
    NB --> This Function No Longer Requires `Grid_Cells_Positions_x` & `Grid_Cells_Positions_y` As An Input
        
    
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """    

    # Plot Soccer Pitch Diagram
    
    fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals, linewidth = 2, markersize = 20 )
    
    
    # Plot Match Frame
    
    TFVFs.Plot_Single_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_row, away_team_tracking_data_row = away_team_tracking_data_row, ball_tracking_data_row = ball_tracking_data_row,
                                   team_colors = team_colors, home_team_players_color_and_style = home_team_players_color_and_style, away_team_players_color_and_style = away_team_players_color_and_style, ball_color_and_style = ball_color_and_style,
                                   include_player_velocities = include_player_velocities, include_ball_velocity = include_ball_velocity,
                                   player_marker_size = player_marker_size, player_alpha = player_alpha,
                                   display_players_currently_in_possession = display_players_currently_in_possession, match_encoded_id = match_encoded_id, frame_number = frame_number,
                                   show_kit_numbers = show_kit_numbers, kit_numbers_on_player_or_next_to_player = kit_numbers_on_player_or_next_to_player,
                                   figax = (fig, ax), metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
    
    
    
    
    # Extracting Which Team Is In Possession of the Ball At the Specified Frame #/Instant of the Match
    
    if team_in_possession_of_ball_series.loc[frame_number] == 1.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
    if team_in_possession_of_ball_series.loc[frame_number] == 2.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Away"
    
    
    
    
    
    # Plot Pitch Control surface
            
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('b', 'r') ):
        
        Color_Map = 'bwr_r'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('b', 'r') ):
        
        Color_Map = 'bwr'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('m', 'g') ):
        
        Color_Map = 'PiYG_r'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('m', 'g') ):
        
        Color_Map = 'PiYG'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'k') ):
        
        Color_Map = 'RdGy_r'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'k') ):
        
        Color_Map = 'RdGy'
        
        
        
    # Swapping/Reversing Surface's Colormap's Colours If the Team's Colours Are Reversed    
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'b') ):
        
        Color_Map = 'bwr'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'b') ):
        
        Color_Map = 'bwr_r'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('g', 'm') ):
        
        Color_Map = 'PiYG'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('g', 'm') ):
        
        Color_Map = 'PiYG_r'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('k', 'r') ):
        
        Color_Map = 'RdGy'
            
            
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('k', 'r') ):
        
        Color_Map = 'RdGy_r'
            
        
    
    
    # Get Pitch Dimensions Depending On the Metric Unit Used
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
    
    
    # Plot Pitch Control's Surface
    
    ax.imshow( np.flipud(PPCF_attacking_team), extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
               interpolation = 'spline36', vmin = 0, vmax = 1, cmap = Color_Map, alpha = Pitch_Control_surface_alpha )
    
    
        
    
    return fig, ax


    
    
    
    
    

    
    
def Save_Match_Possession_Pitch_Control_Surface_VideoClip( start_frame, end_frame, frames_per_second, home_team_tracking_data_df, away_team_tracking_data_df, ball_tracking_data_df, team_in_possession_of_ball_series, GK_kit_numbers, Pitch_Control_model_params, team_colors = ('b', 'r'), home_team_players_color_and_style = "bo", away_team_players_color_and_style = "ro", ball_color_and_style = "ko", Pitch_Control_surface_alpha = 0.45, number_grid_cells_x = 50, include_offsides = True, include_players_trajectories = False, include_ball_trajectory = False, include_player_velocities = True, include_ball_velocity = False, player_marker_size = 10, player_alpha = 0.7, display_players_currently_in_possession = True, match_encoded_id = None, show_kit_numbers = True, kit_numbers_on_player_or_next_to_player = "next to player", figax = None, metric_unit = "cm", pitch_color = "white", style_of_the_goals = "entire_goal", file_path = "Shots', Goals' & Possessions' Movies", file_name = "Match_Possession_Pitch_Control_Surface_Test_VideoClip" ):
    """
    Function That Generates a Movie From Match Tracking Data & Visualising the Pitch Control Model's Surface, Saving It As An `.mp4` File In the Path `file_path` Directory With File Name `file_name`
    
    Input: start_frame = Starting Frame # (Frame In Which the Trajectory Starts)
    Input: end_frame = Ending Frame # (Frame In Which the Trajectory Ends)
    Input: frames_per_second = # Frames Per Second (Frequency) To Assume When Generating the Movie; Default == 25
    Input: home_team_tracking_data_df = Home Team's Tracking Data DataFrame - Movie Will Be Created From All Rows In the DataFrame
    Input: away_team_tracking_data_df = Away Team's Tracking Data DataFrame - The Indices of This DataFrame MUST ≡ Indices From the `home_team_tracking_data_df` DataFrame
    Input: ball_tracking_data_df = Ball's Tracking Data DataFrame
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    Input: team_colors = Tuple Containing the Team Colors of the Home & Away Teams; Default == ('b', 'r')  -->  'b' (Blue, Home Team) & 'r' (Red, Away Team)
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: Pitch_Control_surface_alpha = Alpha (Transparency) Coefficient of the Pitch Control Model's Surface; Default == 0.5
    Input: number_grid_cells_x = Integer Number of Pixels In the Grid (In the X-Direction) That Covers the Surface of the Pitch; If `metric_unit = "cm"`  -->  Default == 50   /   If `metric_unit = "m"`  -->  Default == 50
                                 `number_grid_cells_y` --> Will Be Calculated Based On `number_grid_cells_x` & the `Pitch_Dimensions`
    Input: include_offsides = Boolean Value, Staing Whether Off-Sides Rules Are Taken Into Consideration In the Pitch Control Model Calculations. If `include_offsides = True`  -->  Find & Remove Off-Side Attacking Players From the Calculation; Default == True
    Input: include_players_trajectories = Boolean Value, That Determines Whether To Include & Visualise the Players' Trajectories, Or To Only Visualise Them As Single Points
    Input: include_ball_trajectory = Boolean Value, That Determines Whether To Include & Visualise the Ball's Trajectory, Or To Only Visualise It As a Single Point
    Input: include_player_velocities = Boolean Value, That Determines Whether Player Velocities Are Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: include_ball_velocity = Boolean Value, That Determines Whether the Ball's Velocity Is Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: player_alpha = Alpha (Transparency) Coefficient of Players' Markers; Default == 0.7
    Input: display_players_currently_in_possession = Boolean Value, Stating Whether the Video-Clip Should Include & Display An Indication of the Player Currently In Possession of the Ball, By Adding a Yellow/Golden Ring Around the Player's Marker; Default == True
    Input: match_encoded_id = Integer Value, Indicating the Encoded Match ID (≡ Match# - 1)  --  Ex: Match# = 84  -->  Match ID ≡ `match_encoded_id` = 83
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: kit_numbers_on_player_or_next_to_player = String That Determines Whether the Players' Kit Numbers Should Be Shown On the Players' Marker Or Next To It; Options  -->  {"next to player", "on player"}; Default == "next to player"
    Input: figax = Tuple of the Form `(fig, ax)`, That Can Be Used To Pass In the `(fig, ax)` Objects of a Previously Generated Pitch; Set To `(fig, ax)` To Re-Use An Existing/Old Pitch (With Data On It Or Not), Or None (the Default) To Generate a New Pitch Plot
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "white"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
    Input: file_path = Directory To Save the Movie In; Default == "Shots', Goals' & Possessions' Movies"
    Input: file_name = Movie's File-Name; Default == "Match_Possession_Pitch_Control_Surface_Test_VideoClip"
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    # Set Figure & Movie Settings
    
    FFMpegWriter = animation.writers["ffmpeg"]
    
    MetaData = dict( title = file_name, artist = "Hertha BSC Broadcast Tracking Data Video-Clip", comment = "Matplotlib" )
    
    Writer = FFMpegWriter(fps = frames_per_second, metadata = MetaData)
    
    File_Name = file_path + '/' +  file_name + ' (Pitch Control).mp4'   # Directory Path + File-Name
    
    
    # Create Soccer Pitch
    
    if figax is None:  # Create a New Pitch
        
        fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
        
    else: # Overlay On a Previously Generated Pitch
        
        fig, ax = figax  # Unpack Specified Tuple Argument of the Parameter
        
    fig.set_tight_layout(True)
    
    
    # Generate Movie
    
    print("Generating Video-Clip... \n \n", end = '')
    
    Team_Colors = (home_team_players_color_and_style, away_team_players_color_and_style)
    
    
    if display_players_currently_in_possession == True:
    
        Possessions_df = TFVFs.Read_Possessions_Dataset( all_possessions_with_shots_and_goals = True )
                        
        Possessions_of_Current_Match_df = Possessions_df[Possessions_df["MatchId"] == match_encoded_id]
        
        Frames_At_Which_Possession_Starts_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["frames"].values.astype(int)
                        
        Possession_Durations_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["duration"].values.astype(int)
        
        Players_Currently_In_Possession_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["players"].values.astype(int)
    
    
    with Writer.saving(fig, File_Name, 100):
        
        
        for Frame in range(start_frame, end_frame + 1):
            
            Figure_Objects = []   # This Is Used To Collect Up All the Axis Objects So That They Can Be Deleted After Each Iteration

            
            
            # Plot Home & Away Teams In Order
    
            for Team, Color in zip( [home_team_tracking_data_df.loc[Frame], away_team_tracking_data_df.loc[Frame]], Team_Colors ):
        
                X_Columns = [c for c in Team.keys() if c[0] == 'X']  # Column Name For Players' X-Coordinate Positions
                Y_Columns = [c for c in Team.keys() if c[0] == 'Y']  # Column Name For Players' Y-Coordinate Positions
        
                
                if include_players_trajectories == False:
                    
                    if display_players_currently_in_possession == False:
                        
                    
                        Objects, = ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                        Figure_Objects.append(Objects)
                
                
                
                
                    if display_players_currently_in_possession == True:
                        
                        
                        Objects, = ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                        Figure_Objects.append(Objects)
                
                
                
                        for Frames_At_Which_Possession_Starts_series_Value, Possession_Durations_series_Value, Players_Currently_In_Possession_series_Value in zip(Frames_At_Which_Possession_Starts_series_Values, Possession_Durations_series_Values, Players_Currently_In_Possession_series_Values):
        
                            if Frame in range(Frames_At_Which_Possession_Starts_series_Value, (Frames_At_Which_Possession_Starts_series_Value + Possession_Durations_series_Value) + 1):
        
                                Player_Currently_In_Possession_X_Coordinate_Column_Name = "X" + str(Players_Currently_In_Possession_series_Value)
                                Player_Currently_In_Possession_Y_Coordinate_Column_Name = "Y" + str(Players_Currently_In_Possession_series_Value)
                
                
                
                                if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Home_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Home_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                                    Objects, = ax.plot( home_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_X_Coordinate_Column_Name], home_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                                        home_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                                    Figure_Objects.append(Objects)
                
                
                
                
                                if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Away_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Away_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                                    Objects, = ax.plot( away_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_X_Coordinate_Column_Name], away_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                                        away_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                                    Figure_Objects.append(Objects)
                
                
                
                
                if include_players_trajectories == True:
            
                    ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = 3, alpha = player_alpha )  # Plot Players' Positions
                
                
                
                if show_kit_numbers == True:
            
                    if metric_unit == "cm":
                    
                        if kit_numbers_on_player_or_next_to_player == "next to player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]+75, Team[y]+75, "".join(list(x)[1 : ]), fontsize = 10, color = Color[0]  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List
                    
                
                        if kit_numbers_on_player_or_next_to_player == "on player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]-50, Team[y]-50, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List            
                        
                
                        for Kit_Number in Kit_Numbers_List:
                        
                            Figure_Objects.append(Kit_Number)
                
                
                    
                    if metric_unit == "m":
                        
                        if kit_numbers_on_player_or_next_to_player == "next to player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]+2, Team[y]+2, "".join(list(x)[1 : ]), fontsize = 10, color = Color[0]  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List
                    
                    
                        if kit_numbers_on_player_or_next_to_player == "on player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]-1.5, Team[y]-1.5, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List                    
                    
                
                        for Kit_Number in Kit_Numbers_List:
                        
                            Figure_Objects.append(Kit_Number)
                
                
        
        
                if include_player_velocities == True:
            
                    Vx_Columns = [c for c in Team.keys() if c[ : 3] == 'V_x']  # Column Name For Players' Velocity Component In the X-Direction
                    Vy_Columns = [c for c in Team.keys() if c[ : 3] == 'V_y']  # Column Name For Players' Velocity Component In the Y-Direction
            
            
                    Objects =  ax.quiver( Team[X_Columns].values.astype(np.float64), Team[Y_Columns].values.astype(np.float64),
                                          Team[Vx_Columns].values.astype(np.float64), Team[Vy_Columns].values.astype(np.float64),
                                          color = Color[0], scale_units = 'inches', scale = 1000, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
            
                    
                
                    Figure_Objects.append(Objects)
            
            
            
            
            
            # Plot the Ball
    
            # Since Some -ve Values Have Been Spotted For the Ball's Height ("Z"), Which Is Not Possible:
            # Check if There Are Values < 0 In Column "Z" (i.e. Height of the Ball) --> Convert -ve Values Into Their Respective Absolute Values, & the Original Values That Are >= 0 Are Retained
    
            if (ball_tracking_data_df.loc[Frame, "Z"] < 0).any():
        
                ball_tracking_data_df.loc[Frame, "Z"] = np.abs(ball_tracking_data_df.loc[Frame, "Z"])
            
            
            
            if include_ball_trajectory == False:
        
                Objects, = ax.plot( ball_tracking_data_df.loc[Frame, "X"], ball_tracking_data_df.loc[Frame, "Y"],
                                    ball_color_and_style, markersize = np.log(ball_tracking_data_df.loc[Frame, "Z"]), alpha = 1.0, linewidth = 0 )
                    
                Figure_Objects.append(Objects)
                
                
                
            if include_ball_trajectory == True:
                
                ax.plot( ball_tracking_data_df.loc[Frame, "X"], ball_tracking_data_df.loc[Frame, "Y"],
                         ball_color_and_style, markersize = np.log(ball_tracking_data_df.loc[Frame, "Z"]), alpha = 1.0, linewidth = 0 )
                
            
            
            
            
            
            # Generate & Evaluate Pitch Control Surface For Every Frame `Frame`

            PPCF_Attacking_Team, Grid_Cells_Positions_x, Grid_Cells_Positions_y = TFVFs.Generate_Pitch_Control_Surface_For_Single_Match_Frame( frame_number = Frame, team_in_possession_of_ball_series = team_in_possession_of_ball_series,
                                                                                                                                               home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame],
                                                                                                                                               away_team_tracking_data_row = away_team_tracking_data_df.loc[Frame],
                                                                                                                                               ball_tracking_data_row = ball_tracking_data_df.loc[Frame],
                                                                                                                                               GK_kit_numbers = GK_kit_numbers,
                                                                                                                                               Pitch_Control_model_params = Pitch_Control_model_params,
                                                                                                                                               metric_unit = metric_unit, number_grid_cells_x = number_grid_cells_x, include_offsides = include_offsides )
            
            
        
    
    
    
            # Extracting Which Team Is In Possession of the Ball At the Specified Frame #/Instant of the Match
    
            if team_in_possession_of_ball_series.loc[Frame] == 1.0:
        
                Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
            if team_in_possession_of_ball_series.loc[Frame] == 2.0:
        
                Team_In_Possesion_At_Starting_Frame_Number = "Away"
    
    
    
    
    
            # Plot Pitch Control surface
            
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('b', 'r') ):
        
                Color_Map = 'bwr_r'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('b', 'r') ):
        
                Color_Map = 'bwr'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('m', 'g') ):
        
                Color_Map = 'PiYG_r'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('m', 'g') ):
        
                Color_Map = 'PiYG'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'k') ):
        
                Color_Map = 'RdGy_r'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'k') ):
        
                Color_Map = 'RdGy'
        
        
        
            # Swapping/Reversing Surface's Colormap's Colours If the Team's Colours Are Reversed    
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'b') ):
        
                Color_Map = 'bwr'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'b') ):
        
                Color_Map = 'bwr_r'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('g', 'm') ):
        
                Color_Map = 'PiYG'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('g', 'm') ):
        
                Color_Map = 'PiYG_r'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('k', 'r') ):
        
                Color_Map = 'RdGy'
            
            
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('k', 'r') ):
        
                Color_Map = 'RdGy_r'
            
        
    
    
            # Get Pitch Dimensions Depending On the Metric Unit Used
    
            if metric_unit == "cm":
        
                Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
            if metric_unit == "m":
        
                Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
    
    
    
            # Plot Pitch Control's Surface
        
            Objects = ax.imshow( np.flipud(PPCF_Attacking_Team), extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
                                 interpolation = 'spline36', vmin = 0, vmax = 1, cmap = Color_Map, alpha = Pitch_Control_surface_alpha )
            
            
            Figure_Objects.append(Objects)
            
            
            
            
            
            
            
            # Include Match Time At the Top
            
            Frame_Minute =  int( (Frame / frames_per_second) / 60 )
            
            Frame_Second =  ( ((Frame / frames_per_second) / 60) - Frame_Minute ) * 60
            
            Match_Time_String = f"{Frame_Minute}:{Frame_Second:1.2f}"
            
            
            if metric_unit == "cm":
        
                Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
            
                Objects = ax.text( -350, Pitch_Dimensions[1]/2 + 100, Match_Time_String, fontsize = 14 )
                
            
            if metric_unit == "m":
        
                Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
            
                Objects = ax.text( -3.5, Pitch_Dimensions[1]/2 + 1, Match_Time_String, fontsize = 14 )
            
            
            
            
            Figure_Objects.append(Objects)
            
            Writer.grab_frame()
            
            
            # Delete all axis objects (other than pitch lines) in preperation for next frame
            
            for Figure_Object in Figure_Objects:
                
                Figure_Object.remove()

                
    
    print("\033[91m\033[1m\033[4m FINISHED \033[0m")
    
    plt.clf()
    
    plt.close(fig)

    
    
    
    

    
    
    
    
    
######################################################################
#        EXPECTED POSSESSION VALUES (EPV)-RELATED FUNCTIONS          #
######################################################################



"""
Calculating An Expected Possession Value (EPV) Surface

EPV (Surface) = The Probability That a Possession Will End With a Goal Given the Current Position/Location of the Ball

Expected' EPV Surface At a Specific Location/Position = Multiplying Pitch Control Surface By An EPV Surface (i.e. Pitch Control Surface x EPV Surface)
                                                      ≡ The Expected Possession Value of Moving the Ball To Any Location, Accounting For the Probability That the Ball Move (Pass/Carry) Is Successful

The EPV Surface Model Can Be Loaded Using `Load_EPV_Surface_Model_Grid_Values()`


Methodology Inspired and Described In:

--> "POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data" By Cervone D, D'amour A, Bornn L et al., 2014

--> "The expected value of possession in professional rugby league match-play" By Kempton T, Kennedy N, Coutts A, 2016

--> "Wide Open Spaces: A statistical technique for measuring space creation in professional soccer" By Fernandez J, Bornn L, 2018

--> "Predicting goal probabilities for possessions in football" By Mackay N, 2018

--> "Decomposing the Immeasurable Sport: A deep learning expected possession value framework for soccer" By Fernandez J, Bornn L, 2019

--> "SoccerMap: A Deep Learning Architecture for Visually-Interpretable Analysis in Soccer" By Fernandez J, Bornn L, 2020

--> "A framework for the fine-grained evaluation of the instantaneous expected value of soccer possessions" By Fernandez J, Bornn L, Cervone D, 2021

--> "A framework for the analytical and visual interpretation of complex spatiotemporal dynamics in soccer in Artificial Intelligence" By Fernández J, Bornn L, Gavaldà R, 2022

    



Functions
----------

Load_EPV_Surface_Model_Grid_Values() --> Loads the Pre-Generated EPV Surface Model From the File `EPV_Surface_Model_Grid_Values.csv`

Plot_EPV_Surface_Model() --> Plots the Pre-Generated Expected Possession Value (EPV) Surface

Extract_EPV_Surface_Value_At_Location() --> Returns the EPV Surface Value At a Given (x, y) Position/Location

Calculate_Expected_EPV_Added() --> Calculates the Expected Possession Value (EPV)-Added By a Pass

Find_Max_Expected_EPV_Added_At_Target() --> Finds the Max Expected Possession Value (EPV) That Could Have Been Achieved For a Pass By Searching the Entire Field For the Best Target (i.e. Location To Move the Ball To)

Plot_EPV_x_Pitch_Control_Surface_For_Single_Match_Frame() --> Plots the (EPV x Pitch Control) Surface At the Frame #/Instant of the Match --> Players' & Ball's Positions & Velocities Are Overlaid

"""




def UpSample_EPV_Surface_Model_Grid_Values_From_m_To_cm_Discrete( file_to_modify = "EPV_Surface_Model_Grid_Values_m_Discrete.csv", new_dimensions = (3600, 5250), new_file_name = "EPV_Surface_Model_Grid_Values_cm_Discrete.csv" ):
    """
    Function That Loads the Specified CSV File Into a Pandas DataFrame, Converts It To a Numpy Array, Then Calculates the Necessary Repeat Factor For Each Dimension - It Uses `numpy.repeat` To Upsample the Data In the Original CSV File, Then Converts the Result Back Into a DataFrame & Saves It To a New CSV File With the Specified File-Name
    
    NOTE: This Method Ensures That the Exact Values & Distribution From the Original Data Are Preserved, But They Are Repeated Across the Larger Dimensions of the New Data
    
    Input: file_to_modify = String of the `.csv` File-Name That We Want To Modify (Including ".csv" At the End of the String); Default == "EPV_Surface_Model_Grid_Values_m_Discrete.csv"
    Inupt: new_dimensions = Tuple, Describing the New Dimensions of the New `.csv` File
    Input: new_file_name = String of the New `.csv` File-Name That We Want To Save (Including ".csv" At the End of the String); Default == "EPV_Surface_Model_Grid_Values_cm_Discrete.csv"
    
    Output: String --> Stating That the File Was Successfully Saved
    """
    
    # Load `.csv` File To Modify
    
    df = pd.read_csv(file_to_modify)
    
    
    # Convert DataFrame of the Original Data Into a Numpy Array
    
    Data_np_Array = df.to_numpy()
    

    # Calculate the Repeat-Factor For Each Dimension
    
    Repeat_Factor = (new_dimensions[0] // Data_np_Array.shape[0], new_dimensions[1] // Data_np_Array.shape[1])
    

    # Use `numpy.repeat` To Up-Sample the Original Data
    
    UpSampled_Data_np_Array = np.repeat( np.repeat( Data_np_Array, Repeat_Factor[0], axis = 0 ), Repeat_Factor[1], axis = 1 )
    

    # If Needed, Convert the Up-Sampled Data Back To a DataFrame
    
    UpSampled_df = pd.DataFrame(UpSampled_Data_np_Array)
    
    
    # Make the 1st Row the Column Headers
    
    UpSampled_df.columns = UpSampled_df.iloc[0]
    
    UpSampled_df = UpSampled_df[1 : ]


    # Save the Up-Sampled DataFrame To a New `.csv` File
    
    UpSampled_df.to_csv(new_file_name, index = False)
    
    
    
    
    return print(f"\033[92m\033[1m `{file_to_modify}` Up-Sampled To `{new_file_name}` With New Dimensions {new_dimensions} --> Succesfully Saved \033[0m", '\n')
    









def UpSample_EPV_Surface_Model_Grid_Values_From_m_To_cm_Smooth( file_to_modify = "EPV_Surface_Model_Grid_Values_m_Discrete.csv", new_dimensions = (3600, 5250), new_file_name = "EPV_Surface_Model_Grid_Values_cm_Smooth.csv" ):
    """
    Function That Loads the Specified CSV File Into a Pandas DataFrame, Converts It To a Numpy Array, Then Calculates the Necessary Zoom Level For Each Dimension - It Uses `scipy.ndimage.zoom` To Upsample the Data In the Original CSV File, Then Converts the Result Back Into a DataFrame & Saves It To a New CSV File With the Specified File-Name
    
    NOTE: `scipy.ndimage.zoom` Uses `spline` Interpolation, Which Should Preserve the Overall Distribution of the Original Data. However, It Does Not Guarantee To Preserve the Exact Values of Each Data Point/Grid Value Due To the Nature of Interpolation. If Need To Keep the Exact Values & Just Increase the Size, Will Need a Different Approach, Possibly Involving Repeating Values Or Generating New Data That Fits the Existing Distribution
    
    Input: file_to_modify = String of the `.csv` File-Name That We Want To Modify (Including ".csv" At the End of the String); Default == "EPV_Surface_Model_Grid_Values_m_Discrete.csv"
    Inupt: new_dimensions = Tuple, Describing the New Dimensions of the New `.csv` File
    Input: new_file_name = String of the New `.csv` File-Name That We Want To Save (Including ".csv" At the End of the String); Default == "EPV_Surface_Model_Grid_Values_cm_Smooth.csv"
    
    Output: String --> Stating That the File Was Successfully Saved
    """
    
    # Load `.csv` File To Modify
    
    df = pd.read_csv(file_to_modify)
    
    
    # Convert DataFrame of the Original Data Into a Numpy Array
    
    Data_np_Array = df.to_numpy()
    

    # Calculate the Zoom-Level For Each Dimension
    
    Zoom_Level = (new_dimensions[0] / Data_np_Array.shape[0], new_dimensions[1] / Data_np_Array.shape[1])
    

    # Use `scipy.ndimage.zoom` To Up-Sample the Original Data
    
    UpSampled_Data_np_Array = zoom(Data_np_Array, Zoom_Level)
    

    # If Needed, Convert the Up-Sampled Data Back To a DataFrame
    
    UpSampled_df = pd.DataFrame(UpSampled_Data_np_Array)
    
    
    # Make the 1st Row the Column Headers
    
    UpSampled_df.columns = UpSampled_df.iloc[0]
    
    UpSampled_df = UpSampled_df[1 : ]


    # Save the Up-Sampled DataFrame To a New `.csv` File
    
    UpSampled_df.to_csv(new_file_name, index = False)
    
    
    
    
    return print(f"\033[92m\033[1m `{file_to_modify}` Up-Sampled To `{new_file_name}` With New Dimensions {new_dimensions} --> Succesfully Saved \033[0m", '\n')










def Load_EPV_Surface_Model_Grid_Values( metric_unit = "cm", smooth_or_discrete_data = "discrete" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Loads the Pre-Generated EPV Surface Model From the File `EPV_Surface_Model_Grid_Values.csv`
    
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: smooth_or_discrete_data = String, Stating Whether the Output Pre-Generated EPV Surface Model Grid Values Should Be Smooth Or Discrete; Options  -->  {"discrete", "smooth"}; Default == "Discrete"
        
    Output: EPV_Surface_Grid_Values = The (Pre-Generated) EPV Surface Model (Grid Values Determined By the Values In the Loaded `.csv` File)
    """
    
    if ( metric_unit == "cm" ) & ( smooth_or_discrete_data == "smooth" ) :
        
        EPV_Surface_Grid_Values = np.loadtxt(fname = 'EPV_Surface_Model_Grid_Values_cm_Smooth.csv', delimiter = ',')
        
        
        
    if ( metric_unit == "cm" ) & ( smooth_or_discrete_data == "discrete" ) :
        
        EPV_Surface_Grid_Values = np.loadtxt(fname = 'EPV_Surface_Model_Grid_Values_cm_Discrete.csv', delimiter = ',')
        
        
        
    if ( metric_unit == "m" ) & ( smooth_or_discrete_data == "smooth" ) :
        
        EPV_Surface_Grid_Values = np.loadtxt(fname = 'EPV_Surface_Model_Grid_Values_m_Smooth.csv', delimiter = ',')
    
    
    
    if ( metric_unit == "m" ) & ( smooth_or_discrete_data == "discrete" ) :
        
        EPV_Surface_Grid_Values = np.loadtxt(fname = 'EPV_Surface_Model_Grid_Values_m_Discrete.csv', delimiter = ',')
    
    
    
    
    return EPV_Surface_Grid_Values









    
def Plot_EPV_Surface_Model( EPV_Surface_grid_values, EPV_Surface_color_map = "Blues", attacking_direction = 1, metric_unit = "cm", pitch_color = "white", style_of_the_goals = "entire_goal" ):
    """ 
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Plots the Pre-Generated Expected Possession Value (EPV) Surface
    
    Input: EPV_Surface_grid_values = The Pre-Generated (32 x 50) EPV Surface Model  (Grid Values Determined By the Values In the Loaded `.csv` File Using `Load_EPV_Surface_Model_Grid_Values()`)
                                     EPV (Surface) = The Probability That a Possession Will End With a Goal Given the Current Position/Location of the Ball
    Input: EPV_Surface_color_map = String Stating the Color Map `cmap` That Matplotlib Should Display For the Colour of the EPV's Surface Model; Options  -->  {"Blues", "Reds", "Greens", "Oranges", "Purples", "Greys", "binary"}; Default == "Blues"
    Input: attacking_direction = Sets the Attacking Direction; Options  -->  {1 : Left --> Right, -1 : Right --> Left}; Default == 1
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
            
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """    
    
    if attacking_direction == -1:
        
        
        # Flip Direction of EPV's Surface Grid If Team Is Attacking From Right --> Left
        
        EPV_Surface_grid_values = np.fliplr(EPV_Surface_grid_values)
        
    
    Number_Grid_Values_y, Number_Grid_Values_x = EPV_Surface_grid_values.shape
    
    
    # Plot a Soccer/Football Pitch
    
    fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals, linewidth = 2, markersize = 20 )
    
    
    
    # Get Pitch Dimensions Depending On the Metric Unit Used
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
    
    
    # Plot the EPV's Surface
    
    ax.imshow( EPV_Surface_grid_values, extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
               vmin = 0, vmax = 0.6, cmap = EPV_Surface_color_map, alpha = 0.6 )
             
             # interpolation = 'spline36',  ???
    
    
    
    
    
    
    


    
def Plot_EPV_Surface_Model_m_Smooth( EPV_Surface_grid_values, EPV_Surface_color_map = "Blues", attacking_direction = 1, metric_unit = "cm", pitch_color = "white", style_of_the_goals = "entire_goal" ):
    """ 
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Plots the Pre-Generated Expected Possession Value (EPV) Surface
    
    Input: EPV_Surface_grid_values = The Pre-Generated (32 x 50) EPV Surface Model  (Grid Values Determined By the Values In the Loaded `.csv` File Using `Load_EPV_Surface_Model_Grid_Values()`)
                                     EPV (Surface) = The Probability That a Possession Will End With a Goal Given the Current Position/Location of the Ball
    Input: EPV_Surface_color_map = String Stating the Color Map `cmap` That Matplotlib Should Display For the Colour of the EPV's Surface Model; Options  -->  {"Blues", "Reds", "Greens", "Oranges", "Purples", "Greys", "binary"}; Default == "Blues"
    Input: attacking_direction = Sets the Attacking Direction; Options  -->  {1 : Left --> Right, -1 : Right --> Left}; Default == 1
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "green"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
            
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """    
    
    if attacking_direction == -1:
        
        
        # Flip Direction of EPV's Surface Grid If Team Is Attacking From Right --> Left
        
        EPV_Surface_grid_values = np.fliplr(EPV_Surface_grid_values)
        
    
    Number_Grid_Values_y, Number_Grid_Values_x = EPV_Surface_grid_values.shape
    
    
    # Plot a Soccer/Football Pitch
    
    fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals, linewidth = 2, markersize = 20 )
    
    
    
    # Get Pitch Dimensions Depending On the Metric Unit Used
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
    
    
    # Plot the EPV's Surface
    
    ax.imshow( EPV_Surface_grid_values, extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
               interpolation = 'spline36', vmin = 0, vmax = 0.6, cmap = EPV_Surface_color_map, alpha = 0.6 )
    
    
    
    
    
    
    


    
def Extract_EPV_Surface_Value_At_Location( position, EPV_Surface_grid_values, attacking_direction, metric_unit = "cm" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Returns the EPV Surface Value At a Given (x, y) Position/Location
    
    Input: position = Tuple `(x, y)`, Containing the Pitch Position/Location That We Are Interested In Extracting the EPV Surface Value From
    Input: EPV_Surface_grid_values = The Pre-Generated (32 x 50) EPV Surface Model  (Grid Values Determined By the Values In the Loaded `.csv` File Using `Load_EPV_Surface_Model_Grid_Values()`)
                                     EPV (Surface) = The Probability That a Possession Will End With a Goal Given the Current Position/Location of the Ball
    Input: attacking_direction = Sets the Attacking Direction; Options  -->  {1 : Left --> Right, -1 : Right --> Left}; Default == 1
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
            
    Output: EPV_Surface_Values_At_Specified_Location = EPV Surface Value At the Specified Input Position/Location  
    """
    
    x, y = position
    
    
    # Get Pitch Dimensions Depending On the Metric Unit Used
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
    
    
    
    
    if abs(x) > Pitch_Dimensions[0]/2 or abs(y) > Pitch_Dimensions[1]/2:
        
        return 0   # If Position Is Off the Playing Area of the Pitch --> `EPV_Surface_Values_At_Specified_Location` = 0
    
    
    else:
        
        if attacking_direction == -1:
            
            EPV_Surface_grid_values = np.fliplr(EPV_Surface_grid_values)
            
        
        Number_Grid_Values_y, Number_Grid_Values_x = EPV_Surface_grid_values.shape
        
        dx = Pitch_Dimensions[0] / float(Number_Grid_Values_x)
        dy = Pitch_Dimensions[1] / float(Number_Grid_Values_y)
        
        
        if metric_unit == "cm":
        
            ix = (x + Pitch_Dimensions[0]/2 - 0.01) / dx
            iy = (y + Pitch_Dimensions[1]/2 - 0.01) / dy
        
        
        if metric_unit == "m":
        
            ix = (x + Pitch_Dimensions[0]/2 - 0.0001) / dx
            iy = (y + Pitch_Dimensions[1]/2 - 0.0001) / dy
        
        
        EPV_Surface_Values_At_Specified_Location = EPV_Surface_grid_values[int(iy), int(ix)]
        
        
        
        return EPV_Surface_Values_At_Specified_Location
    
    
    
    
    
    
    
    
    
    
def Calculate_Expected_EPV_Added( start_frame, end_frame, team_in_possession_of_ball_series, home_team_tracking_data_df, away_team_tracking_data_df, ball_tracking_data_df, GK_kit_numbers, EPV_Surface_grid_values, Pitch_Control_model_params, include_offsides = True, metric_unit = "cm" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Calculates the Expected (Expected Possession Value) EPV Value-Added & the Direct Defined Change In EPV Surface Value (Not the Expected Change, i.e. Ignoring Pitch Control Surface Values), Between Starting & End/Target Location/Position
    
    Input: start_frame = Starting Frame # (Frame In Which the Trajectory Starts)
    Input: end_frame = Ending Frame # (Frame In Which the Trajectory Ends)
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: home_team_tracking_data_df = Home Team's Tracking Data DataFrame - Movie Will Be Created From All Rows In the DataFrame
    Input: away_team_tracking_data_df = Away Team's Tracking Data DataFrame - The Indices of This DataFrame MUST ≡ Indices From the `home_team_tracking_data_df` DataFrame
    Input: ball_tracking_data_df = Ball's Tracking Data DataFrame
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: EPV_Surface_grid_values = The Pre-Generated (32 x 50) EPV Surface Model  (Grid Values Determined By the Values In the Loaded `.csv` File Using `Load_EPV_Surface_Model_Grid_Values()`)
                                     EPV (Surface) = The Probability That a Possession Will End With a Goal Given the Current Position/Location of the Ball
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    Input: include_offsides = Boolean Value, Staing Whether Off-Sides Rules Are Taken Into Consideration In the Pitch Control Model Calculations. If `include_offsides = True`  -->  Find & Remove Off-Side Attacking Players From the Calculation; Default == True
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    
    Output: Expected_EPV_Added = (Expected) EPV Value-Added ≡ Difference In Expected EPV Surface Value, Between Starting & End/Target Location/Position
    Output: EPV_Surface_Value_Difference = (Raw) Direct Defined Change In EPV Surface Value (Not the Expected Change, i.e. Ignoring Pitch Control Surface Values), Between Starting & End/Target Location/Position
    """
    
    # Get the Details of the Specified Frame #/Given Instant of the Match (Team In Possession, Ball's Starting & End/Target Location/Position)
    
    if team_in_possession_of_ball_series.loc[start_frame] == 1.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
    if team_in_possession_of_ball_series.loc[start_frame] == 2.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Away"
        
        
        
    Ball_Starting_Position = np.array( [ ball_tracking_data_df["X"].loc[start_frame], ball_tracking_data_df["Y"].loc[start_frame] ] )
    Ball_Target_Position = np.array( [ ball_tracking_data_df["X"].loc[end_frame], ball_tracking_data_df["Y"].loc[end_frame] ] )
    
    
    
    # Playing Direction For Attacking Team (So We Know Whether To Flip the EPV Surface Model's Grid of Values Or Not)
    
    Home_Team_Attacking_Direction = TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[start_frame], verbose = False )
    
    
    if Team_In_Possesion_At_Starting_Frame_Number == 'Home':
        
        Attacking_Direction_of_Team_In_Possession = Home_Team_Attacking_Direction
        
        Attacking_Players = TFVFs.Initialize_Players( team_name = 'Home', team_tracking_data_row = home_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[0], Pitch_Control_model_params = Pitch_Control_model_params )
        Defending_Players = TFVFs.Initialize_Players( team_name = 'Away', team_tracking_data_row = away_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[1], Pitch_Control_model_params = Pitch_Control_model_params )
        
    
    elif Team_In_Possesion_At_Starting_Frame_Number == 'Away':
        
        Attacking_Direction_of_Team_In_Possession = Home_Team_Attacking_Direction * -1
        
        Defending_Players = TFVFs.Initialize_Players( team_name = 'Home', team_tracking_data_row = home_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[0], Pitch_Control_model_params = Pitch_Control_model_params )
        Attacking_Players = TFVFs.Initialize_Players( team_name = 'Away', team_tracking_data_row = away_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[1], Pitch_Control_model_params = Pitch_Control_model_params )
        
    
    
    # Find & Flag Any Attacking Players That Are Off-Side & Remove Them From the Pitch Control Calculation
    
    if include_offsides == True:
        
        Attacking_Players = TFVFs.Check_OffSides( attacking_players = Attacking_Players, defending_players = Defending_Players, ball_starting_position = Ball_Starting_Position, GK_kit_numbers = GK_kit_numbers,
                                                  verbose = True, metric_unit = metric_unit )
    
    
    
    # Pitch Control Surface At Starting Location/Position
    
    PPCF_Attacking_Team_At_Starting_Position,_ = TFVFs.Calculate_Pitch_Control_Surface_At_Target( target_position = Ball_Starting_Position,
                                                                                                  attacking_players = Attacking_Players, defending_players = Defending_Players,
                                                                                                  ball_starting_position = Ball_Starting_Position,
                                                                                                  Pitch_Control_model_params = Pitch_Control_model_params )
    
    
    
    # Pitch Control Surface At End/Target Location/Position
    
    PPCF_Attacking_Team_At_Target_Position,_ = TFVFs.Calculate_Pitch_Control_Surface_At_Target( target_position = Ball_Target_Position,
                                                                                                attacking_players = Attacking_Players, defending_players = Defending_Players,
                                                                                                ball_starting_position = Ball_Starting_Position,
                                                                                                Pitch_Control_model_params = Pitch_Control_model_params )
    
    
    
    # EPV Surface At Starting Location/Position
    
    EPV_Surface_Values_At_Starting_Location = TFVFs.Extract_EPV_Surface_Value_At_Location( position = Ball_Starting_Position, EPV_Surface_grid_values = EPV_Surface_grid_values,
                                                                                           attacking_direction = Attacking_Direction_of_Team_In_Possession, metric_unit = metric_unit )
    
    
    
    # EPV Surface At End/Target Location/Position
    
    EPV_Surface_Values_At_Target_Location = TFVFs.Extract_EPV_Surface_Value_At_Location( position = Ball_Target_Position, EPV_Surface_grid_values = EPV_Surface_grid_values,
                                                                                         attacking_direction = Attacking_Direction_of_Team_In_Possession, metric_unit = metric_unit )
    
    
    
    # 'Expected' EPV Surface At a Specific Location/Position = Multiplying Pitch Control Surface By An EPV Surface (i.e. Pitch Control Surface x EPV Surface)
    #                                                        ≡ The Expected Possession Value of Moving the Ball To Any Location, Accounting For the Probability That the Ball Move (Pass/Carry) Is Successful
    # 'Expected' EPV At Target & Starting Location/Position
    
    Expected_EPV_Surface_Value_At_Starting_Position = PPCF_Attacking_Team_At_Starting_Position * EPV_Surface_Values_At_Starting_Location
    
    Expected_EPV_Surface_Value_At_Target_Position = PPCF_Attacking_Team_At_Target_Position * EPV_Surface_Values_At_Target_Location
        
    
    
    # (Expected) EPV-Added = Difference In Expected EPV Surface Value Between Starting & End/Target Location/Position
    
    Expected_EPV_Added = Expected_EPV_Surface_Value_At_Target_Position - Expected_EPV_Surface_Value_At_Starting_Position
    
    
    
    # (Raw) Direct Defined Change In EPV Surface Value (Not the Expected Change, i.e. Ignoring Pitch Control Surface Values), Between Starting & End/Target Location/Position
    
    EPV_Surface_Value_Difference = EPV_Surface_Values_At_Target_Location - EPV_Surface_Values_At_Starting_Location
    

    
    
    return Expected_EPV_Added, EPV_Surface_Value_Difference










def Find_Max_Expected_EPV_Added_At_Target( frame_number, team_in_possession_of_ball_series, home_team_tracking_data_df, away_team_tracking_data_df, ball_tracking_data_df, GK_kit_numbers, EPV_Surface_grid_values, Pitch_Control_model_params, include_offsides = True, metric_unit = "cm" ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Finds the Max Expected Possession Value (EPV) That Could Have Been Achieved For a Pass By Searching the Entire Field For the Best Target (i.e. Location To Move the Ball To)
    
    Input: frame_number = Frame # (Number), i.e. Specified Instant of the Match (≡ Match Tracking DataFrames' Index)
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: home_team_tracking_data_df = Home Team's Tracking Data DataFrame - Movie Will Be Created From All Rows In the DataFrame
    Input: away_team_tracking_data_df = Away Team's Tracking Data DataFrame - The Indices of This DataFrame MUST ≡ Indices From the `home_team_tracking_data_df` DataFrame
    Input: ball_tracking_data_df = Ball's Tracking Data DataFrame
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: EPV_Surface_grid_values = The Pre-Generated (32 x 50) EPV Surface Model  (Grid Values Determined By the Values In the Loaded `.csv` File Using `Load_EPV_Surface_Model_Grid_Values()`)
                                     EPV (Surface) = The Probability That a Possession Will End With a Goal Given the Current Position/Location of the Ball
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    Input: include_offsides = Boolean Value, Staing Whether Off-Sides Rules Are Taken Into Consideration In the Pitch Control Model Calculations. If `include_offsides = True`  -->  Find & Remove Off-Side Attacking Players From the Calculation; Default == True
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
        
    Output: Max_Expected_EPV_Surface_Value_Added = Max Expected EPV Value-Added That Could Be Achieved At the Current Frame #/Instant of the Match (Difference Between EPV At Location With Max Expected EPV & Expected EPV At Current Ball Location)
    Output: Location_of_Max_Expected_EPV_Surface_Value_Added = (x, y) Location of the Position of the Max Expected EPV Surface Value-Added `Max_Expected_EPV_Surface_Value_Added`
    """
    
    # Get the Details of the Specified Frame #/Given Instant of the Match (Team In Possession, Ball's Starting Position)
    
    if team_in_possession_of_ball_series.loc[frame_number] == 1.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
    if team_in_possession_of_ball_series.loc[frame_number] == 2.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Away"
        
        
        
    Ball_Current_Position = np.array( [ ball_tracking_data_df["X"].loc[frame_number], ball_tracking_data_df["Y"].loc[frame_number] ] )
    
    
    
    # Playing Direction For Attacking Team (So We Know Whether To Flip the EPV Surface Model's Grid of Values Or Not)
    
    Home_Team_Attacking_Direction = TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[start_frame], verbose = False )
    
    
    if Team_In_Possesion_At_Starting_Frame_Number == 'Home':
        
        Attacking_Direction_of_Team_In_Possession = Home_Team_Attacking_Direction
        
        Attacking_Players = TFVFs.Initialize_Players( team_name = 'Home', team_tracking_data_row = home_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[0], Pitch_Control_model_params = Pitch_Control_model_params )
        Defending_Players = TFVFs.Initialize_Players( team_name = 'Away', team_tracking_data_row = away_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[1], Pitch_Control_model_params = Pitch_Control_model_params )
        
    
    elif Team_In_Possesion_At_Starting_Frame_Number == 'Away':
        
        Attacking_Direction_of_Team_In_Possession = Home_Team_Attacking_Direction * -1
        
        Defending_Players = TFVFs.Initialize_Players( team_name = 'Home', team_tracking_data_row = home_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[0], Pitch_Control_model_params = Pitch_Control_model_params )
        Attacking_Players = TFVFs.Initialize_Players( team_name = 'Away', team_tracking_data_row = away_team_tracking_data_df.loc[start_frame], GK_kit_number = GK_kit_numbers[1], Pitch_Control_model_params = Pitch_Control_model_params )
        
    
    
    # Find & Flag Any Attacking Players That Are Off-Side & Remove Them From the Pitch Control Calculation
    
    if include_offsides == True:
        
        Attacking_Players = TFVFs.Check_OffSides( attacking_players = Attacking_Players, defending_players = Defending_Players, ball_starting_position = Ball_Current_Position, GK_kit_numbers = GK_kit_numbers,
                                                  verbose = True, metric_unit = metric_unit )
    
    
    
    # Pitch Control Surface At Current Location/Position
    
    PPCF_Attacking_Team_At_Current_Position,_ = TFVFs.Calculate_Pitch_Control_Surface_At_Target( target_position = Ball_Current_Position,
                                                                                                  attacking_players = Attacking_Players, defending_players = Defending_Players,
                                                                                                  ball_starting_position = Ball_Current_Position,
                                                                                                  Pitch_Control_model_params = Pitch_Control_model_params )
    
    
    
    # EPV Surface At Current Location/Position
    
    EPV_Surface_Values_At_Current_Location = TFVFs.Extract_EPV_Surface_Value_At_Location( position = Ball_Current_Position, EPV_Surface_grid_values = EPV_Surface_grid_values,
                                                                                           attacking_direction = Attacking_Direction_of_Team_In_Possession, metric_unit = metric_unit )
    
    
    
    # Generate & Evaluate Pitch Control Surface For Frame #/Instant `frame_number` of the Match
    
    PPCF_Attacking_Team, Grid_Cells_Positions_x, Grid_Cells_Positions_y = TFVFs.Generate_Pitch_Control_Surface_For_Single_Match_Frame( frame_number = frame_number, team_in_possession_of_ball_series = team_in_possession_of_ball_series,
                                                                                                                                       home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number],
                                                                                                                                       away_team_tracking_data_row = away_team_tracking_data_df.loc[frame_number],
                                                                                                                                       ball_tracking_data_row = ball_tracking_data_df.loc[frame_number],
                                                                                                                                       GK_kit_numbers = GK_kit_numbers,
                                                                                                                                       Pitch_Control_model_params = Pitch_Control_model_params,
                                                                                                                                       metric_unit = metric_unit, number_grid_cells_x = 50, include_offsides = include_offsides )

    
        
    # 'Expected' EPV Surface At a Specific Location/Position = Multiplying Pitch Control Surface By An EPV Surface (i.e. Pitch Control Surface x EPV Surface)
    #                                                        ≡ The Expected Possession Value of Moving the Ball To Any Location, Accounting For the Probability That the Ball Move (Pass/Carry) Is Successful
    # Expected EPV Surface At Frame #/Instant `frame_number` of the Match
    
    if Attacking_Direction_of_Team_In_Possession == -1:
        
        Expected_EPV_Surface_Values = PPCF_Attacking_Team * np.fliplr(EPV_Surface_grid_values)
        
    
    else:
        
        Expected_EPV_Surface_Values = PPCF_Attacking_Team * EPV_Surface_grid_values
        
        
    
    # Find Index of the Max Expected EPV
    
    Max_Expected_EPV_Index = np.unravel_index(Expected_EPV_Surface_Values.argmax(), Expected_EPV_Surface_Values.shape)
    
    
    
    # Expected EPV Surface Value At Current Ball Position/Location
    
    Expected_EPV_Surface_Value_At_Current_Position = PPCF_Attacking_Team_At_Current_Position * EPV_Surface_Values_At_Current_Location
    
    
    
    # Max Expected EPV Value-Added (Difference Between EPV At Location With Max Expected EPV & Expected EPV At Current Ball Location)
    
    Max_Expected_EPV_Surface_Value_Added = Expected_EPV_Surface_Values.max() - Expected_EPV_Surface_Value_At_Current_Position
    
    
    
    # Location Where Max Expected EPV Surface Value-Added Is Situated
    
    Location_of_Max_Expected_EPV_Surface_Value_Added = ( Grid_Cells_Positions_x[Max_Expected_EPV_Index[1]], Grid_Cells_Positions_y[Max_Expected_EPV_Index[0]] )
    

    
    
    return Max_Expected_EPV_Surface_Value_Added, Location_of_Max_Expected_EPV_Surface_Value_Added










def Plot_Expected_EPV_Surface_For_Single_Match_Frame( frame_number, team_in_possession_of_ball_series, home_team_tracking_data_df, away_team_tracking_data_df, ball_tracking_data_df, GK_kit_numbers, Pitch_Control_model_params, include_offsides = True, team_colors = ('b', 'r'), home_team_players_color_and_style = "bo", away_team_players_color_and_style = "ro", ball_color_and_style = "ko", home_team_EPV_Surface_color_map = "Blues", away_team_EPV_Surface_color_map = "Reds", max_value_of_color_scale_of_EPV_Surface = 1.0, Expected_EPV_Surface_alpha = 0.7, display_max_Expected_EPV_Added = True, include_player_velocities = True, include_ball_velocity = False, player_marker_size = 10, player_alpha = 0.7, display_players_currently_in_possession = True, match_encoded_id = None, show_kit_numbers = True, kit_numbers_on_player_or_next_to_player = "next to player", metric_unit = "cm", pitch_color = "white", style_of_the_goals = "entire_goal", display_value_of_Expected_EPV_Added = True, number_of_frames_into_future = 25 ):
    """
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    Function That Plots the 'Expected' EPV Surface [ ≡ (EPV x Pitch Control) Surface ] At a Specific Location/Position At the Frame #/Instant of the Match --> Players' & Ball's Positions & Velocities Are Overlaid
    
    Input: frame_number = Frame # (Number), i.e. Specified Instant of the Match (≡ Match Tracking DataFrames' Index)
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: home_team_tracking_data_df = Home Team's Tracking Data DataFrame - Movie Will Be Created From All Rows In the DataFrame
    Input: away_team_tracking_data_df = Away Team's Tracking Data DataFrame - The Indices of This DataFrame MUST ≡ Indices From the `home_team_tracking_data_df` DataFrame
    Input: ball_tracking_data_df = Ball's Tracking Data DataFrame
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    Input: include_offsides = Boolean Value, Staing Whether Off-Sides Rules Are Taken Into Consideration In the Pitch Control Model Calculations. If `include_offsides = True`  -->  Find & Remove Off-Side Attacking Players From the Calculation; Default == True
    Input: team_colors = Tuple Containing the Team Colors of the Home & Away Teams; Default == ('b', 'r')  -->  'b' (Blue, Home Team) & 'r' (Red, Away Team)
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: home_team_EPV_Surface_color_map = String, Stating the EPV Surface's Colour-Map For the Home Team; Options  -->  {"Blues", "Reds", "Greens", "Oranges", "Purples", "Greys", "binary"}; Default == "Blues"
    Input: away_team_EPV_Surface_color_map = String, Stating the EPV Surface's Colour-Map For the Away Team; Options  -->  {"Blues", "Reds", "Greens", "Oranges", "Purples", "Greys", "binary"}; Default == "Reds"
    Input: max_value_of_color_scale_of_EPV_Surface = If Set To `True` --> Uses the Max Value of the EPV Surface To Define the Colour-Scale of the Image. If Set To a Value In the Range `[0, 1]` --> Uses This Value As the Max of the Colour-Scale; Options  -->  {`True`, [0, 1]}; Default == 1.0
    Input: Expected_EPV_Surface_alpha = Alpha (Transparency) Coefficient of the Expected EPV Surface [ ≡ (EPV x Pitch Control) Surface ]
    Input: display_max_Expected_EPV_Added = Boolean Value, Determining Whether To Display the Region of the Pitch Where the Max Expected EPV-Added Value Is Located, By Marking It Using A Contoured-Line Surrounding Such Region
    Input: include_player_velocities = Boolean Value, That Determines Whether Player Velocities Are Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: include_ball_velocity = Boolean Value, That Determines Whether the Ball's Velocity Is Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: player_alpha = Alpha (Transparency) Coefficient of Players' Markers; Default == 0.7
    Input: display_players_currently_in_possession = Boolean Value, Stating Whether the Video-Clip Should Include & Display An Indication of the Player Currently In Possession of the Ball, By Adding a Yellow/Golden Ring Around the Player's Marker; Default == True
    Input: match_encoded_id = Integer Value, Indicating the Encoded Match ID (≡ Match# - 1)  --  Ex: Match# = 84  -->  Match ID ≡ `match_encoded_id` = 83; `match_encoded_id` Only Has An Argument Passed To It IF --> `display_players_currently_in_possession = True`
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: kit_numbers_on_player_or_next_to_player = String That Determines Whether the Players' Kit Numbers Should Be Shown On the Players' Marker Or Next To It; Options  -->  {"next to player", "on player"}; Default == "next to player"
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "white"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
    Input: display_value_of_Expected_EPV_Added = Boolean Value, Stating Whether a Title Should Be Included For the Plot, Explicitly Stating the Expected EPV Value-Added Generated In `number_of_frames_into_future` Number of Frames Into the Future
    Input: number_of_frames_into_future = Number of Frames Into the Future With Respect To the Current Frame `frame_number`
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """    

    # Plot Frame #/Instant of the Match
    
    fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals, linewidth = 2, markersize = 20 )
    
    
    TFVFs.Plot_Single_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number],
                                   away_team_tracking_data_row = away_team_tracking_data_df.loc[frame_number],
                                   ball_tracking_data_row = ball_tracking_data_df.loc[frame_number],
                                   team_colors = team_colors, home_team_players_color_and_style = home_team_players_color_and_style, away_team_players_color_and_style = away_team_players_color_and_style, ball_color_and_style = ball_color_and_style,
                                   include_player_velocities = include_player_velocities, include_ball_velocity = include_ball_velocity,
                                   player_marker_size = player_marker_size, player_alpha = player_alpha,
                                   display_players_currently_in_possession = display_players_currently_in_possession, match_encoded_id = match_encoded_id, frame_number = frame_number,
                                   show_kit_numbers = show_kit_numbers, kit_numbers_on_player_or_next_to_player = kit_numbers_on_player_or_next_to_player,
                                   figax = (fig, ax), metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
    
       
    
    # Extracting Which Team Is In Possession of the Ball At the Specified Frame #/Instant of the Match
    
    if team_in_possession_of_ball_series.loc[frame_number] == 1.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
    if team_in_possession_of_ball_series.loc[frame_number] == 2.0:
        
        Team_In_Possesion_At_Starting_Frame_Number = "Away"
        
        
        
        
    # Load the Pre-Generated EPV Surface Model's Grid Values [m]

    EPV_Surface_Grid_Values = TFVFs.Load_EPV_Surface_Model_Grid_Values( metric_unit = "m", smooth_or_discrete_data = "discrete" )

    
    
    
    # Plot Pitch Control Surface
    
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('b', 'r') ):
        
        EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'b'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('b', 'r') ):
        
        EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
        
    # If Teams' Colours Are Reversed
    
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'b') ):
        
        EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'b') ):
        
        EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'b'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
    
    
    # Plot Pitch Control Surface
    
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('m', 'g') ):
        
        EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'm'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('m', 'g') ):
        
        EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'g'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
    
    # If Teams' Colours Are Reversed
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('g', 'm') ):
        
        EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'g'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('g', 'm') ):
        
        EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'm'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
        
    # Plot Pitch Control Surface
    
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'k') ):
        
        EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'k') ):
        
        EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'y'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
    
    # If Teams' Colours Are Reversed
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('k', 'r') ):
        
        EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'y'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
    if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('k', 'r') ):
        
        EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
        Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
        EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
        
    
    # Generate & Evaluate Pitch Control Surface For Frame #/Instant `frame_number` of the Match
    
    PPCF_Attacking_Team, Grid_Cells_Positions_x, Grid_Cells_Positions_y = TFVFs.Generate_Pitch_Control_Surface_For_Single_Match_Frame( frame_number = frame_number, team_in_possession_of_ball_series = team_in_possession_of_ball_series,
                                                                                                                                       home_team_tracking_data_row = home_team_tracking_data_df.loc[frame_number],
                                                                                                                                       away_team_tracking_data_row = away_team_tracking_data_df.loc[frame_number],
                                                                                                                                       ball_tracking_data_row = ball_tracking_data_df.loc[frame_number],
                                                                                                                                       GK_kit_numbers = GK_kit_numbers,
                                                                                                                                       Pitch_Control_model_params = Pitch_Control_model_params,
                                                                                                                                       metric_unit = metric_unit, number_grid_cells_x = 50, include_offsides = include_offsides )
    
    
    
    
    # 'Expected' EPV Surface At a Specific Location/Position = Multiplying Pitch Control Surface By An EPV Surface (i.e. Pitch Control Surface x EPV Surface)
    #                                                        ≡ The Expected Possession Value of Moving the Ball To Any Location, Accounting For the Probability That the Ball Move (Pass/Carry) Is Successful
    # Expected EPV Surface At Frame #/Instant `frame_number` of the Match
    
    Expected_EPV_Surface_Values = PPCF_Attacking_Team * EPV_Surface_Grid_Values
    
    
    if max_value_of_color_scale_of_EPV_Surface == True:
        
        Max_EPV_Surface_Value = np.max(Expected_EPV_Surface_Values)*2.
        
    
    elif max_value_of_color_scale_of_EPV_Surface >= 0 and max_value_of_color_scale_of_EPV_Surface <= 1:
        
        Max_EPV_Surface_Value = max_value_of_color_scale_of_EPV_Surface
        
    
    else:
        
        assert False, "`max_value_of_color_scale_of_EPV_Surface` Must Be Either {`True` Or a Float Value In the Range `[0, 1]`}"
        
    
    
    # Get Pitch Dimensions Depending On the Metric Unit Used
    
    if metric_unit == "cm":
        
        Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
    if metric_unit == "m":
        
        Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
        
        
    
    # Plot the 'Expected' EPV Surface At a Specific Location/Position ≡ (EPV x Pitch Control) Surface
    
    ax.imshow( np.flipud(Expected_EPV_Surface_Values), extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
               interpolation = 'spline36', vmin = 0, vmax = Max_EPV_Surface_Value, cmap = EPV_Surface_Colour_Map, alpha = Expected_EPV_Surface_alpha)
    
    
    if display_max_Expected_EPV_Added == True:
        
        ax.contour( Expected_EPV_Surface_Values, extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
                    levels = np.array([0.75]) * np.max(Expected_EPV_Surface_Values), colors = Line_Colour_of_Max_Expected_EPV_Added_Contour, alpha = 1.0)
    
    
    
    # Display Title Explicitly Stating/Showing the Value of the Expected EPV Value-Added
    
    if display_value_of_Expected_EPV_Added == True:
        
        Expected_EPV_Added, EPV_Surface_Value_Difference = TFVFs.Calculate_Expected_EPV_Added( start_frame = frame_number, end_frame = frame_number + number_of_frames_into_future,
                                                                                               team_in_possession_of_ball_series = team_in_possession_of_ball_series,
                                                                                               home_team_tracking_data_df = home_team_tracking_data_df,
                                                                                               away_team_tracking_data_df = away_team_tracking_data_df,
                                                                                               ball_tracking_data_df = ball_tracking_data_df,
                                                                                               GK_kit_numbers = GK_kit_numbers,
                                                                                               EPV_Surface_grid_values = EPV_Surface_Grid_Values,
                                                                                               Pitch_Control_model_params = Pitch_Control_model_params, include_offsides = include_offsides, metric_unit = metric_unit )
        
        
        
        # Calculate How Much Time [s] Into the Future, We Want To Calculate the Expected EPV Value-Added For
            
        Seconds_Into_the_Future = (1 / 25) * number_of_frames_into_future
        
        
        fig.suptitle(f"`{number_of_frames_into_future}` Frames ( ≡ {Seconds_Into_the_Future:.2f}s ) Into the Future $\\rightarrow$ Expected EPV Value-Added = {Expected_EPV_Added:.3f}", y = 0.1);

        
    
 
    return fig, ax










def Save_Match_Possession_Expected_EPV_Surface_VideoClip( start_frame, end_frame, frames_per_second, home_team_tracking_data_df, away_team_tracking_data_df, ball_tracking_data_df, team_in_possession_of_ball_series, GK_kit_numbers, Pitch_Control_model_params, team_colors = ('b', 'r'), home_team_players_color_and_style = "bo", away_team_players_color_and_style = "ro", ball_color_and_style = "ko", home_team_EPV_Surface_color_map = "Blues", away_team_EPV_Surface_color_map = "Reds", max_value_of_color_scale_of_EPV_Surface = 1.0, Expected_EPV_Surface_alpha = 0.7, display_max_Expected_EPV_Added = True, include_offsides = True, include_players_trajectories = False, include_ball_trajectory = False, include_player_velocities = True, include_ball_velocity = False, player_marker_size = 10, player_alpha = 0.7, display_players_currently_in_possession = True, match_encoded_id = None, show_kit_numbers = True, kit_numbers_on_player_or_next_to_player = "next to player", figax = None, metric_unit = "cm", pitch_color = "white", style_of_the_goals = "entire_goal", file_path = "Shots', Goals' & Possessions' Movies", file_name = "Match_Possession_Expected_EPV_Surface_Test_VideoClip" ):
    """
    Function That Generates a Movie From Match Tracking Data & Visualising the Pitch Control Model's Surface, Saving It As An `.mp4` File In the Path `file_path` Directory With File Name `file_name`
    
    Input: start_frame = Starting Frame # (Frame In Which the Trajectory Starts)
    Input: end_frame = Ending Frame # (Frame In Which the Trajectory Ends)
    Input: frames_per_second = # Frames Per Second (Frequency) To Assume When Generating the Movie; Default == 25
    Input: home_team_tracking_data_df = Home Team's Tracking Data DataFrame - Movie Will Be Created From All Rows In the DataFrame
    Input: away_team_tracking_data_df = Away Team's Tracking Data DataFrame - The Indices of This DataFrame MUST ≡ Indices From the `home_team_tracking_data_df` DataFrame
    Input: ball_tracking_data_df = Ball's Tracking Data DataFrame
    Input: team_in_possession_of_ball_series = Series (i.e. Column of a DataFrame) `"BallPossession"` of the Match Tracking DataFrame, Representing the Team In Possession of the Ball At a Given Match Frame/Instant  --> `Match_Tracking_df["BallPossession"]`
    Input: GK_kit_numbers = List of Integers Containing the Player IDs of the GoalKeepers For the [Home Team, Away Team]
    Input: Pitch_Control_model_params = Dictionary of Model Parameters; Default Model Parameters Can Be Generated Using the `Default_Pitch_Control_Model_Parameters()` Function
    Input: team_colors = Tuple Containing the Team Colors of the Home & Away Teams; Default == ('b', 'r')  -->  'b' (Blue, Home Team) & 'r' (Red, Away Team)
    Input: home_team_players_color_and_style = String Defining the Colour & Style In Which Home Team Players Should Be Plotted
    Input: away_team_players_color_and_style = String Defining the Colour & Style In Which Away Team Players Should Be Plotted
    Input: ball_color_and_style = String Defining the Colour & Style In Which the Ball Should Be Plotted
    Input: home_team_EPV_Surface_color_map = String, Stating the EPV Surface's Colour-Map For the Home Team; Options  -->  {"Blues", "Reds", "Greens", "Oranges", "Purples", "Greys", "binary"}; Default == "Blues"
    Input: away_team_EPV_Surface_color_map = String, Stating the EPV Surface's Colour-Map For the Away Team; Options  -->  {"Blues", "Reds", "Greens", "Oranges", "Purples", "Greys", "binary"}; Default == "Reds"
    Input: max_value_of_color_scale_of_EPV_Surface = If Set To `True` --> Uses the Max Value of the EPV Surface To Define the Colour-Scale of the Image. If Set To a Value In the Range `[0, 1]` --> Uses This Value As the Max of the Colour-Scale; Options  -->  {`True`, [0, 1]}; Default == 1.0
    Input: Expected_EPV_Surface_alpha = Alpha (Transparency) Coefficient of the Expected EPV Surface [ ≡ (EPV x Pitch Control) Surface ]
    Input: display_max_Expected_EPV_Added = Boolean Value, Determining Whether To Display the Region of the Pitch Where the Max Expected EPV-Added Value Is Located, By Marking It Using A Contoured-Line Surrounding Such Region
    Input: include_offsides = Boolean Value, Staing Whether Off-Sides Rules Are Taken Into Consideration In the Pitch Control Model Calculations. If `include_offsides = True`  -->  Find & Remove Off-Side Attacking Players From the Calculation; Default == True
    Input: include_players_trajectories = Boolean Value, That Determines Whether To Include & Visualise the Players' Trajectories, Or To Only Visualise Them As Single Points
    Input: include_ball_trajectory = Boolean Value, That Determines Whether To Include & Visualise the Ball's Trajectory, Or To Only Visualise It As a Single Point
    Input: include_player_velocities = Boolean Value, That Determines Whether Player Velocities Are Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: include_ball_velocity = Boolean Value, That Determines Whether the Ball's Velocity Is Also Plotted (As Quivers - see "https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.quiver.html"); Default == False
    Input: player_marker_size = Size of the Individual Players' Markers; Default == 10
    Input: player_alpha = Alpha (Transparency) Coefficient of Players' Markers; Default == 0.7
    Input: display_players_currently_in_possession = Boolean Value, Stating Whether the Video-Clip Should Include & Display An Indication of the Player Currently In Possession of the Ball, By Adding a Yellow/Golden Ring Around the Player's Marker; Default == True
    Input: match_encoded_id = Integer Value, Indicating the Encoded Match ID (≡ Match# - 1)  --  Ex: Match# = 84  -->  Match ID ≡ `match_encoded_id` = 83
    Input: show_kit_numbers = Boolean Value, That Determines Whether Players' Jersey/Kit Numbers Are Added To the Plot; Default == False
    Input: kit_numbers_on_player_or_next_to_player = String That Determines Whether the Players' Kit Numbers Should Be Shown On the Players' Marker Or Next To It; Options  -->  {"next to player", "on player"}; Default == "next to player"
    Input: figax = Tuple of the Form `(fig, ax)`, That Can Be Used To Pass In the `(fig, ax)` Objects of a Previously Generated Pitch; Set To `(fig, ax)` To Re-Use An Existing/Old Pitch (With Data On It Or Not), Or None (the Default) To Generate a New Pitch Plot
    Input: metric_unit = Metric Unit In Which the Pitch Should Be Plotted; Options  -->  {"cm", "m"}; Default == "cm"
    Input: pitch_color = Color of Pitch; Options  -->  {'green', 'white'}; Default == "white"
    Input: style_of_the_goals = Style In Which To Visualise the Goals At Both Ends of the Pitch; Options  -->  {"entire_goal", "only_squared_posts"}; Default == "entire_goal"
    Input: file_path = Directory To Save the Movie In; Default == "Shots', Goals' & Possessions' Movies"
    Input: file_name = Movie's File-Name; Default == "Match_Possession_Expected_EPV_Surface_Test_VideoClip"
        
    Output: fig, ax = Figure & Aixs Objects (So That Other Data Can Be Plotted On Top of the Pitch For More Visual Insights)
    """
    
    # Set Figure & Movie Settings
    
    FFMpegWriter = animation.writers["ffmpeg"]
    
    MetaData = dict( title = file_name, artist = "Hertha BSC Broadcast Tracking Data Video-Clip", comment = "Matplotlib" )
    
    Writer = FFMpegWriter(fps = frames_per_second, metadata = MetaData)
    
    File_Name = file_path + '/' +  file_name + ' (Expected EPV Surface).mp4'   # Directory Path + File-Name
    
    
    # Create Soccer Pitch
    
    if figax is None:  # Create a New Pitch
        
        fig, ax = TFVFs.Plot_Soccer_Pitch( metric_unit = metric_unit, pitch_color = pitch_color, style_of_the_goals = style_of_the_goals )
        
    else: # Overlay On a Previously Generated Pitch
        
        fig, ax = figax  # Unpack Specified Tuple Argument of the Parameter
        
    fig.set_tight_layout(True)
    
    
    # Generate Movie
    
    print("Generating Video-Clip... \n \n", end = '')
    
    Team_Colors = (home_team_players_color_and_style, away_team_players_color_and_style)
    
    
    if display_players_currently_in_possession == True:
    
        Possessions_df = TFVFs.Read_Possessions_Dataset( all_possessions_with_shots_and_goals = True )
                        
        Possessions_of_Current_Match_df = Possessions_df[Possessions_df["MatchId"] == match_encoded_id]
        
        Frames_At_Which_Possession_Starts_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["frames"].values.astype(int)
                        
        Possession_Durations_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["duration"].values.astype(int)
        
        Players_Currently_In_Possession_series_Values = Possessions_of_Current_Match_df[Possessions_of_Current_Match_df["is_start"] == True]["players"].values.astype(int)
    
    
    with Writer.saving(fig, File_Name, 100):
        
        
        for Frame in range(start_frame, end_frame + 1):
            
            Figure_Objects = []   # This Is Used To Collect Up All the Axis Objects So That They Can Be Deleted After Each Iteration

            
            
            # Plot Home & Away Teams In Order
    
            for Team, Color in zip( [home_team_tracking_data_df.loc[Frame], away_team_tracking_data_df.loc[Frame]], Team_Colors ):
        
                X_Columns = [c for c in Team.keys() if c[0] == 'X']  # Column Name For Players' X-Coordinate Positions
                Y_Columns = [c for c in Team.keys() if c[0] == 'Y']  # Column Name For Players' Y-Coordinate Positions
        
                
                if include_players_trajectories == False:
                    
                    if display_players_currently_in_possession == False:
                        
                    
                        Objects, = ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                        Figure_Objects.append(Objects)
                
                
                
                
                    if display_players_currently_in_possession == True:
                        
                        
                        Objects, = ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = player_marker_size, alpha = player_alpha )  # Plot Players' Positions
            
                        Figure_Objects.append(Objects)
                
                
                
                        for Frames_At_Which_Possession_Starts_series_Value, Possession_Durations_series_Value, Players_Currently_In_Possession_series_Value in zip(Frames_At_Which_Possession_Starts_series_Values, Possession_Durations_series_Values, Players_Currently_In_Possession_series_Values):
        
                            if Frame in range(Frames_At_Which_Possession_Starts_series_Value, (Frames_At_Which_Possession_Starts_series_Value + Possession_Durations_series_Value) + 1):
        
                                Player_Currently_In_Possession_X_Coordinate_Column_Name = "X" + str(Players_Currently_In_Possession_series_Value)
                                Player_Currently_In_Possession_Y_Coordinate_Column_Name = "Y" + str(Players_Currently_In_Possession_series_Value)
                
                
                
                                if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Home_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Home_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                                    Objects, = ax.plot( home_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_X_Coordinate_Column_Name], home_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                                        home_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                                    Figure_Objects.append(Objects)
                
                
                
                
                                if (Player_Currently_In_Possession_X_Coordinate_Column_Name in Away_Team_X_Coordinates_Tracking_Data_Columns) & (Player_Currently_In_Possession_Y_Coordinate_Column_Name in Away_Team_Y_Coordinates_Tracking_Data_Columns):
            
                                
                                    Objects, = ax.plot( away_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_X_Coordinate_Column_Name], away_team_tracking_data_df.loc[Frame][Player_Currently_In_Possession_Y_Coordinate_Column_Name],
                                                        away_team_players_color_and_style, markersize = player_marker_size, markeredgecolor = "yellow", markeredgewidth = 1.5, alpha = player_alpha )  # Display Player Currently In Possession
            
                                    Figure_Objects.append(Objects)
                
                
                
                
                if include_players_trajectories == True:
            
                    ax.plot( Team[X_Columns], Team[Y_Columns], Color, markersize = 3, alpha = player_alpha )  # Plot Players' Positions
                
                
                
                if show_kit_numbers == True:
            
                    if metric_unit == "cm":
                    
                        if kit_numbers_on_player_or_next_to_player == "next to player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]+75, Team[y]+75, "".join(list(x)[1 : ]), fontsize = 10, color = Color[0]  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List
                    
                
                        if kit_numbers_on_player_or_next_to_player == "on player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]-50, Team[y]-50, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List            
                        
                
                        for Kit_Number in Kit_Numbers_List:
                        
                            Figure_Objects.append(Kit_Number)
                
                
                    
                    if metric_unit == "m":
                        
                        if kit_numbers_on_player_or_next_to_player == "next to player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]+2, Team[y]+2, "".join(list(x)[1 : ]), fontsize = 10, color = Color[0]  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List
                    
                    
                        if kit_numbers_on_player_or_next_to_player == "on player":
            
                            Kit_Numbers_List = [ ax.text( Team[x]-1.5, Team[y]-1.5, "".join(list(x)[1 : ]), fontsize = 9, color = "white"  ) for x, y in zip(X_Columns, Y_Columns) if not ( np.isnan(Team[x]) or np.isnan(Team[y]) ) ]
                
                            Kit_Numbers_List                    
                    
                
                        for Kit_Number in Kit_Numbers_List:
                        
                            Figure_Objects.append(Kit_Number)
                
                
        
        
                if include_player_velocities == True:
            
                    Vx_Columns = [c for c in Team.keys() if c[ : 3] == 'V_x']  # Column Name For Players' Velocity Component In the X-Direction
                    Vy_Columns = [c for c in Team.keys() if c[ : 3] == 'V_y']  # Column Name For Players' Velocity Component In the Y-Direction
            
            
                    Objects = ax.quiver( Team[X_Columns].values.astype(np.float64), Team[Y_Columns].values.astype(np.float64),
                                         Team[Vx_Columns].values.astype(np.float64), Team[Vy_Columns].values.astype(np.float64),
                                         color = Color[0], scale_units = 'inches', scale = 1000, width = 0.0015, headlength = 5, headwidth = 3, alpha = player_alpha)
            
                    
                
                    Figure_Objects.append(Objects)
            
            
            
            
            
            # Plot the Ball
    
            # Since Some -ve Values Have Been Spotted For the Ball's Height ("Z"), Which Is Not Possible:
            # Check if There Are Values < 0 In Column "Z" (i.e. Height of the Ball) --> Convert -ve Values Into Their Respective Absolute Values, & the Original Values That Are >= 0 Are Retained
    
            if (ball_tracking_data_df.loc[Frame, "Z"] < 0).any():
        
                ball_tracking_data_df.loc[Frame, "Z"] = np.abs(ball_tracking_data_df.loc[Frame, "Z"])
            
            
            
            if include_ball_trajectory == False:
        
                Objects, = ax.plot( ball_tracking_data_df.loc[Frame, "X"], ball_tracking_data_df.loc[Frame, "Y"],
                                    ball_color_and_style, markersize = np.log(ball_tracking_data_df.loc[Frame, "Z"]), alpha = 1.0, linewidth = 0 )
                    
                Figure_Objects.append(Objects)
                
                
                
            if include_ball_trajectory == True:
                
                ax.plot( ball_tracking_data_df.loc[Frame, "X"], ball_tracking_data_df.loc[Frame, "Y"],
                         ball_color_and_style, markersize = np.log(ball_tracking_data_df.loc[Frame, "Z"]), alpha = 1.0, linewidth = 0 )
                
            
            
            
            
            
            # Extracting Which Team Is In Possession of the Ball At the Specified Frame #/Instant of the Match
    
            if team_in_possession_of_ball_series.loc[Frame] == 1.0:
        
                Team_In_Possesion_At_Starting_Frame_Number = "Home"
        
        
            if team_in_possession_of_ball_series.loc[Frame] == 2.0:
        
                Team_In_Possesion_At_Starting_Frame_Number = "Away"
        
        
        
        
            # Load the Pre-Generated EPV Surface Model's Grid Values [m]

            EPV_Surface_Grid_Values = TFVFs.Load_EPV_Surface_Model_Grid_Values( metric_unit = "m", smooth_or_discrete_data = "discrete" )

    
    
    
            # Plot Pitch Control Surface
    
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('b', 'r') ):
        
                EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'b'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('b', 'r') ):
        
                EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
        
            # If Teams' Colours Are Reversed
    
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'b') ):
        
                EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'b') ):
        
                EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'b'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
    
    
            # Plot Pitch Control Surface
    
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('m', 'g') ):
        
                EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'm'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('m', 'g') ):
        
                EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'g'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
    
            # If Teams' Colours Are Reversed
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('g', 'm') ):
        
                EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'g'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('g', 'm') ):
        
                EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'm'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
        
            # Plot Pitch Control Surface
    
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('r', 'k') ):
        
                EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('r', 'k') ):
        
                EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'y'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
    
            # If Teams' Colours Are Reversed
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Home' ) & ( team_colors == ('k', 'r') ):
        
                EPV_Surface_Colour_Map = home_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'y'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == -1 else EPV_Surface_Grid_Values
        
        
            if ( Team_In_Possesion_At_Starting_Frame_Number == 'Away' ) & ( team_colors == ('k', 'r') ):
        
                EPV_Surface_Colour_Map = away_team_EPV_Surface_color_map
        
                Line_Colour_of_Max_Expected_EPV_Added_Contour = 'r'
        
                EPV_Surface_Grid_Values = np.fliplr(EPV_Surface_Grid_Values) if TFVFs.Find_Playing_Direction_of_Teams_At_Any_Given_Match_Frame( home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame], verbose = False ) == 1 else EPV_Surface_Grid_Values
        
        
        
    
            # Generate & Evaluate Pitch Control Surface For Frame #/Instant `Frame` of the Match
    
            PPCF_Attacking_Team, Grid_Cells_Positions_x, Grid_Cells_Positions_y = TFVFs.Generate_Pitch_Control_Surface_For_Single_Match_Frame( frame_number = Frame, team_in_possession_of_ball_series = team_in_possession_of_ball_series,
                                                                                                                                               home_team_tracking_data_row = home_team_tracking_data_df.loc[Frame],
                                                                                                                                               away_team_tracking_data_row = away_team_tracking_data_df.loc[Frame],
                                                                                                                                               ball_tracking_data_row = ball_tracking_data_df.loc[Frame],
                                                                                                                                               GK_kit_numbers = GK_kit_numbers,
                                                                                                                                               Pitch_Control_model_params = Pitch_Control_model_params,
                                                                                                                                               metric_unit = metric_unit, number_grid_cells_x = 50, include_offsides = include_offsides )
    
    
    
    
            # 'Expected' EPV Surface At a Specific Location/Position = Multiplying Pitch Control Surface By An EPV Surface (i.e. Pitch Control Surface x EPV Surface)
            #                                                        ≡ The Expected Possession Value of Moving the Ball To Any Location, Accounting For the Probability That the Ball Move (Pass/Carry) Is Successful
            # Expected EPV Surface At Frame #/Instant `Frame` of the Match
    
            Expected_EPV_Surface_Values = PPCF_Attacking_Team * EPV_Surface_Grid_Values
    
    
            if max_value_of_color_scale_of_EPV_Surface == True:
        
                Max_EPV_Surface_Value = np.max(Expected_EPV_Surface_Values)*2.
        
    
            elif max_value_of_color_scale_of_EPV_Surface >= 0 and max_value_of_color_scale_of_EPV_Surface <= 1:
        
                Max_EPV_Surface_Value = max_value_of_color_scale_of_EPV_Surface
        
    
            else:
        
                assert False, "`max_value_of_color_scale_of_EPV_Surface` Must Be Either {`True` Or a Float Value In the Range `[0, 1]`}"
        
    
    
            # Get Pitch Dimensions Depending On the Metric Unit Used
    
            if metric_unit == "cm":
        
                Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
    
    
            if metric_unit == "m":
        
                Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
        
        
    
            # Plot the 'Expected' EPV Surface At a Specific Location/Position ≡ (EPV x Pitch Control) Surface
    
            Objects = ax.imshow( np.flipud(Expected_EPV_Surface_Values), extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
                                 interpolation = 'spline36', vmin = 0, vmax = Max_EPV_Surface_Value, cmap = EPV_Surface_Colour_Map, alpha = Expected_EPV_Surface_alpha)
        
        
            Figure_Objects.append(Objects)
            
    
    
    
            if display_max_Expected_EPV_Added == True:
        
                Objects = ax.contour( Expected_EPV_Surface_Values, extent = ( -Pitch_Dimensions[0]/2, Pitch_Dimensions[0]/2, -Pitch_Dimensions[1]/2, Pitch_Dimensions[1]/2 ),
                                      levels = np.array([0.75]) * np.max(Expected_EPV_Surface_Values), colors = Line_Colour_of_Max_Expected_EPV_Added_Contour, alpha = 1.0)
            
            
                Figure_Objects.append(Objects)
            
            
            
            
            
            
            
            # Include Match Time At the Top
            
            Frame_Minute =  int( (Frame / frames_per_second) / 60 )
            
            Frame_Second =  ( ((Frame / frames_per_second) / 60) - Frame_Minute ) * 60
            
            Match_Time_String = f"{Frame_Minute}:{Frame_Second:1.2f}"
            
            
            if metric_unit == "cm":
        
                Pitch_Dimensions = (10500, 6800)   # (Length, Width) of Pitch
            
                Objects = ax.text( -350, Pitch_Dimensions[1]/2 + 100, Match_Time_String, fontsize = 14 )
                
            
            if metric_unit == "m":
        
                Pitch_Dimensions = (105, 68)   # (Length, Width) of Pitch
            
                Objects = ax.text( -3.5, Pitch_Dimensions[1]/2 + 1, Match_Time_String, fontsize = 14 )
            
            
            
            
            Figure_Objects.append(Objects)
            
            Writer.grab_frame()
            
            
            # Delete all axis objects (other than pitch lines) in preperation for next frame
            
            for Figure_Object in Figure_Objects:
                
                Figure_Object.remove()

                
    
    print("\033[91m\033[1m\033[4m FINISHED \033[0m")
    
    plt.clf()
    
    plt.close(fig)