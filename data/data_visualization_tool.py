import matplotlib.pyplot as plt


# Visualization functions using Matplotlib
def bar_chart(x_labels, data, title, x_label, y_label):
    # Create a bar chart
    plt.bar(x_labels, data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.show()
def line_chart(x_data, y_data, title, x_label, y_label):
    # Create a line chart
    plt.plot(x_data, y_data, marker='o')
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
def scatter_plot(x_data, y_data, title, x_label, y_label):
    # Create a scatter plot
    plt.scatter(x_data, y_data)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()
def pie_chart(labels, sizes, title):
    # Create a pie chart
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(title)
    plt.axis('equal')
    plt.show()

#To check if the data input is numeric
def is_numeric(data):
    try:
        float(data)
        return True
    except ValueError:
        return False
#To validate the data by checking the entries on x and y axis
def validate_data(x_data, y_data):
    if len(x_data) != len(y_data):
        return False

    if not all(is_numeric(data) for data in x_data) or not all(is_numeric(data) for data in y_data):
        return False

    return True

def get_user_input():
    print("Select the visualization type:")
    print("1. Bar Chart")
    print("2. Line Chart")
    print("3. Scatter Plot")
    print("4. Pie Chart")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == "1":
        x_labels = input("Enter x-axis labels (space-separated): ").split()
        data = list(map(float, input("Enter data values (space-separated): ").split()))
        # 'split()' function splits the data on the basis of space  
        # 'map()' function assigns the function 'float()' to each indivual data point to convert it into floating data point, 
        # list converts the mapped entries into a list,
        # e.g. 20,30,40 is converted into [20, 30, 40]
        title = input("Enter the title: ")
        x_label = input("Enter the x-axis label: ")
        y_label = input("Enter the y-axis label: ")
        bar_chart(x_labels, data, title, x_label, y_label)

    elif choice == "2":
        x_data = list(map(float, input("Enter x-axis data (space-separated): ").split()))
        y_data = list(map(float, input("Enter y-axis data (space-separated): ").split()))
        title = input("Enter the title: ")
        x_label = input("Enter the x-axis label: ")
        y_label = input("Enter the y-axis label: ")
        line_chart(x_data, y_data, title, x_label, y_label)

    elif choice == "3":
        x_data = list(map(float, input("Enter x-axis data (space-separated): ").split()))
        y_data = list(map(float, input("Enter y-axis data (space-separated): ").split()))
        title = input("Enter the title: ")
        x_label = input("Enter the x-axis label: ")
        y_label = input("Enter the y-axis label: ")
        scatter_plot(x_data, y_data, title, x_label, y_label)

    elif choice == "4":
        labels = input("Enter labels for the pie chart (space-separated): ").split()
        sizes = list(map(float, input("Enter sizes for the pie chart (space-separated): ").split()))
        title = input("Enter the title: ")
        pie_chart(labels, sizes, title)


    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    get_user_input()
