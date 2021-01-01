def plotting () :
    import matplotlib.pyplot as plt
    x = list (input ('Enter the first axis data points: ').split ())
    y = list (input ('Enter the other axis data points: ').split ())
    plt.title (input ('Enter a title for the graph: '))
    plt.xlabel (input ('Enter a name for x-axis: '))
    plt.ylabel (input ('Enter a name for y-axis: '))
    plt.plot(x, y)
    plt.show ()
def colToRow () :
    import pyperclip
    items = list (pyperclip.paste().split ())
    string = ''
    for i in range (len (items)) :
        string += items[i]
        string += ' '
    pyperclip.copy (string)
    
option = int (input ('Enter 1 for Task 3 helper, 0 to plot a graph: '))
if option == 0:
    plotting ()
else :
    x = int (input ('Enter 1 to convert a column to a row, 0 otherwise: '))
    if x == 1:
        colToRow ()
        print ('Converted Rows are copied to the clipboard! ')
    dataSet = list (map (float, input ('Enter your data set separated by spaces: ').split()))
    print (f'Loaded. A list with {len (dataSet)} items. Max = {max (dataSet)}, Min = {min (dataSet)}')
    means = list (map (int, input ('Enter the sample size, that you want to calculate its mean (ranges are separated by a space): ').split()))
    for i in range (len (means)) :
        print (means[i],"\t", round (sum (dataSet[ : means[i]]) / means[i], 3))
