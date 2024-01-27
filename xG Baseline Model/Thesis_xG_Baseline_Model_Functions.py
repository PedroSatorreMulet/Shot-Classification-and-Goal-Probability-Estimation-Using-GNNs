####################################################
#   UNIVERSAL IMPORTS USED THROUGHOUT THE MODULE   #
####################################################



import numpy as np
import pandas as pd


from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score, precision_score, recall_score, f1_score, roc_curve, auc, roc_auc_score, log_loss, brier_score_loss


import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')



import sys   # Provides Access To Some Variables Used Or Maintained By the Python Interpreter & To Functions That Interact Strongly With the Interpreter --> Used For Manipulating the Python Runtime Environment & Interacting With the Interpreter Itself


sys.path.append("../")


# Import the Thesis' Preparing Data For Models Functions Module

import Thesis_Preparing_Data_For_Models_Functions as TPD4MFs












######################################
#         xG MODEL FUNCTIONS         #
######################################



def Read_Relevant_Tracking_Data_4_xG_Model( from_training_or_test_data = "training" ):
    """
    Function That Reads the Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal
    
        
    Output: Relevant_Data_4_xG_Model = Final Version of the Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred Throughout the Season, On 1 Same Target Goal
    """
    
    if from_training_or_test_data == "training":
    
        print('\n',
              f"Loading & Reading In the Final Version of the Augmented Training Relevant Tracking Data For the xG Model - Only Containing the Frames In Which Shots Occurred, On 1 Same Target Goal",
              '\n')
    
    
        xG_Model_Data_Folder = f"Data For xG Model/"
    
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
    
    
        xG_Model_Data_Folder = f"Data For xG Model/"
    
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
    
    
    
    
