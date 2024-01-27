import tkinter as tk
from tkinter import filedialog

import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)

import matplotlib.pyplot as plt





def Browse_Appropriate_Hold_Out_Test_Dataset_File(  ):
    """
    Function to browse and select .csv files for HGT and xG models' predictions, and .parquet file for test dataset. 
    It then filters the test dataset based on the largest discrepancies in predicted probabilities between the two models for the minority class.
    
    Input: top_K_discrepancies (int) = Integer Stating the Top "K" Discrepancies To Show
            
    Output: DataFrame with filtered rows based on specified conditions.
    """
        
    print('\n',
          "Select the (Un-Preprocessed) Hold-Out Test `.parquet` File",
          '\n')
    
    # Initialize Tkinter + Hide the Main Window
    Root = tk.Tk()   # Initialize Tkinter
    Root.withdraw()  # Hide the Main Window
    
    # Open File-Dialog/Explorer To Select Files
    Test_Data_Parquet_File_Path = filedialog.askopenfilename( title = "Select the (Un-Preprocessed) Hold-Out Test `.parquet` File", filetypes = [("Parquet Files", "*.parquet")] )
    
    # Read Files into DataFrames
    Test_Data_df = pd.read_parquet(Test_Data_Parquet_File_Path, engine = "auto")
    
    return Test_Data_df










def Browse_Appropriate_Files_and_Extract_Shot_Frames_With_Largest_Discrepancy_Between_Models_Predicting_Goals( top_K_discrepancies = 5 ):
    """
    Function to browse and select .csv files for HGT and xG models' predictions, and .parquet file for test dataset.
    It then filters the test dataset based on the largest discrepancies in predicted probabilities between the two models for the minority class.
    
    Input: top_K_discrepancies (int) = Integer Stating the Top "K" Discrepancies To Show
            
    Output: DataFrame with filtered rows based on specified conditions.
    """

    print("\n", "Select the (Un-Preprocessed) Hold-Out Test `.parquet` File and the `.csv` Files for the HGT & xG Models", "\n")

    # Initialize Tkinter + Hide the Main Window
    Root = tk.Tk()
    Root.withdraw()

    # Open File-Dialog/Explorer To Select Files
    Test_Data_Parquet_File_Path = filedialog.askopenfilename(title="Select the (Un-Preprocessed) Hold-Out Test `.parquet` File", filetypes=[("Parquet Files", "*.parquet")])
    HGT_CSV_File_Path = filedialog.askopenfilename(title="Select the HGT Model's `.csv` File Containing its Predicted Probabilities On the Hold-Out Test Dataset", filetypes=[("CSV Files", "*.csv")])
    XG_CSV_File_Path = filedialog.askopenfilename(title="Select the xG Model's `.csv` File Containing its Predicted Probabilities On the Hold-Out Test Dataset", filetypes=[("CSV Files", "*.csv")])

    if not all([Test_Data_Parquet_File_Path, HGT_CSV_File_Path, XG_CSV_File_Path]):
        print("All Required Files Were Not Selected - Please Try Again.")
        return None

    # Read Files into DataFrames
    Test_Data_df = pd.read_parquet(Test_Data_Parquet_File_Path, engine="auto")
    HGT_Predicted_Probabilities_df = pd.read_csv(HGT_CSV_File_Path)
    xG_Predicted_Probabilities_df = pd.read_csv(XG_CSV_File_Path)

    # Merge DataFrames
    merged_df = Test_Data_df.merge(HGT_Predicted_Probabilities_df, left_index=True, right_index=True)
    merged_df = merged_df.merge(xG_Predicted_Probabilities_df, left_index=True, right_index=True)

    # Filter Rows
    filtered_df = merged_df[(merged_df["Will_Be_a_Goal"] == 1.0) & 
                            (merged_df["Complex HGT Model Test Predicted/Classified Class Labels"] == 1.0) & 
                            (merged_df["xG Model Test Predicted/Classified Class Labels"] == 0.0)]

    # Finding rows where HGT probability is as large as possible and xG probability is also as large as possible
    filtered_df["Combined_Probability"] = filtered_df["Complex HGT Model Test Class Labels' Predicted Probabilities"] + filtered_df["xG Model Test Class Labels' Predicted Probabilities"]

    top_K_discrepancies_df = filtered_df.nlargest(top_K_discrepancies, "Combined_Probability")

    return top_K_discrepancies_df[ [ "Will_Be_a_Goal",
                                    "Complex HGT Model Test Class Labels' Predicted Probabilities", "Complex HGT Model Test Predicted/Classified Class Labels",
                                    "xG Model Test Class Labels' Predicted Probabilities", "xG Model Test Predicted/Classified Class Labels"] \
                                   + [col for col in Test_Data_df.columns if col != "Will_Be_a_Goal"] ]










def Browse_Appropriate_Files_and_Extract_Shot_Frames_With_Largest_Discrepancy_Between_Models_Predicting_Goals_2( top_K_discrepancies = 5 ):
    """
    Function to browse and select .csv files for HGT and xG models' predictions, and .parquet file for test dataset.
    It then filters the test dataset based on the largest discrepancies in predicted probabilities between the two models for the minority class.
    
    Input: top_K_discrepancies (int) = Integer Stating the Top "K" Discrepancies To Show
            
    Output: DataFrame with filtered rows based on specified conditions.
    """

    print("\n", "Select the (Un-Preprocessed) Hold-Out Test `.parquet` File and the `.csv` Files for the HGT & xG Models", "\n")

    # Initialize Tkinter + Hide the Main Window
    Root = tk.Tk()
    Root.withdraw()

    # Open File-Dialog/Explorer To Select Files
    Test_Data_Parquet_File_Path = filedialog.askopenfilename(title="Select the (Un-Preprocessed) Hold-Out Test `.parquet` File", filetypes=[("Parquet Files", "*.parquet")])
    HGT_CSV_File_Path = filedialog.askopenfilename(title="Select the HGT Model's `.csv` File Containing its Predicted Probabilities On the Hold-Out Test Dataset", filetypes=[("CSV Files", "*.csv")])
    XG_CSV_File_Path = filedialog.askopenfilename(title="Select the xG Model's `.csv` File Containing its Predicted Probabilities On the Hold-Out Test Dataset", filetypes=[("CSV Files", "*.csv")])

    if not all([Test_Data_Parquet_File_Path, HGT_CSV_File_Path, XG_CSV_File_Path]):
        print("All Required Files Were Not Selected - Please Try Again.")
        return None

    # Read Files into DataFrames
    Test_Data_df = pd.read_parquet(Test_Data_Parquet_File_Path, engine="auto")
    HGT_Predicted_Probabilities_df = pd.read_csv(HGT_CSV_File_Path)
    xG_Predicted_Probabilities_df = pd.read_csv(XG_CSV_File_Path)

    # Merge DataFrames
    merged_df = Test_Data_df.merge(HGT_Predicted_Probabilities_df, left_index=True, right_index=True)
    merged_df = merged_df.merge(xG_Predicted_Probabilities_df, left_index=True, right_index=True)

    # Filter Rows
    filtered_df = merged_df[(merged_df["Will_Be_a_Goal"] == 1.0) & 
                            (merged_df["Complex HGT Model Test Predicted/Classified Class Labels"] == 1.0) & 
                            (merged_df["xG Model Test Predicted/Classified Class Labels"] == 0.0) &
                            (merged_df["Complex HGT Model Test Class Labels' Predicted Probabilities"] > merged_df["xG Model Test Class Labels' Predicted Probabilities"]) ]

    # Find Top 5 Discrepancies
    filtered_df["Probability_Difference"] = abs( filtered_df["Complex HGT Model Test Class Labels' Predicted Probabilities"] - filtered_df["xG Model Test Class Labels' Predicted Probabilities"] )
    
    top_K_discrepancies_df = filtered_df.nlargest( top_K_discrepancies, "Probability_Difference" )
    

    return top_K_discrepancies_df[ [ "Will_Be_a_Goal",
                                     "Complex HGT Model Test Class Labels' Predicted Probabilities", "Complex HGT Model Test Predicted/Classified Class Labels",
                                     "xG Model Test Class Labels' Predicted Probabilities", "xG Model Test Predicted/Classified Class Labels",
                                     "Probability_Difference" ] + [col for col in Test_Data_df.columns if col != "Will_Be_a_Goal"] ]










def Browse_Appropriate_Files_and_Extract_Shot_Frames_With_Largest_Discrepancy_Between_Models_Predicting_Goals_3( top_K_discrepancies = 5 ):
    """
    Function to browse and select .csv files for HGT and xG models' predictions, and .parquet file for test dataset. 
    It then filters the test dataset based on the largest discrepancies in predicted probabilities between the two models for the minority class.
    
    Input: top_K_discrepancies (int) = Integer Stating the Top "K" Discrepancies To Show
            
    Output: DataFrame with filtered rows based on specified conditions.
    """
        
    print('\n',
          "Select the (Un-Preprocessed) Hold-Out Test `.parquet` File and the `.csv` Files for the HGT & xG Models",
          '\n')
    
    # Initialize Tkinter + Hide the Main Window
    Root = tk.Tk()   # Initialize Tkinter
    Root.withdraw()  # Hide the Main Window
    
    # Open File-Dialog/Explorer To Select Files
    Test_Data_Parquet_File_Path = filedialog.askopenfilename( title = "Select the (Un-Preprocessed) Hold-Out Test `.parquet` File", filetypes = [("Parquet Files", "*.parquet")] )
    HGT_CSV_File_Path = filedialog.askopenfilename( title = "Select the HGT Model's `.csv` File Containing its Predicted Probabilities On the Hold-Out Test Dataset", filetypes = [("CSV Files", "*.csv")] )
    XG_CSV_File_Path = filedialog.askopenfilename( title = "Select the xG Model's `.csv` File Containing its Predicted Probabilities On the Hold-Out Test Dataset", filetypes = [("CSV Files", "*.csv")] )
    
    if not all([Test_Data_Parquet_File_Path, HGT_CSV_File_Path, XG_CSV_File_Path]):
        print("All Required Files Were Not Selected - Please Try Again.")
        return None
    
    # Read Files into DataFrames
    Test_Data_df = pd.read_parquet(Test_Data_Parquet_File_Path, engine = "auto")
    Test_Data_df = Test_Data_df.reset_index(names = "Index-Value Within the Original Test Data df's Index")
    HGT_Predicted_Probabilities_df = pd.read_csv(HGT_CSV_File_Path)
    xG_Predicted_Probabilities_df = pd.read_csv(XG_CSV_File_Path)
    
    # Merge DataFrames
    merged_df = Test_Data_df.merge(HGT_Predicted_Probabilities_df, left_index=True, right_index=True)
    merged_df = merged_df.merge(xG_Predicted_Probabilities_df, left_index=True, right_index=True)
    
    
    # Filter Rows
    filtered_df = merged_df[ ( merged_df["Will_Be_a_Goal"] == 1.0 ) &
                             ( merged_df["Complex HGT Model Test Predicted/Classified Class Labels"] == 1.0 ) &
                             ( merged_df["xG Model Test Predicted/Classified Class Labels"] == 1.0 ) &
                             ( merged_df["Complex HGT Model Test Class Labels' Predicted Probabilities"] > merged_df["xG Model Test Class Labels' Predicted Probabilities"] ) ]

    # Find Top 5 Discrepancies
    filtered_df["Probability_Difference"] = abs( filtered_df["Complex HGT Model Test Class Labels' Predicted Probabilities"] - filtered_df["xG Model Test Class Labels' Predicted Probabilities"] )
    
    top_K_discrepancies_df = filtered_df.nlargest( top_K_discrepancies, "Probability_Difference" )
    

    return top_K_discrepancies_df[ [ "Will_Be_a_Goal",
                                     "Complex HGT Model Test Class Labels' Predicted Probabilities", "Complex HGT Model Test Predicted/Classified Class Labels",
                                     "xG Model Test Class Labels' Predicted Probabilities", "xG Model Test Predicted/Classified Class Labels",
                                     "Probability_Difference" ] + [col for col in Test_Data_df.columns if col != "Will_Be_a_Goal"] ]











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










def kit_number_display(ax, player_id, player_x, player_y, color, metric_unit, kit_numbers_on_player_or_next_to_player):
    offset_cm = -50 if kit_numbers_on_player_or_next_to_player == "on player" else 75
    offset_m = -1.5 if kit_numbers_on_player_or_next_to_player == "on player" else 2

    offset_x = offset_cm if metric_unit == "cm" else offset_m
    offset_y = offset_cm if metric_unit == "cm" else offset_m

    font_size_of_kit_numbers = 9 if kit_numbers_on_player_or_next_to_player == "on player" else 10

    color_of_kit_numbers = "white" if kit_numbers_on_player_or_next_to_player == "on player" else color

    ax.text(player_x + offset_x, player_y + offset_y, str(player_id), fontsize = font_size_of_kit_numbers, color=color_of_kit_numbers)




def plot_ball(ax, data_row, ball_style, include_velocity):
    ball_x, ball_y, ball_vx, ball_vy = data_row["X"], data_row["Y"], data_row["V_xBall"], data_row["V_yBall"]
    data_row["Z"] = abs(data_row["Z"]) if data_row["Z"] < 0 else data_row["Z"]
    ax.plot(ball_x, ball_y, ball_style, markersize=np.log(data_row["Z"]), alpha=1.0, linewidth=0)

    if include_velocity:
        ax.quiver(ball_x, ball_y, ball_vx, ball_vy, color="k", scale_units='inches', scale=1000, 
                  width=0.0015, headlength=5, headwidth=3, alpha=1.0)
        
        
        
        
def Plot_Static_Shot_Frame(shot_frame_tracking_data_row, team_colors=("b", "r"), 
                           home_team_players_color_and_style="bo", away_team_players_color_and_style="ro", 
                           ball_color_and_style="ko", include_player_velocities=True, 
                           include_ball_velocity=False, player_marker_size=10, player_alpha=0.7, 
                           show_kit_numbers=True, kit_numbers_on_player_or_next_to_player="on player", 
                           figax=None, metric_unit="cm", pitch_color="green", style_of_the_goals="entire_goal"):
    """
    Function to plot a single frame of match tracking data on a soccer pitch.
    """

    if figax is None:
        fig, ax = Plot_Soccer_Pitch(metric_unit=metric_unit, pitch_color=pitch_color, style_of_the_goals=style_of_the_goals)
    else:
        fig, ax = figax

    # Process and plot home and away team data
    for team_range, color, style in [(range(1, 12), team_colors[0], home_team_players_color_and_style), 
                                     (range(12, 23), team_colors[1], away_team_players_color_and_style)]:
        for player_id in team_range:
            player_x = shot_frame_tracking_data_row[f"X{player_id}"]
            player_y = shot_frame_tracking_data_row[f"Y{player_id}"]
            player_vx = shot_frame_tracking_data_row[f"V_x{player_id}"]
            player_vy = shot_frame_tracking_data_row[f"V_y{player_id}"]

            ax.plot(player_x, player_y, style, markersize=player_marker_size, alpha=player_alpha)
            if include_player_velocities:
                ax.quiver(player_x, player_y, player_vx, player_vy, color=color, scale_units='inches', 
                          scale=1000, width=0.0015, headlength=5, headwidth=3, alpha=player_alpha)

            if show_kit_numbers:
                kit_number_display(ax, player_id, player_x, player_y, color, metric_unit, kit_numbers_on_player_or_next_to_player)

    # Plotting the ball
    plot_ball(ax, shot_frame_tracking_data_row, ball_color_and_style, include_ball_velocity)

    return fig, ax

