import pandas as pd
import krippendorff
import numpy as np

while True:
    file = input("Enter the file name: ")
    if file == "exit" or file == "":
        break
    else:
        try:        
            df = pd.read_excel(file)
            annotations = df[['a', 'b', 'c', 'd', 'e']].values.T
            alpha = krippendorff.alpha(reliability_data=annotations, level_of_measurement='nominal')
            print(f"{file} Krippendorff's Alpha: {alpha:.3f}")
        except FileNotFoundError:
            print("File not found. Please try again.")
        except KeyError:
            print("The file does not contain the required columns. Please try again.")
        except ValueError:
            print("The file contains invalid data. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")