####################################################
#   UNIVERSAL IMPORTS USED THROUGHOUT THE MODULE   #
####################################################



import numpy as np
import pandas as pd

import random   # Used To Generate Pseudo-Random Numbers --> Used To Randomize the Order of Elements In a List, Select a Random Element From a List, Generate Random Integers, Floats, etc.

import itertools
from itertools import combinations


from tqdm.auto import tqdm   # For Visualizing Progress Bars While Code Is Being Executed

import os

import tkinter as tk
from tkinter import filedialog

import gc   # Python's Garbage Collector


import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import seaborn as sns

sns.set_style('darkgrid')


from sklearn.model_selection import StratifiedShuffleSplit

from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score, roc_curve, roc_auc_score


import networkx as nx


# PyTorch Library
# torch_geometric ≡ PyTorch Geormetric (PyG) Library

import torch
from torch_geometric.data import HeteroData, InMemoryDataset
from torch_geometric.utils import to_networkx, to_undirected
from torch_geometric.transforms import ToUndirected






# Import the Thesis' Simple HGT Functions Module

import Thesis_Simple_HGT_Model_Functions as TSHGTMFs











############################################
#         DATA-RELATED FUNCTIONS           #
############################################



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










def Read_Tracking_Data_4_Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  ):
    """
    Function That Reads the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: augmented_training_shots_on_1_same_target_goal_df = Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    Simple_PyG_GNN_Model_DataFrame_Data_Folder = f"PyG DataFrame-Format Data/"
    
    augmented_training_shots_on_1_same_target_goal_df = pd.read_parquet(f"{Simple_PyG_GNN_Model_DataFrame_Data_Folder}Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Final Version of the Augmented Training Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {augmented_training_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Augmented Training Dataset  =  \033[91m\033[1m\033[4m{augmented_training_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Augmented Training Dataset    
    
    Total_Goals_Scored_Throughout_Dataset = TSHGTMFs.Count_Total_Goals_Scored( df = augmented_training_shots_on_1_same_target_goal_df )
    
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


    plt.show()
    
    
    
    return augmented_training_shots_on_1_same_target_goal_df










def Read_Tracking_Data_4_Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models(  ):
    """
    Function That Reads the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: test_shots_on_1_same_target_goal_df = Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    print('\n',
          f"Loading & Reading In the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
          '\n')
    
    
    Simple_PyG_GNN_Model_DataFrame_Data_Folder = f"PyG DataFrame-Format Data/"
    
    test_shots_on_1_same_target_goal_df = pd.read_parquet(f"{Simple_PyG_GNN_Model_DataFrame_Data_Folder}Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models.parquet", engine = "auto")
    
    
    # Dimensions of the Test Final Version of the Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal

    print(f"Dimensions of the Final Version of the Test Tracking Data For All Models - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal  =  {test_shots_on_1_same_target_goal_df.shape}", '\n')
    
    print(f"∴ The Total Number of Shots Taken Throughout This Test Dataset  =  \033[91m\033[1m\033[4m{test_shots_on_1_same_target_goal_df.shape[0]}\033[0m", '\n')
    
    
    # Counting Total Number of Goals Scored Throughout the Season    
    
    Total_Goals_Scored_Throughout_Dataset = TSHGTMFs.Count_Total_Goals_Scored( df = test_shots_on_1_same_target_goal_df )
    
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


    plt.show()
    
    
    
    return test_shots_on_1_same_target_goal_df










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
    
    Total_Goals_Scored_Throughout_Dataset = TSHGTMFs.Count_Total_Goals_Scored( df = preprocessed_shots_on_1_same_target_goal_df )
    
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








# Set a Randomness Seed To Ensure One Always Obtains the Same Results No Matter How Many Times the Code Is Ran & Executed Whenever Some Random Process Is Involed  
    
def Set_Seed( random_seed = 7 ):
    """
    Function That Fixes a Random Seed On Every Library Used Where Some Randomness Could Occur,
            So We ALWAYS Obtain Same Results, No Matter How Many Times We Restart & Rerun the Kernel
            
    Input: seed == Arbitrary Seed Value ; Default Value = 7
    """
    
    import os
    import random
    import numpy as np
    # import tensorflow as tf
    import torch

    
    
    os.environ['PYTHONHASHSEED'] = str( random_seed )
    
    random.seed( random_seed )
    
    np.random.seed( random_seed )
    
    np.random.RandomState( random_seed )
    
    # tf.random.set_seed( random_seed )
    
    torch.manual_seed( random_seed )
    
    torch.cuda.manual_seed( random_seed )
    
    torch.backends.cudnn.deterministic = True











######################################################################
#         SIMPLE PyG GNN MODEL-RELATED CLASSES & FUNCTIONS           #
######################################################################




def Get_Flattened_Node_or_Edge_Features( features ):
        """
        Function To Flatten the Node or Edge Features If They Are Not Already 1D
        
        Input: features ( df_row[df_columns_list] ) = Node or Edge Features To Flatten (If Required)
        
        Output: features = Flattened (1D-Array) Features
        """
        
        if isinstance(features, np.ndarray) and features.ndim > 1:
            
            return features.flatten()
        
        
        return features
    









def Create_Soccer_Graph_Adjacency_Matrix_Graph_Edges_and_Edge_Features( df_row, want_directed_or_undirected_edges = "undirected" ):
    """
    Function to Create the Soccer Heterogeneous Graph's Edge Indices & Edge Features
    
    Input: df_row (series ≡ df row) = DataFrame Row ≡ Series Object
    Input: want_directed_or_undirected_edges (str) = Whether the Data Should Have Edges With Direction or Not (i.e. Whether We Should Have Directed or Undirected Graphs);  Options == {"directed", "undirected"};  Default == "undirected"
    
    Output: Ball_Player_Edge_Indices (torch.tensor): Edge Indices For Ball-Player Edges
    Output: Ball_Player_Edge_Features (torch.tensor): Edge Features For Ball-Player Edges
    Output: Player_Player_Edge_Indices (torch.tensor): Edge Indices For Player-Player Edges
    Output: Player_Player_Edge_Features (torch.tensor): Edge Features For Player-Player Edges
    """
    
    Num_Players = 22
    

    
    # Create Ball-Player Edges (Edge-Type #1)
    
    
    if want_directed_or_undirected_edges == "directed":   # Create Uni-Directional Edges

        # Ball-Player Edges' Tensor of Edge-Features

        Directed_Ball_Player_Edge_Features_tensor = torch.tensor( np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[f"Dist_Between_Ball_{Player_ID}"] ) for Player_ID in range(1, Num_Players + 1) ] ), dtype = torch.float )   # Tensor Shape/Dim == [#Edges, #Edge-Features]
    

        # Ball-Player Edges' Tensor of Indices
        
        Directed_Ball_Player_Edge_Indices_array = np.array( [ [0]*Num_Players, list( range(0, Num_Players) ) ] )
        
        Directed_Ball_Player_Edge_Indices_tensor = torch.tensor( Directed_Ball_Player_Edge_Indices_array, dtype = torch.long )   # COO-Format Adjacency Matrix --> Tensor Shape/Dim == [2, #Edges]
        
        
    
    if want_directed_or_undirected_edges == "undirected":   # Create Bi-Directional Edges (To Cancel Each Other Out During Message Passing)

        # Ball-Player Edges' Tensor of Edge-Features

        Directed_Ball_Player_Edge_Features_tensor = torch.tensor( np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[f"Dist_Between_Ball_{Player_ID}"] ) for Player_ID in range(1, Num_Players + 1) ] ), dtype = torch.float )   # Tensor Shape/Dim == [#Edges, #Edge-Features]
    

        # Ball-Player Edges' Tensor of Indices
        
        Directed_Ball_Player_Edge_Indices_array = np.array( [ [0]*Num_Players, list( range(0, Num_Players) ) ] )
        
        Directed_Ball_Player_Edge_Indices_tensor = torch.tensor( Directed_Ball_Player_Edge_Indices_array, dtype = torch.long )   # COO-Format Adjacency Matrix --> Tensor Shape/Dim == [2, #Edges]

        
        # Transform Into Undirected Graphs In the Required Format By PyTorch / PyG

        Undirected_Ball_Player_Edge_Indices_and_Edge_Features_tuple = to_undirected( edge_index = Directed_Ball_Player_Edge_Indices_tensor, edge_attr = Directed_Ball_Player_Edge_Features_tensor )

        Undirected_Ball_Player_Edge_Indices_tensor = Undirected_Ball_Player_Edge_Indices_and_Edge_Features_tuple[0]

        Undirected_Ball_Player_Edge_Features_tensor = Undirected_Ball_Player_Edge_Indices_and_Edge_Features_tuple[1]
    

    
    
    
    # Create Player-Player Edges (Edge-Type #2)


    Player_ID_Combinations = list( combinations( range(1, Num_Players + 1), 2 ) )
    
    Player_Index_Combinations = list( combinations( range(0, Num_Players), 2 ) )
    
    
    if want_directed_or_undirected_edges == "directed":   # Create Uni-Directional Edges

        # Player-Player Edges' Tensor of Edge-Features

        Directed_Player_Player_Edge_Features_tensor = torch.tensor( np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[ [f"Dist_Between_{Player_ID_1}_{Player_ID_2}", f"Same_Team_{Player_ID_1}_{Player_ID_2}"] ].values ) for Player_ID_1, Player_ID_2 in Player_ID_Combinations ] ), dtype = torch.float )   # Tensor Shape/Dim == [#Edges, #Edge-Features]
    

        # Player-Player Edges' Tensor of Indices

        Source_Player_ID_Nodes, Target_Player_ID_Nodes = [], []

        for Source_Node, Target_Node in Player_Index_Combinations:
            
            Source_Player_ID_Nodes.append(Source_Node)
            Target_Player_ID_Nodes.append(Target_Node)

        
        Directed_Player_Player_Edge_Indices_array = np.array( [Source_Player_ID_Nodes, Target_Player_ID_Nodes] )

        Directed_Player_Player_Edge_Indices_tensor = torch.tensor( Directed_Player_Player_Edge_Indices_array, dtype = torch.long )   # COO-Format Adjacency Matrix --> Tensor Shape/Dim == [2, #Edges]
    
    
    
    if want_directed_or_undirected_edges == "undirected":   # Create Edges In Both Directions (To Cancel Each Other Out During Message Passing)

        # Player-Player Edges' Tensor of Edge-Features

        Directed_Player_Player_Edge_Features_tensor = torch.tensor( np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[ [f"Dist_Between_{Player_ID_1}_{Player_ID_2}", f"Same_Team_{Player_ID_1}_{Player_ID_2}"] ].values ) for Player_ID_1, Player_ID_2 in Player_ID_Combinations ] ), dtype = torch.float )   # Tensor Shape/Dim == [#Edges, #Edge-Features]
    

        # Player-Player Edges' Tensor of Indices

        Source_Player_ID_Nodes, Target_Player_ID_Nodes = [], []

        for Source_Node, Target_Node in Player_Index_Combinations:
            
            Source_Player_ID_Nodes.append(Source_Node)
            Target_Player_ID_Nodes.append(Target_Node)

        
        Directed_Player_Player_Edge_Indices_array = np.array( [Source_Player_ID_Nodes, Target_Player_ID_Nodes] )

        Directed_Player_Player_Edge_Indices_tensor = torch.tensor( Directed_Player_Player_Edge_Indices_array, dtype = torch.long )   # COO-Format Adjacency Matrix --> Tensor Shape/Dim == [2, #Edges]

        
        # Transform Into Undirected Graphs In the Required Format By PyTorch / PyG

        Undirected_Player_Player_Edge_Indices_and_Edge_Features_tuple = to_undirected( edge_index = Directed_Player_Player_Edge_Indices_tensor, edge_attr = Directed_Player_Player_Edge_Features_tensor )

        Undirected_Player_Player_Edge_Indices_tensor = Undirected_Player_Player_Edge_Indices_and_Edge_Features_tuple[0]

        Undirected_Player_Player_Edge_Features_tensor = Undirected_Player_Player_Edge_Indices_and_Edge_Features_tuple[1]
        
    

    
    
    if want_directed_or_undirected_edges == "directed":
        
        return Directed_Ball_Player_Edge_Indices_tensor, Directed_Ball_Player_Edge_Features_tensor, Directed_Player_Player_Edge_Indices_tensor, Directed_Player_Player_Edge_Features_tensor


    if want_directed_or_undirected_edges == "undirected":
        
        return Undirected_Ball_Player_Edge_Indices_tensor, Undirected_Ball_Player_Edge_Features_tensor, Undirected_Player_Player_Edge_Indices_tensor, Undirected_Player_Player_Edge_Features_tensor










def Create_Soccer_Heterogeneous_Graph_Data_From_Tracking_DataFrame_Rows( df_row, want_directed_or_undirected_edges = "undirected", simple_or_complex_graphs = "simple" ):
    """
    Function To Create (Simple or Complex) Soccer Heterogeneous Graph Data From Tracking DataFrame Rows
    
    Input: df_row (series ≡ df row) = DataFrame Row ≡ Series Object
    Input: want_directed_or_undirected_edges (str) = Whether the Data Should Have Edges With Direction or Not (i.e. Whether We Should Have Directed or Undirected Graphs);  Options == {"directed", "undirected"};  Default == "undirected"
    Input: simple_or_complex_graphs (str) = String Indcating Whether To Create Simple or Complex Soccer Graphs;  Options == {"simple", "complex"};  Default == "simple"
    
    Output: Heterogeneous_Soccer_Graph (torch_geometric.data.HeteroData) = PyG HeteroData Object Representing the (Simple or Complex) Soccer Heterogeneous Graph
    """
    
    Num_Players = 22
    
    Heterogeneous_Soccer_Graph = HeteroData()
    
    
    
    # Extract Node Features For the Ball Node
    
    Ball_Features_Columns_dict = { "simple" : [ "X", "Y", "Dist_Between_Ball_TargetGoal", "Angle_Between_Ball_TargetGoal_Rad" ],
                                   "complex"  : [ "X", "Y", "Z", "V_xBall", "V_yBall", "V_zBall", "SpeedBall", "Dist_Between_Ball_TargetGoal", "Angle_Between_Ball_TargetGoal_Rad" ] }   # , "is_1st_Half", "Match_Minute_Clock", "Match_Seconds_Clock" ] }
    
                                                                                                 #   For "complex" Graphs --> Concatenate Global/Graph-Level Features At the End:  "is_1st_Half", "Match_Minute_Clock", "Match_Seconds_Clock"
    
    
    Ball_Node_Features = np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[ Ball_Features_Columns_dict[simple_or_complex_graphs] ].values ) ] )
    
    
    Heterogeneous_Soccer_Graph["Ball"].x = torch.tensor( Ball_Node_Features, dtype = torch.float )   # Tensor Shape/Dim == [#Nodes, #Node-Features]



    # Encode the Ball's Node Position

    Ball_Node_Position_Coordinates = ["X", "Y"] if simple_or_complex_graphs == "simple" else ["X", "Y", "Z"]
    
    Ball_Node_Position_Coordinates = np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[ Ball_Node_Position_Coordinates ].values ) ] )

    Heterogeneous_Soccer_Graph["Ball"].pos = torch.tensor( Ball_Node_Position_Coordinates, dtype = torch.float )   # Tensor Shape/Dim == [#Nodes, #Position-Dimensions]
    
    
    
    
    # Extract Node Features For the 22 Player Nodes
    
    Players_Features_Columns_dict = { "simple" : lambda Player_ID: [ f"X{Player_ID}", f"Y{Player_ID}", f"Team_In_Possession_{Player_ID}" ],
                                      "complex"  : lambda Player_ID: [ f"X{Player_ID}", f"Y{Player_ID}", f"V_x{Player_ID}", f"V_y{Player_ID}", f"Speed{Player_ID}", f"Dist_Between_{Player_ID}_TargetGoal", f"Angle_Between_{Player_ID}_TargetGoal_Rad",
                                                                       f"Team_In_Possession_{Player_ID}" ] }   # , "is_1st_Half", "Match_Minute_Clock", "Match_Seconds_Clock" ] }
    
                        #   For "complex" Graphs --> Concatenate Global/Graph-Level Features At the End:  "is_1st_Half", "Match_Minute_Clock", "Match_Seconds_Clock"
    
    
    Players_Node_Features = np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[ Players_Features_Columns_dict[simple_or_complex_graphs](Player_ID) ].values ) for Player_ID in range(1, Num_Players + 1) ] )
    
    
    Heterogeneous_Soccer_Graph["Player"].x = torch.tensor( Players_Node_Features, dtype = torch.float )   # Tensor Shape/Dim == [#Nodes, #Node-Features]



    # Encode the Players' Node Positions

    Players_Node_Position_Coordinates = lambda Player_ID: [f"X{Player_ID}", f"Y{Player_ID}"]
    
    Players_Node_Position_Coordinates = np.array( [ TSHGTMFs.Get_Flattened_Node_or_Edge_Features( features = df_row[ Players_Node_Position_Coordinates(Player_ID) ].values ) for Player_ID in range(1, Num_Players + 1) ] )

    Heterogeneous_Soccer_Graph["Player"].pos = torch.tensor( Players_Node_Position_Coordinates, dtype = torch.float )   # Tensor Shape/Dim == [#Nodes, #Position-Dimensions]
        
        
        
        
    
    if want_directed_or_undirected_edges == "directed":
        
        # Create All Edges' (-Types') Indices' & Features' PyTorch Tensors
    
        Directed_Ball_Player_Edge_Indices_tensor, Directed_Ball_Player_Edge_Features_tensor, Directed_Player_Player_Edge_Indices_tensor, Directed_Player_Player_Edge_Features_tensor = TSHGTMFs.Create_Soccer_Graph_Adjacency_Matrix_Graph_Edges_and_Edge_Features( df_row = df_row, want_directed_or_undirected_edges = want_directed_or_undirected_edges )


        # Split the Edges' Indices & Features For Ball-Player & Player-Player Edge Types
    
        Heterogeneous_Soccer_Graph["Ball", "Interacts", "Player"].edge_index = Directed_Ball_Player_Edge_Indices_tensor   # Tensor Shape/Dim == [2, #Edges]
    
        Heterogeneous_Soccer_Graph["Ball", "Interacts", "Player"].edge_attr = Directed_Ball_Player_Edge_Features_tensor   # Tensor Shape/Dim == [#Edges, #Edge-Features]
    
    
        Heterogeneous_Soccer_Graph["Player", "Connects", "Player"].edge_index = Directed_Player_Player_Edge_Indices_tensor   # Tensor Shape/Dim == [2, #Edges]
    
        Heterogeneous_Soccer_Graph["Player", "Connects", "Player"].edge_attr = Directed_Player_Player_Edge_Features_tensor   # Tensor Shape/Dim == [#Edges, #Edge-Features]



    if want_directed_or_undirected_edges == "undirected":
        
        # Create All Edges' (-Types') Indices' & Features' PyTorch Tensors
    
        Undirected_Ball_Player_Edge_Indices_tensor, Undirected_Ball_Player_Edge_Features_tensor, Undirected_Player_Player_Edge_Indices_tensor, Undirected_Player_Player_Edge_Features_tensor = TSHGTMFs.Create_Soccer_Graph_Adjacency_Matrix_Graph_Edges_and_Edge_Features( df_row = df_row, want_directed_or_undirected_edges = want_directed_or_undirected_edges )


        # Split the Edges' Indices & Features For Ball-Player & Player-Player Edge Types
    
        Heterogeneous_Soccer_Graph["Ball", "Interacts", "Player"].edge_index = Undirected_Ball_Player_Edge_Indices_tensor   # Tensor Shape/Dim == [2, #Edges]
    
        Heterogeneous_Soccer_Graph["Ball", "Interacts", "Player"].edge_attr = Undirected_Ball_Player_Edge_Features_tensor   # Tensor Shape/Dim == [#Edges, #Edge-Features]
    
    
        Heterogeneous_Soccer_Graph["Player", "Connects", "Player"].edge_index = Undirected_Player_Player_Edge_Indices_tensor   # Tensor Shape/Dim == [2, #Edges]
    
        Heterogeneous_Soccer_Graph["Player", "Connects", "Player"].edge_attr = Undirected_Player_Player_Edge_Features_tensor   # Tensor Shape/Dim == [#Edges, #Edge-Features]

    
    
    
    # Create Target Variable's PyTorch Tensor
    
    Heterogeneous_Soccer_Graph.y = torch.tensor( [ df_row["Will_Be_a_Goal"] ], dtype = torch.long )
    
    
    

    return Heterogeneous_Soccer_Graph










class Soccer_Heterogeneous_Graphs_Dataset( InMemoryDataset ):
    """
    Convert Soccer (Preprocessed) Tracking Data From DataFrame Format Into Heterogeneous Graphs' Raw Graph-Data Format, & Then Group These Heterogeneous Graphs Into a PyG "InMemoryDataset" Dataset Object
           - Dataset Can Be Specified To Be Made of Training or Test Heterogeneous Graphs
           - Heterogeneous Graphs Can Be Specified To Be Directed or Undirected (i.e. Edges Having Direction Or Not)
           - Heterogeneous Graphs Can Be Specified To Be Simple or Complex
    
    Input: root (str) = String Indicating the (Root) Directory Path of the Folder In Which the Final Processed Dataset of Soccer Heterogeneous Graphs Should Be Saved;  Options == {"Simple GNN Model/PyG Graph-Format Data/", "Complex GNN Model/PyG Graph-Format Data/"}
    Input: transform (torch_geometric.transforms): A Transformation Function/Method From the `torch_geometric.transforms`, That Takes In a `torch_geometric.data.Data` Object or `torch_geometric.data.HeteroData` Object & Returns a Transformed Version of It
                                                        The `Data` or `HeteroData` Object (or Entire Dataset) Will Be Transformed Before Every (Loading) Access To the Dataset
    Input: pre_transform (torch_geometric.transforms): A Transformation Function/Method From the `torch_geometric.transforms`, That Takes In a `torch_geometric.data.Data` Object or `torch_geometric.data.HeteroData` Object & Returns a Transformed Version of It;  Default == ToUndirected( merge = False )
                                                        The `Data` or `HeteroData` Object (or Entire Dataset) Will Be Transformed Before Being Saved To Disk (i.e. Locally)
    Input: training_or_test_data (str) = String Indcating Whether To Create the Dataset From Training or Test Data;  Options == {"training", "test"};  Default == "training"
    Input: want_directed_or_undirected_edges (str) = Whether the Data Should Have Edges With Direction or Not (i.e. Whether We Should Have Directed or Undirected Graphs);  Options == {"directed", "undirected"};  Default == "directed"
    Input: simple_or_complex_graphs (str) = String Indcating Whether To Create Simple or Complex Soccer Graphs;  Options == {"simple", "complex"};  Default == "simple"
    Input: log (bool) = Whether To Print Any Console Output While Downloading & Processing the Dataset
    
    Output: 
    """
    
    def __init__( self, root = ".", transform = None, pre_transform = ToUndirected( merge = False ), training_or_test_data = "training", want_directed_or_undirected_edges = "directed", simple_or_complex_graphs = "simple", log = True ):
        
        # Use `root = "."` If Both, the Python Script In Which I Am Writing This Class & the Notebook In Which the Dataset Class Will Be Instantiated, Are Located In the Same Directory/Folder As the Folders In Which the Raw Data (DataFrame) `.parquet` Files ('PyG DataFrame-Format Data/') & the Proccessed Data (Graphs Dataset) `.pt` Files ('PyG Graph-Format Data/') Are In
        
        self.training_or_test_data = training_or_test_data
        
        self.want_directed_or_undirected_edges = want_directed_or_undirected_edges
        
        self.simple_or_complex_graphs = simple_or_complex_graphs
        
        super( Soccer_Heterogeneous_Graphs_Dataset, self ).__init__( root, transform, pre_transform )
        
        self.data, self.slices = torch.load( self.processed_paths[0] )
        
        
        
        
    @property
    def raw_dir(self):
        """
        Function That Points To the Directory/Folder Where the Raw Data (DataFrame) `.parquet` Is Located In
        
        """
        return os.path.join( self.root, "PyG DataFrame-Format Data/" )
    
    

    @property
    def processed_dir(self):
        """
        Function That Points To the Directory/Folder Where the Processed Data (Graphs Dataset) `.pt` Will Be Saved In + Will Be Located In
        
        """
        return os.path.join( self.root, "PyG Graph-Format Data/" )
        
        
        

        
    @property
    def raw_file_names(self):
        """
        Function That Extracts the File Name of the Training or Test Raw DataFrame-Format Data of the Soccer Tracking Data
                If the Files Exist In the `raw_dir`, the `download` Method From the `InMemoryDataset` Will Not Be Triggered
        
        """
        
        DataFrame_Format_File_Name = "Augmented_Training_Shots_Frames_On_1_Same_Target_Goal_4_All_Models-Preprocessed.parquet" if self.training_or_test_data == "training" else "Test_Shots_Frames_On_1_Same_Target_Goal_4_All_Models-Preprocessed.parquet"
        
        
        
        return [DataFrame_Format_File_Name]
    

    
    
    @property
    def processed_file_names(self):
        """
        Function That Extracts the File Name of the Training or Test Processed Graph-Format Data of the Soccer Tracking Data - For Simple or Complex Graphs
                If These Files Are Found In `raw_dir`, Then the `process` Method Is Not Executed & Is Skipped
        
        """
        
        if self.training_or_test_data == "training":
            
            if self.simple_or_complex_graphs == "simple":
                
                Graphs_Format_File_Name = f"Augmented_Training_Shots_Simple_Graphs_Dataset.pt"
                
                
        if self.training_or_test_data == "test":
            
            if self.simple_or_complex_graphs == "simple":
                
                Graphs_Format_File_Name = f"Test_Shots_Simple_Graphs_Dataset.pt"
        
        
        
        
        if self.training_or_test_data == "training":
            
            if self.simple_or_complex_graphs == "complex":
                
                Graphs_Format_File_Name = f"Augmented_Training_Shots_Complex_Graphs_Dataset.pt"
                        
                
        if self.training_or_test_data == "test":
            
            if self.simple_or_complex_graphs == "complex":
                
                Graphs_Format_File_Name = f"Test_Shots_Complex_Graphs_Dataset.pt"
                
                
        return [Graphs_Format_File_Name]
    

    
    
    def download(self):
        """
        Downloads the Processed Data (Graphs Dataset) Into the `self.raw_dir` Folder
        
        """
        
        pass
    

    
    
    def process(self):
        """
        Function That Converts the Soccer Tracking Data From DataFrame Format Into Heterogeneous Graphs' Raw Graph-Data Format, & Then Group These Heterogeneous Graphs Into a PyG "InMemoryDataset" Dataset Object
        
        """
        
        # Read Soccer Tracking Data As a DataFrame
        
        Soccer_Tracking_Data_df = pd.read_parquet( os.path.join( self.raw_dir, self.raw_file_names[0] ) )
        
        
        # Convert Each DataFrame Row Into a Heterogeneous Graph Using the `Create_Soccer_Heterogeneous_Graph_Data_From_Tracking_DataFrame_Rows()` Function
        
        Soccer_Heterogeneous_Graphs_Data_list = [ TSHGTMFs.Create_Soccer_Heterogeneous_Graph_Data_From_Tracking_DataFrame_Rows( df_row = DataFrame_Row, want_directed_or_undirected_edges = self.want_directed_or_undirected_edges, simple_or_complex_graphs = self.simple_or_complex_graphs ) for Index, DataFrame_Row in tqdm( Soccer_Tracking_Data_df.iterrows(), total = Soccer_Tracking_Data_df.shape[0] ) ]
            

        
        if self.pre_filter is not None:
            
            Soccer_Heterogeneous_Graphs_Data_list = [ data for data in Soccer_Heterogeneous_Graphs_Data_list if self.pre_filter(data) ]
            

        
        if self.pre_transform is not None:
        
            Soccer_Heterogeneous_Graphs_Data_list = [ self.pre_transform(data) for data in Soccer_Heterogeneous_Graphs_Data_list ]
            

            
        
        data, slices = self.collate(Soccer_Heterogeneous_Graphs_Data_list)
        
        torch.save( (data, slices), self.processed_paths[0] )










def Stratified_Shuffled_K_Splits_of_Soccer_Graphs_Dataset( PyG_dataset, num_K_splits = 5, validation_size = 0.3, random_seed = 7 ):
    """
    Function that performs a shuffled stratified split of the soccer graphs in the dataset, into training and validation sets, by outputting their respective indices

    Input: PyG_dataset (torch_geometric.data.InMemoryDataset or torch_geometric.data.Dataset) = PyG Dataset object
    Input: num_K_splits (int) = Number of re-shuffling & splitting iterations;  Default == 5
    Input: validation_size (float) = Proportion size of the validation set;  Default == 0.3
    Input: random_seed (int) = Controls the randomness of the training and testing indices produced. Pass an int for reproducible output across multiple function calls;  Default == 7

    Output: train_indices, val_indices (int) = Indices if the training and validation sets, respectively
    
    """
    
    # Extracting Class Labels
    
    Class_Labels_array = PyG_dataset._data.y.numpy()
    

    # Stratified Shuffled K Split
    
    Stratified_Shuffled_K_Splits_CV = StratifiedShuffleSplit( n_splits = num_K_splits, test_size = validation_size, random_state = random_seed )
    
    for Fold_i, (Training_Indices, Validation_Indices) in enumerate( Stratified_Shuffled_K_Splits_CV.split( np.zeros( len(Class_Labels_array) ), Class_Labels_array ) ):

        print(f"Fold {Fold_i}:")
        print(f"  Training Indices = {Training_Indices}")
        print(f"  Validation Indices = {Validation_Indices}", "\n")

    
    










def Plot_CV_Splitted_Indices( PyG_dataset, cv_strategy, figure_axes, num_K_splits = 5, lw = 10 ):
    """
    Inspiration Taken From Function In --> https://scikit-learn.org/stable/auto_examples/model_selection/plot_cv_indices.html#sphx-glr-auto-examples-model-selection-plot-cv-indices-py
    
    Function that creates a sample plot for indices of a cross-validation object

    Input: PyG_dataset (torch_geometric.data.InMemoryDataset or torch_geometric.data.Dataset) = PyG Dataset object
    Input: cv_strategy = Cross-Validation strategy to follow
    Input: num_K_splits (int) = Number of re-shuffling & splitting iterations;  Default == 5
    Input: figure_axes = Figure's axes
    Input: lw = Line-width
    """

    X = PyG_dataset._data["Ball"].x.numpy()

    y = PyG_dataset._data.y.numpy()
    

    cmap_data = plt.cm.Paired
    cmap_cv = plt.cm.winter

    # Generate the training/validation visualizations for each CV split
    for ii, (tr, val) in enumerate(cv_strategy.split(X=X, y=y)):
        # Fill in indices with the training/validation groups
        indices = np.array([np.nan] * len(X))
        indices[val] = 1
        indices[tr] = 0

        # Visualize the results
        figure_axes.scatter(
            range(len(indices)),
            [ii + 0.5] * len(indices),
            c=indices,
            marker="_",
            lw=lw,
            cmap=cmap_cv,
            vmin=-0.2,
            vmax=1.2,
        )

    # Plot the data classes at the end
    figure_axes.scatter(
        range(len(X)), [ii + 1.5] * len(X), c=y, marker="_", lw=lw, cmap=cmap_data
    )

    # Formatting
    yticklabels = list(range(num_K_splits)) + ["Class Labels'\nDistribution"]
    figure_axes.set(
        yticks=np.arange(num_K_splits + 1) + 0.5,
        yticklabels=yticklabels,
        xlabel="Individual Graphs' Indices",
        ylabel="CV Iteration",
        ylim=[num_K_splits + 1.4, -0.2],
        xlim=[0, len(X)],
    )
    
    figure_axes.set_title(f"Train-Val {type(cv_strategy).__name__}", fontsize=15)

    # Create legend handles
    training_patch = Patch(color=cmap_cv(0.5), label="Training Set")
    validation_patch = Patch(color=cmap_cv(0.85), label="Validation Set")
    legend_handles = [training_patch, validation_patch]


    # Add class labels to the legend
    unique_classes = np.unique(y)
    # Normalize the class labels to range between 0 and 1
    norm = plt.Normalize(vmin=y.min(), vmax=y.max())
    # Get the actual colors used by the scatter plot for each class label
    class_colors = [cmap_data(norm(cls)) for cls in unique_classes]
    labels_dict = {0 : "Not Goals", 1 : "Goals"}
    class_patches = [Patch(color=class_colors[cls], label=labels_dict.get(cls, f'{cls}')) for cls in range(len(unique_classes))]
    legend_handles.extend(class_patches)
    

    # Add legend to the plot
    figure_axes.legend(handles=legend_handles, loc=(1.005, 0.725))

    
    return figure_axes
    









def Visualize_Undirected_Homogeneous_Graph( graph, graph_node_color ):
    """
    Function That Creates a Visualization of a Graph Data Object

    Input: graph = PyG `HeteroData()` Graph Data Object
    Input: graph_node_color (str, list of str, or graph.y) = Color With Which To Represent/Fill the Graph's Nodes
    
    """

    Graph = to_networkx( graph, to_undirected = True )
    
    
    plt.figure( figsize = (8, 8) )
    
    plt.xticks([])
    plt.yticks([])
    
    nx.draw_networkx( G = Graph, pos = nx.spring_layout(G = Graph, seed = 7), with_labels = False,
                      node_color = graph_node_color, cmap = "Set2" )
    
    plt.show()










def Visualize_Soccer_Unidrected_Heterogeneous_Graph( heterogeneous_graph, ball_color = "green", home_team_color = "blue", away_team_color = "red" ):
    """
    Function That Creates a Visualization of a Graph Data Object

    Includes Functionalities To Ensure That Self-Loops Are Removed + To Also Enforce Only True Nodes Are Plotted:
            - It Seems That Due To the Way In Which the Graph Data In the PyG `heterogeneous_graph` Data Object Is Processed By the NetworkX Library When Passed Into the `to_networkx()` --> It Added a 1 Artificial Self-Loop + 1 Extra Artificial Node

    Input: graph (torch_geometric.data.HeteroData) = PyG `HeteroData()` Graph Data Object
    Input: ball_color (str) = Color With Which To Visualize the Ball Node
    Input: home_team_color (str) = Color With Which To Visualize the Home Team Players' Nodes
    Input: away_team_color (str) = Color With Which To Visualize the Away Team Players' Nodes
    
    """

    Graph = to_networkx( heterogeneous_graph, node_attrs = ["pos"] )


    
    # Extract the Actual (Valid) Nodes From the `heterogeneous_graph`
    
    Actual_Valid_Nodes = [ Node for Node in range(heterogeneous_graph.num_nodes) ]  # Assuming Nodes Are Indexed From 0 To `num_nodes`-1


    
    # Manually Make the Graph Undirected By Adding Edges In Both Directions, While Also Filtering Out Self-Loops & Edges Involving Invalid Node IDs
    
    Undirected_Edges_Without_Self_Loops = []
    
    
    for (Source_Node, Target_Node) in Graph.edges():
        
        if Source_Node in Actual_Valid_Nodes and Target_Node in Actual_Valid_Nodes and Source_Node != Target_Node:
            
            Undirected_Edges_Without_Self_Loops.append( (Source_Node, Target_Node) )
            
            Undirected_Edges_Without_Self_Loops.append( (Target_Node, Source_Node) )
            

    
    # Now Remove Duplicate Edges (Since Adding Reverse Edges Could Create Duplicates)
    
    Undirected_Edges_Without_Self_Loops = list( set(Undirected_Edges_Without_Self_Loops) )
    

    
    # Clear the Existing Edges & Add the Undirected Ones
    
    Graph.clear_edges()
    
    Graph.add_edges_from(Undirected_Edges_Without_Self_Loops)
    

    

    # Define Colors For Each Node Type
    
    Color_Map_dict = { 0 : ball_color,   # Ball
                       1 : home_team_color,    # Home Team Players
                       2 : away_team_color }    # Away Team Players

    
    # Assign Colors To Nodes Based On Their Types
    
    Graph_Node_Colors = []

    Node_Positions = {}  # Stores the Positions (Coordinates) of Nodes
    
    
    for Node in Graph.nodes( data = True ):
        
        Node_ID = Node[0]
        
        Node_Data = Node[1]
        
        
        if Node_ID == 0:
            
            Graph_Node_Colors.append( Color_Map_dict[0] )  # Ball
            
        elif 1 <= Node_ID <= 11:
            
            Graph_Node_Colors.append( Color_Map_dict[1] )  # Home Team Players
            
        elif 12 <= Node_ID <= 22:
            
            Graph_Node_Colors.append( Color_Map_dict[2] )  # Away Team Players



        # Check If `'pos'` Is a Tensor & Convert To Numpy, & Then To Tuple
        
        Node_Position_Coordinates = Node_Data.get("pos")
        
        
        if Node_Position_Coordinates is not None:

            if hasattr( Node_Position_Coordinates, "numpy" ):  # Check If It's a Tensor
                
                Node_Position_Coordinates = Node_Position_Coordinates.numpy()
                
                
            Node_Positions[Node_ID] = tuple( Node_Position_Coordinates )  # Convert Array-Like To Tuple
            
    
    
    plt.figure( figsize = (8, 8) )
    
    plt.xticks([])
    plt.yticks([])


    
    # Draw the Graph With Node Labels For Actual Nodes Only
    
    nx.draw_networkx_nodes (G = Graph, pos = Node_Positions, nodelist = Actual_Valid_Nodes, node_color = Graph_Node_Colors )
    
    nx.draw_networkx_edges( G = Graph, pos = Node_Positions, edgelist = Graph.edges, arrows = False )
    
    nx.draw_networkx_labels( G = Graph, pos = Node_Positions, labels = { Node : Node for Node in Actual_Valid_Nodes }, font_size = 12, font_color = "white" )

    
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
def Display_Classification_Report_and_Confusion_Matrix( y_test_true_class_labels, y_test_pred_class_labels, confusion_matrix_cmap = "Greens" ):
    """
    Displays the classification report and confusion matrix for the given true and predicted labels of the unseen test set

    Input: y_test_true_class_labels (array-like) = True class labels of the unseen test set
    Input: y_test_pred_class_labels (array-like) = Predicted class labels of the unseen test set
    Input: confusion_matrix_cmap (str) = String indicating the colour map to employ for the Confusion Matrix
    
    """
    
    # Classification Report
    
    print("Classification Report:", '\n')
    
    print( classification_report(y_test_true_class_labels, y_test_pred_class_labels) )
    

    # Confusion Matrix
    
    Confusion_Matrix = confusion_matrix(y_test_true_class_labels, y_test_pred_class_labels)
    
    Test_Set_Confusion_Matrix_Display = ConfusionMatrixDisplay( confusion_matrix = Confusion_Matrix )
    
    Test_Set_Confusion_Matrix_Display.plot( include_values = True, cmap = confusion_matrix_cmap, colorbar = True );
    

    tick_marks = np.arange( 2 )
    
    class_labels = ["Not Goal", "Goal"]
    

    plt.xticks( tick_marks, class_labels, rotation = 0 )
    
    plt.yticks( tick_marks, class_labels )
    

    plt.title( "Confusion Matrix", fontsize = 12 )
    
    plt.xlabel( "Predicted Class Label", fontsize = 10 )
    
    plt.ylabel( "True Class Label", fontsize = 10 )
    
    
    plt.tight_layout()
    
    plt.show()
    
    
    
    
    
    
    
    
    
    
def Model_Test_Set_Accuracy( y_test_true_class_labels, y_test_pred_class_labels ):
    """
    Calculates and displays the accuracy of the model on the unseen test set

    Input: y_test_true_class_labels (array-like) = True class labels of the unseen test set
    Input: y_test_pred_class_labels (array-like) = Predicted class labels of the unseen test set
    
    """
    
    
    print("Accuracy = From All the Data, How Many Class Labels Are Correctly Predicted/Classified", '\n',
          "i.e.      TP + TN / (All Data)", '\n')

    test_Accuracy = accuracy_score(y_test_true_class_labels, y_test_pred_class_labels)

    print(f"Model's Test Set Accuracy = \033[91m\033[1m\033[4m{test_Accuracy * 100 :.2f} %\033[0m", '\n')
    
    
    
    
    return test_Accuracy
    
    
    
    
    
    
    
    
    
    
def Model_Test_Set_Precision_Score( y_test_true_class_labels, y_test_pred_class_labels, positive_class_label = 1.0, averaging_strategy = "binary" ):
    """
    Calculates and displays the Precision Score of the model on the unseen test set

    Input: y_test_true_class_labels (array-like) = True class labels of the unseen test set
    Input: y_test_pred_class_labels (array-like) = Predicted class labels of the unseen test set
    Input: positive_class_label (int or float) = Positive class label;  Default == 1.0
    Input: averaging_strategy (str) = Averaging strategy - this parameter is required for multiclass/multilabel targets. If None, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:
                                                            "binary" ==> Only report results for the class specified by pos_label. This is applicable only if targets ( `y_{true,pred}` ) are binary
                                                            "micro" ==> Calculate metrics globally by counting the total true positives, false negatives and false positives
                                                            "macro" ==> Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account
                                                            "weighted" ==> Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label)
                                                                                This alters ‘macro’ to account for label imbalance; it can result in an F1-score that is not between precision and recall
                                                            "samples" ==> Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from `accuracy_score`)
                                      Options == {"binary", "micro", "macro", "weighted", "samples"};  Default == "binary"
    
    """
    
    
    print("Precision = Ratio of TP From All the Data, or Classes, That Have Been Predicted (or Classified) As a +ve Class", '\n',
          "i.e.      TP / (TP + FP)", '\n')

    test_Precision_Score = precision_score( y_true = y_test_true_class_labels, y_pred = y_test_pred_class_labels,
                                            pos_label = positive_class_label, average = averaging_strategy )

    print(f"Model's Test Set Precision Score = \033[91m\033[1m\033[4m{test_Precision_Score * 100 :.2f} %\033[0m", '\n')
    
    
    
    
    return test_Precision_Score
    
    
    
    
    
    
    
    
    
    
def Model_Test_Set_Recall_Score( y_test_true_class_labels, y_test_pred_class_labels, positive_class_label = 1.0, averaging_strategy = "binary" ):
    """
    Calculates and displays the Recall (For the +ve Class) ≡ Sensitivity ≡ True Positive Rate (TPR) Score of the model on the unseen test set

    Input: y_test_true_class_labels (array-like) = True class labels of the unseen test set
    Input: y_test_pred_class_labels (array-like) = Predicted class labels of the unseen test set
    Input: positive_class_label (int or float) = Positive class label;  Default == 1.0
    Input: averaging_strategy (str) = Averaging strategy - this parameter is required for multiclass/multilabel targets. If None, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:
                                                            "binary" ==> Only report results for the class specified by pos_label. This is applicable only if targets ( `y_{true,pred}` ) are binary
                                                            "micro" ==> Calculate metrics globally by counting the total true positives, false negatives and false positives
                                                            "macro" ==> Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account
                                                            "weighted" ==> Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label)
                                                                                This alters ‘macro’ to account for label imbalance; it can result in an F1-score that is not between precision and recall
                                                            "samples" ==> Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from `accuracy_score`)
                                      Options == {"binary", "micro", "macro", "weighted", "samples"};  Default == "binary"
    
    """
    
    
    print("Recall (For the +ve Class) ≡ Sensitivity ≡ True Positive Rate (TPR) = Ratio of TP From All the Data That Actually and Truly Are a +ve Class", '\n',
          "i.e.      TP / (TP + FN)", '\n')

    test_Recall_Score = recall_score( y_true = y_test_true_class_labels, y_pred = y_test_pred_class_labels,
                                      pos_label = positive_class_label, average = averaging_strategy )

    print(f"Model's Test Set Recall (≡ Sensitivity ≡ TPR) Score = \033[91m\033[1m\033[4m{test_Recall_Score * 100 :.2f} %\033[0m", '\n')
    
    
    
    
    return test_Recall_Score
    
    
    
    
    
    
    
    
    
    
def Model_Test_Set_F1_Score( y_test_true_class_labels, y_test_pred_class_labels, positive_class_label = 1.0, averaging_strategy = "binary" ):
    """
    Calculates and displays the F1-Score of the model on the unseen test set

    Input: y_test_true_class_labels (array-like) = True class labels of the unseen test set
    Input: y_test_pred_class_labels (array-like) = Predicted class labels of the unseen test set
    Input: positive_class_label (int or float) = Positive class label;  Default == 1.0
    Input: averaging_strategy (str) = Averaging strategy - this parameter is required for multiclass/multilabel targets. If None, the scores for each class are returned. Otherwise, this determines the type of averaging performed on the data:
                                                            "binary" ==> Only report results for the class specified by pos_label. This is applicable only if targets ( `y_{true,pred}` ) are binary
                                                            "micro" ==> Calculate metrics globally by counting the total true positives, false negatives and false positives
                                                            "macro" ==> Calculate metrics for each label, and find their unweighted mean. This does not take label imbalance into account
                                                            "weighted" ==> Calculate metrics for each label, and find their average weighted by support (the number of true instances for each label)
                                                                                This alters ‘macro’ to account for label imbalance; it can result in an F1-score that is not between precision and recall
                                                            "samples" ==> Calculate metrics for each instance, and find their average (only meaningful for multilabel classification where this differs from `accuracy_score`)
                                      Options == {"binary", "micro", "macro", "weighted", "samples"};  Default == "binary"
    
    """
    
    
    print("F1-Score = Harmonic Mean of Precision and Recall", '\n',
          "i.e.      2 x ( (Precision x Recall) / (Precision + Recall) )", '\n', '\n', 
          "Where,  Precision (For +ve Class) = TP / (TP + FP)", '\n',
          "And, Recall (For +ve Class) == Sensitivity = TP / (TP + FN)", '\n')

    test_F1_Score = f1_score( y_true = y_test_true_class_labels, y_pred = y_test_pred_class_labels,
                              pos_label = positive_class_label, average = averaging_strategy )

    print(f"Model's Test Set F1-Score = \033[91m\033[1m\033[4m{test_F1_Score * 100 :.2f} %\033[0m", '\n')
    
    
    
    
    return test_F1_Score
    
    
    
    
    
    
    
    
    
    
def Plot_ROC_Curve_of_Unseen_Test_Set( y_test_true_class_labels, y_test_pred_class_probabilities, figure_size = (8, 6) ):
    """
    Plots the model's ROC curve for the unseen test set

    Input: y_test_true_class_labels (array-like) = True class labels of the unseen test set
    Input: y_test_pred_class_probabilities (array-like) = Predicted class labels' probabilities of the unseen test set
    Input: figure_size (tuple) = Size of the figure;  Default == (8, 6)
    
    """
    
    # Compute ROC curve and ROC area
    
    FPR, TPR, Threshold = roc_curve( y_test_true_class_labels, y_test_pred_class_probabilities )
    
    test_AUC_of_ROC = roc_auc_score( y_test_true_class_labels, y_test_pred_class_probabilities )
    

    
    plt.figure( figsize = figure_size )
    

    plt.plot( FPR, TPR, color = "darkorange", label = f"Model's ROC Curve (AUC = {test_AUC_of_ROC:.4f})" )   # Plotting the ROC-Curve
    
    plt.plot( [0, 1], [0, 1], color = "navy", linewidth = 2, linestyle = "--" )   # Plotting the Threshold Limit line  ⇒  AUC_Threshold = 0.50
    

    plt.xlim( [0.0, 1.0] )
    
    plt.ylim( [0.0, 1.05] )
    

    plt.title( "Model's Receiver Operating Characteristic (ROC) Curve", fontsize = 12 )
    
    plt.xlabel( "False Positive Rate (FPR)", fontsize = 10 )
    
    plt.ylabel( "True Positive Rate (TPR) | Recall", fontsize = 10 )
    

    plt.legend( loc = "lower right", edgecolor = "k", fontsize = "large" )
    
    plt.show()
    
    
    
    
    return test_AUC_of_ROC




