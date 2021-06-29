# Import pandas library
import pandas as pd

def main():
    print("hello pandas!")
    # initialize list of lists
    data = [['tom', 10], ['nick', 15], ['juli', 14]]
  
    # Create the pandas DataFrame
    df = pd.DataFrame(data, columns = ['Name', 'Age'])
  
    # print dataframe.
    print("My dataframe",df)

if __name__ == "__main__":
    main()
