####################################################
#   UNIVERSAL IMPORTS USED THROUGHOUT THE MODULE   #
####################################################



import numpy as np
import pandas as pd

import itertools
from itertools import combinations


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')


import random   # Used To Generate Pseudo-Random Numbers --> Used To Randomize the Order of Elements In a List, Select a Random Element From a List, Generate Random Integers, Floats, etc.

import tkinter as tk
from tkinter import filedialog

import gc   # Python's Garbage Collector




from sklearn.preprocessing import MaxAbsScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer



# Import the Thesis' Preparing Data For Models Functions Module

import Thesis_Preparing_Data_For_Models_Functions as TPD4MFs











##########################################
#         DATA-LOADING FUNCTIONS         #
##########################################



def Read_Final_Version_Match_Tracking_Data( match_num = None ):
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










def Read_Tracking_Data_4_All_Season_Shots_Frames( ):
    """
    Function That Reads the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season
    
        
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the "match_num_Final.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season",
          '\n')
    
    
    all_season_shots_df = pd.read_parquet("All_Season_Shots_Frames.parquet", engine = "auto")
    
    
    # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

    print(f"Dimensions of the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season  =  {all_season_shots_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{all_season_shots_df.shape[0]}\033[0m", '\n')
    
    
    
    return all_season_shots_df










def Read_Tracking_Data_4_Match_Num_4_xG_Model( match_num = None ):
    """
    Function That Reads the Final Version of the Tracking Data of the Specified Football Match Number `match_num`
    
    Input: match_num = Integer Number Representing the "match_num_Final.parquet" File Containing the Tracking Data of That Football Match
    
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the "match_num_Final.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    match_num = int(input("For Which Match Would You Like To Load & Read Its Respective Tracking Data? -- NOTE: Must Choose a Number In the Range [0, 360]  -->  "))
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data For Match #{match_num + 1}",
          '\n')
    
    
    xG_Model_Tracking_Data_Folder = "xG Model/Data For xG Model/"
    
    Final_Match_Tracking_Data_For_Match_Num_df = pd.read_parquet(f"{xG_Model_Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
    
    
    
    
    # Dimensions of the Dataset of the Final Version of the Tracking Data For Match `match_num`

    print(f"Dimensions of the Dataset of the Final Version of the Tracking Data For Match #{match_num + 1} = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
    
    
    return Final_Match_Tracking_Data_For_Match_Num_df










def Read_Tracking_Data_4_xG_Model(  ):
    """
    Function That Reads the Final Preprocessed Version of the Tracking Data, Prepared For the xG Model
    
    Output: Final_Preprocessed_Data_4_xG_Model_df = Final Preprocessed Version of the Tracking Data, Prepared For the xG Model
    """
    
    print('\n',
          f"Loading & Reading In the Final Preprocessed Version of the Tracking Data For the xG Model",
          '\n')
    
    
    xG_Model_Folder = "xG Model/"    
    
    Final_Preprocessed_Data_4_xG_Model_df = pd.read_parquet(f"{xG_Model_Folder}Final_Preprocessed_Data_4_xG_Model.parquet", engine = "auto")
    
    
    
    
    # Dimensions of the Dataset of the Tracking Data For the xG Model
    
    print(f"Final Dimensions of the Preprocessed Dataset of the Tracking Data For the xG Model = {Final_Preprocessed_Data_4_xG_Model_df.shape}", '\n')
    
    
    return Final_Preprocessed_Data_4_xG_Model_df












#########################################################
#         DATA-PREPARATION 4 xG MODEL FUNCTIONS         #
#########################################################



def Filter_Shots_Frames( df ):
    """
    Function that iterates through the DataFrame and filters out rows where a shot is taken, based on the transition in the "Will_Be_a_Shot" column from 1.0 to 0.0
    
    Input: df = Match Tracking DataFrame To Inspect & Filter
    
    Output: df.loc[shot_frames] = Filtered DataFrame Only Containing the Frames With the Shots of That Match
    """
        
    # Identifying the rows/indices/frames where the value changes from 1.0 to 0.0
    
    shot_frames = df.index[ df['Will_Be_a_Shot'].diff() == -1.0 ].tolist()   # These indices correspond to the rows where the value just changed to 0.0
    
    
    # Adjusting indices to get the frame before the change occurs (i.e. the rows/indices/frames where value is 1.0, not 0.0 as it was before), by subtracting by 1 (i.e. i - 1)
    
    shot_frames = [ i - 1 for i in shot_frames if i > 0 ]
    
    
    # Filtering the DataFrame
    
    return df.loc[shot_frames]










def Filter_and_Concatenate_All_Tracking_Matches_To_Contain_All_Season_Shots_Frames( matches_to_filter = range(0, 361) ):
    """
    Function that processes each match tracking data file, applies the `Filter_Shots_Frames()` function to each, and concatenate them into a single DataFrame which contains all the shots (frames) taken in the entire season.
    
    Input: matches_to_filter = List or Range of Integer Numbers of the Matches To Filter
    """
    
    all_season_shots = []
    
    
    for Match_Num in matches_to_filter:
        
        
        # Read-In/Load-In the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Match_Tracking_Data_For_Match_Num_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")#, columns = xG_Model_Relevant_Columns)    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} = {Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
        
        
        
        # Filter the Tracking Datasets For Each Match To Only Contain the Frames In Which Shots Occur In That Match, Using the `Filter_Shots_Frames()` Function
        
        filtered_df = TPD4MFs.Filter_Shots_Frames( df = Match_Tracking_Data_For_Match_Num_df )
        
        
        # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

        print(f"Final Dimensions of the Filtered Dataset of the Tracking Data For Match #{Match_Num + 1}, Only Containing the Frames In Which Shots Occurred  =  {filtered_df.shape}", '\n')
        
        
        # Store This Filtered DataFrame Inside a Global List
        
        all_season_shots.append(filtered_df)
        
        
        # Explicitly Release Memory Using Python's Garbage Collector
        
        del Match_Tracking_Data_For_Match_Num_df, filtered_df
        
        gc.collect()  # Enforce & Call Python's Garbage Collector To Delete From Memory
        
                
        
        print(f"\033[92m\033[1m Filtered Tracking Data For Match #{Match_Num + 1}, Only Containing the Frames In Which Shots Occurred  -->  Succesfully Concatenated \033[0m", '\n')
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
    
    # Concatenate all filtered DataFrames
    
    all_season_shots_df = pd.concat( all_season_shots, axis = 0 )
    
    
    # Resetting the index of the concatenated DataFrame

    all_season_shots_df.reset_index( drop = True, inplace = True )
    
    
    # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

    print(f"Final Dimensions of the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season  =  {all_season_shots_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{all_season_shots_df.shape[0]}\033[0m", '\n')
    
    
    # Explicitly Release Memory Using Python's Garbage Collector
        
    del all_season_shots
        
    gc.collect()  # Enforce & Call Python's Garbage Collector To Delete From Memory
    
    
    
    # Save Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season As a New "All_Season_Shots_Frames.parquet" File
    
    all_season_shots_df.to_parquet("All_Season_Shots_Frames.parquet", engine = "auto")


    print(f"\033[92m\033[1m Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season  -->  Succesfully Saved In the 'All_Season_Shots_Frames.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Tracking_Data_4_All_Season_Shots_Frames_4_xG_Model( ):
    """
    Function That Reads the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season -- For the xG Model
    
        
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the "match_num_Final.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    all_season_shots_df = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_4_xG_Model.parquet", engine = "auto")
    
    
    # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

    print(f"Dimensions of the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season  =  {all_season_shots_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{all_season_shots_df.shape[0]}\033[0m", '\n')
    
    
    
    return all_season_shots_df


    
    
    
    
    
    
    
    
# def Extracting_Unique_xG_Values( possessions_df ):
#     """
#     Function That Extracts the Unique (Sum of) xG Values From the `nextxgfor` & `nextxgagainst` Columns From the Possessions Dataset
    
#     Input: possessions_df = DataFrame of the Possessions Dataset
    
#     Output: List_of_Unique_xG_Values = List of the Unique (Sum of) xG Values
#     """
    
#     Stored_xG_Values = []
#     List_of_Unique_xG_Values = []
    

#     for Row_Index, Row_Data in possessions_df.iterrows():
        
#         Next_xG_For_Row_Value = Row_Data["nextxgfor"]
#         Next_xG_Against_Row_Value = Row_Data["nextxgagainst"]

        
#         if Next_xG_For_Row_Value == 0.0 and Next_xG_Against_Row_Value == 0.0:
            
#             continue  # Ignore Rows With Both Values As 0.0
            

#         if Next_xG_For_Row_Value > 0.0 and Next_xG_For_Row_Value not in Stored_xG_Values:
            
#             List_of_Unique_xG_Values.append(Next_xG_For_Row_Value)
#             Stored_xG_Values.append(Next_xG_For_Row_Value)

            
#         if Next_xG_Against_Row_Value > 0.0 and Next_xG_Against_Row_Value not in Stored_xG_Values:
            
#             List_of_Unique_xG_Values.append(Next_xG_Against_Row_Value)
#             Stored_xG_Values.append(Next_xG_Against_Row_Value)

            
#         if 0.0 in Stored_xG_Values and (Next_xG_For_Row_Value > 0.0 or Next_xG_Against_Row_Value > 0.0):
            
#             continue  # Continue to the next row until a non-zero value is found
            
            

#     return List_of_Unique_xG_Values










# def Extract_Tracking_Data_of_Shots_Frames_Only( possessions_df, matches_to_filter = range(0, 361) ):
    # """
    
    # """
    
    
    
    # # Extracting Into a List the Unique Values of the (Sum of) xG In the Match
    
        # List_of_Unique_xG_Values = TCEDAFs.Extracting_Unique_xG_Values(possessions_df = Possessions_of_Shots_Only_Without_NextGoal_Related_Columns_For_Match_Num_df)
    
    
        # if want_to_debug == True:
            
            # print(List_of_Unique_xG_Values)
        
    
        # # For Every Unique (Sum of) xG Value Present, Find the First & Last Index Values In Which Appears & Fill In Any `0.0`-Valued Gaps In Between With Their Respective Values
    
        # for xG_Value in List_of_Unique_xG_Values:
            
            # if want_to_debug == True:
            
                # print(xG_Value)
                # print(Final_Match_Tracking_Data_For_Match_Num_df[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] == xG_Value ]["(Sum_of)_xG"])
            
            
            # Starting_Frame_of_xG_Value = Final_Match_Tracking_Data_For_Match_Num_df[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] == xG_Value ].index[0]
            # Final_Frame_of_xG_Value = Final_Match_Tracking_Data_For_Match_Num_df[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] == xG_Value ].index[-1]
        
            # Final_Match_Tracking_Data_For_Match_Num_df.loc[Starting_Frame_of_xG_Value : Final_Frame_of_xG_Value, "(Sum_of)_xG"] = xG_Value
            
            
            
            
            
            
            
            
            
            
def Adjust_Away_Team_Shooting_Direction(  ):
    """
    Function that ensures that all shots are directed towards the same target goal on the right of the soccer pitch
    
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    all_season_shots_df = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_4_xG_Model.parquet", engine = "auto")
    
    
    
    
    def Flip_Ball_Coordinates( df_row ):
        """
        Function that flips the X- and Y-coordinates for the away team's shots
        """
        
        df_row['X'] = abs(df_row['X'])  # Making X always positive
        
        
        if df_row['BallPossesion'] == 2.0:
            
            df_row['Y'] = -df_row['Y']      # Inverting Y
            
            
        return df_row

    
    
    # Apply the `Flip_Ball_Coordinates()` function to each row
    
    all_season_shots_on_1_same_target_goal_df = all_season_shots_df.apply( Flip_Ball_Coordinates, axis = 1 )
    
    
    # Save Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet" File
    
    all_season_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet", engine = "auto")


    print(f"\033[92m\033[1m Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Saved In the 'All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Tracking_Data_4_All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model(  ):
    """
    Function That Reads the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal -- For the xG Model
    
        
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the "match_num_Final.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    all_season_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet", engine = "auto")
    
    
    # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

    print(f"Dimensions of the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  =  {all_season_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{all_season_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    
    return all_season_shots_on_1_same_target_goal_df










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










def Calculate_2D_Distance( x1, y1, x2, y2 ):
    """
    Function That Calculates the 2D Euclidean Distance Between 2 Sets of 2D (x, y) Position Points
    
    Output = 2D Euclidean Distance
    """
    
    return np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 )










def Calculate_Ball_Angle_To_TargetGoal( ball_x, ball_y, target_goal_width = 731.52, angle_in_degrees_or_radians = "Radians" ):
    """
    Function That Calculates the Angle: θ_Ball_TargetGoal = arctan( ( Target_Goal_Width * Ball_x ) / ( Ball_x**2 + Ball_y**2 - (Target_Goal_Width / 2)**2 ) ) That the Ball Makes With Both of the Posts of the Target Goal
            ∴ Calculates the Angle That the Ball "Sees" the Target Goal ⇒ Following the Formula In: https://soccermatics.readthedocs.io/en/latest/lesson2/GeometryOfShooting.html#goal-angle
            
    Input: ball_x = X-Coordinate of the Ball
    Input: ball_y = Y-Coordinate of the Ball
    Input: target_goal_width = Width of the Goal Line/Goal-Mouth of the Target Goal - In [cm]
    Input: angle_in_degrees_or_radians = String Stating Which Angle Unit Should the Angle Be Output In; Options  -->  {"Radians", "Degrees"}; Default == "Radians"
    
    Output: Ball_Angle_To_TargetGoal = Angle That the Ball Makes With Both of the Posts of the Target Goal (In Radians Or Degrees)
    """
    
    if angle_in_degrees_or_radians == "Radians":
    
        Ball_Angle_To_TargetGoal = abs( np.arctan( ( target_goal_width * ball_x ) / ( ball_x**2 + ball_y**2 - (target_goal_width / 2)**2 ) ) )
        
        
    if angle_in_degrees_or_radians == "Degrees":
        
        Ball_Angle_To_TargetGoal = abs( np.degrees( np.arctan( ( target_goal_width * ball_x ) / ( ball_x**2 + ball_y**2 - (target_goal_width / 2)**2 ) ) ) )
    
    
    
    
    return Ball_Angle_To_TargetGoal










def Calculate_Player_Angle_To_TargetGoal( player_x, player_y, target_goal_width = 731.52, angle_in_degrees_or_radians = "Radians" ):
    """
    Function That Calculates the Angle: θ_Player_TargetGoal = arctan( ( Target_Goal_Width * Player_x ) / ( Player_x**2 + Player_y**2 - (Target_Goal_Width / 2)**2 ) ) That the Player Makes With Both of the Posts of the Target Goal
            ∴ Calculates the Angle That the Player "Sees" the Target Goal ⇒ Following the Formula In: https://soccermatics.readthedocs.io/en/latest/lesson2/GeometryOfShooting.html#goal-angle
            
    Input: player_x = X-Coordinate of the Player
    Input: player_y = Y-Coordinate of the Player
    Input: target_goal_width = Width of the Goal Line/Goal-Mouth of the Target Goal - In [cm]
    Input: angle_in_degrees_or_radians = String Stating Which Angle Unit Should the Angle Be Output In; Options  -->  {"Radians", "Degrees"}; Default == "Radians"
    
    Output: Player_Angle_To_TargetGoal = Angle That the Player Makes With Both of the Posts of the Target Goal (In Radians Or Degrees)
    """
    
    if angle_in_degrees_or_radians == "Radians":
    
        Player_Angle_To_TargetGoal = abs( np.arctan( ( target_goal_width * player_x ) / ( player_x**2 + player_y**2 - (target_goal_width / 2)**2 ) ) )
        
        
    if angle_in_degrees_or_radians == "Degrees":
        
        Player_Angle_To_TargetGoal = abs( np.degrees( np.arctan( ( target_goal_width * player_x ) / ( player_x**2 + player_y**2 - (target_goal_width / 2)**2 ) ) ) )
    
    
    
    
    return Player_Angle_To_TargetGoal










def Calculate_Ball_Angle_To_Post( ball_x, ball_y, goal_centre_x, post_y, angle_in_degrees_or_radians = "Radians" ):
    """
    Function That Calculates the Angle: θ_Ball_Post = arctan2( ( Post_y - Ball_y ) / ( Goal_Centre_x - Ball_x ) ) That the Ball Makes With 1 of the Posts of the Goal
            θ_Ball_Post = arctan( ( Post_y - Ball_y ) / ( Goal_Centre_x - Ball_x ) )  -->  But Will Return Values From [−π/2, π/2] ≡ [-90°, 90°]. This Might Cause Ambiguity Since One Can't Determine the Quadrant of the Angle
    ∴ ⇒    θ_Ball_Post = arctan2() Is Used Instead, Since It Is the Same Function Than θ = arctan(Δy / Δx) --> But Instead, Will Return Values From [−π, π] ≡ [-180°, 180°]. Hence Giving Info. About the Quadrant of the Angle
    ∴ ⇒    In the Context of a Soccer Pitch --> Using arctan2() Makes It Easier To Compute Angles Relative To the 2 Goals Since It Handles Various Quadrants Seamlessly
            
    Input: ball_x = X-Coordinate of the Ball
    Input: ball_y = Y-Coordinate of the Ball
    Input: goal_centre_x = X-Coordinate of the Centre of the Goal
    Input: post_y = Y-Coordinate of the Post We Want To Measure the Anlge With
    Input: angle_in_degrees_or_radians = String Stating Which Angle Unit Should the Angle Be Output In; Options  -->  {"Radians", "Degrees"}; Default == "Radians"
    
    Output: Ball_Angle_To_Post = Angle That the Ball Makes With 1 of the Posts of the Goal (In Radians Or Degrees)
    """
    
    if angle_in_degrees_or_radians == "Radians":
    
        Ball_Angle_To_Post = np.arctan2( post_y - ball_y, goal_centre_x - ball_x )
        
        
    if angle_in_degrees_or_radians == "Degrees":
        
        Ball_Angle_To_Post = np.degrees( np.arctan2( post_y - ball_y, goal_centre_x - ball_x ) )
    
    
    
    
    return Ball_Angle_To_Post










def Adding_Distance_and_Angles_Between_Ball_and_Target_Goal(  ):
    """
    Function That Adds 2 New Columns To the Tracking Data Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal:
    
                                                                           - `Dist_Between_Ball_TargetGoal`, Which Represents the Distance Between the Ball & the Centre of the Target Goal (On the Right Side of the Pitch)
                                                                           - `Angle_Between_Ball_TargetGoal`, Which Represents the Angle That the Ball "Sees" the Target Goal (On the Right Side of the Pitch)
    
    """
    
    # Constants
    
    Target_Goal_Width = 731.52
    
    Target_Goal_Centre_Coordinates = (5250, 0)
    
    # Target_Goal_Top_Post_y, Target_Goal_Bottom_Post_y = Target_Goal_Width / 2, -(Target_Goal_Width / 2)
    
    
    # xG_Model_Relevant_Columns = ["X", "Y", "Will_Be_a_Goal"]
    
    
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    all_season_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet", engine = "auto")#, columns = xG_Model_Relevant_Columns)
    
    
    # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

    print(f"Dimensions of the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  =  {all_season_shots_on_1_same_target_goal_df.shape}", '\n')
        
        
        
        
        # Invert All Player Positions & Velocity Components In the 2nd Halves of the Matches, Using the `To_Single_Playing_Direction( match_tracking_data_df )`, To Ensure We Always Have 1 Same Single Playing Direction Across the Full Time of the Matches: Home Team Attacks Left --> Right  &  Away Team Attack Right --> Left
        
        # Final_Match_Tracking_Data_For_Match_Num_To_Single_Playing_Direction_df = TPD4MFs.To_Single_Playing_Direction( match_tracking_data_df = Final_Match_Tracking_Data_For_Match_Num_df )
        
        
        
    
        
    # Compute Distances of the Ball To the Centre of the (Right) Target Goal
        
    all_season_shots_on_1_same_target_goal_df["Dist_Between_Ball_TargetGoal"] = TPD4MFs.Calculate_2D_Distance( x1 = all_season_shots_on_1_same_target_goal_df["X"], y1 = all_season_shots_on_1_same_target_goal_df["Y"],
                                                                                                               x2 = Target_Goal_Centre_Coordinates[0], y2 = Target_Goal_Centre_Coordinates[1] )
    
    
    
            
        # This Is the Total Visual Angle the Ball Has of the Goal, the Angle That the Ball "Sees" of the Goal, As It Would Be Perceived From the Ball's Position
        #        i.e. Angle Considering the Ball's Relative Position To Each Goal Post --> It Finds the Angle Between the Ball & Both Posts
        
        # Calculate the Angles To the Top & Bottom Posts For the Target Goal, & Then Subtract These To Find the Angle That the Ball "Sees" the Goal
        # θ_Ball_Goal = |θ_Top_Post - θ_Bottom_Post|
        
        ## Angles To Target Goal's Posts
        
        # Angle_To_Target_Goal_Top_Post = TPD4MFs.Calculate_Ball_Angle_To_Post( ball_x = Final_Match_Tracking_Data_For_Match_Num_df['X'], ball_y = Final_Match_Tracking_Data_For_Match_Num_df['Y'], 
                                                                              # goal_centre_x = Target_Goal_Centre_Coordinates[0], post_y = Target_Goal_Top_Post_y, angle_in_degrees_or_radians = "Radians" )
        
        # Angle_To_Target_Goal_Bottom_Post = TPD4MFs.Calculate_Ball_Angle_To_Post( ball_x = Final_Match_Tracking_Data_For_Match_Num_df['X'], ball_y = Final_Match_Tracking_Data_For_Match_Num_df['Y'], 
                                                                                 # goal_centre_x = Target_Goal_Centre_Coordinates[0], post_y = Target_Goal_Bottom_Post_y, angle_in_degrees_or_radians = "Radians" )
        
        
        
        
        # Final_Match_Tracking_Data_For_Match_Num_df["Angle_Between_Ball_TargetGoal"] = np.abs( Angle_To_Target_Goal_Top_Post - Angle_To_Target_Goal_Bottom_Post )
        
        
        
    ## Angle That the Ball "Sees" the (Right) Target Goal - In [rad]
    
    all_season_shots_on_1_same_target_goal_df["Angle_Between_Ball_TargetGoal_Rad"] = TPD4MFs.Calculate_Ball_Angle_To_TargetGoal( ball_x = all_season_shots_on_1_same_target_goal_df["X"], ball_y = all_season_shots_on_1_same_target_goal_df["Y"],
                                                                                                                                 target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Radians" )
    
    
    ## Angle That the Ball "Sees" the (Right) Target Goal - In [deg] ≡ [°]
    
    all_season_shots_on_1_same_target_goal_df["Angle_Between_Ball_TargetGoal_Deg"] = TPD4MFs.Calculate_Ball_Angle_To_TargetGoal( ball_x = all_season_shots_on_1_same_target_goal_df["X"], ball_y = all_season_shots_on_1_same_target_goal_df["Y"],
                                                                                                                                 target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Degrees" )
        
    
    
    
    # Dimensions of the Filtered Dataset of the Tracking Data For Match `Match_Num`, Only Contining Shots For That Match

    print(f"Dimensions of the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  =  {all_season_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
    # Save Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet" File
    
    all_season_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet", engine = "auto")
        
        
        
        # Explicitly Release Memory Using Python's Garbage Collector
        
        # del Final_Match_Tracking_Data_For_Match_Num_df, Final_Match_Tracking_Data_For_Match_Num_df["Dist_Between_Ball_TargetGoal"], Angle_To_Target_Goal_Top_Post, Angle_To_Target_Goal_Bottom_Post, Final_Match_Tracking_Data_For_Match_Num_df["Angle_Between_Ball_TargetGoal"]
        
        # gc.collect()  # Enforce & Call Python's Garbage Collector To Delete From Memory the 2 Large DataFrames For the Specific `Match_Num`
        
                
        
    print(f"\033[92m\033[1m Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Saved In the 'All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Extract_Relevant_Data_4_xG_Model(  ):
    """
    Function that extract only the releveant data/features for the xG model
    
    """
    
    xG_Model_Relevant_Columns = ["X", "Y", "Dist_Between_Ball_TargetGoal", "Angle_Between_Ball_TargetGoal_Rad", "Will_Be_a_Goal"]
    
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    Relevant_Data_4_xG_Model = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_xG_Model.parquet", engine = "auto", columns = xG_Model_Relevant_Columns)
    
    
    # Dimensions of the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal

    print(f"Dimensions of the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  =  {Relevant_Data_4_xG_Model.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0]}\033[0m", '\n')
    
    
    
    # Save Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Final_xG_Model_Data.parquet" File
    
    Relevant_Data_4_xG_Model.to_parquet(f"{xG_Model_Data_Folder}Final_xG_Model_Data.parquet", engine = "auto")


    print(f"\033[92m\033[1m Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Saved In the 'Final_xG_Model_Data.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Count_Total_Goals_Scored( df ):
    """
    Function that counts the total number of goals scored
    
    """
    
    return int( df["Will_Be_a_Goal"].sum() )










def Count_Total_Non_Scored_Shots( df ):
    """
    Function that counts the total number of non-scored shots
    
    """
    
    return int( df.shape[0] - df["Will_Be_a_Goal"].sum() )










def Read_xG_Model_Relevant_Data(  ):
    """
    Function That Reads the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    
        
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the "match_num_Final.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    Relevant_Data_4_xG_Model = pd.read_parquet(f"{xG_Model_Data_Folder}Final_xG_Model_Data.parquet", engine = "auto")
    
    
    # Dimensions of the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal

    print(f"Dimensions of the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  =  {Relevant_Data_4_xG_Model.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Season    
    
    Total_Goals_Scored_Throughout_Season = TPD4MFs.Count_Total_Goals_Scored( df = Relevant_Data_4_xG_Model )
    
    
    print(f"∴ The Total Number of Goals Scored Throughout the Season  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Season}\033[0m", '\n')
    
    
    
    return Relevant_Data_4_xG_Model










def Count_Ocurrence_of_Specific_Value( df, column_name, specific_value ):
    """
    Function that counts the number of times that a specific value occurs within a DataFrame's column
    
    Input: df = DataFrame to inspect
    Input: column_name = String of the name of the column
    Input: specific_value = Specific value to inspect for and count its occurrences
    
    Output: ( df[column_name] == specific_value ).sum() = the number of times that a specific value occurs within a DataFrame's column
    """
    
    return ( df[column_name] == specific_value ).sum()










def Count_Ocurrence_of_Values_Above_or_Below_Threshold( df, column_name, threshold, above = True ):
    """
    Function to count the number of rows where a column's value is either above or below a specified threshold

    Input: df = The DataFrame to analyze
    Input: column_name = String of the name of the column to check
    Input: threshold = The threshold value to compare against
    Input: above = True to count values above the threshold, False to count values below

    Output: count = The count of rows where the column's value is either above or below the threshold
    """
    
    if above:
        count = ( df[column_name] > threshold ).sum()
        
    else:
        count = ( df[column_name] < threshold ).sum()

        
    return count










def Check_Goals_For_Specific_Value_of_Specific_Column( df, specific_column_name, specific_value, goal_column = "Will_Be_a_Goal" ):
    """
    Function that checks if a goal was scored in the rows where a specific column has a specific value.

    Parameters:
    Input: df = The DataFrame to analyze
    Input: column_name = String of the name of the column to check
    Input: value_to_check = The specific value to check in the specified column
    Input: goal_column = The name of the column indicating if a goal was scored (default "Will_Be_a_Goal")

    Output: goals_count = The count of goals scored when the specified column has the given value
    """
    
    # Filter rows where the specified column equals the value to check and the goal column equals 1.0
    
    filtered_rows = df[ (df[specific_column_name] == specific_value) & (df[goal_column] == 1.0) ]
    

    # Count the number of such rows
    
    goals_count = len(filtered_rows)
    

    
    return goals_count










def Check_Goals_For_Values_Above_or_Below_Threshold_of_Specific_Column( df, column_name, threshold, above = True, goal_column = "Will_Be_a_Goal" ):
    """
    Function to count how many rows with values above or below a specific threshold in a specified column ended up in a goal

    Input: df = The DataFrame to analyze
    Input: column_name = The name of the column to check
    Input: threshold = The threshold value to compare against
    Input: above = True to count goals for values above the threshold, False for below
    Input: goal_column = The name of the column indicating if a goal was scored (default 'Will_Be_a_Goal')

    Output: goals_count = The count of goals scored in rows where the specified column's value is either above or below the threshold
    """
    
    if above:
        filtered_rows = df[(df[column_name] > threshold) & (df[goal_column] == 1.0)]
        
    else:
        filtered_rows = df[(df[column_name] < threshold) & (df[goal_column] == 1.0)]
        
    
    goals_count = len(filtered_rows)

    
    return goals_count










def Read_Tracking_Data_4_All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  ):
    """
    Function That Reads the Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    
        
    Output: all_season_shots_on_1_same_target_goal_df = Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    all_season_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Dimensions of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal

    print(f"Dimensions of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  =  {all_season_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Season  =  \033[91m\033[1m\033[4m{all_season_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Season    
    
    Total_Goals_Scored_Throughout_Season = TPD4MFs.Count_Total_Goals_Scored( df = all_season_shots_on_1_same_target_goal_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout the Season  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Season}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Season    
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout the Season  =  \033[91m\033[1m\033[4m{all_season_shots_on_1_same_target_goal_df.shape[0] - Total_Goals_Scored_Throughout_Season}\033[0m", '\n')
    
    
    
    return all_season_shots_on_1_same_target_goal_df










def Adjust_Attacking_Team_Shooting_Direction_and_Drop_Irrelevant_Columns(  ):
    """
    Function that ensures that all shots are directed towards the same target goal on the right of the soccer pitch, based on which team is in possession of the ball at the instant of the shot
            By default, the home team attacks from left to right throughout the whole match (this was ensured by previously using in the project the `To_Single_Playing_Direction()` function), therefore when the home team is in possession at the instant of the shot there should be no modifications.
            Thus by default, the away team attacks from right to left throughout the whole match, therefore when the away team is in possession of the ball at the instant of the shot, the ball's and all the players' X- & Y-coordinates and X- & Y-velocity components should be flipped.
            
            + Drops the Irrelevant & Unnecessary Columns: "Visable", "Visable1" --> "Visable 22", "BallStatus", "Match_Clock", "(Sum_of)_xG", "Will_Be_a_Shot",
                                                          "Dist_Between_Ball_1" --> "Dist_Between_Ball_22",  # Ball-Player Distances
                                                          "Dist_Between_1_2" --> "Dist_Between_21_22",  # Player-Player Distances
                                                          "Dist_Between_Ball_HomeGoal", "Dist_Between_Ball_AwayGoal", "Angle_Between_Ball_HomeGoal", "Angle_Between_Ball_AwayGoal",
                                                          "Dist_Between_HomeGoal_1" --> "Dist_Between_HomeGoal_22",
                                                          "Dist_Between_AwayGoal_1" --> "Dist_Between_AwayGoal_22",
                                                          "Angle_Between_HomeGoal_1" --> "Angle_Between_HomeGoal_22",
                                                          "Angle_Between_AwayGoal_1" --> "Angle_Between_AwayGoal_22".
    
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    all_season_shots_df = pd.read_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Drop Irrelevant & Unnecessary Columns
    
    Columns_To_Drop = [ Column for Column in all_season_shots_df.columns if any( substring in Column for substring in ["Visable", "Dist", "Angle"] ) ] + ["BallStatus", "Match_Clock", "(Sum_of)_xG", "Will_Be_a_Shot"]
        
    all_season_shots_df.drop( columns = Columns_To_Drop, inplace = True )
    
    
    
    
    def Flip_Ball_and_Players_Coordinates_and_Velocity_Components( df_row ):
        """
        Function that flips the X- and Y-coordinates & the X- and Y-velocity components of the ball and all the players for those rows/shot frames where the away team is in possession of the ball (i.e. is currently being the attacking team)
        """
        
        df_row["X"] = abs( df_row["X"] )  # Making X (Ball's X-Coordinate) ALWAYS +ve (thus always on the right side of the pitch at the instant of the shot) - regardless of who is in possession of the ball (i.e. who is the attacking team)
        
        
        if df_row["BallPossesion"] == 2.0:
            
            # Ball's Features
            
            df_row["Y"] = -df_row["Y"]      # Inverting Y - Ball's Y-Coordinate
            
            df_row["V_xBall"] = -df_row["V_xBall"]      # Inverting V_xBall - Ball's X-Velocity Component
            
            df_row["V_yBall"] = -df_row["V_yBall"]      # Inverting V_yBall - Ball's Y-Velocity Component
            
            
            # Players' Features
            
            for Player in range(1, 23):  # Players 1 --> 22
            
                df_row[f"X{Player}"] = -df_row[f"X{Player}"]      # Inverting X1 --> X22 - Players' X-Coordinate
            
                df_row[f"Y{Player}"] = -df_row[f"Y{Player}"]      # Inverting Y1 --> Y22 - Players' Y-Coordinate
            
                df_row[f"V_x{Player}"] = -df_row[f"V_x{Player}"]      # Inverting V_x1 --> V_x22 - Players' X-Velocity Component
                
                df_row[f"V_y{Player}"] = -df_row[f"V_y{Player}"]      # Inverting V_y1 --> V_y22 - Players' Y-Velocity Component
            
            
            
            
        return df_row

    
    
    
    # Apply the `Flip_Ball_Coordinates()` function to each row
    
    all_season_shots_on_1_same_target_goal_df = all_season_shots_df.apply( Flip_Ball_and_Players_Coordinates_and_Velocity_Components, axis = 1 )
    
    
    # Save Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
    all_season_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")


    print(f"\033[92m\033[1m Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Saved In the 'All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Replace_Multiple_Values_From_Multiple_Columns_and_Save_Modified_Data_Into_File( df, exact_replacements_dict, file_path, conditional_replacements_dict = None, above = None ):
    """
    Function to replace multiple specified exact values and multiple specified conditional values from multiple columns of the DataFrame, and save the changes

    Input: df = The DataFrame to modify
    Input: replacement_dict = A dictionary where each key is a column name and each value is a dictionary of exact value replacements for that column
    Input: file_path = The file path where the modified DataFrame will be saved
    Input: conditional_replacements = A dictionary for conditional replacements, where the key is the column name, and the value is a tuple of conditional (threshold, new_value) replacements
    Input: above = True to count goals for values above the threshold, False for below

    Output: The function saves the modified DataFrame to the given file path
    """
    
    # Make values in 'Angle_Between_Ball_TargetGoal_Rad' always positive
    
    # df['Angle_Between_Ball_TargetGoal_Rad'] = df['Angle_Between_Ball_TargetGoal_Rad'].abs()

    
    # Handle exact replacements - Iterate over the replacement_dict and perform replacements for each column
    
    for column_name, replacements in exact_replacements_dict.items():
        
        df[column_name].replace(replacements, inplace = True)
        
        
    # Handle conditional replacements
    
    if conditional_replacements_dict is not None:
        
        for column_name, (threshold, new_value) in conditional_replacements_dict.items():
        
            if above:
        
                df.loc[ df[column_name] > threshold, column_name ] = new_value
            
            else:
            
                df.loc[ df[column_name] < threshold, column_name ] = new_value

        
    # Save the modified DataFrame back to the parquet file
    
    df.to_parquet(file_path, engine = 'auto')
    
    
    print(f"\033[92m\033[1m Modifications On Outliers & Nonsensical Values, Within the Relevant Tracking Data For the xG Model  -->  Succesfully Saved In the 'All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Stratified_DataFrame_Train_Test_Split(  ):
    """
    Function that performs a train-test split in a stratified manner to preserve the original proportion of class labels within each new splitted training (+ validating) set & test set
    
    """
    
    All_Season_Shots_On_1_Same_Target_Goal_df = TPD4MFs.Read_Tracking_Data_4_All_Season_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  )
    
    
    # Features
    
    X = All_Season_Shots_On_1_Same_Target_Goal_df.drop( "Will_Be_a_Goal", axis = 1, inplace = False )
    
    
    # Target Variable
    
    y = All_Season_Shots_On_1_Same_Target_Goal_df["Will_Be_a_Goal"]
    

    # Stratified Split To Maintain the Proportion of Target Variable Classes/Labels:

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.3, stratify = y, random_state = 42 )   # 30% Test ⇒ ... Shots In Test Set  <==>  ... Shots In Training (+ Validation) Set
    
    
    
    # Creating the DataFrame for Training Shots
    
    Training_Shots_df = pd.concat( [X_train, y_train], axis = 1 )
    
    
    # Dimensions of the Training Shots Tracking Data df

    print(f"Dimensions of the Training Shots Tracking Data df  =  {Training_Shots_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Training Shots Tracking Data df  =  \033[91m\033[1m\033[4m{Training_Shots_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Training Shots Tracking Data df
    
    Total_Goals_Scored_Throughout_Training_Shots = TPD4MFs.Count_Total_Goals_Scored( df = Training_Shots_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout the Training Shots Tracking Data df  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Training_Shots}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Training Shots Tracking Data df
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout the Training Shots Tracking Data df  =  \033[91m\033[1m\033[4m{Training_Shots_df.shape[0] - Total_Goals_Scored_Throughout_Training_Shots}\033[0m", '\n')
    
    
    
    # Saving the Training Shots DataFrame as a .parquet file
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    Training_Shots_df.to_parquet( f"{xG_Model_Data_Folder}Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = 'auto' )
    

    
    
    # Creating the DataFrame for Test Shots
    
    Test_Shots_df = pd.concat( [X_test, y_test], axis = 1 )
    
    
    # Dimensions of the Test Shots Tracking Data df

    print(f"Dimensions of the Test Shots Tracking Data df  =  {Test_Shots_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout the Test Shots Tracking Data df  =  \033[91m\033[1m\033[4m{Test_Shots_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Test Shots Tracking Data df    
    
    Total_Goals_Scored_Throughout_Test_Shots = TPD4MFs.Count_Total_Goals_Scored( df = Test_Shots_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout the Test Shots Tracking Data df  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Test_Shots}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Test Shots Tracking Data df    
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout the Test Shots Tracking Data df  =  \033[91m\033[1m\033[4m{Test_Shots_df.shape[0] - Total_Goals_Scored_Throughout_Test_Shots}\033[0m", '\n')
    
    
    
    # Saving the Test Shots DataFrame as a .parquet file
    
    Test_Shots_df.to_parquet( f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = 'auto' )
    
    
    
    print(f"\033[92m\033[1m Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Split Into Training & Test Sets In a Stratified Manner, & Each Saved Into the 'Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' & 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' Files \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Tracking_Data_4_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  ):
    """
    Function That Reads the Training Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: training_shots_on_1_same_target_goal_df = Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    print('\n',
          f"Loading & Reading In the Training Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Dimensions of the Training Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Training Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Training Dataset  =  \033[91m\033[1m\033[4m{training_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Season    
    
    Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = training_shots_on_1_same_target_goal_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout This Training Dataset  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Season    
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout This Training Dataset  =  \033[91m\033[1m\033[4m{training_shots_on_1_same_target_goal_df.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
    sns.countplot(data = training_shots_on_1_same_target_goal_df, x = "Will_Be_a_Goal", edgecolor = "k")


    # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


    plt.title("Distribution of the Binary Target Variable \n In the Training Set")
    
    
    # Create custom legend
    
    import matplotlib.patches as mpatches
    
    legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                       mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
    plt.legend(handles = legend_patches, edgecolor = "k")



    plt.savefig("xG Model/xG EDA Figures/Training Distribution of the Binary Target Variable.png")

    plt.show()
    
    
    
    return training_shots_on_1_same_target_goal_df










def Read_Tracking_Data_4_Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  ):
    """
    Function That Reads the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: test_shots_on_1_same_target_goal_df = Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Test Dataset  =  \033[91m\033[1m\033[4m{test_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Season    
    
    Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = test_shots_on_1_same_target_goal_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout This Test Dataset  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Season    
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout This Test Dataset  =  \033[91m\033[1m\033[4m{test_shots_on_1_same_target_goal_df.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
    sns.countplot(data = test_shots_on_1_same_target_goal_df, x = "Will_Be_a_Goal", edgecolor = "k")


    # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


    plt.title("Distribution of the Binary Target Variable \n In the Test Set")
    
    
    # Create custom legend
    
    import matplotlib.patches as mpatches
    
    legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                       mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
    plt.legend(handles = legend_patches, edgecolor = "k")



    plt.savefig("xG Model/xG EDA Figures/Test Distribution of the Binary Target Variable.png")

    plt.show()
    
    
    
    return test_shots_on_1_same_target_goal_df









def Apply_Geometric_Y_Coordinate_and_Velocity_Component_Flipping_Transformation( df ):
    """
    Function that flips the Y-coordinates & the Y-velocity components of the ball and of all players to simulate shots from symmetrical positions
    
    """
    
    geometrically_y_transformed_data = df.copy()
    
    
    # Ball's Features
    
    geometrically_y_transformed_data["Y"] = -geometrically_y_transformed_data["Y"]      # Inverting Y - Ball's Y-Coordinate
    
    geometrically_y_transformed_data["V_yBall"] = -geometrically_y_transformed_data["V_yBall"]      # Inverting V_yBall - Ball's Y-Velocity Component
    
    
    
    # Players' Features
            
    for Player in range(1, 23):  # Players 1 --> 22
        
        geometrically_y_transformed_data[f"Y{Player}"] = -geometrically_y_transformed_data[f"Y{Player}"]      # Inverting Y1 --> Y22 - Players' Y-Coordinate
        
        geometrically_y_transformed_data[f"V_y{Player}"] = -geometrically_y_transformed_data[f"V_y{Player}"]      # Inverting V_y1 --> V_y22 - Players' Y-Velocity Component
    
    
    
    
    return geometrically_y_transformed_data










def Generate_Synthetic_Shots_Data( df, num_synthetic_samples, x_std = 100, y_std = 100, x_halfline = 0.0, x_max = 5250.0, y_min = -3400.0, y_max = 3400.0, random_seed = 42 ):
    """
    Function that generates synthetic shots data, preserving the class label distribution from the original data
    Hence, generates synthetic shots by varying "X" and "Y" coordinates of the ball of sampled shots, within specified ranges using the normal probability distribution:
          For the X-Coordinate:
                                - if the ball is closer than 20m away from the goal --> Synthetic X-Coordinate is generated using a Uniform Distribution with a STD of 1m (100cm)
                                - if the ball is 20m away from the goal or further away --> Synthetic X-Coordinate is generated using a Normal Distribution with a STD of 2m (200cm)
          For the Y-Coordinate: Always generated using a Normal Distribution with a STD of 1m (100cm)
    Also finds & updates the position of the closest player of the attacking team to the ball, moving its position right next to the ball
    The function sets a random seed to ensure reproducibility

    Input: df (DataFrame) = The DataFrame to use for generating synthetic data
    Input: num_synthetic_samples (int) = Number of synthetic samples to generate
    Input: x_std, y_std (int) = Standard Deviation (STD) of the Normal Distribution used to modify the 'X'- and 'Y'-Coordinates when generating the synthetic values - In [cm] ;  Default == {x_std = 100, y_std = 100}  (i.e. 1m)
    Input: x_halfline, x_max, y_min, y_max (float) = Boundaries for the 'X' and 'Y' coordinates to ensure they remain within the pitch;  Default == {x_halfline = 0.0, x_max = 5250.0, y_min = -3400.0, y_max = 3400.0}

    Output: synthetic_shots = A DataFrame containing the synthetic goals
    """
    
    np.random.seed(random_seed)  # Set the Random Seed For Reproducibility
    
    
    # Separate Original DataFrame Based On the Target Variable "Will_Be_a_Goal" Class Labels
    
    goals_df = df[ df["Will_Be_a_Goal"] == 1.0 ]
    
    non_goals_df = df[ df["Will_Be_a_Goal"] == 0.0 ]
    
    
    # Calculate the Proportion of Goals & Non-Goals - To Preserve the Class Label Distribution From the Original Data
    
    prop_goals = len(goals_df) / len(df)
    
    prop_non_goals = len(non_goals_df) / len(df)
    
    
    # Number of Synthetic Samples For Each Class Label
    
    num_goals_samples = int( num_synthetic_samples * prop_goals )
    
    num_non_goals_samples = num_synthetic_samples - num_goals_samples
    
    
    synthetic_shots_rows = []
    
    
    for df_subset, num_samples in [ (goals_df, num_goals_samples), (non_goals_df, num_non_goals_samples) ]:
    
        for _ in range(num_samples):
        
            # Randomly selecting a row (goal) to modify
        
            row_to_alter = df_subset.sample().copy()
        
        
            original_sampled_x = row_to_alter["X"].iloc[0]
        
        
            # Generate new 'X' coordinate
        
            if original_sampled_x <= 3250.0:   # i.e. 20 m  ≡  2000 cm  away from the goal or further away
            
                # Normal Distribution for "X"
            
                new_ball_x = np.random.normal( loc = original_sampled_x, scale = x_std )
            
        
            else:   # i.e. 20 m  ≡  2000 cm  away from the goal or closer
            
                # Normal Distribution for "X"
            
                new_ball_x = np.random.normal( loc = original_sampled_x, scale = x_std + 100 )   # x_std = 200
            

            # Normal Distribution for "Y"
        
            new_ball_y = np.random.normal( loc = row_to_alter["Y"].iloc[0], scale = y_std )
        
        
            # Ensuring the new coordinates are within the pitch boundaries
        
            new_ball_x = max( min(new_ball_x, x_max), x_halfline )
            new_ball_y = max( min(new_ball_y, y_max), y_min )
        
            row_to_alter["X"] = new_ball_x
            row_to_alter["Y"] = new_ball_y
        
        
            # Find the closest player of the attacking team to the ball
        
            ball_possession = row_to_alter["BallPossesion"].iloc[0]
        
            player_id_range = range(1, 12) if ball_possession == 1.0 else range(12, 23)
        
            closest_player, min_distance = None, float("inf")
        
        
            for player_id in player_id_range:
            
                player_x = row_to_alter[f"X{player_id}"].iloc[0]
            
                player_y = row_to_alter[f"Y{player_id}"].iloc[0]
        
                distance = TPD4MFs.Calculate_2D_Distance( new_ball_x, new_ball_y,
                                                          player_x, player_y )
            
            
                if distance < min_distance:
                
                    closest_player, min_distance = player_id, distance
                

            # Update the x-coordinate of the closest player
        
            if closest_player is not None:
            
                new_player_x = new_ball_x - 20  # New location to be 20 units less than the ball's x-coordinate
            
                row_to_alter[f"X{closest_player}"] = new_player_x
        
        
        
            # Append the modified row to the list
            
            synthetic_shots_rows.append(row_to_alter)
            

            
    # Concatenate all synthetic rows into a single DataFrame
    
    synthetic_shots = pd.concat( synthetic_shots_rows, ignore_index = True )
    
        

    
    return synthetic_shots










def Create_Augmented_Training_Shots_Dataset( original_training_shots_df, geometrically_transformed_shots_df, synthetically_generated_shots_df, random_seed = 42, file_path = "xG Model/Data For xG Model/Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" ):
    """
    Concatenates 3 DataFrames, shuffles the rows to distribute the class labels of "Will_Be_a_Goal", & saves the DataFrame to a parquet file

    Input: original_training_shots_df, geometrically_transformed_shots_df, synthetically_generated_shots_df (DataFrame) = DataFrames to be concatenated and shuffled
    Input: random_seed (int) = Random seed for reproducibility
    Input: file_path (str) = String of the exact file path and directory to which save the resulting DataFrame

    """
    
    # Concatenate the DataFrames
    
    augmented_training_df = pd.concat( [original_training_shots_df, geometrically_transformed_shots_df, synthetically_generated_shots_df], ignore_index = True )
    

    # Shuffle the DataFrame rows
    
    np.random.seed(random_seed)  # Set the random seed for reproducibility
    
    shuffled_augmented_training_df = augmented_training_df.sample( frac = 1, random_state = random_seed ).reset_index(drop = True)
    

    # Save the DataFrame to a parquet file
    
    shuffled_augmented_training_df.to_parquet(file_path, engine = 'auto')
    

    print(f"\033[92m\033[1m Augmented Training Data Concatenated & Randomly Shuffled  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Tracking_Data_4_Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  ):
    """
    Function That Reads the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: augmented_training_shots_on_1_same_target_goal_df = Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
    augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Augmented Training Dataset  =  \033[91m\033[1m\033[4m{augmented_training_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Augmented Training Dataset    
    
    Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = augmented_training_shots_on_1_same_target_goal_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout This Augmented Training Dataset  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Season    
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout This Augmented Training Dataset  =  \033[91m\033[1m\033[4m{augmented_training_shots_on_1_same_target_goal_df.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
    sns.countplot(data = augmented_training_shots_on_1_same_target_goal_df, x = "Will_Be_a_Goal", edgecolor = "k")


    # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


    plt.title("Distribution of the Binary Target Variable \n In the Augmented Training Set")
    
    
    # Create custom legend
    
    import matplotlib.patches as mpatches
    
    legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                       mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
    plt.legend(handles = legend_patches, edgecolor = "k")



    plt.savefig("xG Model/xG EDA Figures/Augmented Training Distribution of the Binary Target Variable.png")

    plt.show()
    
    
    
    return augmented_training_shots_on_1_same_target_goal_df










def Adding_Distances_and_Angles_Between_Ball_and_Target_Goal( to_training_or_test_data = "training" ):
    """
    Function That Adds New Columns To Either the Final Version of the Augmented Training or Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal:
            For the Ball:
                          - `Dist_Between_Ball_TargetGoal`, Which Represents the Distance Between the Ball & the Centre of the Target Goal (On the Right Side of the Pitch)
                          - `Angle_Between_Ball_TargetGoal_Rad`, Which Represents the Angle [rad] That the Ball "Sees" the Target Goal (On the Right Side of the Pitch)
                          - `Angle_Between_Ball_TargetGoal_Deg`, Which Represents the Angle [°] That the Ball "Sees" the Target Goal (On the Right Side of the Pitch)
                          
    Input: to_training_or_test_data (str) = String specifiying which set of data to apply this function in - training or test
    
    """
    
    # Constants
    
    Target_Goal_Width = 731.52
    
    Target_Goal_Centre_Coordinates = (5250, 0)
    
    
    
    if to_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
        
        
        
        # Compute Distances of the Ball To the Centre of the (Right) Target Goal
        
        augmented_training_shots_on_1_same_target_goal_df["Dist_Between_Ball_TargetGoal"] = TPD4MFs.Calculate_2D_Distance( x1 = augmented_training_shots_on_1_same_target_goal_df["X"], y1 = augmented_training_shots_on_1_same_target_goal_df["Y"],
                                                                                                                           x2 = Target_Goal_Centre_Coordinates[0], y2 = Target_Goal_Centre_Coordinates[1] )
    
    
    
            
        # Angle That the Ball "Sees" the (Right) Target Goal - In [rad]
    
        augmented_training_shots_on_1_same_target_goal_df["Angle_Between_Ball_TargetGoal_Rad"] = TPD4MFs.Calculate_Ball_Angle_To_TargetGoal( ball_x = augmented_training_shots_on_1_same_target_goal_df["X"],
                                                                                                                                             ball_y = augmented_training_shots_on_1_same_target_goal_df["Y"],
                                                                                                                                             target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Radians" )
    
    
        # Angle That the Ball "Sees" the (Right) Target Goal - In [deg] ≡ [°]
    
        augmented_training_shots_on_1_same_target_goal_df["Angle_Between_Ball_TargetGoal_Deg"] = TPD4MFs.Calculate_Ball_Angle_To_TargetGoal( ball_x = augmented_training_shots_on_1_same_target_goal_df["X"],
                                                                                                                                             ball_y = augmented_training_shots_on_1_same_target_goal_df["Y"],
                                                                                                                                             target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Degrees" )
        
    
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Augmented Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Augmented Training Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        augmented_training_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
    if to_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
        
        
        
        # Compute Distances of the Ball To the Centre of the (Right) Target Goal
        
        test_shots_on_1_same_target_goal_df["Dist_Between_Ball_TargetGoal"] = TPD4MFs.Calculate_2D_Distance( x1 = test_shots_on_1_same_target_goal_df["X"], y1 = test_shots_on_1_same_target_goal_df["Y"],
                                                                                                             x2 = Target_Goal_Centre_Coordinates[0], y2 = Target_Goal_Centre_Coordinates[1] )
    
    
    
            
        # Angle That the Ball "Sees" the (Right) Target Goal - In [rad]
    
        test_shots_on_1_same_target_goal_df["Angle_Between_Ball_TargetGoal_Rad"] = TPD4MFs.Calculate_Ball_Angle_To_TargetGoal( ball_x = test_shots_on_1_same_target_goal_df["X"], ball_y = test_shots_on_1_same_target_goal_df["Y"],
                                                                                                                               target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Radians" )
    
    
        # Angle That the Ball "Sees" the (Right) Target Goal - In [deg] ≡ [°]
    
        test_shots_on_1_same_target_goal_df["Angle_Between_Ball_TargetGoal_Deg"] = TPD4MFs.Calculate_Ball_Angle_To_TargetGoal( ball_x = test_shots_on_1_same_target_goal_df["X"], ball_y = test_shots_on_1_same_target_goal_df["Y"],
                                                                                                                               target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Degrees" )
        
    
    
    
        # Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Test TrackingData - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        test_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
    
    
    
    
    
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Adding_Distances_and_Angles_Between_Players_and_Target_Goal( to_training_or_test_data = "training" ):
    """
    Function That Adds New Columns To Either the Final Version of the Augmented Training or Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal:
            For the Players:
                          - `Dist_Between_1_TargetGoal` --> `Dist_Between_22_TargetGoal`, Which Represents the Distance Between the Players & the Centre of the Target Goal (On the Right Side of the Pitch)
                          - `Angle_Between_1_TargetGoal_Rad` --> `Angle_Between_22_TargetGoal_Rad`, Which Represents the Angle [rad] That the Players "See" the Target Goal (On the Right Side of the Pitch)
                          - `Angle_Between_1_TargetGoal_Deg` --> `Angle_Between_22_TargetGoal_Deg`, Which Represents the Angle [°] That the Players "See" the Target Goal (On the Right Side of the Pitch)
                          
    Input: to_training_or_test_data (str) = String specifiying which set of data to apply this function in - training or test
    
    """
    
    # Constants
    
    Target_Goal_Width = 731.52
    
    Target_Goal_Centre_Coordinates = (5250, 0)
    
    
    
    if to_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
        
        
        
        # Compute Distances of the Players To the Centre of the (Right) Target Goal
    
        for PlayerID in range(1, 23):
        
            augmented_training_shots_on_1_same_target_goal_df[f"Dist_Between_{PlayerID}_TargetGoal"] = TPD4MFs.Calculate_2D_Distance( x1 = augmented_training_shots_on_1_same_target_goal_df[f"X{PlayerID}"],
                                                                                                                                      y1 = augmented_training_shots_on_1_same_target_goal_df[f"Y{PlayerID}"],
                                                                                                                                      x2 = Target_Goal_Centre_Coordinates[0], y2 = Target_Goal_Centre_Coordinates[1] )
    
    
    
            
        # Angle That the Players "See" the (Right) Target Goal - In [rad]
    
        for PlayerID in range(1, 23):
    
            augmented_training_shots_on_1_same_target_goal_df[f"Angle_Between_{PlayerID}_TargetGoal_Rad"] = TPD4MFs.Calculate_Player_Angle_To_TargetGoal( player_x = augmented_training_shots_on_1_same_target_goal_df[f"X{PlayerID}"],
                                                                                                                                                          player_y = augmented_training_shots_on_1_same_target_goal_df[f"Y{PlayerID}"],
                                                                                                                                                          target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Radians" )
    
    
        # Angle That the Players "See" the (Right) Target Goal - In [deg] ≡ [°]
    
            augmented_training_shots_on_1_same_target_goal_df[f"Angle_Between_{PlayerID}_TargetGoal_Deg"] = TPD4MFs.Calculate_Player_Angle_To_TargetGoal( player_x = augmented_training_shots_on_1_same_target_goal_df[f"X{PlayerID}"],
                                                                                                                                                          player_y = augmented_training_shots_on_1_same_target_goal_df[f"Y{PlayerID}"],
                                                                                                                                                          target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Degrees" )
        
    
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Augmented Training Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        augmented_training_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
    if to_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
        
        
        
        # Compute Distances of the Players To the Centre of the (Right) Target Goal
    
        for PlayerID in range(1, 23):
        
            test_shots_on_1_same_target_goal_df[f"Dist_Between_{PlayerID}_TargetGoal"] = TPD4MFs.Calculate_2D_Distance( x1 = test_shots_on_1_same_target_goal_df[f"X{PlayerID}"],
                                                                                                                        y1 = test_shots_on_1_same_target_goal_df[f"Y{PlayerID}"],
                                                                                                                        x2 = Target_Goal_Centre_Coordinates[0], y2 = Target_Goal_Centre_Coordinates[1] )
    
    
    
            
        # Angle That the Players "See" the (Right) Target Goal - In [rad]
    
        for PlayerID in range(1, 23):
    
            test_shots_on_1_same_target_goal_df[f"Angle_Between_{PlayerID}_TargetGoal_Rad"] = TPD4MFs.Calculate_Player_Angle_To_TargetGoal( player_x = test_shots_on_1_same_target_goal_df[f"X{PlayerID}"],
                                                                                                                                            player_y = test_shots_on_1_same_target_goal_df[f"Y{PlayerID}"],
                                                                                                                                            target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Radians" )
    
    
        # Angle That the Players "See" the (Right) Target Goal - In [deg] ≡ [°]
    
            test_shots_on_1_same_target_goal_df[f"Angle_Between_{PlayerID}_TargetGoal_Deg"] = TPD4MFs.Calculate_Player_Angle_To_TargetGoal( player_x = test_shots_on_1_same_target_goal_df[f"X{PlayerID}"],
                                                                                                                                            player_y = test_shots_on_1_same_target_goal_df[f"Y{PlayerID}"],
                                                                                                                                            target_goal_width = Target_Goal_Width, angle_in_degrees_or_radians = "Degrees" )
        
    
    
    
        # Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Test Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        test_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Adding_Team_In_Possession_Binary_Indicator_For_Players_Columns( to_training_or_test_data = "training" ):
    """
    Function That Adds New Binary Columns To Either the Final Version of the Augmented Training or Test Tracking Data For All Models:
            To Indicate For Each Player Whether Their Team Was Currently In Possession of the Ball Or Not
                          
    Input: to_training_or_test_data (str) = String specifiying which set of data to apply this function in - training or test

    """
    
    if to_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
        

                
        for Player_ID in range(1, 23):
            
            if Player_ID <= 11:   # Home Team Players
                
                augmented_training_shots_on_1_same_target_goal_df[f"Team_In_Possession_{Player_ID}"] = augmented_training_shots_on_1_same_target_goal_df["BallPossesion"].apply(lambda Team_In_Possession: 1.0 if Team_In_Possession == 1.0 else 0.0)
            
            else:   # Away Team Players
                
                augmented_training_shots_on_1_same_target_goal_df[f"Team_In_Possession_{Player_ID}"] = augmented_training_shots_on_1_same_target_goal_df["BallPossesion"].apply(lambda Team_In_Possession: 1.0 if Team_In_Possession == 2.0 else 0.0)
            

        
        
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Augmented Training Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        augmented_training_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
    if to_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
        

        for Player_ID in range(1, 23):
            
            if Player_ID <= 11:   # Home Team Players
                
                test_shots_on_1_same_target_goal_df[f"Team_In_Possession_{Player_ID}"] = test_shots_on_1_same_target_goal_df["BallPossesion"].apply(lambda Team_In_Possession: 1.0 if Team_In_Possession == 1.0 else 0.0)
            
            else:   # Away Team Players
                
                test_shots_on_1_same_target_goal_df[f"Team_In_Possession_{Player_ID}"] = test_shots_on_1_same_target_goal_df["BallPossesion"].apply(lambda Team_In_Possession: 1.0 if Team_In_Possession == 2.0 else 0.0)
            

        
        
        # Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Test Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        test_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Calculate_3D_Distance(x1, y1, z1, x2, y2, z2):
    """
    Function That Calculates the 3D Euclidean Distance Between 2 Sets of 3D (x, y, z) Position Points
    
    Output = 3D Euclidean Distance
    """
    
    return np.sqrt( (x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2 )










def Adding_Distances_Between_Ball_and_Players( to_training_or_test_data = "training" ):
    """
    Function That Adds Several New Columns To Either the Final Version of the Augmented Training or Test Tracking Data For All Models:
            With Column Name Pattern `Dist_Between_Ball_{Player}`, Which Represents the Distance Between the Ball & All 22 Players On the Pitch
                          
    Input: to_training_or_test_data (str) = String specifiying which set of data to apply this function in - training or test
    
    """
    
    if to_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
        
    
    
        Distance_Between_Ball_and_Players_Columns = {}
    
    
        for Player in range(1, 23):  # All 22 Players
            
            Player_x, Player_y = f"X{Player}", f"Y{Player}"
            
            Distance_Between_Ball_and_Players_Columns[f"Dist_Between_Ball_{Player}"] = TPD4MFs.Calculate_3D_Distance( x1 = augmented_training_shots_on_1_same_target_goal_df["X"],
                                                                                                                      y1 = augmented_training_shots_on_1_same_target_goal_df["Y"],
                                                                                                                      z1 = augmented_training_shots_on_1_same_target_goal_df["Z"],
                                                                                                                      x2 = augmented_training_shots_on_1_same_target_goal_df[Player_x],
                                                                                                                      y2 = augmented_training_shots_on_1_same_target_goal_df[Player_y],
                                                                                                                      z2 = 0 )
            
    
                
        augmented_training_shots_on_1_same_target_goal_df = pd.concat( [ augmented_training_shots_on_1_same_target_goal_df, pd.DataFrame(Distance_Between_Ball_and_Players_Columns) ], axis = 1 )
        
        
        
        
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Augmented Training Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        augmented_training_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
    if to_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
        
    
    
        Distance_Between_Ball_and_Players_Columns = {}
    
    
        for Player in range(1, 23):  # All 22 Players
            
            Player_x, Player_y = f"X{Player}", f"Y{Player}"
            
            Distance_Between_Ball_and_Players_Columns[f"Dist_Between_Ball_{Player}"] = TPD4MFs.Calculate_3D_Distance( x1 = test_shots_on_1_same_target_goal_df["X"],
                                                                                                                      y1 = test_shots_on_1_same_target_goal_df["Y"],
                                                                                                                      z1 = test_shots_on_1_same_target_goal_df["Z"],
                                                                                                                      x2 = test_shots_on_1_same_target_goal_df[Player_x],
                                                                                                                      y2 = test_shots_on_1_same_target_goal_df[Player_y],
                                                                                                                      z2 = 0 )
            
    
                
        test_shots_on_1_same_target_goal_df = pd.concat( [ test_shots_on_1_same_target_goal_df, pd.DataFrame(Distance_Between_Ball_and_Players_Columns) ], axis = 1 )
        
        
        
        
        # Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Test Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        test_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')











def Adding_Distances_Between_Players_Themselves( to_training_or_test_data = "training" ):
    """
    Function That Adds Several New Columns To Either the Final Version of the Augmented Training or Test Tracking Data For All Models:
            With Column Name Pattern `Dist_Between_{Pair[0]}_{Pair[1]}`, Which Represents the Distance Between ALL 22 Players On the Pitch
                          
    Input: to_training_or_test_data (str) = String specifiying which set of data to apply this function in - training or test
    
    """
    
    if to_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
        
    
    
        Distance_Between_Players_Columns = {}
    
        
        for Pair in itertools.combinations(range(1, 23), 2):  # Pairs of All Players On the Pitch
                
            Col_1_x, Col_1_y = f"X{Pair[0]}", f"Y{Pair[0]}"
        
            Col_2_x, Col_2_y = f"X{Pair[1]}", f"Y{Pair[1]}"
        
                
            Distance_Between_Players_Columns[f"Dist_Between_{Pair[0]}_{Pair[1]}"] = TPD4MFs.Calculate_2D_Distance( x1 = augmented_training_shots_on_1_same_target_goal_df[Col_1_x], y1 = augmented_training_shots_on_1_same_target_goal_df[Col_1_y],
                                                                                                                   x2 = augmented_training_shots_on_1_same_target_goal_df[Col_2_x], y2 = augmented_training_shots_on_1_same_target_goal_df[Col_2_y] )
        
        
        augmented_training_shots_on_1_same_target_goal_df = pd.concat( [ augmented_training_shots_on_1_same_target_goal_df, pd.DataFrame(Distance_Between_Players_Columns) ], axis = 1 )
    
        
        
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Augmented Training Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        augmented_training_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
    if to_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
        
    
    
        Distance_Between_Players_Columns = {}
    
        
        for Pair in itertools.combinations(range(1, 23), 2):  # Pairs of All Players On the Pitch
                
            Col_1_x, Col_1_y = f"X{Pair[0]}", f"Y{Pair[0]}"
        
            Col_2_x, Col_2_y = f"X{Pair[1]}", f"Y{Pair[1]}"
        
                
            Distance_Between_Players_Columns[f"Dist_Between_{Pair[0]}_{Pair[1]}"] = TPD4MFs.Calculate_2D_Distance( x1 = test_shots_on_1_same_target_goal_df[Col_1_x], y1 = test_shots_on_1_same_target_goal_df[Col_1_y],
                                                                                                                   x2 = test_shots_on_1_same_target_goal_df[Col_2_x], y2 = test_shots_on_1_same_target_goal_df[Col_2_y] )
        
        
        test_shots_on_1_same_target_goal_df = pd.concat( [ test_shots_on_1_same_target_goal_df, pd.DataFrame(Distance_Between_Players_Columns) ], axis = 1 )
    
        
        
        # Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Test Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        test_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Adding_Same_Team_Binary_Indicator_Columns( to_training_or_test_data = "training" ):
    """
    Function That Adds New Binary Columns To Either the Final Version of the Augmented Training or Test Tracking Data For All Models:
            To Indicate Whether Edges Connect Players of the Same Team Or Not
                          
    Input: to_training_or_test_data (str) = String specifiying which set of data to apply this function in - training or test

    """
    
    if to_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
        

        for Pair in itertools.combinations( range(1, 23), 2 ):   # Pairs of All Players On the Pitch
            
            
            # Initialize the Same_Team_Flag to 0 (Assuming Different Teams)
            
            Same_Team_Flag = 0.0
            
            
            # Check If Players Are From the Same Team
            
            if (Pair[0] >= 1 and Pair[0] <= 11) and (Pair[1] >= 1 and Pair[1] <= 11):   # Pairs of Players of the Home Team
                
                Same_Team_Flag = 1.0
                
            
            elif (Pair[0] >= 12 and Pair[0] <= 22) and (Pair[1] >= 12 and Pair[1] <= 22):   # Pairs of Players of the Away Team
                
                Same_Team_Flag = 1.0
                

            # Add New Columns To the DataFrame
            
            augmented_training_shots_on_1_same_target_goal_df[f"Same_Team_{Pair[0]}_{Pair[1]}"] = Same_Team_Flag
            

        
        
        # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Augmented Training Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        augmented_training_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
    if to_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
        # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
        

        for Pair in itertools.combinations( range(1, 23), 2 ):   # Pairs of All Players On the Pitch
            
            
            # Initialize the Same_Team_Flag to 0 (Assuming Different Teams)
            
            Same_Team_Flag = 0.0
            
            
            # Check If Players Are From the Same Team
            
            if (Pair[0] >= 1 and Pair[0] <= 11) and (Pair[1] >= 1 and Pair[1] <= 11):   # Pairs of Players of the Home Team
                
                Same_Team_Flag = 1.0
                
            
            elif (Pair[0] >= 12 and Pair[0] <= 22) and (Pair[1] >= 12 and Pair[1] <= 22):   # Pairs of Players of the Away Team
                
                Same_Team_Flag = 1.0
                

            # Add New Columns To the DataFrame
            
            test_shots_on_1_same_target_goal_df[f"Same_Team_{Pair[0]}_{Pair[1]}"] = Same_Team_Flag
            

        
        
        # Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    
    
        # Save Final Version of the Test Tracking Data - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet" File
    
        test_shots_on_1_same_target_goal_df.to_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
        
        
        
        print(f"\033[92m\033[1m Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet' File \033[0m", '\n')
        
        
        
        
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Filter_Relevant_Data_4_xG_Model( from_training_or_test_data = "training" ):
    """
    Function that filters only the releveant data/features for the xG model
    
    """
    
    xG_Model_Relevant_Columns = ["X", "Y", "Dist_Between_Ball_TargetGoal", "Angle_Between_Ball_TargetGoal_Rad", "Will_Be_a_Goal"]
    
    
    
    if from_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        Relevant_Data_4_xG_Model = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto", columns = xG_Model_Relevant_Columns)
    
    
        # Dimensions of the Relevant Data of the Augmented Training Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Relevant Data of the Augmented Training Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {Relevant_Data_4_xG_Model.shape}", '\n')
    
        print(f"∴ The Total Number of Shots Taken Throughout the Augmented Training Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0]}\033[0m", '\n')
    
    
        # Counting Total Number of Goals Scored Throughout the Augmented Training Dataset Relevant For the xG Model
    
        Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = Relevant_Data_4_xG_Model )
    
        print(f"∴ The Total Number of Goals Scored Throughout the Augmented Training Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
        # Counting Total Number of Non-Scored Shots Throughout the Augmented Training Dataset Relevant For the xG Model
    
        print(f"∴ The Total Number of Non-Scored Shots Throughout the Augmented Training Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    
        # Save Final Version of the Augmented Training Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Augmented_Training_Relevant_Data_4_xG_Model.parquet" File
    
        Relevant_Data_4_xG_Model.to_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Relevant_Data_4_xG_Model.parquet", engine = "auto")


        print(f"\033[92m\033[1m Final Version of the Augmented Training Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Saved In the 'Augmented_Training_Relevant_Data_4_xG_Model.parquet' File \033[0m", '\n')
        
        
    
    
    
    if from_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        Relevant_Data_4_xG_Model = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto", columns = xG_Model_Relevant_Columns)
    
    
        # Dimensions of the Relevant Data of the Test Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Relevant Data of the Test Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {Relevant_Data_4_xG_Model.shape}", '\n')
    
        print(f"∴ The Total Number of Shots Taken Throughout the Test Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0]}\033[0m", '\n')
    
    
        # Counting Total Number of Goals Scored Throughout the Test Dataset Relevant For the xG Model
    
        Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = Relevant_Data_4_xG_Model )
    
        print(f"∴ The Total Number of Goals Scored Throughout the Test Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
        # Counting Total Number of Non-Scored Shots Throughout the Test Dataset Relevant For the xG Model
    
        print(f"∴ The Total Number of Non-Scored Shots Throughout the Test Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    
        # Save Final Version of the Test Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal As a New "Test_Relevant_Data_4_xG_Model.parquet" File
    
        Relevant_Data_4_xG_Model.to_parquet(f"{xG_Model_Data_Folder}Test_Relevant_Data_4_xG_Model.parquet", engine = "auto")


        print(f"\033[92m\033[1m Final Version of the Test Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal  -->  Succesfully Saved In the 'Test_Relevant_Data_4_xG_Model.parquet' File \033[0m", '\n')
        
    
    
    
    
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Relevant_Tracking_Data_4_xG_Model( from_training_or_test_data = "training" ):
    """
    Function That Reads the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: Relevant_Data_4_xG_Model = Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    if from_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        Relevant_Data_4_xG_Model = pd.read_parquet(f"{xG_Model_Data_Folder}Augmented_Training_Relevant_Data_4_xG_Model.parquet", engine = "auto")
    
    
        # Dimensions of the Relevant Data of the Augmented Training Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Relevant Data of the Augmented Training Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {Relevant_Data_4_xG_Model.shape}", '\n')
    
        print(f"∴ The Total Number of Shots Taken Throughout the Augmented Training Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0]}\033[0m", '\n')
    
    
        # Counting Total Number of Goals Scored Throughout the Augmented Training Dataset Relevant For the xG Model
    
        Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = Relevant_Data_4_xG_Model )
    
        print(f"∴ The Total Number of Goals Scored Throughout the Augmented Training Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
        # Counting Total Number of Non-Scored Shots Throughout the Augmented Training Dataset Relevant For the xG Model
    
        print(f"∴ The Total Number of Non-Scored Shots Throughout the Augmented Training Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
        # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
        sns.countplot(data = Relevant_Data_4_xG_Model, x = "Will_Be_a_Goal", edgecolor = "k")


        # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


        plt.title("Distribution of the Binary Target Variable \n In the Augmented Training Set Relevent To the xG Model")
    
    
        # Create custom legend
    
        import matplotlib.patches as mpatches
    
        legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                           mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
        plt.legend(handles = legend_patches, edgecolor = "k")

    

        plt.show()
        
        
        
        
        
    if from_training_or_test_data == "test":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Test Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"xG Model/Data For xG Model/"
    
        Relevant_Data_4_xG_Model = pd.read_parquet(f"{xG_Model_Data_Folder}Test_Relevant_Data_4_xG_Model.parquet", engine = "auto")
    
    
        # Dimensions of the Relevant Data of the Test Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

        print(f"Dimensions of the Relevant Data of the Test Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {Relevant_Data_4_xG_Model.shape}", '\n')
    
        print(f"∴ The Total Number of Shots Taken Throughout the Test Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0]}\033[0m", '\n')
    
    
        # Counting Total Number of Goals Scored Throughout the Test Dataset Relevant For the xG Model
    
        Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = Relevant_Data_4_xG_Model )
    
        print(f"∴ The Total Number of Goals Scored Throughout the Test Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
        # Counting Total Number of Non-Scored Shots Throughout the Test Dataset Relevant For the xG Model
    
        print(f"∴ The Total Number of Non-Scored Shots Throughout the Test Dataset Relevant For the xG Model  =  \033[91m\033[1m\033[4m{Relevant_Data_4_xG_Model.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
        
        
        
        # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
        sns.countplot(data = Relevant_Data_4_xG_Model, x = "Will_Be_a_Goal", edgecolor = "k")


        # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


        plt.title("Distribution of the Binary Target Variable \n In the Test Set Relevent To the xG Model")
    
    
        # Create custom legend
    
        import matplotlib.patches as mpatches
    
        legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                           mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
        plt.legend(handles = legend_patches, edgecolor = "k")

    

        plt.show()
    
    
    
    return Relevant_Data_4_xG_Model







####################################################################################################################################################################################
####################################################################################################################################################################################







def Data_Preprocessing_Pipeline_4_PyG_GNN_Models( preprocess_training_or_test_data, numerical_features_to_scale, categorical_features = None, features_to_drop = ["BallPossesion", "Section", "Match_Minute_Clock", "Match_Seconds_Clock"], target_variable = ["Will_Be_a_Goal"] ):
    """
    Function That Implements a (Numerical & Categorical) Data-Preprocessing Pipeline:
                                                                                        1) Performing Max Absolute (MaxAbs) Scaling On the Specified Numerical Columns
                                                                                            i) [-1, 1] Range For Columns With -ve & +ve Values
                                                                                           ii) [-1, 0] Range For Columns Which Only Have -ve Values (<0)
                                                                                          iii) [0, 1] Range For Columns Which Only Have +ve Values (>0)
                                                                                        2) Performing 1-Hot-Encoding of the "Section" Feature + Rename the 1-Hot-Encoded "Section_1.0" Column To "is_1st_Half"
                                                                                        3) Drop All the Angle "_Deg" Columns & the "BallPossesion" + "Section_2.0" Columns
                                                                                        4) Places the Target Variable Column At the Right-End of the Resulting DataFrame
                                                                                        5) Re-Convert the Array of Preprocessed Data Into a DataFrame
                                                                                        6) Save PyG GNN Models Data In the "PyG DataFrame-Format Data" Folder
    
    Input: preprocess_training_or_test_data = String Stating Whether To Preprocess the Training or Test Data;  Options == {"training", "test"}
    Input: numerical_features_to_scale = List of Column Names of Numerical Variables With -ve & +ve Values That Should Be Preprocessed
    Input: categorical_features = List of String(s) of Column Name(s) of Categorical Variable(s) That Should Be Preprocessed
    Input: features_to_drop = List of String(s) of Column Name(s) of Features That Should Be Dropped
    Input: target_variable = List of 1 String of the Column Name of the Target Variable

    """
                    
    Data_Is_Augmented_Training_or_Test = "Augmented Training" if preprocess_training_or_test_data == "training" else "Test"
    
    print('\n',
          f"Loading & Reading In the \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    Simple_PyG_GNN_Model_DataFrame_Data_Folder = f"Simple GNN Model/PyG DataFrame-Format Data/"
    
    File_Name_Prefix = "Augmented_Training" if preprocess_training_or_test_data == "training" else "Test"
    
    Shots_On_1_Same_Target_Goal_df = pd.read_parquet( f"{Simple_PyG_GNN_Model_DataFrame_Data_Folder}{File_Name_Prefix}_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet",
                                                      engine = "auto" )
    
    
    
    
    # Dimensions of the Dataset of the Tracking Data 

    print(f"Dimensions of the \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal = {Shots_On_1_Same_Target_Goal_df.shape}",
          '\n')
        
    
    # Drop Angle Columns Measured In Degrees (i.e. COlumn Names Ending With "_Deg")
    
    Angle_Deg_Columns_To_Drop = [ Column for Column in Shots_On_1_Same_Target_Goal_df.columns if Column.endswith("_Deg") ]
    
    Shots_On_1_Same_Target_Goal_df.drop( columns = Angle_Deg_Columns_To_Drop, inplace = True )
    
    
        
    # Drop the "BallPossesion" Column
    
    Shots_On_1_Same_Target_Goal_df.drop( columns = features_to_drop, inplace = True )
        
        
                
    # Define the Data Transformers For the Numerical & Categorical Features
        
    Numerical_Data_Max_Abs_Transformer = MaxAbsScaler( copy = True )   # If Both -ve & +ve Values Are Present, the Range Is [-1, 1]
                                                                       # If Only -ve Values Are Present, the Range Is [-1, 0]
                                                                       # If Only +ve Values Are Present, the Range Is [0, 1]
        
    Categorical_Data_Transformer = OneHotEncoder( sparse_output = False )
        
        

    # Create a Column Transformer That Will Apply the Different Transformers To the Specified Features
    
    if categorical_features == None:
        
        Data_Preprocessor = ColumnTransformer( transformers = [ ("MaxAbs", Numerical_Data_Max_Abs_Transformer, numerical_features_to_scale) ],
                                               remainder = "passthrough",   # Leaves Other (Remaining) Columns Untouched
                                               verbose_feature_names_out = True )
    
    else:
        
        Data_Preprocessor = ColumnTransformer( transformers = [ ("MaxAbs", Numerical_Data_Max_Abs_Transformer, numerical_features_to_scale),
                                                                ("Categorical", Categorical_Data_Transformer, categorical_features) ],
                                               remainder = "passthrough",   # Leaves Other (Remaining) Columns Untouched
                                               verbose_feature_names_out = True )
        

    # Apply the Transformations
        
    Data_array = Data_Preprocessor.fit_transform( Shots_On_1_Same_Target_Goal_df )
        
        
        
    # Extracting the New Column Names Created/Assigned By the `ColumnTransformer( )` & Cleaning Them So That They Can Be Re-Used As the New Column Names of the New DataFrame
        
    Transformer_Names_Prefixes_List = ["MaxAbs__", "Categorical__", "remainder__"]

    Cleaned_Column_Names = [ Column.replace(Prefix, "") for Column in Data_Preprocessor.get_feature_names_out(input_features = None) for Prefix in Transformer_Names_Prefixes_List if Prefix in Column ]

        

        
    # Create a DataFrame From the Transformed Data
        
    Preprocessed_Shots_On_1_Same_Target_Goal_df = pd.DataFrame( data = Data_array, columns = Cleaned_Column_Names )
    
    
    
    # Rename the "Section_1.0" Column To "is_1st_Half"
    
    if "Section_1.0" in Preprocessed_Shots_On_1_Same_Target_Goal_df.columns:
        
        Preprocessed_Shots_On_1_Same_Target_Goal_df.rename( columns = { "Section_1.0" : "is_1st_Half" }, inplace = True )
        

    # Drop the "Section_2.0" Column
    
    if "Section_2.0" in Preprocessed_Shots_On_1_Same_Target_Goal_df.columns:
        
        Preprocessed_Shots_On_1_Same_Target_Goal_df.drop( columns = ["Section_2.0"], inplace = True )
        
        
        
        
    # Move Specified Target Variable Column To the Right-End of the DataFrame            
            
    Columns = [Column for Column in Preprocessed_Shots_On_1_Same_Target_Goal_df.columns if Column not in target_variable] + target_variable
        
    Preprocessed_Shots_On_1_Same_Target_Goal_df = Preprocessed_Shots_On_1_Same_Target_Goal_df[Columns]

        
        
        
    # Dimensions of the Dataset of the Tracking Data
    
    print(f"Final Dimensions of the Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal = {Preprocessed_Shots_On_1_Same_Target_Goal_df.shape}", '\n')
            
            
            
                
    # Save Final Preprocessed Version of the Tracking Data For the PyG GNN Models As a New {File_Name_Prefix}_Shots_Frames_On_1_Same_Target_Goal_4_All_Models-Preprocessed.parquet" File
        
    Preprocessed_Shots_On_1_Same_Target_Goal_df.to_parquet(f"{Simple_PyG_GNN_Model_DataFrame_Data_Folder}{File_Name_Prefix}_Shots_Frames_On_1_Same_Target_Goal_4_All_Models-Preprocessed.parquet", engine = "auto")
    
    
    
    Complex_PyG_GNN_Model_DataFrame_Data_Folder = f"Complex GNN Model/PyG DataFrame-Format Data/"
    
    Preprocessed_Shots_On_1_Same_Target_Goal_df.to_parquet(f"{Complex_PyG_GNN_Model_DataFrame_Data_Folder}{File_Name_Prefix}_Shots_Frames_On_1_Same_Target_Goal_4_All_Models-Preprocessed.parquet", engine = "auto")
        
        
        
    print(f"\033[92m\033[1m Final Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m \033[92m\033[1mTracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  -->  Succesfully Saved In the Folders 'PyG DataFrame-Format Data' \033[0m", '\n')
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
                
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Preprocessed_Tracking_Data_4_PyG_GNN_Models( training_or_test_data ):
    """
    Function That Reads the Preprocessed Version of the Augmented Training or Test Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
    Input: training_or_test_data (str) = Whether To Read the Preprocessed Augmented Training or Test Tacking Data;  Options == {"training", "test"}
            
    Output: preprocessed_shots_on_1_same_target_goal_df = Preprocessed Version of the Augmented Training or Test Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    """
    
    Data_Is_Augmented_Training_or_Test = "Augmented Training" if training_or_test_data == "training" else "Test"
    
    print('\n',
          f"Loading & Reading In the Preprocessed Version of the \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    Simple_PyG_GNN_Model_DataFrame_Data_Folder = f"Simple GNN Model/PyG DataFrame-Format Data/"
    
    File_Name_Prefix = "Augmented_Training" if training_or_test_data == "training" else "Test"
    
    preprocessed_shots_on_1_same_target_goal_df = pd.read_parquet(f"{Simple_PyG_GNN_Model_DataFrame_Data_Folder}{File_Name_Prefix}_Shots_Frames_On_1_Same_Target_Goal_4_All_Models-Preprocessed.parquet", engine = "auto")
    
    
    # Dimensions of the Preprocessed Version of the Augmented Training or Test Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Preprocessed Version of the \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {preprocessed_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Dataset  =  \033[91m\033[1m\033[4m{preprocessed_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Preprocessed Dataset    
    
    Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = preprocessed_shots_on_1_same_target_goal_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout This Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Dataset  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Preprocessed Dataset   
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout This Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Dataset  =  \033[91m\033[1m\033[4m{preprocessed_shots_on_1_same_target_goal_df.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
    sns.countplot(data = preprocessed_shots_on_1_same_target_goal_df, x = "Will_Be_a_Goal", edgecolor = "k")


    # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


    plt.title(f"Distribution of the Binary Target Variable \n In the {Data_Is_Augmented_Training_or_Test} Set")
    
    
    # Create custom legend
    
    import matplotlib.patches as mpatches
    
    legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                       mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
    plt.legend(handles = legend_patches, edgecolor = "k")


    plt.show()
    
    
    
    return preprocessed_shots_on_1_same_target_goal_df










def Browse_and_Select_Reading_Preprocessed_Tracking_Data_4_PyG_GNN_Models( training_or_test_data ):
    """
    Function That Reads a Selected `.parquet` File Using File-Dialog/Explorer To Browse For the Preprocessed Version of the Augmented Training or Test Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
    Input: training_or_test_data (str) = Whether To Read the Preprocessed Augmented Training or Test Tacking Data;  Options == {"training", "test"}
            
    Output: preprocessed_shots_on_1_same_target_goal_df = Preprocessed Version of the Augmented Training or Test Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    """
    
    Data_Is_Augmented_Training_or_Test = "Augmented Training" if training_or_test_data == "training" else "Test"
    
    print('\n',
          f"Loading & Reading In the Preprocessed Version of the \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    # Initialize Tkinter + Hide the Main Window
    
    Root = tk.Tk()   # Initialize Tkinter
    
    Root.withdraw()   # Hide the Main Window
    

    # Open File-Dialog/Explorer To Select a `.parquet` File
    
    File_Path = filedialog.askopenfilename( title = f"Select the {Data_Is_Augmented_Training_or_Test} `.parquet` File", filetypes = [ ("Parquet Files", "*.parquet") ] )
    
    if not File_Path:  # If No Appropriate File Is Selected
        
        print("No File Was Selected")
        
        return None
    
    
    preprocessed_shots_on_1_same_target_goal_df = pd.read_parquet( File_Path, engine = "auto" )
    
    
    
    # Dimensions of the Preprocessed Version of the Augmented Training or Test Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Preprocessed Version of the \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Tracking Data For the PyG GNN Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {preprocessed_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Dataset  =  \033[91m\033[1m\033[4m{preprocessed_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Preprocessed Dataset    
    
    Total_Goals_Scored_Throughout_Dataset = TPD4MFs.Count_Total_Goals_Scored( df = preprocessed_shots_on_1_same_target_goal_df )
    
    print(f"∴ The Total Number of Goals Scored Throughout This Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Dataset  =  \033[91m\033[1m\033[4m{Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Counting Total Number of Non-Scored Shots Throughout the Preprocessed Dataset   
    
    print(f"∴ The Total Number of Non-Scored Shots Throughout This Preprocessed \033[91m\033[1m\033[4m{Data_Is_Augmented_Training_or_Test}\033[0m Dataset  =  \033[91m\033[1m\033[4m{preprocessed_shots_on_1_same_target_goal_df.shape[0] - Total_Goals_Scored_Throughout_Dataset}\033[0m", '\n')
    
    
    # Plot Count-Plot of the Number of Goals & Non-Scored Shots
    
    sns.countplot(data = preprocessed_shots_on_1_same_target_goal_df, x = "Will_Be_a_Goal", edgecolor = "k")


    # Will_Be_a_Goal = Forecasts/Predicts Whether the Shot Will Be a Goal Or Not At the Moment of the Shot


    plt.title(f"Distribution of the Binary Target Variable \n In the {Data_Is_Augmented_Training_or_Test} Set")
    
    
    # Create custom legend
    
    import matplotlib.patches as mpatches
    
    legend_patches = [ mpatches.Patch( color = sns.color_palette()[0], label = "Non-Scored Shots" ),
                       mpatches.Patch( color = sns.color_palette()[1], label = "Scored Shots" ) ]
    
    plt.legend(handles = legend_patches, edgecolor = "k")


    plt.show()
    
    
    
    return preprocessed_shots_on_1_same_target_goal_df




