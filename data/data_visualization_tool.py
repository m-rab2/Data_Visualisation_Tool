import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd

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

# Function to get plot data from Excel
def get_scatter_plot_data_from_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            x_data = df['X'].tolist()
            y_data = df['Y'].tolist()
            return x_data, y_data
        except Exception as e:
            messagebox.showerror("Error", f"Error reading data from the Excel file: {e}")
    return None, None
def get_scatter_plot_data():
    choice = messagebox.askquestion("Data Input Format", "Do you want to input data from an Excel file?")
    if choice == 'yes':
        x_data, y_data = get_data_from_excel()
        return x_data, y_data
    else:
        x_data = list(map(float, input("Enter x-axis data (space-separated): ").split()))
    y_data = list(map(float, input("Enter y-axis data (space-separated): ").split()))
    return x_data, y_data
def get_pie_chart_data():
    choice = messagebox.askquestion("Data Input Format", "Do you want to input data from an Excel file?")
    if choice == 'yes':
        labels, sizes = get_data_from_excel()
        return labels, sizes
    else:
        labels = input("Enter labels for the pie chart (space-separated): ").split()
        sizes = list(map(float, input("Enter sizes for the pie chart (space-separated): ").split()))
        return labels, sizes
def get_line_chart_data_from_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            x_data = df['X'].tolist()
            y_data = df['Y'].tolist()
            return x_data, y_data
        except Exception as e:
            messagebox.showerror("Error", f"Error reading data from the Excel file: {e}")
    return None, None
def get_data_from_excel():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        try:
            df = pd.read_excel(file_path)
            x_data = df['X'].tolist()
            y_data = df['Y'].tolist()
            return x_data, y_data
        except Exception as e:
            messagebox.showerror("Error", f"Error reading data from the Excel file: {e}")
    return None, None


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

def open_viz_window(choice, root):
    viz_window = tk.Toplevel(root)
    viz_window.title("Visualization Configuration")
    if choice == "Bar Chart" or choice == "Line Chart" or choice == "Scatter Plot":
        choice_text = "Excel" if choice == "Line Chart" else "Excel" if choice == "Scatter Plot" else "Excel"
        choice_func = get_line_chart_data_from_excel if choice == "Line Chart" else get_scatter_plot_data_from_excel
        choice_label = tk.Label(viz_window, text=f"Do you want to input data from an {choice_text} file?")
        choice_label.pack()

        def input_from_file():
            x_data, y_data = choice_func()
            x_data_entry.delete(0, tk.END)
            y_data_entry.delete(0, tk.END)
            x_data_entry.insert(0, " ".join(map(str, x_data)))
            y_data_entry.insert(0, " ".join(map(str, y_data)))

        file_input_button = tk.Button(viz_window, text="Choose File", command=input_from_file)
        file_input_button.pack()
    # Function to handle the 'Visualize' button click
    def visualize():
        if choice == "Bar Chart":
            x_labels = x_labels_entry.get().split()
            data = list(map(float, data_entry.get().split()))
            title = title_entry.get()
            x_label = x_label_entry.get()
            y_label = y_label_entry.get()
            bar_chart(x_labels, data, title, x_label, y_label)
        elif choice == "Line Chart":
            x_data = list(map(float, x_data_entry.get().split()))
            y_data = list(map(float, y_data_entry.get().split()))
            title = title_entry.get()
            x_label = x_label_entry.get()
            y_label = y_label_entry.get()
            line_chart(x_data, y_data, title, x_label, y_label)
        elif choice == "Scatter Plot":
            x_data = list(map(float, x_data_entry.get().split()))
            y_data = list(map(float, y_data_entry.get().split()))
            title = title_entry.get()
            x_label = x_label_entry.get()
            y_label = y_label_entry.get()
            scatter_plot(x_data, y_data, title, x_label, y_label)
        elif choice == "Pie Chart":
            labels = labels_entry.get().split()
            sizes = list(map(float, sizes_entry.get().split()))
            title = title_entry.get()
            pie_chart(labels, sizes, title)
        else:
            messagebox.showerror("Error", "Invalid choice. Please try again.")

    if choice in ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"]:
        if choice == "Bar Chart":
            x_labels_label = tk.Label(viz_window, text="Enter x-axis labels (space-separated):")
            x_labels_label.pack()
            x_labels_entry = tk.Entry(viz_window)
            x_labels_entry.pack()

            data_label = tk.Label(viz_window, text="Enter data values (space-separated):")
            data_label.pack()
            data_entry = tk.Entry(viz_window)
            data_entry.pack()

            title_label = tk.Label(viz_window, text="Enter the title:")
            title_label.pack()
            title_entry = tk.Entry(viz_window)
            title_entry.pack()

            x_label_label = tk.Label(viz_window, text="Enter the x-axis label:")
            x_label_label.pack()
            x_label_entry = tk.Entry(viz_window)
            x_label_entry.pack()

            y_label_label = tk.Label(viz_window, text="Enter the y-axis label:")
            y_label_label.pack()
            y_label_entry = tk.Entry(viz_window)
            y_label_entry.pack()

        elif choice == "Line Chart":
            x_data_label = tk.Label(viz_window, text="Enter x-axis data (space-separated):")
            x_data_label.pack()
            x_data_entry = tk.Entry(viz_window)
            x_data_entry.pack()

            y_data_label = tk.Label(viz_window, text="Enter y-axis data (space-separated):")
            y_data_label.pack()
            y_data_entry = tk.Entry(viz_window)
            y_data_entry.pack()

            title_label = tk.Label(viz_window, text="Enter the title:")
            title_label.pack()
            title_entry = tk.Entry(viz_window)
            title_entry.pack()

            x_label_label = tk.Label(viz_window, text="Enter the x-axis label:")
            x_label_label.pack()
            x_label_entry = tk.Entry(viz_window)
            x_label_entry.pack()

            y_label_label = tk.Label(viz_window, text="Enter the y-axis label:")
            y_label_label.pack()
            y_label_entry = tk.Entry(viz_window)
            y_label_entry.pack()

        elif choice == "Scatter Plot":
            x_data_label = tk.Label(viz_window, text="Enter x-axis data (space-separated):")
            x_data_label.pack()
            x_data_entry = tk.Entry(viz_window)
            x_data_entry.pack()

            y_data_label = tk.Label(viz_window, text="Enter y-axis data (space-separated):")
            y_data_label.pack()
            y_data_entry = tk.Entry(viz_window)
            y_data_entry.pack()

            title_label = tk.Label(viz_window, text="Enter the title:")
            title_label.pack()
            title_entry = tk.Entry(viz_window)
            title_entry.pack()

            x_label_label = tk.Label(viz_window, text="Enter the x-axis label:")
            x_label_label.pack()
            x_label_entry = tk.Entry(viz_window)
            x_label_entry.pack()

            y_label_label = tk.Label(viz_window, text="Enter the y-axis label:")
            y_label_label.pack()
            y_label_entry = tk.Entry(viz_window)
            y_label_entry.pack()

        elif choice == "Pie Chart":
            labels_label = tk.Label(viz_window, text="Enter labels for the pie chart (space-separated):")
            labels_label.pack()
            labels_entry = tk.Entry(viz_window)
            labels_entry.pack()

            sizes_label = tk.Label(viz_window, text="Enter sizes for the pie chart (space-separated):")
            sizes_label.pack()
            sizes_entry = tk.Entry(viz_window)
            sizes_entry.pack()

            title_label = tk.Label(viz_window, text="Enter the title:")
            title_label.pack()
            title_entry = tk.Entry(viz_window)
            title_entry.pack()
        visualize_button = tk.Button(viz_window, text="Visualize", command=visualize)
        visualize_button.pack(pady=10)
    else:
        messagebox.showerror("Error", "Invalid choice. Please try again.")

# Main GUI function
def create_gui():
    def visualize_data():
        selected_viz = viz_combobox.get()
        open_viz_window(selected_viz, root)

    # Create the main window
    root = tk.Tk()
    root.title("Data Visualization Tool")
    root.geometry("500x500")
    root.iconbitmap("waves.ico")
    
    # Define styles
    title_font = ("Helvetica", 16, "bold")
    button_font = ("Helvetica", 12)
    bg_color = "#f0f0f0"  # Light gray background color

    # Set the background color for the entire window
    root.configure(bg=bg_color)
    #  GUI components
    viz_label = tk.Label(root, text="Select Visualization Type:", font=title_font, bg=bg_color)
    viz_label.pack(pady=15)

    viz_options = ["Bar Chart", "Line Chart", "Scatter Plot", "Pie Chart"]
    viz_combobox = ttk.Combobox(root, values=viz_options, font=button_font)
    viz_combobox.pack(pady=25)

    visualize_button = tk.Button(root, text="Visualize", command=visualize_data, font=button_font, bg="#4CAF50", fg="white")
    visualize_button.pack(pady=20)

    root.mainloop()

# Main entry point
if __name__ == "__main__":
    create_gui()

