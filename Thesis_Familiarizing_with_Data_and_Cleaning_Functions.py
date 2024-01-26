####################################################
#   UNIVERSAL IMPORTS USED THROUGHOUT THE MODULE   #
####################################################



import numpy as np
import pandas as pd
import scipy.signal as signal
import itertools

import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')


# Import the Thesis' Data Familiarization + Cleaning Functions Module

import Thesis_Familiarizing_with_Data_and_Cleaning_Functions as TFwDCFs











###################################################
#         DATA-TRANSFORAMTION FUNCTIONS           #
###################################################



def Flatten_a_List_of_Lists( list_of_lists ):
    """
    Function That Flattens a List of Lists `list_of_lists` Into One Single List `flattened_list`
    
    Input: list_of_lists = List of Lists
    
    Output: flattened_list = Single Flattened List
    """
    
    flattened_list = [item for sublist in list_of_lists for item in sublist]   # [item for sublist in list_of_lists]
    
    
    return flattened_list










def Encoding_and_Decoding_MatchID_FileName_Dictionaries():
    """
    Function That Gives 2 Dictionaries:
                                        1) Dictionary Encoding the Original `MatchId` File Names Into the New `MatchId` File Names ( [0, 360] )
                                        2) Dictionary Decoding the New `MatchId` File Names ( [0, 360] ) Into the Original `MatchId` File Names
    
    Output: MatchId_File_Name_Dictionary = Dictionary Encoding the Original `MatchId` File Names Into the New `MatchId` File Names ( [0, 360] )
    Output: Inverted_MatchId_File_Name_Dictionary = Dictionary Decoding the New `MatchId` File Names ( [0, 360] ) Into the Original `MatchId` File Names
    """
    
    # Read the "MatchId Encoding-Decoding" Sheet Within the Excel File "Thesis Files' & Data's Dictionaries.xlsx"
    
    df = pd.read_excel("Thesis Files' & Data's Dictionaries.xlsx", sheet_name = "MatchId Encoding-Decoding")
    
    

    # Extract the two columns of numbers
    
    Original_MatchId_File_Name = df["Original MatchId File Name"].tolist()
    
    New_Encoded_MatchId_File_Name = df["New Encoded MatchId File Name"].tolist()
    
    

    # Create a dictionary from the two columns
    
    MatchId_File_Name_Dictionary = dict(zip(Original_MatchId_File_Name, New_Encoded_MatchId_File_Name))
    
    

    # Inverted dictionary, so that the keys of the original dictionary become the values, and the values of the original dictionary beomce the keys
    
    Inverted_MatchId_File_Name_Dictionary = {value: key for key, value in MatchId_File_Name_Dictionary.items()}


    
    
    return MatchId_File_Name_Dictionary, Inverted_MatchId_File_Name_Dictionary










def Encoding_MatchID_Column_Into_New_FileNames( df ):
    """
    Function That Encodes the Original `MatchId` File-Names Into the New `MatchId` File-Names ( [0, 360] )
                                        
    Input: df = DataFrame We Want To Inspect
    
    Output: df_With_Encoded_MatchID = DataFrame With the `MatchId` Column's Values Encoded Into the New File-Names ( [0, 360] )
    """
    
    df_With_Encoded_MatchID = df.copy()
    
    
    
    # Outputting the Encoded & Decoded `MatchId` Column File-Names' Dictionaries
    
    MatchId_File_Name_Dictionary, Inverted_MatchId_File_Name_Dictionary = TFwDCFs.Encoding_and_Decoding_MatchID_FileName_Dictionaries()
    
    

    # Encoding the Original `MatchId` File-Names Into the New `MatchId` File-Names ( [0, 360] )
    
    df_With_Encoded_MatchID["MatchId"] = df_With_Encoded_MatchID["MatchId"].replace(MatchId_File_Name_Dictionary)
    
    
    
    
    return df_With_Encoded_MatchID










def Decoding_MatchID_Column_Into_New_FileNames( df ):
    """
    Function That Decodes the New `MatchId` File-Names ( [0, 360] ) Into the Original `MatchId` File-Names
                                        
    Input: df = DataFrame We Want To Inspect
    
    Output: df_With_Decoded_MatchID = DataFrame With the `MatchId` Column's Values Decoded From the New File-Names ( [0, 360] ) Into the Original `MatchId` File-Names
    """
    
    df_With_Decoded_MatchID = df.copy()
    
    
    
    # Outputting the Encoded & Decoded `MatchId` Column File-Names' Dictionaries
    
    MatchId_File_Name_Dictionary, Inverted_MatchId_File_Name_Dictionary = TFwDCFs.Encoding_and_Decoding_MatchID_FileName_Dictionaries()
    
    

    # Encoding the Original `MatchId` File-Names Into the New `MatchId` File-Names ( [0, 360] )
    
    df_With_Decoded_MatchID["MatchId"] = df_With_Decoded_MatchID["MatchId"].replace(Inverted_MatchId_File_Name_Dictionary)
    
    
    
    
    return df_With_Decoded_MatchID











###################################################
#     DEALING WITH MISSING VALUES FUNCTIONS       #
###################################################



def List_of_Row_Indices_Where_NaNs_Are_Present_In_Feature( df, column_name ):
    """
    Function That Displays the List of Row Indices Where Missing (`NaN`) Values Are Present In the Specified Column/Feature `column_name`
    
    Input: df = DataFrame We Want To Inspect
    Input: column_name = (String) Name of the Column/Feature We Want To Inspect
    
    Output: List_of_Row_Indices_Where_NaNs_Are_Present = List of Row Indices Where Missing (`NaN`) Values Are Present In the Specified Column/Feature `column_name`
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    List_of_Row_Indices_Where_NaNs_Are_Present = df.index[df[column_name].isna() == True].unique().tolist()
    
    
    return List_of_Row_Indices_Where_NaNs_Are_Present










def df_of_Row_Indices_Where_NaNs_Are_Present_In_Feature( df, list_of_row_indices_where_NaNs_are_present ):
    """
    Function That Displays the DataFrame of Row Indices Where Missing (`NaN`) Values Are Present In the Specified Column/Feature
    
    Input: df = DataFrame We Want To Inspect
    Input: list_of_row_indices_where_NaNs_are_present = List of Row Indices Where Missing (`NaN`) Values Are Present In the Specified Column/Feature `column_name`
    
    Output: df_of_Row_Indices_Where_NaNs_Are_Present = DataFrame of Row Indices Where Missing (`NaN`) Values Are Present
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    df_of_Row_Indices_Where_NaNs_Are_Present = df.loc[list_of_row_indices_where_NaNs_are_present]
    
    
    return df_of_Row_Indices_Where_NaNs_Are_Present










def Display_Columns_With_More_Than_50_Percent_Values_Missing( df, df_name, list_of_columns_to_inspect ):
    """
    Function That Displays the Columns of the DataFrame `df` Which Have >50% of Its Rows Filled Up With Missing (`NaN`) Values
    
    Input: df = DataFrame We Want To Inspect
    Input: df_name = (String) Name of the DataFrame We Want To Inspect
    Input: list_of_columns_to_inspect = List of Columns We Want To Inspect OR Single String Specifying the Unique Column To Inspect
    
    Output: String(s) Stating the % of Missing Values In a Set of Column(s)
    """
    
    Num_Rows_In_df = df.shape[0]
    
    
    for Column in list_of_columns_to_inspect:
        
        Num_Missing_Values_In_Column = df[Column].isna().sum()
        
        Percentage_of_Missing_Values_In_Column = (Num_Missing_Values_In_Column / Num_Rows_In_df) * 100
        
        
        if Percentage_of_Missing_Values_In_Column > 50.0:
            
            print(f"Column `{Column}` In DataFrame {df_name} Has {Percentage_of_Missing_Values_In_Column:.2f} % of Its Values Missing", '\n')










def Display_Number_of_Rows_With_More_Than_50_Percent_Values_Missing( df ):
    """
    Function That Displays How Many Rows There Are Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
    
    Input: df = DataFrame We Want To Inspect
    
    Output: Two_Column_List = A 2-Column List Displaying the #Missing (`NaN`) Values There Are Present In How Many #Rows Containing Those Amounts of Missing Values
                                i.e. (Left Column = List of #Missing Values / Right Column = List of #Rows Containing the #Missing Values Displayed To Their Left)
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    print("(Left Column = List of #Missing Values | Right Column = List of #Rows Containing the #Missing Values Displayed To Their Left)", '\n')
    
    
    Num_Columns_In_df = df.shape[1]
    
    Num_Missing_Values_Per_Row = df.isna().apply(lambda row: sum(row == True), axis = 1)

    Two_Column_List = Num_Missing_Values_Per_Row.value_counts()[ Num_Missing_Values_Per_Row.value_counts().index > Num_Columns_In_df/2 ]
    
    
    return Two_Column_List










def Display_Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing( df ):
    """
    Function That Displays the Indeces of the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
    
    Input: df = DataFrame We Want To Inspect
    
    Output: List_of_Row_Indeces_With_More_Than_50_Percent_Values_Missing = List of Indeces of the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
    """

    Num_Columns_In_df = df.shape[1]
    
    Num_Missing_Values_Per_Row = df.isna().apply(lambda row: sum(row == True), axis = 1)
    
    List_of_Row_Indeces_With_More_Than_50_Percent_Values_Missing = Num_Missing_Values_Per_Row[ Num_Missing_Values_Per_Row >= Num_Columns_In_df/2 ].index.tolist()
    
    
    print(f"#Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values, & ∴ Will Be Removed = \033[91m\033[1m\033[4m{len(List_of_Row_Indeces_With_More_Than_50_Percent_Values_Missing)}\033[0m", '\n')
    
    
    return List_of_Row_Indeces_With_More_Than_50_Percent_Values_Missing











###################################################
#                 EDA FUNCTIONS                   #
###################################################



def Correlation_Heat_Map_Between_Features( df, dataset_string_name, figure_size = (14, 12) ):
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



def Display_Missing_Values_From_Players_Info_Dataset( df ):
    """
    Function That Displays How Many Missing (`NaN`) Values There Is In Each Column/Feature In the Players' Info. Dataset
    
    Input: df = DataFrame We Want To Inspect
    
    Output: Two_Column_List = A 2-Column List Displaying the #Missing (`NaN`) Values There Is In Each Column/Feature  -  (Left Column = List of Column Names / Right Column = List of #Missing Values)
    """
    
    pd.set_option('display.max_rows', None)
    
    
    Num_Rows_Players_Info = df.shape[0]
    
    Num_Columns_Players_Info = df.shape[1]
    
    Num_Missing_Values_Players_Info_df = df.isna().apply(lambda column: column[column == True].count()).sum()
    

    print('\n',
          f"Total Number of Missing Values In the Players' Info. Dataset = {Num_Missing_Values_Players_Info_df}", '\n',
          f"This Represents {(Num_Missing_Values_Players_Info_df / (Num_Rows_Players_Info * Num_Columns_Players_Info))*100:.2f} % of the Players' Info. Dataset", '\n')
    
    
    
    # Explore How Many Missing Values (`NaN`) We Have In Each Column/Per Feature In the Tracking Data (For Macth `match_num`) Dataset

    Two_Column_List = df.isna().apply( lambda column: column[column == True].count() )
    
    
    
    return Two_Column_List










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



def Display_Missing_Values_From_Possessions_and_Targets_Dataset( df ):
    """
    Function That Displays How Many Missing (`NaN`) Values There Is In Each Column/Feature In the Possessions & Targets Dataset
    
    Input: df = DataFrame We Want To Inspect
    
    Output: Two_Column_List = A 2-Column List Displaying the #Missing (`NaN`) Values There Is In Each Column/Feature  -  (Left Column = List of Column Names / Right Column = List of #Missing Values)
    """
    
    pd.set_option('display.max_rows', None)
    
    
    Num_Rows_Possessions_and_Targets = df.shape[0]
    
    Num_Columns_Possessions_and_Targets = df.shape[1]
    
    Num_Missing_Values_Possessions_and_Targets_df = df.isna().apply(lambda column: column[column == True].count()).sum()
    

    print('\n',
          f"Total Number of Missing Values In the Possessions & Targets' Dataset = {Num_Missing_Values_Possessions_and_Targets_df}", '\n',
          f"This Represents {(Num_Missing_Values_Possessions_and_Targets_df / (Num_Rows_Possessions_and_Targets * Num_Columns_Possessions_and_Targets))*100:.2f} % of the Possessions & Targets' Dataset", '\n')
    
    
    
    # Explore How Many Missing Values (`NaN`) We Have In Each Column/Per Feature In the Tracking Data (For Macth `match_num`) Dataset

    Two_Column_List = df.isna().apply( lambda column: column[column == True].count() )[df.isna().apply( lambda column: column[column == True].count() ) > 0]
    
    
    
    return Two_Column_List










def Reducing_the_Possessions_and_Targets_Data( df, keep_corner_events_only = None, keep_freekick_events_only = None, keep_corner_and_freekick_events = None, remove_all_extra_events = None ):
    """
    Function That Reduces the Possessions & Targets' DataFrame `Possessions_and_Targets_df`
    
    Input: df = DataFrame We Want To Inspect  -->  Default: `df = Possessions_and_Targets_df`
    
    Only 1 of the Below 'Inputs' Must Be Set To "True"! - The Other Parameters May Be Ommitted Within the Function When Instanciating It:
    ↓
    Input: keep_corner_events_only = Boolean Value Stating Whether the Corner-Related Columns ("nextconerfor", "nextconeragainst", "nextconerfor_timeto", "nextconeragainst_timeto") Should Be Included Or Not
    Input: keep_freekick_events_only = Boolean Value Stating Whether the Free-Kick-Related Columns ("nextfreekickfor", "nextfreekickforx", "nextfreekickfory",
                                                                                                    "nextfreekickagainst", "nextfreekickagainstx", "nextfreekickagainsty",
                                                                                                    "nextfreekickfor_timeto", "nextfreekickagainst_timeto") Should Be Included Or Not
    Input: keep_corner_and_freekick_events = Boolean Value Stating Whether All the Above Stated Columns Should Be Included Or Not
    Input: remove_all_extra_events = Boolean Value Stating Whether All Extra Events-Related Columns Should Be Removed Or Not
    
    Output: Possessions_and_Targets_df_Reduced_Final = Final Reduced DataFrame of the Possessions & Targets' DataFrame `Possessions_and_Targets_df`
    """
    
    Possessions_and_Targets_df = df.copy()
    
    
    
    TFwDCFs.Display_Missing_Values_From_Possessions_and_Targets_Dataset(df)
    
    
    
    
    if keep_corner_events_only == True:
        
        Possessions_and_Targets_df_Reduced_With_Corners_Only = Possessions_and_Targets_df.drop(columns = ["nextpenaltyfor", "nextpenaltyagainst", "nextpenaltyfor_timeto", "nextpenaltyagainst_timeto",
                                                                                                                  "nextthrowfor", "nextthrowagainst", "nextthrowfor_timeto", "nextthrowagainst_timeto",
                                                                                                                  "nextfreekickfor", "nextfreekickforx", "nextfreekickfory",
                                                                                                                  "nextfreekickagainst", "nextfreekickagainstx", "nextfreekickagainsty",
                                                                                                                  "nextfreekickfor_timeto", "nextfreekickagainst_timeto"],
                                                                                                       inplace = False)
        
        
        Possessions_and_Targets_df_Reduced = Possessions_and_Targets_df_Reduced_With_Corners_Only
        
        print(f"New Dimensions of the Possessions & Targets' Dataset After Removing the Unneccessary/Irrelevant Columns = {Possessions_and_Targets_df_Reduced.shape}", '\n')
        


    if keep_freekick_events_only == True:
        
        Possessions_and_Targets_df_Reduced_With_FreeKicks_Only = Possessions_and_Targets_df.drop(columns = ["nextpenaltyfor", "nextpenaltyagainst", "nextpenaltyfor_timeto", "nextpenaltyagainst_timeto",
                                                                                                                    "nextconerfor", "nextconeragainst", "nextconerfor_timeto", "nextconeragainst_timeto",
                                                                                                                    "nextthrowfor", "nextthrowagainst", "nextthrowfor_timeto", "nextthrowagainst_timeto"],
                                                                                                         inplace = False)
        
        
        Possessions_and_Targets_df_Reduced = Possessions_and_Targets_df_Reduced_With_FreeKicks_Only
        
        print(f"New Dimensions of the Possessions & Targets' Dataset After Removing the Unneccessary/Irrelevant Columns = {Possessions_and_Targets_df_Reduced.shape}", '\n')
        
        

    if keep_corner_and_freekick_events == True:
        
        Possessions_and_Targets_df_Reduced_With_FreeKicks_and_Corners = Possessions_and_Targets_df.drop(columns = ["nextpenaltyfor", "nextpenaltyagainst", "nextpenaltyfor_timeto", "nextpenaltyagainst_timeto",
                                                                                                                           "nextthrowfor", "nextthrowagainst", "nextthrowfor_timeto", "nextthrowagainst_timeto"],
                                                                                                                inplace = False)
        
        
        Possessions_and_Targets_df_Reduced = Possessions_and_Targets_df_Reduced_With_FreeKicks_and_Corners
        
        print(f"New Dimensions of the Possessions & Targets' Dataset After Removing the Unneccessary/Irrelevant Columns = {Possessions_and_Targets_df_Reduced.shape}", '\n')
        
        
        
    if remove_all_extra_events == True:
        
        Possessions_and_Targets_df_Reduced_Without_Extra_Events = Possessions_and_Targets_df.drop(columns = ["nextpenaltyfor", "nextpenaltyagainst", "nextpenaltyfor_timeto", "nextpenaltyagainst_timeto",
                                                                                                                     "nextconerfor", "nextconeragainst", "nextconerfor_timeto", "nextconeragainst_timeto",
                                                                                                                     "nextthrowfor", "nextthrowagainst", "nextthrowfor_timeto", "nextthrowagainst_timeto",
                                                                                                                     "nextfreekickfor", "nextfreekickforx", "nextfreekickfory",
                                                                                                                     "nextfreekickagainst", "nextfreekickagainstx", "nextfreekickagainsty",
                                                                                                                     "nextfreekickfor_timeto", "nextfreekickagainst_timeto"],
                                                                                                          inplace = False)
        
        
        Possessions_and_Targets_df_Reduced = Possessions_and_Targets_df_Reduced_Without_Extra_Events
        
        print(f"New Dimensions of the Possessions & Targets' Dataset After Removing the Unneccessary/Irrelevant Columns = {Possessions_and_Targets_df_Reduced.shape}", '\n')
        
        
        
        
        
    TFwDCFs.Display_Missing_Values_From_Possessions_and_Targets_Dataset(Possessions_and_Targets_df_Reduced)        

    
    
    return Possessions_and_Targets_df_Reduced










def Adding_Shots_and_Goals_To_Possessions_and_Targets_Dataset( df ):
    """
    Function That Adds 2 New Columns To the Possessions & Targets' Dataset: `Will_Be_a_Shot` & `Will_Be_a_Goal`, Representing Whether a Shot or a Goal Occurred/Will Occur Within 10s of the Possession.
        Optionally, It Also Drops/Removes All the Next-Goal-Related Columns; This Is Done To Avoid Having Any Missing (`NaN`) Values Present In the Dataset.
    
    Input: df = DataFrame We Want To Inspect
    Input: remove_next_goal_related_columns = Boolean Value Stating Whether All Next-Goal-Related Columns Should Be Removed Or Not
    
    Output: df_Shots_and_Goals = Possessions & Targets DataFrame With Shots & Goals Indications Included 
    """
    
    df_Shots_and_Goals = df.copy()
    
    
    #  Create (Target) Variable `Will_Be_a_Shot` Extracting Whether There Will Be a Shot/Chance To Score Within the Next 10s (≡ 250 Frames), This Info./Threshold Being Intrinsically Encapsulated Within the `nextxgfor/against` Columns

    df_Shots_and_Goals["Will_Be_a_Shot"] = 0.0    

    df_Shots_and_Goals.loc[ ( df_Shots_and_Goals["nextxgfor"] > 0 ) | ( df_Shots_and_Goals["nextxgagainst"] > 0 ), "Will_Be_a_Shot" ] = 1.0
    
    
    
    
    # Create (Target) Variable `Will_Be_a_Goal` Extracting Whether There Will Be a Goal Within the Next 10s (≡ 250 Frames)
    
    Frames_Window_10s = 250
    

    df_Shots_and_Goals["Will_Be_a_Goal"] = 0.0    

    df_Shots_and_Goals.loc[ ( df_Shots_and_Goals["nextgoalfor_timeto"] <= Frames_Window_10s ) | ( df_Shots_and_Goals["nextgoalagainst_timeto"] <= Frames_Window_10s ), "Will_Be_a_Goal" ] = 1.0
        

    
    
    
    # Check For "Unrecorded" Goals That Did Very Clearly Occur, But the Possessions 10s Before the Goal Leading Up TO It Has Not Been Recorded/Logged-In Into the Dataset
    
    for Row in range(len(df_Shots_and_Goals.index)):
    
        if Row == ( len(df_Shots_and_Goals.index) - 1):
        
            continue
        
        
        
        # Case Number 1:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 1.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 1.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
    
        # Case Number 2:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 1.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 1.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
    
        # Case Number 3:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 2.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 2.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
    
        # Case Number 4:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 2.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 2.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
            
        
        
        # Case Number 5:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 1.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 2.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst_timeto"] ) ):
    #if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 1.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 2.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
        
        # Case Number 6:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 1.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 2.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
    
        # Case Number 7:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 2.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 1.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalfor_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalagainst_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
    
        # Case Number 8:
    
        if ( ( df_Shots_and_Goals.iloc[Row]["teams"] == 2.0 ) & ( df_Shots_and_Goals.iloc[Row + 1]["teams"] == 1.0 ) ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst"] != df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( ( df_Shots_and_Goals.iloc[Row + 1]["frames"] >= (df_Shots_and_Goals.iloc[Row]["frames"] + df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"]) ) & ( df_Shots_and_Goals.iloc[Row + 1]["frames"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor"] ) & ( df_Shots_and_Goals.iloc[Row]["nextgoalagainst_timeto"] < df_Shots_and_Goals.iloc[Row + 1]["nextgoalfor_timeto"] ) ):
        
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Shot")] = 1.0
            df_Shots_and_Goals.iloc[Row, df_Shots_and_Goals.columns.get_loc("Will_Be_a_Goal")] = 1.0
    
    
    
    
    
    
    # Inspecting & Displaying Any Missing Values Remaining (This Should Hopefully Output 0 Missing Values)
    
    TFwDCFs.Display_Missing_Values_From_Possessions_and_Targets_Dataset(df_Shots_and_Goals)
    
    print(f"New Dimensions of the Possessions & Targets' Dataset = {df_Shots_and_Goals.shape}", '\n')
    
    
    
    
    # Save Reduced Version of the Tracking Data As a New ".parquet" File
    
    df_Shots_and_Goals.to_parquet(f"Possessions_and_Targets_With_Shots_and_Goals.parquet", engine = "auto")
    
    
    
    return df_Shots_and_Goals










def Filter_Shots_and_Goals_Only_Possessions_and_Targets_Dataset( df ):
    """
    Function That Filters In All the Possessions That Will End Up Being a Shot Or a Goal.
        Then It Saves This Final Dataset As a `.parquet` File Named As `Possessions_and_Targets_of_Shots_and_Goals_Only_Clean.parquet` --> This Dataset Will Be the One Used For Our Models
    
    Input: df = DataFrame We Want To Inspect
    
    Output: df_Shots_and_Goals_Only = Filtered Version of the DataFrame, Containing Only Those Possessions That Will End Up Being a Shot Or a Goal
    """
    
    df_Shots_and_Goals_Only = df[ df["Will_Be_a_Shot"] == 1.0 ]
    
    
    # Inspecting & Displaying Any Missing Values Remaining (This Should Hopefully Output 0 Missing Values)
    
    TFwDCFs.Display_Missing_Values_From_Possessions_and_Targets_Dataset(df_Shots_and_Goals_Only)
    
    print(f"New Dimensions of the Final Possessions & Targets' Dataset of Only Shots & Goals = {df_Shots_and_Goals_Only.shape}", '\n')

    
    
    
    return df_Shots_and_Goals_Only










def Save_Possessions_and_Targets_df( possessions_df_with_next_goal_related_columns, remove_next_goal_related_columns = True ):
    """
    Function That Saves the Possessions & Targets DataFrame As a `.parquet` File
    
    Input: possessions_df_with_next_goal_related_columns = Possessions & Targets DataFrame That I Want To Save (As It Is, Or After Dropping the `nextgoal`-Related Columns)
    Input: are_next_goal_related_columns_removed = Boolean Value, Stating Whether the `nextgoalfor/against` & `nextgoalfor/against_timeto` Columns Should Be Removed From the DataFrame `possessions_df` To Be Saved; Default == True
    
    Output: String Stating That the File Was Successfully Saved
    """
    
    if remove_next_goal_related_columns == True:
        
        possessions_df_without_next_goal_related_columns = possessions_df_with_next_goal_related_columns.drop(columns = ["nextgoalfor", "nextgoalagainst", "nextgoalfor_timeto", "nextgoalagainst_timeto"], inplace = False)
        
               
        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (Without the `nextgoal`-Related Columns Present) = {possessions_df_without_next_goal_related_columns.shape}", '\n')
        
        
        if possessions_df_without_next_goal_related_columns.shape[1] == 13:
            
            
            # Save Possessions & Targets DataFrame As a New ".parquet" File
    
            possessions_df_without_next_goal_related_columns.to_parquet(f"Possessions_and_Targets_of_Shots_and_Goals_Only_Without_NextGoal_Related_Columns.parquet", engine = "auto")
            
            
            return print(f"\033[92m\033[1m Possessions' & Targets' Data of Shots + Goals Only (Without `nextgoal`-Related Columns) --> Succesfully Saved \033[0m", '\n')
        
        
        
        if possessions_df_without_next_goal_related_columns.shape[1] != 13:
            
            return print(f"\033[92m\033[1m --> Columns Were Not Removed Properly! \033[0m", '\n')
    
    
    
    
    if remove_next_goal_related_columns == False:
        
        print(f"Dimensions of the Version of the Possessions' & Targets' Dataset, In Which Only Possessions Leading-Up To a Shot &/Or Goal Are Included (With the `nextgoal`-Related Columns Present) = {possessions_df_with_next_goal_related_columns.shape}", '\n')
        
        
        if possessions_df_with_next_goal_related_columns.shape[1] == 17:
            
            # Save Possessions & Targets DataFrame As a New ".parquet" File
    
            possessions_df_with_next_goal_related_columns.to_parquet(f"Possessions_and_Targets_of_Shots_and_Goals_Only_With_NextGoal_Related_Columns.parquet", engine = "auto")
        
            
            return print(f"\033[92m\033[1m Possessions' & Targets' Data of Shots + Goals Only (With `nextgoal`-Related Columns) --> Succesfully Saved \033[0m", '\n')
        
        
        
        if possessions_df_with_next_goal_related_columns.shape[1] != 17:
            
            return print(f"\033[92m\033[1m --> Something Went Wrong! \033[0m", '\n')


    
    
    
    
    
    
    

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











###################################################
#        TRACKING DATA-RELATED FUNCTIONS          #
###################################################



def Read_Original_Match_Tracking_Data( match_num = None ):
    """
    Function That Reads the Original Tracking Data File of the Specified Football Match Number `match_num`
    
    Input: match_num = Integer Number Representing the "match_num.parquet" File Containing the Tracking Data of That Football Match
    
    Output: Tracking_Data_Match_df = DataFrame of the "match_num.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    match_num = int(input("For Which Match Would You Like To Load & Read Its Respective Tracking Data? -- NOTE: Must Choose a Number In the Range [0, 360]  -->  "))
    
    print('\n',
          f"Loading & Reading In the Tracking Data For Match #{match_num + 1}",
          '\n')
    
    
    Tracking_Data_Folder = "Tracking Data/"
    
    Tracking_Data_Match_df = pd.read_parquet(f"{Tracking_Data_Folder}{match_num}.parquet", engine = "auto")
    
    
    
    
    # Dimensions of the Dataset of the Tracking Data For Match `match_num`

    print(f"Dimensions of the Dataset of the Tracking Data For Match #{match_num + 1} = {Tracking_Data_Match_df.shape}", '\n')
    
    
    return Tracking_Data_Match_df










def Display_Missing_Values_From_Original_Match_Tracking_Data( match_num = None ):
    """
    Function That Displays How Many Missing (`NaN`) Values There Is In Each Column/Feature In the Original Tracking Data (For Match `match_num`) Dataset That Does Have Missing Values Present
    
    Input: match_num = Integer Number Representing the "match_num.parquet" File Containing the Tracking Data of That Football Match
    
    Output: Two_Column_List = A 2-Column List Displaying the #Missing (`NaN`) Values There Is In Each Column/Feature  -  (Left Column = List of Column Names / Right Column = List of #Missing Values)
    """
    
    pd.set_option('display.max_rows', None)

    
    
    match_num = int(input("For Which Match Would You Like To Load & Read Its Respective Tracking Data? -- NOTE: Must Choose a Number In the Range [0, 360]  -->  "))
    
    
    
    
    # Read-In/Load-In the Tracking Dataset For Match `match_num`
    
    print('\n',
          f"Loading & Reading In the Tracking Data For Match #{match_num + 1}",
          '\n')
    
    
    Tracking_Data_Folder = "Tracking Data/"
    
    Tracking_Data_Match_df = pd.read_parquet(f"{Tracking_Data_Folder}{match_num}.parquet", engine = "auto")
    
    
    
    
    # Dimensions of the Dataset of the Tracking Data For Match `match_num`

    print(f"Dimensions of the Dataset of the Tracking Data For Match #{match_num + 1} = {Tracking_Data_Match_df.shape}", '\n')

    Num_Rows_Tracking_Data_Match = Tracking_Data_Match_df.shape[0]

    Num_Columns_Tracking_Data_Match = Tracking_Data_Match_df.shape[1]
    
    
    
    Num_Missing_Values_Tracking_Data_Match_df = Tracking_Data_Match_df.isna().apply(lambda column: column[column == True].count()).sum()

    print(f"Total Number of Missing Values In the Tracking Data (For Match #{match_num + 1}) Dataset = {Num_Missing_Values_Tracking_Data_Match_df}", '\n',
          f"This Represents {(Num_Missing_Values_Tracking_Data_Match_df / (Num_Rows_Tracking_Data_Match * Num_Columns_Tracking_Data_Match))*100:.2f} % of the Tracking Data (For Match #{match_num + 1}) Dataset",
          '\n')
    
    
    
    
    # Explore How Many Missing Values (`NaN`) We Have In Each Column/Per Feature In the Tracking Data (For Macth `match_num`) Dataset

    Two_Column_List = Tracking_Data_Match_df.isna().apply( lambda column: column[column == True].count() )[Tracking_Data_Match_df.isna().apply( lambda column: column[column == True].count() ) > 0]
    
    
    
    return Two_Column_List










def Display_Missing_Values_From_Modified_Match_Tracking_Data( match_tracking_data_df, match_num ):
    """
    Function That Displays How Many Missing (`NaN`) Values There Is In Each Column/Feature In the Currently Modified Tracking Data Dataset
    
    Input: match_tracking_data_df = DataFrame of the Currently Modified Tracking Data Dataset
    Input: match_num = Number (- 1) of the Match For Which We Are Reading It's Tracking Data
    
    Output: Two_Column_List = A 2-Column List Displaying the #Missing (`NaN`) Values There Is In Each Column/Feature  -  (Left Column = List of Column Names / Right Column = List of #Missing Values)
    """
    
    pd.set_option('display.max_rows', None)

    
    
    # Dimensions of the Dataset of the Tracking Data For Match `match_num`

    print(f"Dimensions of the Dataset of the Currently Modified Tracking Data For Match #{match_num + 1} = {match_tracking_data_df.shape}", '\n')

    Num_Rows_Tracking_Data_Match = match_tracking_data_df.shape[0]

    Num_Columns_Tracking_Data_Match = match_tracking_data_df.shape[1]
    
    
    
    Num_Missing_Values_Tracking_Data_Match_df = match_tracking_data_df.isna().apply(lambda column: column[column == True].count()).sum()

    print(f"Total Number of Missing Values In the Tracking Data (For Match #{match_num + 1}) Dataset = {Num_Missing_Values_Tracking_Data_Match_df}", '\n',
          f"This Represents {(Num_Missing_Values_Tracking_Data_Match_df / (Num_Rows_Tracking_Data_Match * Num_Columns_Tracking_Data_Match))*100:.2f} % of the Tracking Data (For Match #{match_num + 1}) Dataset",
          '\n')
    
    
    
    
    # Explore How Many Missing Values (`NaN`) We Have In Each Column/Per Feature In the Tracking Data (For Macth `match_num`) Dataset

    Two_Column_List = match_tracking_data_df.isna().apply( lambda column: column[column == True].count() )[match_tracking_data_df.isna().apply( lambda column: column[column == True].count() ) > 0]
    
    
    
    return Two_Column_List










def Cleaning_Match_Tracking_Data( matches_to_clean = range(0, 361) ):
    """
    Function That Reduces & Cleans the Match Tracking Data For Match #`match_num`, By Removing/Dropping the Following Columns: "frame", "timestamp", "period", "possession.group", "possession.trackable_object"
                                                                                   & By Removing/Dropping All Those Rows/Indeces Where There Are Missing Values Present In the Players' & Ball's Speeds Columns: `S` & `S1`-`S22`
                                                                                   
    Input: matches_to_clean = List Or Range `range( ·, ·)` of Matches To Be Cleaned
    
    Output: Match_Tracking_Data_df_Clean = Reduced & Clean Version of the DataFrame of the Match Tracking Data
    """
    
    pd.set_option('display.max_rows', None)
    
        
    
    Match_Numbers = matches_to_clean

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Tracking_Data_Match_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Original Dataset of the Tracking Data For Match #{Match_Num + 1} = {Tracking_Data_Match_df.shape}", '\n')
    
    
    
    
        # Dropping/Removing the Unnecessary or Irrelevant Columns
    
        Match_Tracking_Data_df_Reduced = Tracking_Data_Match_df.copy()

        Match_Tracking_Data_df_Reduced.drop(columns = ["frame", "timestamp", "period", "possession.group", "possession.trackable_object"],
                                            inplace = True)

        print(f'New Dimensions of the Reduced Tracking Data For Match #{Match_Num + 1} After Removing the Unneccessary/Irrelevant Columns = {Match_Tracking_Data_df_Reduced.shape}', '\n')
    
    
    
    
        # Dropping/Removing the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
    
        Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing_Match_Tracking_Data = TFwDCFs.Display_Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing(df = Match_Tracking_Data_df_Reduced)

        Match_Tracking_Data_df_Reduced.drop(index = Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing_Match_Tracking_Data,
                                             inplace = True)
    

        print(f'New Dimensions of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Which Have >50% of Its Values Missing = {Match_Tracking_Data_df_Reduced.shape}', '\n')
    
    
    
    
        # Finding the Indices/Rows Where Missing (`NaN`) Values Are Present In the Following Columns: `S` & `S1`-`S22`

        Indices_Where_Players_and_Ball_Speeds_Are_Missing = Match_Tracking_Data_df_Reduced.index[(Match_Tracking_Data_df_Reduced["S"].isna() == True) | (Match_Tracking_Data_df_Reduced["S1"].isna() == True) & (Match_Tracking_Data_df_Reduced["S2"].isna() == True) & (Match_Tracking_Data_df_Reduced["S3"].isna() == True) & (Match_Tracking_Data_df_Reduced["S4"].isna() == True) & (Match_Tracking_Data_df_Reduced["S5"].isna() == True) & (Match_Tracking_Data_df_Reduced["S6"].isna() == True) & (Match_Tracking_Data_df_Reduced["S7"].isna() == True) & (Match_Tracking_Data_df_Reduced["S8"].isna() == True) & (Match_Tracking_Data_df_Reduced["S9"].isna() == True) & (Match_Tracking_Data_df_Reduced["S10"].isna() == True) & (Match_Tracking_Data_df_Reduced["S11"].isna() == True) & (Match_Tracking_Data_df_Reduced["S12"].isna() == True) & (Match_Tracking_Data_df_Reduced["S13"].isna() == True) & (Match_Tracking_Data_df_Reduced["S14"].isna() == True) & (Match_Tracking_Data_df_Reduced["S15"].isna() == True) & (Match_Tracking_Data_df_Reduced["S16"].isna() == True) & (Match_Tracking_Data_df_Reduced["S17"].isna() == True) & (Match_Tracking_Data_df_Reduced["S18"].isna() == True) & (Match_Tracking_Data_df_Reduced["S19"].isna() == True) & (Match_Tracking_Data_df_Reduced["S20"].isna() == True) & (Match_Tracking_Data_df_Reduced["S21"].isna() == True) & (Match_Tracking_Data_df_Reduced["S22"].isna() == True)].unique().tolist()
    
    
        print(f"#Rows Which Have the Players' and the Ball's Speed Values Missing, & ∴ Will Be Removed = \033[91m\033[1m\033[4m{len(Indices_Where_Players_and_Ball_Speeds_Are_Missing)}\033[0m", '\n')
    
    
        Match_Tracking_Data_df_Clean = Match_Tracking_Data_df_Reduced.drop(index = Indices_Where_Players_and_Ball_Speeds_Are_Missing, inplace = False)
    
    
        print(f"New Dimensions of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Where Values For the Players' and the Ball's Speeds Are Missing = \033[91m\033[1m\033[4m{Match_Tracking_Data_df_Clean.shape}\033[0m", '\n')
    
    
        Num_Rows_Tracking_Data = Match_Tracking_Data_df_Clean.shape[0]

        Num_Columns_Tracking_Data = Match_Tracking_Data_df_Clean.shape[1]
    
    
    
        Num_Missing_Values_Tracking_Data_df_Clean = Match_Tracking_Data_df_Clean.isna().apply(lambda column: column[column == True].count()).sum()

        print(f"Total Number of Missing Values In the Final Tracking Data (For Match #{Match_Num + 1}) Dataset = \033[91m\033[1m\033[4m{Num_Missing_Values_Tracking_Data_df_Clean}\033[0m", '\n',
              f"This Represents \033[91m\033[1m\033[4m{(Num_Missing_Values_Tracking_Data_df_Clean / (Num_Rows_Tracking_Data * Num_Columns_Tracking_Data))*100:.2f} %\033[0m of the Final Tracking Data (For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m) Dataset",
              '\n')
    
    
    
        # Save Reduced Version of the Tracking Data As a New ".parquet" File
    
        Match_Tracking_Data_df_Clean.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Clean.parquet", engine = "auto")
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
    
    
    return  print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Read_Clean_Match_Tracking_Data( match_num = None ):
    """
    Function That Reads the Clean Version of the Tracking Data of the Specified Football Match Number `match_num`
    
    Input: match_num = Integer Number Representing the "match_num.parquet" File Containing the Tracking Data of That Football Match
    
    Output: Clean_Match_Tracking_Data_df = Clean Version of the DataFrame of the "match_num_Clean.parquet" File Containing the Tracking Data of the Specified Football Match
    """
    
    match_num = int(input("For Which Match Would You Like To Load & Read Its Respective Tracking Data? -- NOTE: Must Choose a Number In the Range [0, 360]  -->  "))
    
    print('\n',
          f"Loading & Reading In the Tracking Data For Match #{match_num + 1}",
          '\n')
    
    
    Tracking_Data_Folder = "Tracking Data/"    
    
    Clean_Match_Tracking_Data_df = pd.read_parquet(f"{Tracking_Data_Folder}{match_num}_Clean.parquet", engine = "auto")
    
    
    
    
    # Dimensions of the Dataset of the Clean Tracking Data For Match `match_num`

    print(f"Dimensions of the Dataset of the Tracking Data For Match #{match_num + 1} = {Clean_Match_Tracking_Data_df.shape}", '\n')
    
    
    return Clean_Match_Tracking_Data_df










def Display_Remaining_Missing_Values_From_Clean_Match_Tracking_Data( matches_to_display = range(0, 361) ):
    """
    Function That Displays How Many Missing (`NaN`) Values There Is In Each Column/Feature In the Currently "Cleaned" Tracking Data Dataset
    
    Input: matches_to_display = List Or Range `range( ·, ·)` of Matches To Be Displayed
    Input: match_num = Number (- 1) of the Match For Which We Are Reading It's Tracking Data
    
    Output: Two_Column_List = A 2-Column List Displaying the #Missing (`NaN`) Values There Is In Each Column/Feature  -  (Left Column = List of Column Names / Right Column = List of #Missing Values)
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    Match_Numbers = matches_to_display

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Match_Tracking_Data_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Clean.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the "Clean" Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Original 'Clean' Dataset of the Tracking Data For Match #{Match_Num + 1} = {Match_Tracking_Data_df.shape}", '\n')

        Num_Rows_Match_Tracking_Data = Match_Tracking_Data_df.shape[0]

        Num_Columns_Match_Tracking_Data = Match_Tracking_Data_df.shape[1]
    
    
    
        Num_Missing_Values_Match_Tracking_Data_df = Match_Tracking_Data_df.isna().apply(lambda column: column[column == True].count()).sum()

        print(f"Total Number of Missing Values In the Tracking Data (For Match #{Match_Num + 1}) Dataset = \033[91m\033[1m\033[4m{Num_Missing_Values_Match_Tracking_Data_df}\033[0m", '\n',
              f"This Represents \033[91m\033[1m\033[4m{(Num_Missing_Values_Match_Tracking_Data_df / (Num_Rows_Match_Tracking_Data * Num_Columns_Match_Tracking_Data))*100:.2f} %\033[0m of the Tracking Data (For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m) Dataset",
              '\n')
    
    
    
    
        # Explore How Many Missing Values (`NaN`) We Have In Each Column/Per Feature In the Tracking Data (For Macth `match_num`) Dataset

        Two_Column_List = Match_Tracking_Data_df.isna().apply( lambda column: column[column == True].count() )[Match_Tracking_Data_df.isna().apply( lambda column: column[column == True].count() ) > 0]
        
        print(Two_Column_List)
    
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
    
    
    
    return print("\033[92m\033[1m FINISHED \033[0m")










def Calculate_Players_and_Ball_Velocities_and_Speeds( match_tracking_data_df, metric_unit = "cm/s", max_speed = 1200, smoothing = True, filter_type = "Savitzky-Golay", smoothing_window_size = 125, order_of_polynomial = 1 ):
    """ 
    Inspiration From @author: Laurie Shaw (@EightyFivePoint) 2020 From the Soccermatics Online Course
    
    
    Function That Calculates Players' + Ball's Velocities In x- & y- Direciton (i.e. V_x & V_y), & Their Respective Magnitude/Speed At Each Time-Step (25Hz ≡ 0.04s ≡ 1 Frame) of the Match Tracking Data
    
    Input: match_tracking_data_df = DataFrame of the Match Tracking Data Dataset
    Input: metric_unit = Metric Unit In Which the Velocity Components & Speeds Should Be Calculated In; Options  -->  {"cm/s", "m/s"}; Default == "cm/s"
    Input: max_speed = Maximum Speed That a Player Can Realisitically Achieve. Speed Measures That Exceed `max_speed` Are Tagged As Outliers & Set To `max_speed`; Default == 1200 [cm/s]
    Input: smoothing = Boolean Value, That Determines Whether Velocity Measures Should Be Smoothed Or Not; Default == True
    Input: filter_type = Type of Filter To Use When Smoothing the Velocities; Options  -->  {"Savitzky-Golay", "Moving Average"}; Default == "Savitzky-Golay"
    Input: smoothing_window_size = Smoothing Window Size In #Frames - In Case `filter_type = "Savitzky-Golay"` --> Value Must Be An Odd Number, So That the Filter Is Symmetric; Default == 125
    Input: order_of_polynomial = Order of the Polynomial For the "Savitzky-Golay" Filter; Default == 1  (i.e. A Linear Fit To the Velocity ⇒ Gradient ≡ Acceleration)
    
    Output: Match_Tracking_Data_With_Velocities_and_Speeds_df = DataFrame of the Match Tracking Data Dataset With Columns For Velocity Components In the x- & y- Direction (i.e. "V_x{Player_Number}" & "V_y{Player_Number}") & Total Magnitude "Speed" Added At the End of the DataFrame
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    Match_Tracking_Data_With_Velocities_and_Speeds_df = match_tracking_data_df.copy()

    
    
    # Get the Players' IDs
    
    Players_Numbers = []

    for Player_Number in range(1, 23):
    
        Players_Numbers.append(str(Player_Number))
    

    # Calculate the Time-Step From 1 Frame To the Next Frame. Should Always Be = 0.04s Within the Same Half
    
    dt = Match_Tracking_Data_With_Velocities_and_Speeds_df["T"].diff()
    
    dt = dt.dt.total_seconds()
    
    
    # Index of First Frame In 2nd-Half
    
    Second_Half_Index = Match_Tracking_Data_With_Velocities_and_Speeds_df["Section"].idxmax(0)
    
    
    
    
    # Difference In Ball's Position In Time-Step `dt` To Get Unsmoothed Estimate of the Velocity Components In the x-, y- & z-Directions
        
    V_x_Ball = Match_Tracking_Data_With_Velocities_and_Speeds_df["X"].diff() / dt
    V_y_Ball = Match_Tracking_Data_With_Velocities_and_Speeds_df["Y"].diff() / dt
    V_z_Ball = Match_Tracking_Data_With_Velocities_and_Speeds_df["Z"].diff() / dt
    
    Speed_Magnitude_Ball = np.sqrt( V_x_Ball**2 + V_y_Ball**2 + V_z_Ball**2 )
    
    
    if smoothing == True:
            
            if filter_type == "Savitzky-Golay":   # Fits a Polynomial of Order `order_of_polynomial` To the Data Within Each `smoothing_window_size`
                
                # Calculate 1st-Half Velocities
                
                print(f"Checking the Size/Length of the Data For the 1st Half of the Match Is \033[91m\033[1m\033[4m>{smoothing_window_size}\033[0m --> 1st Half's Data Length = \033[91m\033[1m\033[4m{len(V_x_Ball.loc[ : Second_Half_Index])}\033[0m", '\n')
                
                V_x_Ball.loc[ : Second_Half_Index] = signal.savgol_filter(V_x_Ball.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                V_y_Ball.loc[ : Second_Half_Index] = signal.savgol_filter(V_y_Ball.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                V_z_Ball.loc[ : Second_Half_Index] = signal.savgol_filter(V_z_Ball.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                
                
                # Calculate 2nd-Half Velocities
                      
                print(f"Checking the Size/Length of the Data For the 2nd Half of the Match Is \033[91m\033[1m\033[4m>{smoothing_window_size}\033[0m --> 2nd Half's Data Length = \033[91m\033[1m\033[4m{len(V_x_Ball.loc[Second_Half_Index : ])}\033[0m", '\n')
                
                V_x_Ball.loc[Second_Half_Index : ] = signal.savgol_filter(V_x_Ball.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                V_y_Ball.loc[Second_Half_Index : ] = signal.savgol_filter(V_y_Ball.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                V_z_Ball.loc[Second_Half_Index : ] = signal.savgol_filter(V_z_Ball.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                
                 
            
            elif filter_type == "Moving Average":
                
                ma_smoothing_window_size = np.ones( smoothing_window_size ) / smoothing_window_size 
                
                
                # Calculate 1st-Half Velocities
                
                V_x_Ball.loc[ : Second_Half_Index] = np.convolve( V_x_Ball.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" ) 
                V_y_Ball.loc[ : Second_Half_Index] = np.convolve( V_y_Ball.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" )
                V_z_Ball.loc[ : Second_Half_Index] = np.convolve( V_z_Ball.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" )
                
                
                # Calculate 2nd-Half Velocities
                
                V_x_Ball.loc[Second_Half_Index : ] = np.convolve( V_x_Ball.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" ) 
                V_y_Ball.loc[Second_Half_Index : ] = np.convolve( V_y_Ball.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" )
                V_z_Ball.loc[Second_Half_Index : ] = np.convolve( V_z_Ball.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" )
                
                
                
                
    # Put Ball's Velocity Components In x- & y- Direction, & Total Magnitude/Speed Back In the DataFrame
        
    Match_Tracking_Data_With_Velocities_and_Speeds_df["V_xBall"] = V_x_Ball
    Match_Tracking_Data_With_Velocities_and_Speeds_df["V_yBall"] = V_y_Ball
    Match_Tracking_Data_With_Velocities_and_Speeds_df["V_zBall"] = V_z_Ball
    Match_Tracking_Data_With_Velocities_and_Speeds_df["SpeedBall"] = np.sqrt( V_x_Ball**2 + V_y_Ball**2 + V_z_Ball**2 )
                
                
    
    
    # Estimate Velocities' Components V_x & V_y For Players In `Match_Tracking_Data_With_Velocities_and_Speeds_df`
    
    for Player_Number in Players_Numbers:  # Cycle Through Players Individually
        
        # Difference In Players' Positions In Time-Step `dt` To Get Unsmoothed Estimate of the Velocity Components
        
        V_x = Match_Tracking_Data_With_Velocities_and_Speeds_df["X" + Player_Number].diff() / dt
        V_y = Match_Tracking_Data_With_Velocities_and_Speeds_df["Y" + Player_Number].diff() / dt
        
        
        # Maximum Speed That a Player Can Realisitically Achieve. Speed Measures That Exceed `max_speed` Are Tagged As Outliers & Set To `max_speed` 
        
        if metric_unit == "cm/s":
        
            if max_speed > 0:
            
                # Remove Unsmoothed Data Points That Exceed the Maximum Speed (These Are Most Likely Position Errors)
                # If Maximum Speed Is Exceeded -->  Assign the `V_x_max` & `V_y_max` Value to the `V_x` & `V_y` Columns Instead, Since This Specific Value Will Ensure That the Speed Magnitude == `max_speed`
            
                Speed_Magnitude = np.sqrt( V_x**2 + V_y**2 )
                
                if ( np.abs(V_x) == np.abs(V_y) ).any():
                    
                    V_x_max = np.sqrt( max_speed**2 / 2 )
                    V_y_max = np.sqrt( max_speed**2 / 2 )
                        
                        
                    if ( np.sign(V_x) == 1 ).any():
            
                        V_x[ Speed_Magnitude > max_speed ] = V_x_max
                
                    if ( np.sign(V_x) == -1 ).any():
                        
                        V_x[ Speed_Magnitude > max_speed ] = -V_x_max
                            
                    if ( np.sign(V_y) == 1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = V_y_max
                            
                    if ( np.sign(V_y) == -1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = -V_y_max
            
                        # V_x[ Speed_Magnitude > max_speed ] = np.nan
                        # V_y[ Speed_Magnitude > max_speed ] = np.nan
                    
                    
                if ( np.abs(V_x) > np.abs(V_y) ).any():
                        
                    V_x_max = np.sqrt( max_speed**2 - V_y**2 )
                        
                        
                    if ( np.sign(V_x) == 1 ).any():
            
                        V_x[ Speed_Magnitude > max_speed ] = V_x_max
                
                    if ( np.sign(V_x) == -1 ).any():
                        
                        V_x[ Speed_Magnitude > max_speed ] = -V_x_max
                        
                        
                if ( np.abs(V_y) > np.abs(V_x) ).any():
                        
                    V_y_max = np.sqrt( max_speed**2 - V_x**2 )
                        
                        
                    if ( np.sign(V_y) == 1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = V_y_max
                            
                    if ( np.sign(V_y) == -1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = -V_y_max
                        
            
            
        if metric_unit == "m/s":
            
            if max_speed > 0:
            
                # Remove Unsmoothed Data Points That Exceed the Maximum Speed (These Are Most Likely Position Errors)
                # If Maximum Speed Is Exceeded -->  Assign the `V_x_max` & `V_y_max` Value to the `V_x` & `V_y` Columns Instead, Since This Specific Value Will Ensure That the Speed Magnitude == `max_speed`
            
                Speed_Magnitude = np.sqrt( V_x**2 + V_y**2 )
                
                if ( np.abs(V_x) == np.abs(V_y) ).any():
                    
                    V_x_max = np.sqrt( max_speed**2 / 2 )
                    V_y_max = np.sqrt( max_speed**2 / 2 )
                        
                        
                    if ( np.sign(V_x) == 1 ).any():
            
                        V_x[ Speed_Magnitude > max_speed ] = V_x_max
                
                    if ( np.sign(V_x) == -1 ).any():
                        
                        V_x[ Speed_Magnitude > max_speed ] = -V_x_max
                            
                    if ( np.sign(V_y) == 1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = V_y_max
                            
                    if ( np.sign(V_y) == -1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = -V_y_max
            
                        # V_x[ Speed_Magnitude > max_speed ] = np.nan
                        # V_y[ Speed_Magnitude > max_speed ] = np.nan
                    
                    
                if ( np.abs(V_x) > np.abs(V_y) ).any():
                        
                    V_x_max = np.sqrt( max_speed**2 - V_y**2 )
                        
                        
                    if ( np.sign(V_x) == 1 ).any():
            
                        V_x[ Speed_Magnitude > max_speed ] = V_x_max
                
                    if ( np.sign(V_x) == -1 ).any():
                        
                        V_x[ Speed_Magnitude > max_speed ] = -V_x_max
                        
                        
                if ( np.abs(V_y) > np.abs(V_x) ).any():
                        
                    V_y_max = np.sqrt( max_speed**2 - V_x**2 )
                        
                        
                    if ( np.sign(V_y) == 1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = V_y_max
                            
                    if ( np.sign(V_y) == -1 ).any():
                        
                        V_y[ Speed_Magnitude > max_speed ] = -V_y_max

        
            
            
        if smoothing == True:
            
            if filter_type == "Savitzky-Golay":   # Fits a Polynomial of Order `order_of_polynomial` To the Data Within Each `smoothing_window_size`
                
                # Calculate 1st-Half Velocities
                
                V_x.loc[ : Second_Half_Index] = signal.savgol_filter( V_x.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                V_y.loc[ : Second_Half_Index] = signal.savgol_filter( V_y.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                
                
                
                # Calculate 2nd-Half Velocities
                
                V_x.loc[Second_Half_Index : ] = signal.savgol_filter( V_x.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                V_y.loc[Second_Half_Index : ] = signal.savgol_filter( V_y.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                
            
            
            
            elif filter_type == "Moving Average":
                
                ma_smoothing_window_size = np.ones( smoothing_window_size ) / smoothing_window_size 
                
                
                # Calculate 1st-Half Velocities
                
                V_x.loc[ : Second_Half_Index] = np.convolve( V_x.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" ) 
                V_y.loc[ : Second_Half_Index] = np.convolve( V_y.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" )
                
                

                # Calculate 2nd-Half Velocities
                
                V_x.loc[Second_Half_Index : ] = np.convolve( V_x.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" ) 
                V_y.loc[Second_Half_Index : ] = np.convolve( V_y.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" ) 
                
        
        
        
        # Put Players' Velocity Components In x- & y- Direction, & Total Magnitude/Speed Back In the DataFrame
        
        Match_Tracking_Data_With_Velocities_and_Speeds_df["V_x" + Player_Number] = V_x
        Match_Tracking_Data_With_Velocities_and_Speeds_df["V_y" + Player_Number] = V_y
        Match_Tracking_Data_With_Velocities_and_Speeds_df["Speed" + Player_Number] = np.sqrt( V_x**2 + V_y**2 )
        
        
        

    return Match_Tracking_Data_With_Velocities_and_Speeds_df










def Calculate_Players_and_Ball_Accelerations( match_tracking_data_df, metric_unit = "cm/s^2", max_acceleration = 3000, smoothing = True, filter_type = "Savitzky-Golay", smoothing_window_size = 125, order_of_polynomial = 1 ):
    """ 
    Function That Calculates Players' + Ball's Accelerations In x- & y- Direciton (i.e. Acc_x & Acc_y), & Their Respective Magnitude At Each Time-Step (25Hz ≡ 0.04s ≡ 1 Frame) of the Match Tracking Data
    
    Input: match_tracking_data_df = DataFrame of the Match Tracking Data Dataset
    Input: metric_unit = Metric Unit In Which the Acceleration Components & Magnitude Should Be Calculated In; Options  -->  {"cm/s^2", "m/s^2"}; Default == "cm/s^2"
    Input: max_acceleration = Maximum Acceleration Magnitude That a Player Can Realisitically Achieve. Acceleration Magnitude Measures That Exceed `max_acceleration` Are Tagged As Outliers & Set To `max_acceleration`; Default == 3000 [cm/s^2]
    Input: smoothing = Boolean Value, That Determines Whether Acceleration Measures Should Be Smoothed Or Not; Default == True
    Input: filter_type = Type of Filter To Use When Smoothing the Accelerations; Options  -->  {"Savitzky-Golay", "Moving Average"}; Default == "Savitzky-Golay"
    Input: smoothing_window_size = Smoothing Window Size In #Frames - In Case `filter_type = "Savitzky-Golay"` --> Value Must Be An Odd Number, So That the Filter Is Symmetric; Default == 125
    Input: order_of_polynomial = Order of the Polynomial For the "Savitzky-Golay" Filter; Default == 1  ( i.e. A Linear Fit To the Acceleration ⇒ Gradient ≡ dAcceleration / dt )
    
    Output: Match_Tracking_Data_With_Accelerations_df = DataFrame of the Match Tracking Data Dataset With Columns For Acceleration Components In the x- & y- Direction (i.e. "Acc_x{Player_Number}" & "Acc_y{Player_Number}") & Total Acceleration Magnitude Added At the End of the DataFrame
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    Match_Tracking_Data_With_Accelerations_df = match_tracking_data_df.copy()

    
    
    # Get the Players' IDs
    
    Players_Numbers = []

    for Player_Number in range(1, 23):
    
        Players_Numbers.append(str(Player_Number))
    

    # Calculate the Time-Step From 1 Frame To the Next Frame. Should Always Be = 0.04s Within the Same Half
    
    dt = Match_Tracking_Data_With_Accelerations_df["T"].diff()
    
    dt = dt.dt.total_seconds()
    
    
    
    # Index of First Frame In 2nd-Half
    
    Second_Half_Index = Match_Tracking_Data_With_Accelerations_df["Section"].idxmax(0)
    
    
    
    
    # Difference In Ball's Velocity In Time-Step `dt` To Get Unsmoothed Estimate of the Acceleration Components In the x-, y- & z-Directions
        
    Acc_x_Ball = Match_Tracking_Data_With_Accelerations_df["V_xBall"].diff() / dt
    Acc_y_Ball = Match_Tracking_Data_With_Accelerations_df["V_yBall"].diff() / dt
    Acc_z_Ball = Match_Tracking_Data_With_Accelerations_df["V_zBall"].diff() / dt
    
    Acceleration_Magnitude_Ball = np.sqrt( Acc_x_Ball**2 + Acc_y_Ball**2 + Acc_z_Ball**2 )
    
    
    if smoothing == True:
            
            if filter_type == "Savitzky-Golay":   # Fits a Polynomial of Order `order_of_polynomial` To the Data Within Each `smoothing_window_size`
                
                # Calculate 1st-Half Accelerations
                
                Acc_x_Ball.loc[ : Second_Half_Index] = signal.savgol_filter(Acc_x_Ball.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                Acc_y_Ball.loc[ : Second_Half_Index] = signal.savgol_filter(Acc_y_Ball.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                Acc_z_Ball.loc[ : Second_Half_Index] = signal.savgol_filter(Acc_z_Ball.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                
                
                # Calculate 2nd-Half Accelerations
                      
                Acc_x_Ball.loc[Second_Half_Index : ] = signal.savgol_filter(Acc_x_Ball.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                Acc_y_Ball.loc[Second_Half_Index : ] = signal.savgol_filter(Acc_y_Ball.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                Acc_z_Ball.loc[Second_Half_Index : ] = signal.savgol_filter(Acc_z_Ball.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial)
                
                 
            
            elif filter_type == "Moving Average":
                
                ma_smoothing_window_size = np.ones( smoothing_window_size ) / smoothing_window_size 
                
                
                # Calculate 1st-Half Accelerations
                
                Acc_x_Ball.loc[ : Second_Half_Index] = np.convolve( Acc_x_Ball.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" ) 
                Acc_y_Ball.loc[ : Second_Half_Index] = np.convolve( Acc_y_Ball.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" )
                Acc_z_Ball.loc[ : Second_Half_Index] = np.convolve( Acc_z_Ball.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" )
                
                
                # Calculate 2nd-Half Accelerations
                
                Acc_x_Ball.loc[Second_Half_Index : ] = np.convolve( Acc_x_Ball.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" ) 
                Acc_y_Ball.loc[Second_Half_Index : ] = np.convolve( Acc_y_Ball.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" )
                Acc_z_Ball.loc[Second_Half_Index : ] = np.convolve( Acc_z_Ball.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" )
                
                
                
                
    # Put Ball's Acceleration Components In x- & y- Direction, & Total Acceleration Magnitude Back In the DataFrame
        
    Match_Tracking_Data_With_Accelerations_df["Acc_xBall"] = Acc_x_Ball
    Match_Tracking_Data_With_Accelerations_df["Acc_yBall"] = Acc_y_Ball
    Match_Tracking_Data_With_Accelerations_df["Acc_zBall"] = Acc_z_Ball
    Match_Tracking_Data_With_Accelerations_df["Acc_MagnitudeBall"] = np.sqrt( Acc_x_Ball**2 + Acc_y_Ball**2 + Acc_z_Ball**2 )
                
                
    
    
    # Estimate Accelerations' Components Acc_x & Acc_y For Players In `Match_Tracking_Data_With_Accelerations_df`
    
    for Player_Number in Players_Numbers:  # Cycle Through Players Individually
        
        # Difference In Players' Velocities In Time-Step `dt` To Get Unsmoothed Estimate of the Acceleration Components
        
        Acc_x = Match_Tracking_Data_With_Accelerations_df["V_x" + Player_Number].diff() / dt
        Acc_y = Match_Tracking_Data_With_Accelerations_df["V_y" + Player_Number].diff() / dt
        
        
        # Maximum Acceleration Magnitude That a Player Can Realisitically Achieve. Acceleration Magnitude Measures That Exceed `max_acceleration` Are Tagged As Outliers & Set To `max_acceleration` 
        
        if metric_unit == "cm/s^2":
        
            if max_acceleration > 0:
            
                # Remove Unsmoothed Data Points That Exceed the Maximum Acceleration Magnitude (These Are Most Likely Velocity Errors)
                # If Maximum Acceleration Magnitude Is Exceeded -->  Assign the `Acc_x_max` & `Acc_y_max` Value to the `Acc_x` & `Acc_y` Columns Instead, Since This Specific Value Will Ensure That the Acceleration Magnitude Magnitude == `max_acceleration`
            
                Acceleration_Magnitude = np.sqrt( Acc_x**2 + Acc_y**2 )
                
                if ( np.abs(Acc_x) == np.abs(Acc_y) ).any():
                    
                    Acc_x_max = np.sqrt( max_acceleration**2 / 2 )
                    Acc_y_max = np.sqrt( max_acceleration**2 / 2 )
                    
                        
                        
                    if ( np.sign(Acc_x) == 1 ).any():
            
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = Acc_x_max
                
                    if ( np.sign(Acc_x) == -1 ).any():
                        
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = -Acc_x_max
                            
                    if ( np.sign(Acc_y) == 1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = Acc_y_max
                            
                    if ( np.sign(Acc_y) == -1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = -Acc_y_max
            
                        # Acc_x[ Acceleration_Magnitude > max_acceleration ] = np.nan
                        # Acc_y[ Acceleration_Magnitude > max_acceleration ] = np.nan
                    
                    
                if ( np.abs(Acc_x) > np.abs(Acc_y) ).any():
                        
                    Acc_x_max = np.sqrt( max_acceleration**2 - Acc_y**2 )
                        
                        
                    if ( np.sign(Acc_x) == 1 ).any():
            
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = Acc_x_max
                
                    if ( np.sign(Acc_x) == -1 ).any():
                        
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = -Acc_x_max
                        
                        
                if ( np.abs(Acc_y) > np.abs(Acc_x) ).any():
                        
                    Acc_y_max = np.sqrt( max_acceleration**2 - Acc_x**2 )
                        
                        
                    if ( np.sign(Acc_y) == 1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = Acc_y_max
                            
                    if ( np.sign(Acc_y) == -1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = -Acc_y_max
                        
            
            
        if metric_unit == "m/s^2":
            
            if max_acceleration > 0:
            
                # Remove Unsmoothed Data Points That Exceed the Maximum Acceleration Magnitude (These Are Most Likely Velocity Errors)
                # If Maximum Acceleration Magnitude Is Exceeded -->  Assign the `Acc_x_max` & `Acc_y_max` Value to the `Acc_x` & `Acc_y` Columns Instead, Since This Specific Value Will Ensure That the Acceleration Magnitude Magnitude == `max_acceleration`
            
                Acceleration_Magnitude = np.sqrt( Acc_x**2 + Acc_y**2 )
                
                if ( np.abs(Acc_x) == np.abs(Acc_y) ).any():
                    
                    Acc_x_max = np.sqrt( max_acceleration**2 / 2 )
                    Acc_y_max = np.sqrt( max_acceleration**2 / 2 )
                        
                        
                    if ( np.sign(Acc_x) == 1 ).any():
            
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = Acc_x_max
                
                    if ( np.sign(Acc_x) == -1 ).any():
                        
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = -Acc_x_max
                            
                    if ( np.sign(Acc_y) == 1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = Acc_y_max
                            
                    if ( np.sign(Acc_y) == -1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = -Acc_y_max
            
                        # Acc_x[ Acceleration_Magnitude > max_acceleration ] = np.nan
                        # Acc_y[ Acceleration_Magnitude > max_acceleration ] = np.nan
                    
                    
                if ( np.abs(Acc_x) > np.abs(Acc_y) ).any():
                        
                    Acc_x_max = np.sqrt( max_acceleration**2 - Acc_y**2 )
                        
                        
                    if ( np.sign(Acc_x) == 1 ).any():
            
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = Acc_x_max
                
                    if ( np.sign(Acc_x) == -1 ).any():
                        
                        Acc_x[ Acceleration_Magnitude > max_acceleration ] = -Acc_x_max
                        
                        
                if ( np.abs(Acc_y) > np.abs(Acc_x) ).any():
                        
                    Acc_y_max = np.sqrt( max_acceleration**2 - Acc_x**2 )
                        
                        
                    if ( np.sign(Acc_y) == 1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = Acc_y_max
                            
                    if ( np.sign(Acc_y) == -1 ).any():
                        
                        Acc_y[ Acceleration_Magnitude > max_acceleration ] = -Acc_y_max

        
            
            
        if smoothing == True:
            
            if filter_type == "Savitzky-Golay":   # Fits a Polynomial of Order `order_of_polynomial` To the Data Within Each `smoothing_window_size`
                
                # Calculate 1st-Half Accelerations
                
                Acc_x.loc[ : Second_Half_Index] = signal.savgol_filter( Acc_x.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                Acc_y.loc[ : Second_Half_Index] = signal.savgol_filter( Acc_y.loc[ : Second_Half_Index], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                
                
                
                # Calculate 2nd-Half Accelerations
                
                Acc_x.loc[Second_Half_Index : ] = signal.savgol_filter( Acc_x.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                Acc_y.loc[Second_Half_Index : ] = signal.savgol_filter( Acc_y.loc[Second_Half_Index : ], window_length = smoothing_window_size, polyorder = order_of_polynomial )
                
            
            
            
            elif filter_type == "Moving Average":
                
                ma_smoothing_window_size = np.ones( smoothing_window_size ) / smoothing_window_size 
                
                
                # Calculate 1st-Half Accelerations
                
                Acc_x.loc[ : Second_Half_Index] = np.convolve( Acc_x.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" ) 
                Acc_y.loc[ : Second_Half_Index] = np.convolve( Acc_y.loc[ : Second_Half_Index] , ma_smoothing_window_size, mode = "same" )
                
                

                # Calculate 2nd-Half Accelerations
                
                Acc_x.loc[Second_Half_Index : ] = np.convolve( Acc_x.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" ) 
                Acc_y.loc[Second_Half_Index : ] = np.convolve( Acc_y.loc[Second_Half_Index : ] , ma_smoothing_window_size, mode = "same" ) 
                
        
        
        
        # Put Players' Acceleration Components In x- & y- Direction, & Total Acceleration Magnitude Back In the DataFrame
        
        Match_Tracking_Data_With_Accelerations_df["Acc_x" + Player_Number] = Acc_x
        Match_Tracking_Data_With_Accelerations_df["Acc_y" + Player_Number] = Acc_y
        Match_Tracking_Data_With_Accelerations_df["Acc_Magnitude" + Player_Number] = np.sqrt( Acc_x**2 + Acc_y**2 )
        
        
        

    return Match_Tracking_Data_With_Accelerations_df










def Setting_Up_Final_Version_of_Match_Tracking_Data( matches_to_set_up = range(0, 361), frames_per_second = 25, velocity_metric_unit = "cm/s", max_speed = 1200, acceleration_metric_unit = "cm/s^2", max_acceleration = 3000, filter_type = "Savitzky-Golay", smoothing_window_size = 125 ):
    """
    Function That For Every Match Tracking Data For Match #`match_num`:
                                                                        1) Removes/Drops the Following Columns: "frame", "timestamp", "period", "possession.group", "possession.trackable_object", "S" & "S1"-"S22", "H_CHAOS", "A_CHAOS", "SubType", "SubTypeH", & "SubTypeA"
                                                                        
                                                                        2) Drops/Removes the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
                                                                        
                                                                        3) Calculates the "Match_Minute_Clock", "Match_Seconds_Clock" & the "Match_Clock"
                                                                        
                                                                        4) Calculates the X- & Y- Velocity Components "V_x{Player_Number}" & "V_y{Player_Number}", & the Magnitude Speeds "Speed{Player_Number}", & For the Ball "V_xBall", "V_yBall", "V_zBall" & "SpeedBall", Respectively
                                                                        
                                                                        5) Removes/Drops All Those Rows/Indeces (Usually the First 26 Rows) Where There Are Missing (`NaN`) Values Present In the Players' & Ball's Velocity Components & Speeds Columns: "V_x{Player_Number}", "V_y{Player_Number}", "Speed{Player_Number}", "V_xBall", "V_yBall", "V_zBall" & "SpeedBall"
                                                                        
                                                                        6) Calculates the X- & Y- Acceleration Components "Acc_x{Player_Number}" & "Acc_y{Player_Number}", & the Acceleration Magnitudes "Acc_Magnitude{Player_Number}", & For the Ball "Acc_xBall", "Acc_yBall", "Acc_zBall" & "Acc_MagnitudeBall", Respectively
                                                                        
                                                                        7) Removes/Drops All Those Rows/Indeces (Usually the First 26 Rows) Where There Are Missing (`NaN`) Values Present In the Players' & Ball's Acceleration Components & Magnitudes Columns: "Acc_x{Player_Number}", "Acc_y{Player_Number}", "Acc_Magnitude{Player_Number}", "Acc_xBall", "Acc_yBall", "Acc_zBall" & "Acc_MagnitudeBall"
                                                                        
                                                                        8) Removes/Drops the "T" Column
                                                                        
                                                                        9) Saves the Final Version of the DataFrame of the Match Tracking Data Into a `_Final.parquet` File
                                                                                   
    Input: matches_to_set_up = List Or Range `range( ·, ·)` of Matches To Be Cleaned
    Input: frames_per_second = # Frames Per Second (Frequency) To Assume When Generating the Movie; Default == 25
    Input: velocity_metric_unit = Metric Unit In Which the Velocity Components & Speeds Should Be Calculated In; Options  -->  {"cm/s", "m/s"}; Default == "cm/s"
    Input: max_speed = Maximum Speed That a Player Can Realisitically Achieve. Speed Measures That Exceed `max_speed` Are Tagged As Outliers & Set To `max_speed`; Default == 1200 [cm/s]
    Input: acceleration_metric_unit = Metric Unit In Which the Acceleration Components & Magnitudes Should Be Calculated In; Options  -->  {"cm/s^2", "m/s^2"}; Default == "cm/s^2"
    Input: max_acceleration = Maximum Acceleration Magnitude That a Player Can Realisitically Achieve. Acceleration Measures That Exceed `max_acceleration` Are Tagged As Outliers & Set To `max_acceleration`; Default == 3000 [cm/s^2]
    Input: filter_type = Type of Filter To Use When Smoothing the Velocities; Options  -->  {"Savitzky-Golay", "Moving Average"}; Default == "Savitzky-Golay"
    Input: smoothing_window_size = Smoothing Window Size In #Frames - In Case `filter_type = "Savitzky-Golay"` --> Value Must Be An Odd Number, So That the Filter Is Symmetric; Default == 125
    
    
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the Match Tracking Data
    """
    
    pd.set_option('display.max_rows', None)
    
        
    
    Match_Numbers = matches_to_set_up

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Original Version of the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Original Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Tracking_Data_Match_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Dataset of the Original Tracking Data For Match #{Match_Num + 1} = {Tracking_Data_Match_df.shape}", '\n')
    
    
    
    
        
        
        
        # Dropping/Removing the "frame", "timestamp", "period", "possession.group", "possession.trackable_object", "S" & "S1"-"S22", "H_CHAOS", "A_CHAOS", "SubType", "SubTypeH", & "SubTypeA" Columns
    
        Final_Match_Tracking_Data_df = Tracking_Data_Match_df.copy()

        Final_Match_Tracking_Data_df.drop(columns = ["frame", "timestamp", "period", "possession.group", "possession.trackable_object",
                                                     "S", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11",
                                                     "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20", "S21", "S22",
                                                     "H_CHAOS", "A_CHAOS", "SubType", "SubTypeH", "SubTypeA"],
                                          inplace = True)

        print(f'New Dimensions of the Final Version of the Tracking Data For Match #{Match_Num + 1} After Removing the Unneccessary/Irrelevant Columns = {Final_Match_Tracking_Data_df.shape}', '\n')
        
        
        
        
        
        
        # Dropping/Removing the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
    
        Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing_Match_Tracking_Data = TFwDCFs.Display_Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing(df = Final_Match_Tracking_Data_df)
        

        Final_Match_Tracking_Data_df.drop(index = Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing_Match_Tracking_Data,
                                          inplace = True)
    

        print(f'New Dimensions of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Which Have >50% of Its Values Missing = {Final_Match_Tracking_Data_df.shape}', '\n')
    
    
    
    
        
        
        
        # Calculate the "Match_Minute_Clock", "Match_Seconds_Clock" & the "Match_Clock", & Then Removes/Drops the "T" Column
        
        FPS = frames_per_second   # Frames-Per-Second (i.e. Frame Rate / Frequency)
        
        
        for Frame_Number in Final_Match_Tracking_Data_df.index:
            
            
            # Include Match Time At the Top
            
            Frame_Minute =  int( (Frame_Number / FPS) / 60 )
            
            Final_Match_Tracking_Data_df.loc[Frame_Number, "Match_Minute_Clock"] = Frame_Minute
            
            
            Frame_Second =  ( ((Frame_Number / FPS) / 60) - Frame_Minute ) * 60
            
            Final_Match_Tracking_Data_df.loc[Frame_Number, "Match_Seconds_Clock"] = Frame_Second
            
            
            Match_Time_String = "%d:%1.2f" % ( Frame_Minute, Frame_Second )
            
            Final_Match_Tracking_Data_df.loc[Frame_Number, "Match_Clock"] = Match_Time_String
        
        
        
        
        
        
        
        # Calculate the X- & Y- Velocity Components "V_x{Player_Number}" & "V_y{Player_Number}", & the Magnitude Speeds "Speed{Player_Number}", & For the Ball "V_xBall", "V_yBall", "V_zBall"  & "SpeedBall", Respectively
        
        Final_Match_Tracking_Data_df = TFwDCFs.Calculate_Players_and_Ball_Velocities_and_Speeds( match_tracking_data_df = Final_Match_Tracking_Data_df,
                                                                                               metric_unit = velocity_metric_unit, max_speed = max_speed,
                                                                                               smoothing = True, filter_type = filter_type,
                                                                                               smoothing_window_size = smoothing_window_size, order_of_polynomial = 1 )
        
        
        
        
        
        # Finding the Indices/Rows Where Missing (`NaN`) Values Are Present In the Following Columns: "V_x{Player_Number}", "V_y{Player_Number}", "Speed{Player_Number}", "V_xBall", "V_yBall", "V_zBall" & "SpeedBall"

        Indices_Where_Players_and_Ball_Velocities_and_Speeds_Are_Missing = Final_Match_Tracking_Data_df.index[(Final_Match_Tracking_Data_df["V_x1"].isna() == True) & (Final_Match_Tracking_Data_df["V_x2"].isna() == True) & (Final_Match_Tracking_Data_df["V_x3"].isna() == True) & (Final_Match_Tracking_Data_df["V_x4"].isna() == True) & (Final_Match_Tracking_Data_df["V_x5"].isna() == True) & (Final_Match_Tracking_Data_df["V_x6"].isna() == True) & (Final_Match_Tracking_Data_df["V_x7"].isna() == True) & (Final_Match_Tracking_Data_df["V_x8"].isna() == True) & (Final_Match_Tracking_Data_df["V_x9"].isna() == True) & (Final_Match_Tracking_Data_df["V_x10"].isna() == True) & (Final_Match_Tracking_Data_df["V_x11"].isna() == True) & (Final_Match_Tracking_Data_df["V_x12"].isna() == True) & (Final_Match_Tracking_Data_df["V_x13"].isna() == True) & (Final_Match_Tracking_Data_df["V_x14"].isna() == True) & (Final_Match_Tracking_Data_df["V_x15"].isna() == True) & (Final_Match_Tracking_Data_df["V_x16"].isna() == True) & (Final_Match_Tracking_Data_df["V_x17"].isna() == True) & (Final_Match_Tracking_Data_df["V_x18"].isna() == True) & (Final_Match_Tracking_Data_df["V_x19"].isna() == True) & (Final_Match_Tracking_Data_df["V_x20"].isna() == True) & (Final_Match_Tracking_Data_df["V_x21"].isna() == True) & (Final_Match_Tracking_Data_df["V_x22"].isna() == True) & (Final_Match_Tracking_Data_df["V_y1"].isna() == True) & (Final_Match_Tracking_Data_df["V_y2"].isna() == True) & (Final_Match_Tracking_Data_df["V_y3"].isna() == True) & (Final_Match_Tracking_Data_df["V_y4"].isna() == True) & (Final_Match_Tracking_Data_df["V_y5"].isna() == True) & (Final_Match_Tracking_Data_df["V_y6"].isna() == True) & (Final_Match_Tracking_Data_df["V_y7"].isna() == True) & (Final_Match_Tracking_Data_df["V_y8"].isna() == True) & (Final_Match_Tracking_Data_df["V_y9"].isna() == True) & (Final_Match_Tracking_Data_df["V_y10"].isna() == True) & (Final_Match_Tracking_Data_df["V_y11"].isna() == True) & (Final_Match_Tracking_Data_df["V_y12"].isna() == True) & (Final_Match_Tracking_Data_df["V_y13"].isna() == True) & (Final_Match_Tracking_Data_df["V_y14"].isna() == True) & (Final_Match_Tracking_Data_df["V_y15"].isna() == True) & (Final_Match_Tracking_Data_df["V_y16"].isna() == True) & (Final_Match_Tracking_Data_df["V_y17"].isna() == True) & (Final_Match_Tracking_Data_df["V_y18"].isna() == True) & (Final_Match_Tracking_Data_df["V_y19"].isna() == True) & (Final_Match_Tracking_Data_df["V_y20"].isna() == True) & (Final_Match_Tracking_Data_df["V_y21"].isna() == True) & (Final_Match_Tracking_Data_df["V_y22"].isna() == True) & (Final_Match_Tracking_Data_df["Speed1"].isna() == True) & (Final_Match_Tracking_Data_df["Speed2"].isna() == True) & (Final_Match_Tracking_Data_df["Speed3"].isna() == True) & (Final_Match_Tracking_Data_df["Speed4"].isna() == True) & (Final_Match_Tracking_Data_df["Speed5"].isna() == True) & (Final_Match_Tracking_Data_df["Speed6"].isna() == True) & (Final_Match_Tracking_Data_df["Speed7"].isna() == True) & (Final_Match_Tracking_Data_df["Speed8"].isna() == True) & (Final_Match_Tracking_Data_df["Speed9"].isna() == True) & (Final_Match_Tracking_Data_df["Speed10"].isna() == True) & (Final_Match_Tracking_Data_df["Speed11"].isna() == True) & (Final_Match_Tracking_Data_df["Speed12"].isna() == True) & (Final_Match_Tracking_Data_df["Speed13"].isna() == True) & (Final_Match_Tracking_Data_df["Speed14"].isna() == True) & (Final_Match_Tracking_Data_df["Speed15"].isna() == True) & (Final_Match_Tracking_Data_df["Speed16"].isna() == True) & (Final_Match_Tracking_Data_df["Speed17"].isna() == True) & (Final_Match_Tracking_Data_df["Speed18"].isna() == True) & (Final_Match_Tracking_Data_df["Speed19"].isna() == True) & (Final_Match_Tracking_Data_df["Speed20"].isna() == True) & (Final_Match_Tracking_Data_df["Speed21"].isna() == True) & (Final_Match_Tracking_Data_df["Speed22"].isna() == True) & (Final_Match_Tracking_Data_df["V_xBall"].isna() == True) & (Final_Match_Tracking_Data_df["V_yBall"].isna() == True) & (Final_Match_Tracking_Data_df["V_zBall"].isna() == True) & (Final_Match_Tracking_Data_df["SpeedBall"].isna() == True)].unique().tolist()
    
    
        print(f"#Rows Which Have the Players' and the Ball's Velocity Components' & Speeds' Values Missing, & ∴ Will Be Removed = \033[91m\033[1m\033[4m{len(Indices_Where_Players_and_Ball_Velocities_and_Speeds_Are_Missing)}\033[0m", '\n')
    
    
        Final_Match_Tracking_Data_df.drop(index = Indices_Where_Players_and_Ball_Velocities_and_Speeds_Are_Missing, inplace = True)
    
    
        print(f"New Dimensions of the Final Version of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Where Values For the Players' and the Ball's Velocity Components' & Speeds' Are Missing = \033[91m\033[1m\033[4m{Final_Match_Tracking_Data_df.shape}\033[0m", '\n')
        
        
        
        


        
        
        
        # Calculate the X- & Y- Acceleration Components "Acc_x{Player_Number}" & "Acc_y{Player_Number}", & the Acceleration Magnitudes "Acc_Magnitude{Player_Number}", & For the Ball "Acc_xBall", "Acc_yBall", "Acc_zBall"  & "Acc_MagnitudeBall", Respectively
        
        Final_Match_Tracking_Data_df = TFwDCFs.Calculate_Players_and_Ball_Accelerations( match_tracking_data_df = Final_Match_Tracking_Data_df,
                                                                                       metric_unit = acceleration_metric_unit, max_acceleration = max_acceleration,
                                                                                       smoothing = True, filter_type = filter_type,
                                                                                       smoothing_window_size = smoothing_window_size, order_of_polynomial = 1 )
        
        
        
        
        # Finding the Indices/Rows Where Missing (`NaN`) Values Are Present In the Following Columns: "Acc_x{Player_Number}", "Acc_y{Player_Number}", "Acc_Magnitude{Player_Number}", "Acc_xBall", "Acc_yBall", "Acc_zBall" & "Acc_MagnitudeBall"

        Indices_Where_Players_and_Ball_Accelerations_Are_Missing = Final_Match_Tracking_Data_df.index[(Final_Match_Tracking_Data_df["Acc_x1"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x2"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x3"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x4"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x5"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x6"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x7"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x8"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x9"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x10"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x11"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x12"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x13"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x14"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x15"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x16"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x17"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x18"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x19"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x20"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x21"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_x22"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y1"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y2"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y3"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y4"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y5"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y6"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y7"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y8"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y9"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y10"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y11"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y12"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y13"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y14"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y15"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y16"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y17"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y18"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y19"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y20"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y21"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_y22"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude1"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude2"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude3"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude4"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude5"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude6"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude7"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude8"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude9"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude10"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude11"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude12"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude13"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude14"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude15"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude16"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude17"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude18"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude19"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude20"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude21"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_Magnitude22"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_xBall"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_yBall"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_zBall"].isna() == True) & (Final_Match_Tracking_Data_df["Acc_MagnitudeBall"].isna() == True)].unique().tolist()
    
    
        print(f"#Rows Which Have the Players' and the Ball's Acceleration Components' & Magnitudes' Values Missing, & ∴ Will Be Removed = \033[91m\033[1m\033[4m{len(Indices_Where_Players_and_Ball_Accelerations_Are_Missing)}\033[0m", '\n')
    
    
        Final_Match_Tracking_Data_df.drop(index = Indices_Where_Players_and_Ball_Accelerations_Are_Missing, inplace = True)
    
    
        print(f"New Dimensions of the Final Version of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Where Values For the Players' and the Ball's Acceleration Components' & Magnitudes' Are Missing = \033[91m\033[1m\033[4m{Final_Match_Tracking_Data_df.shape}\033[0m", '\n')
        
        
        
        
        
        
        # Remove/Drop the "T" Column
        
        Final_Match_Tracking_Data_df.drop(columns = ["T"], inplace = True)        
    
    
        
        
        
        
        # Displaying the #Missing (`NaN`) Values That Are Remaining - Hopefully = 0  !!
        
        Num_Rows_Tracking_Data = Final_Match_Tracking_Data_df.shape[0]

        Num_Columns_Tracking_Data = Final_Match_Tracking_Data_df.shape[1]
    
    
    
        Num_Missing_Values_Tracking_Data_df_Final = Final_Match_Tracking_Data_df.isna().apply(lambda column: column[column == True].count()).sum()

        print(f"Total Number of Missing Values In the Final Version of the Tracking Data (For Match #{Match_Num + 1}) Dataset = \033[91m\033[1m\033[4m{Num_Missing_Values_Tracking_Data_df_Final}\033[0m", '\n',
              f"This Represents \033[91m\033[1m\033[4m{(Num_Missing_Values_Tracking_Data_df_Final / (Num_Rows_Tracking_Data * Num_Columns_Tracking_Data))*100:.2f} %\033[0m of the Final Tracking Data (For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m) Dataset",
              '\n')
    
    
    
        
        
        # Save Final Version of the Tracking Data As a New "_Final.parquet" File
    
        Final_Match_Tracking_Data_df.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
        print(f"\033[92m\033[1m Final Version of the Tracking Data For Match #{Match_Num + 1} --> Succesfully Saved \033[0m", '\n')
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
    
    
    return  print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Setting_Up_Final_Version_of_Match_Tracking_Datasets( matches_to_set_up = range(0, 361), frames_per_second = 25, velocity_metric_unit = "cm/s", max_speed = 1200, filter_type = "Savitzky-Golay", smoothing_window_size = 150 ):
    """
    Function That For Every Match Tracking Data For Match #`match_num`:
                                                                        1) Removes/Drops the Following Columns: "frame", "timestamp", "period", "possession.group", "possession.trackable_object", "S" & "S1"-"S22", "H_CHAOS", "A_CHAOS", "SubType", "SubTypeH", & "SubTypeA"
                                                                        
                                                                        2) Drops/Removes the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
                                                                        
                                                                        3) Calculates the "Match_Minute_Clock", "Match_Seconds_Clock" & the "Match_Clock"
                                                                        
                                                                        4) Calculates the X- & Y- Velocity Components "V_x{Player_Number}" & "V_y{Player_Number}", & the Magnitude Speeds "Speed{Player_Number}", & For the Ball "V_xBall", "V_yBall", "V_zBall" & "SpeedBall", Respectively
                                                                        
                                                                        5) Removes/Drops All Those Rows/Indeces (Usually the First 26 Rows) Where There Are Missing (`NaN`) Values Present In the Players' & Ball's Velocity Components & Speeds Columns: "V_x{Player_Number}", "V_y{Player_Number}", "Speed{Player_Number}", "V_xBall", "V_yBall", "V_zBall" & "SpeedBall"
                                                                        
                                                                        6) Removes/Drops the "T" Column
                                                                        
                                                                        7) Saves the Final Version of the DataFrame of the Match Tracking Data Into a `_Final.parquet` File
                                                                                   
    Input: matches_to_set_up = List Or Range `range( ·, ·)` of Matches To Be Cleaned
    Input: frames_per_second = # Frames Per Second (Frequency) To Assume When Generating the Movie; Default == 25
    Input: velocity_metric_unit = Metric Unit In Which the Velocity Components & Speeds Should Be Calculated In; Options  -->  {"cm/s", "m/s"}; Default == "cm/s"
    Input: max_speed = Maximum Speed That a Player Can Realisitically Achieve. Speed Measures That Exceed `max_speed` Are Tagged As Outliers & Set To `max_speed`; Default == 1200 [cm/s]
    Input: filter_type = Type of Filter To Use When Smoothing the Velocities; Options  -->  {"Savitzky-Golay", "Moving Average"}; Default == "Savitzky-Golay"
    Input: smoothing_window_size = Smoothing Window Size In #Frames - In Case `filter_type = "Savitzky-Golay"` --> Value Must Be An Odd Number, So That the Filter Is Symmetric; Default == 125
    
    
    Output: Final_Match_Tracking_Data_df = Final Version of the DataFrame of the Match Tracking Data
    """
    
    pd.set_option('display.max_rows', None)
    
        
    
    Match_Numbers = matches_to_set_up

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Original Version of the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Original Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Tracking_Data_Match_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Dataset of the Original Tracking Data For Match #{Match_Num + 1} = {Tracking_Data_Match_df.shape}", '\n')
    
    
    
    
        
        
        
        # Dropping/Removing the "frame", "timestamp", "period", "possession.group", "possession.trackable_object", "S" & "S1"-"S22", "H_CHAOS", "A_CHAOS", "SubType", "SubTypeH", & "SubTypeA" Columns
    
        Final_Match_Tracking_Data_df = Tracking_Data_Match_df.copy()

        Final_Match_Tracking_Data_df.drop(columns = ["frame", "timestamp", "period", "possession.group", "possession.trackable_object",
                                                     "S", "S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "S11",
                                                     "S12", "S13", "S14", "S15", "S16", "S17", "S18", "S19", "S20", "S21", "S22",
                                                     "H_CHAOS", "A_CHAOS", "SubType", "SubTypeH", "SubTypeA"],
                                          inplace = True)

        print(f'New Dimensions of the Final Version of the Tracking Data For Match #{Match_Num + 1} After Removing the Unneccessary/Irrelevant Columns = {Final_Match_Tracking_Data_df.shape}', '\n')
        
        
        
        
        
        
        # Dropping/Removing the Rows Which Have >50% of Its Columns Filled Up With Missing (`NaN`) Values
    
        Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing_Match_Tracking_Data = TFwDCFs.Display_Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing(df = Final_Match_Tracking_Data_df)
        

        Final_Match_Tracking_Data_df.drop(index = Indeces_of_Rows_With_More_Than_50_Percent_Values_Missing_Match_Tracking_Data,
                                          inplace = True)
    

        print(f'New Dimensions of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Which Have >50% of Its Values Missing = {Final_Match_Tracking_Data_df.shape}', '\n')
    
    
    
    
        
        
        
        # Calculate the "Match_Minute_Clock", "Match_Seconds_Clock" & the "Match_Clock", & Then Removes/Drops the "T" Column
        
        FPS = frames_per_second   # Frames-Per-Second (i.e. Frame Rate / Frequency)
        
        
        for Frame_Number in Final_Match_Tracking_Data_df.index:
            
            
            # Include Match Time At the Top
            
            Frame_Minute =  int( (Frame_Number / FPS) / 60 )
            
            Final_Match_Tracking_Data_df.loc[Frame_Number, "Match_Minute_Clock"] = Frame_Minute
            
            
            Frame_Second =  ( ((Frame_Number / FPS) / 60) - Frame_Minute ) * 60
            
            Final_Match_Tracking_Data_df.loc[Frame_Number, "Match_Seconds_Clock"] = Frame_Second
            
            
            Match_Time_String = "%d:%1.2f" % ( Frame_Minute, Frame_Second )
            
            Final_Match_Tracking_Data_df.loc[Frame_Number, "Match_Clock"] = Match_Time_String
        
        
        
        
        
        
        
        # Calculate the X- & Y- Velocity Components "V_x{Player_Number}" & "V_y{Player_Number}", & the Magnitude Speeds "Speed{Player_Number}", & For the Ball "V_xBall", "V_yBall", "V_zBall"  & "SpeedBall", Respectively
        
        Final_Match_Tracking_Data_df = TFwDCFs.Calculate_Players_and_Ball_Velocities_and_Speeds( match_tracking_data_df = Final_Match_Tracking_Data_df,
                                                                                               metric_unit = velocity_metric_unit, max_speed = max_speed,
                                                                                               smoothing = True, filter_type = filter_type,
                                                                                               smoothing_window_size = smoothing_window_size, order_of_polynomial = 1 )
        
        
        
        
        
        # Finding the Indices/Rows Where Missing (`NaN`) Values Are Present In the Following Columns: "V_x{Player_Number}", "V_y{Player_Number}", "Speed{Player_Number}", "V_xBall", "V_yBall", "V_zBall" & "SpeedBall"

        Indices_Where_Players_and_Ball_Velocities_and_Speeds_Are_Missing = Final_Match_Tracking_Data_df.index[(Final_Match_Tracking_Data_df["V_xBall"].isna() == True) & (Final_Match_Tracking_Data_df["V_x1"].isna() == True)].unique().tolist()
    
    
        print(f"#Rows Which Have the Players' and the Ball's Velocity Components' & Speeds' Values Missing, & ∴ Will Be Removed = \033[91m\033[1m\033[4m{len(Indices_Where_Players_and_Ball_Velocities_and_Speeds_Are_Missing)}\033[0m", '\n')
    
    
        Final_Match_Tracking_Data_df.drop(index = Indices_Where_Players_and_Ball_Velocities_and_Speeds_Are_Missing, inplace = True)
    
    
        print(f"New Dimensions of the Final Version of the Tracking Data For Match #{Match_Num + 1} After Removing the Rows Where Values For the Players' and the Ball's Velocity Components' & Speeds' Are Missing = \033[91m\033[1m\033[4m{Final_Match_Tracking_Data_df.shape}\033[0m", '\n')
        
        
        
        
        
        
        
        # Remove/Drop the "T" Column
        
        Final_Match_Tracking_Data_df.drop(columns = ["T"], inplace = True)        
    
    
        
        
        
        
        # Displaying the #Missing (`NaN`) Values That Are Remaining - Hopefully = 0  !!
        
        Num_Rows_Tracking_Data = Final_Match_Tracking_Data_df.shape[0]

        Num_Columns_Tracking_Data = Final_Match_Tracking_Data_df.shape[1]
    
    
    
        Num_Missing_Values_Tracking_Data_df_Final = Final_Match_Tracking_Data_df.isna().apply(lambda column: column[column == True].count()).sum()

        print(f"Total Number of Missing Values In the Final Version of the Tracking Data (For Match #{Match_Num + 1}) Dataset = \033[91m\033[1m\033[4m{Num_Missing_Values_Tracking_Data_df_Final}\033[0m", '\n',
              f"This Represents \033[91m\033[1m\033[4m{(Num_Missing_Values_Tracking_Data_df_Final / (Num_Rows_Tracking_Data * Num_Columns_Tracking_Data))*100:.2f} %\033[0m of the Final Tracking Data (For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m) Dataset",
              '\n')
    
    
    
        
        
        # Save Final Version of the Tracking Data As a New "_Final.parquet" File
    
        Final_Match_Tracking_Data_df.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
        print(f"\033[92m\033[1m Final Version of the Tracking Data For Match #{Match_Num + 1} --> Succesfully Saved \033[0m", '\n')
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
    
    
    return  print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Double_Check_For_Missing_Values_and_Correct_Dimensions( matches_to_check = range(0, 361) ):
    """
    Function That Check Dimensions & Any Remaining Missing Values For Every Match Tracking Data For Match #`match_num`:

    Input: matches_to_check = Matches To Make Checks For
    
    Output: Strings With the Required Checks
    """
    
    pd.set_option('display.max_rows', None)
    
    
    
    Faulty_Match_Datasets = []
    
        
    
    Match_Numbers = matches_to_check

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Final Version of the Tracking Dataset With Velocities For Match `Match_Num`    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Tracking_Data_Match_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
    
    
    
        # Number of Columns
        
        Num_Columns_Tracking_Data = Tracking_Data_Match_df.shape[1]
        
        
    
        # Displaying the #Missing (`NaN`) Values That Are Remaining - Hopefully = 0  !!
        
        Num_Missing_Values_Tracking_Data_df_Final = Tracking_Data_Match_df.isna().apply(lambda column: column[column == True].count()).sum()

                
        
        if ( Num_Columns_Tracking_Data != 216 ) | ( Num_Missing_Values_Tracking_Data_df_Final != 0 ):
            
            Faulty_Match_Datasets.append(Match_Num)
            
            print(f"#Columns For Match #{Match_Num + 1} = {Num_Columns_Tracking_Data}", "\n")
            
            print(f"#Missing Values For Match #{Match_Num + 1} = {Num_Missing_Values_Tracking_Data_df_Final}", "\n")
    
            print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    if Faulty_Match_Datasets != []:
    
        print(f"Faulty Match Tracking Datasets = {Faulty_Match_Datasets}", "\n")
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
    if Faulty_Match_Datasets == []:
    
        print(f"\033[92m\033[1m All Match Tracking Datasets Were Correctly Processed & Cleaned! \033[0m", "\n")
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
    
    
    
    
    return  print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Extracting_Unique_xG_Values( possessions_df ):
    """
    Function That Extracts the Unique (Sum of) xG Values From the `nextxgfor` & `nextxgagainst` Columns From the Possessions Dataset
    
    Input: possessions_df = DataFrame of the Possessions Dataset
    
    Output: List_of_Unique_xG_Values = List of the Unique (Sum of) xG Values
    """
    
    Stored_xG_Values = []
    List_of_Unique_xG_Values = []
    

    for Row_Index, Row_Data in possessions_df.iterrows():
        
        Next_xG_For_Row_Value = Row_Data["nextxgfor"]
        Next_xG_Against_Row_Value = Row_Data["nextxgagainst"]

        
        if Next_xG_For_Row_Value == 0.0 and Next_xG_Against_Row_Value == 0.0:
            
            continue  # Ignore Rows With Both Values As 0.0
            

        if Next_xG_For_Row_Value > 0.0 and Next_xG_For_Row_Value not in Stored_xG_Values:
            
            List_of_Unique_xG_Values.append(Next_xG_For_Row_Value)
            Stored_xG_Values.append(Next_xG_For_Row_Value)

            
        if Next_xG_Against_Row_Value > 0.0 and Next_xG_Against_Row_Value not in Stored_xG_Values:
            
            List_of_Unique_xG_Values.append(Next_xG_Against_Row_Value)
            Stored_xG_Values.append(Next_xG_Against_Row_Value)

            
        if 0.0 in Stored_xG_Values and (Next_xG_For_Row_Value > 0.0 or Next_xG_Against_Row_Value > 0.0):
            
            continue  # Continue to the next row until a non-zero value is found
            
            

    return List_of_Unique_xG_Values










def Adding_xG_To_Match_Tracking_Datasets( all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns_df, matches_to_update = range(0, 361), want_to_debug = False ):
    """
    Function That Adds 1 New Column To the Match Tracking Datasets: `(Sum_of)_xG`, Whether a Shot or a Goal Occurred/Will Occur Within 10s of the Possession, Represented By It's Respective Goal-Scoring Probability Value.
    
    Input: all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns_df = DataFrame of All the Possessions With Shots & Goals Added, Without the `nextgoal`-Related Columns
    Input: matches_to_update = List or Range of Integer Numbers of the Matches To Update
    Input: want_to_debug = Boolean Value, Which States Whether Some Debugging Features Should Be Ouputted To Help You Debug & Correct the Errors In the Possessions Data
    
    """    
    
    pd.set_option('display.max_rows', None)
    
        
    
    Match_Numbers = matches_to_update

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Final Version of the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Final_Match_Tracking_Data_For_Match_Num_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
        
        
        
        
        #  Create (Target) Variable `(Sum_of)_xG` Extracting the (Sum of) xG Value Whenever There Will Be a Shot/Attempt To Score Within the Next 10s (≡ 250 Frames), This Info./Threshold Being Intrinsically Encapsulated Within the `nextxgfor/against` Columns

        Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] = 0.0
        
        
        
        # Extract All Possessions For the Specific Match # `Match_Num`
        
        All_Possessions_With_Shots_and_Goals_Added_Without_NextGoal_Related_Columns_For_Match_Num_df = all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns_df[ all_possessions_with_shots_and_goals_added_without_nextgoal_related_columns_df["MatchId"] == Match_Num ]
        
        
        
        # Filter the Possessions Where Only Shots Occurred (i.e. `nextxgfor` or `nextxgagainst` > 0)
                
        Possessions_of_Shots_Only_Without_NextGoal_Related_Columns_For_Match_Num_df = All_Possessions_With_Shots_and_Goals_Added_Without_NextGoal_Related_Columns_For_Match_Num_df[ ( All_Possessions_With_Shots_and_Goals_Added_Without_NextGoal_Related_Columns_For_Match_Num_df["nextxgfor"] > 0.0 ) | ( All_Possessions_With_Shots_and_Goals_Added_Without_NextGoal_Related_Columns_For_Match_Num_df["nextxgagainst"] > 0.0 ) ]
        
        
                
        for Row_Index, Row_Data in Possessions_of_Shots_Only_Without_NextGoal_Related_Columns_For_Match_Num_df.iterrows():
        
            if Row_Data["is_start"] == True:
                
                Start_Frame = Row_Data["frames"]
                End_Frame = Start_Frame + Row_Data["duration"]
                
                Final_Match_Tracking_Data_For_Match_Num_df.loc[Start_Frame : End_Frame, "(Sum_of)_xG"] = Row_Data['nextxgfor'] if Row_Data['nextxgfor'] > 0.0 else Row_Data['nextxgagainst']
                
                
                
            if Row_Data["is_start"] == False:
                
                End_Frame = Row_Data["frames"]
                Start_Frame = End_Frame - Row_Data["duration"]
                
                Final_Match_Tracking_Data_For_Match_Num_df.loc[Start_Frame : End_Frame, "(Sum_of)_xG"] = Row_Data['nextxgfor'] if Row_Data['nextxgfor'] > 0.0 else Row_Data['nextxgagainst']
                
                
                
                
                
        # Extracting Into a List the Unique Values of the (Sum of) xG In the Match
    
        List_of_Unique_xG_Values = TFwDCFs.Extracting_Unique_xG_Values(possessions_df = Possessions_of_Shots_Only_Without_NextGoal_Related_Columns_For_Match_Num_df)
    
    
        if want_to_debug == True:
            
            print(List_of_Unique_xG_Values)
        
    
        # For Every Unique (Sum of) xG Value Present, Find the First & Last Index Values In Which Appears & Fill In Any `0.0`-Valued Gaps In Between With Their Respective Values
    
        for xG_Value in List_of_Unique_xG_Values:
            
            if want_to_debug == True:
            
                print(xG_Value)
                print(Final_Match_Tracking_Data_For_Match_Num_df[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] == xG_Value ]["(Sum_of)_xG"])
            
            
            Starting_Frame_of_xG_Value = Final_Match_Tracking_Data_For_Match_Num_df[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] == xG_Value ].index[0]
            Final_Frame_of_xG_Value = Final_Match_Tracking_Data_For_Match_Num_df[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] == xG_Value ].index[-1]
        
            Final_Match_Tracking_Data_For_Match_Num_df.loc[Starting_Frame_of_xG_Value : Final_Frame_of_xG_Value, "(Sum_of)_xG"] = xG_Value
                
                
                
                
        
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`, After Adding the (Sum of) xG Column

        print(f"Final Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} With (Sum of) xG Included  = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
    
    
    
        # Save Final Version of the Tracking Data As a New "_Final.parquet" File
    
        Final_Match_Tracking_Data_For_Match_Num_df.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
        print(f"\033[92m\033[1m Final Version of the Tracking Data For Match #{Match_Num + 1} With (Sum of) xG Included  --> Succesfully Saved \033[0m", '\n')
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
    
    
    
    
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Adding_Shots_To_Match_Tracking_Datasets( matches_to_update = range(0, 361), want_to_debug = False ):
    """
    Function That Adds 1 New Column To the Match Tracking Datasets: `Will_Be_a_Shot`, Which Represents Whether a Shot Occurred/Will Occur Within 10s (≡ 250 Frames) of the Possession.
    
    Input: matches_to_update = List or Range of Integer Numbers of the Matches To Update
    
    """    
    
    Match_Numbers = matches_to_update

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Final Version of the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Final_Match_Tracking_Data_For_Match_Num_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
        
        
        
        
        #  Create (Target) Variable `Will_Be_a_Shot` Extracting Whether There Will Be a Shot/Chance To Score Within the Next 10s (≡ 250 Frames), This Info./Threshold Being Intrinsically Encapsulated Within the `(Sum_of)_xG` Column

        Final_Match_Tracking_Data_For_Match_Num_df["Will_Be_a_Shot"] = 0.0    

        Final_Match_Tracking_Data_For_Match_Num_df.loc[ Final_Match_Tracking_Data_For_Match_Num_df["(Sum_of)_xG"] > 0 , "Will_Be_a_Shot" ] = 1.0
        
        
        
        
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`, After Adding the Shots Column

        print(f"Final Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} With Shots Included  = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
    
    
    
        # Save Final Version of the Tracking Data As a New "_Final.parquet" File
    
        Final_Match_Tracking_Data_For_Match_Num_df.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
        print(f"\033[92m\033[1m Final Version of the Tracking Data For Match #{Match_Num + 1} With Shots Included  --> Succesfully Saved \033[0m", '\n')
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
    
    
    
    
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Extracting_Unique_Frames_At_Which_Goals_Occur( possessions_df ):
    """
    Function That Extracts the Unique Frames At Which Goals Occur From the `nextgoalfor` & `nextgoalagainst` Columns From the Possessions Dataset
    
    Input: possessions_df = DataFrame of the Possessions Dataset
    
    Output: List_of_Unique_Frames_At_Which_Goals_Occur = List of the Unique (Sum of) xG Values
    """
    
    Stored_Goal_Frame_Numbers = []
    List_of_Unique_Frames_At_Which_Goals_Occur = []
    

    for Row_Index, Row in possessions_df.iterrows():
        
        Next_Goal_Frame_For_Row_Value = Row["nextgoalfor"]
        Next_Goal_Frame_Against_Row_Value = Row["nextgoalagainst"]

        
        if Next_Goal_Frame_For_Row_Value == 0.0 and Next_xG_Against_Row_Value == 0.0:
            
            continue  # Ignore Rows With Both Values As 0.0
            

        if Next_Goal_Frame_For_Row_Value > 0.0 and Next_Goal_Frame_For_Row_Value not in Stored_Goal_Frame_Numbers:
            
            List_of_Unique_Frames_At_Which_Goals_Occur.append(Next_Goal_Frame_For_Row_Value)
            Stored_Goal_Frame_Numbers.append(Next_Goal_Frame_For_Row_Value)

            
        if Next_Goal_Frame_Against_Row_Value > 0.0 and Next_Goal_Frame_Against_Row_Value not in Stored_Goal_Frame_Numbers:
            
            List_of_Unique_Frames_At_Which_Goals_Occur.append(Next_Goal_Frame_Against_Row_Value)
            Stored_Goal_Frame_Numbers.append(Next_Goal_Frame_Against_Row_Value)

            
        if 0.0 in Stored_Goal_Frame_Numbers and (Next_Goal_Frame_For_Row_Value > 0.0 or Next_Goal_Frame_Against_Row_Value > 0.0):
            
            continue  # Continue to the next row until a non-zero value is found
            
            

    return List_of_Unique_Frames_At_Which_Goals_Occur










def Adding_Goals_To_Match_Tracking_Datasets( all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns_df, matches_to_update = range(0, 361), want_to_debug = False ):
    """
    Function That Adds 1 New Column To the Match Tracking Datasets: `Will_Be_a_Goal`, Which Represents Whether a Goal Occurred/Will Occur Within 10s (≡ 250 Frames) of the Possession, Where the Exact Frame In Which the Goal Occurs Is Pinpointed By the Values > 0.0 In the `nextgoalfor` & `nextgoalagainst` In the Possessions DataFrame
        
    Input: all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns_df = DataFrame of All the Possessions With Shots & Goals Added, With the `nextgoal`-Related Columns
    Input: matches_to_update = List or Range of Integer Numbers of the Matches To Update
    Input: want_to_debug = Boolean Value, Which States Whether Some Debugging Features Should Be Ouputted To Help You Debug & Correct the Errors In the Possessions Data
    
    """    
    
    pd.set_option('display.max_rows', None)
    
        
    
    Match_Numbers = matches_to_update

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Final Version of the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Final_Match_Tracking_Data_For_Match_Num_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
    
    
    
    
        # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`

        print(f"Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
        
        
        
                        
        # Create (Target) Variable `Will_Be_a_Goal` Extracting Whether There Will Be a Goal Within the Next 10s (≡ 250 Frames)
        
        Final_Match_Tracking_Data_For_Match_Num_df["Will_Be_a_Goal"] = 0.0
        
        
        
                        
        # Extract All Possessions For the Specific Match # `Match_Num`
        
        All_Possessions_With_Shots_and_Goals_Added_and_With_NextGoal_Related_Columns_For_Match_Num_df = all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns_df[ all_possessions_with_shots_and_goals_added_with_nextgoal_related_columns_df["MatchId"] == Match_Num ]
        
        
        
        
        # Extracting Into a List the Unique Frame Numbers In Which Goals Occur In the Match
    
        List_of_Unique_Frames_At_Which_Goals_Occur = TFwDCFs.Extracting_Unique_Frames_At_Which_Goals_Occur(possessions_df = All_Possessions_With_Shots_and_Goals_Added_and_With_NextGoal_Related_Columns_For_Match_Num_df )
        
        
        if want_to_debug == True:
            
            print(List_of_Unique_Frames_At_Which_Goals_Occur)
            
        
        
        if List_of_Unique_Frames_At_Which_Goals_Occur == []:    # This Would Imply That the `nextgoalfor` & `nextgoalagainst` Is Full of `NaNs`  ⇒  Match Resulted In a 0-0 Score At the End of the Game
            
            
            # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`, After Adding the Goals Column

            print(f"Final Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} With Goals Included  = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
    
    
    
            # Save Final Version of the Tracking Data As a New "_Final.parquet" File
    
            Final_Match_Tracking_Data_For_Match_Num_df.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
            print(f"\033[92m\033[1m Final Version of the Tracking Data For Match #{Match_Num + 1} With Goals Included  --> Succesfully Saved   --   Final Score Was 0-0 \033[0m", '\n')
        
        
            print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
    
    
        
        
        
        if List_of_Unique_Frames_At_Which_Goals_Occur != []:
        
        
            # Frames' Window For Lead-Up To the Goal & For the Celebration After Scoring a Goal
        
            Lead_Up_To_the_Goal_Frames_Window_10s = 250
            
            Goal_Celebration_Frames_Window_5s = 125
        
        
    
            # For Every Unique Frame Number In Which Goals Occur, Find the First & Last Index Values In Which Appears & Fill In Any `0.0`-Valued Gaps In Between With Their Respective Values
    
            for Goal_Frame_Number in List_of_Unique_Frames_At_Which_Goals_Occur:
            
                            
                Final_Match_Tracking_Data_For_Match_Num_df.loc[Goal_Frame_Number - Lead_Up_To_the_Goal_Frames_Window_10s : Goal_Frame_Number + Goal_Celebration_Frames_Window_5s, "Will_Be_a_Goal"] = 1.0
            
            
                if want_to_debug == True:
            
                    print(Goal_Frame_Number)
                    print(Final_Match_Tracking_Data_For_Match_Num_df.loc[ Final_Match_Tracking_Data_For_Match_Num_df["Will_Be_a_Goal"] == 1.0, ["(Sum_of)_xG", "Will_Be_a_Shot", "Will_Be_a_Goal"] ])
    
    
    
            
            # Dimensions of the Dataset of the Tracking Data For Match `Match_Num`, After Adding the Goals Column

            print(f"Final Dimensions of the Dataset of the Tracking Data For Match #{Match_Num + 1} With Goals Included  = {Final_Match_Tracking_Data_For_Match_Num_df.shape}", '\n')
    
    
    
            # Save Final Version of the Tracking Data As a New "_Final.parquet" File
    
            Final_Match_Tracking_Data_For_Match_Num_df.to_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
            print(f"\033[92m\033[1m Final Version of the Tracking Data For Match #{Match_Num + 1} With Goals Included  --> Succesfully Saved \033[0m", '\n')
        
        
            print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










def Shots_and_Goals_In_a_Match_Counter_From_Tracking_Data( matches_to_inspect = range(0, 361) ):
    """
    Function That Counts the #Shots and #Goals In a Match
    
    Input: matches_to_inspect = List or Range of Integer Numbers of the Matches To Update
    
    Output: String --> Stating the #Shots and #Goals In the Match
    """
    
    Num_Shots_In_Every_Match = []
    Total_Num_Shots_In_the_Data = 0.0
    
    Num_Goals_In_Every_Match = []
    Total_Num_Goals_In_the_Data = 0.0
    
    
    Match_Numbers = matches_to_inspect

    for Match_Num in Match_Numbers:
    
    
    
        # Read-In/Load-In the Final Version of the Tracking Dataset For Match `Match_Num`
    
        print('\n',
              f"Loading & Reading In the Tracking Data File For Match #\033[91m\033[1m\033[4m{Match_Num + 1}\033[0m",
              '\n')
    
    
        Tracking_Data_Folder = "Tracking Data/"
    
        Final_Match_Tracking_Data_For_Match_Num_df = pd.read_parquet(f"{Tracking_Data_Folder}{Match_Num}_Final.parquet", engine = "auto")
        
        
        
        # Count the #Shots Made In the Match
        
        Shots_Count = 0
        Previous_Shot_Row_Value = 0.0
    
    
        for Row_Value in Final_Match_Tracking_Data_For_Match_Num_df["Will_Be_a_Shot"]:
        
            if Row_Value == 1.0 and Previous_Shot_Row_Value == 0.0:
            
                Shots_Count += 1
            
            Previous_Shot_Row_Value = Row_Value
            
            
        Num_Shots_In_Every_Match.append(Shots_Count)
            
            
        print(f"\033[92m\033[1m There Were {Shots_Count} Shots \033[0m", '\n')
        
        
        
        # Count the #Goals Scored In the Match
        
        Goals_Count = 0
        Previous_Goal_Row_Value = 0.0
    
    
        for Row_Value in Final_Match_Tracking_Data_For_Match_Num_df["Will_Be_a_Goal"]:
        
            if Row_Value == 1.0 and Previous_Goal_Row_Value == 0.0:
            
                Goals_Count += 1
            
            Previous_Goal_Row_Value = Row_Value
            
            
        Num_Goals_In_Every_Match.append(Goals_Count)
            
            
        print(f"\033[92m\033[1m There Were {Goals_Count} Goals \033[0m", '\n')
        
        
        print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
    
    Total_Num_Shots_In_the_Data = sum(Num_Shots_In_Every_Match)
    
    Total_Num_Goals_In_the_Data = sum(Num_Goals_In_Every_Match)
    
    
    print(f"\033[92m\033[1m Total #Shots In the Tracking Data  = \033[0m \033[91m\033[1m\033[4m{Total_Num_Shots_In_the_Data}\033[0m", '\n')
    
    print(f"\033[92m\033[1m Total #Goals In the Tracking Data  = \033[0m \033[91m\033[1m\033[4m{Total_Num_Goals_In_the_Data}\033[0m", '\n')
        
        
    print("\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m",
          "\033[36m\033[1m_________________________________________________________________________________________________________________________________________________________________________________\033[0m", '\n')
        
        
        
        
    return print("\033[92m\033[1m FINISHED \033[0m", '\n')










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




