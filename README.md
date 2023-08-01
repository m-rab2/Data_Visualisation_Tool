# Data Visualization Tool using Tkinter and Matplotlib

This is a Python script that provides a simple Data Visualization Tool with a Graphical User Interface (GUI) using the Tkinter library for the GUI components and Matplotlib for generating different types of plots. The tool allows users to create bar charts, line charts, scatter plots, and pie charts based on their input data.

## Features

1. Bar Chart: Users can create a bar chart by providing x-axis labels and corresponding data values.

2. Line Chart: Users can create a line chart by providing x-axis data and y-axis data.

3. Scatter Plot: Users can create a scatter plot by providing x-axis data and y-axis data.

4. Pie Chart: Users can create a pie chart by providing labels and sizes (percentage values) for each segment.

5. Data Input: Users have the option to input data from an Excel file or manually enter the data through the GUI.

6. Data Validation: The tool validates the input data to ensure the correct format is provided.

## Prerequisites

To run this tool, you need to have the following libraries installed:

- Python 3.x
- Tkinter
- Pandas
- Matplotlib

You can install the required libraries using the following pip command:

```bash
pip install tkinter pandas matplotlib
```

## How to Use

1. Clone the repository or download the Python script from GitHub.

2. Make sure you have Python and the required libraries installed.

3. Run the script using the following command:

```bash
python data_visualization_tool.py
```

4. The tool's GUI window will open, allowing you to select the type of visualization you want to create.

5. Depending on the chosen visualization, you will be prompted to enter the required data, either manually or by loading an Excel file.

6. After providing the necessary data, click the "Visualize" button to generate the plot.

7. The plot will be displayed using Matplotlib's interactive window.

8. You can close the plot window and create another visualization or exit the tool.

## Examples

1. Creating a Bar Chart:
   - Select "Bar Chart" from the drop-down menu.
   - Enter x-axis labels and corresponding data values.
   - Click "Visualize" to generate the bar chart.

2. Creating a Line Chart:
   - Select "Line Chart" from the drop-down menu.
   - Enter x-axis data and y-axis data.
   - Click "Visualize" to generate the line chart.

3. Creating a Scatter Plot:
   - Select "Scatter Plot" from the drop-down menu.
   - Enter x-axis data and y-axis data.
   - Click "Visualize" to generate the scatter plot.

4. Creating a Pie Chart:
   - Select "Pie Chart" from the drop-down menu.
   - Enter labels and sizes (percentage values) for each segment.
   - Click "Visualize" to generate the pie chart.

## Note

- Ensure that the input data is in a valid format (numeric values for numerical plots) to avoid errors.

- The tool will display a message box if any error occurs during data loading or visualization.

- The tool's GUI design and usability can be further enhanced to suit specific needs.

Feel free to explore the code and modify it according to your requirements.

## License

This tool is released under the [MIT License](LICENSE). You are free to use, modify, and distribute the code as per the terms of the license.

## Acknowledgments

This tool was developed using the Python programming language with the help of the Tkinter and Matplotlib libraries. Special thanks to the developers and contributors of these open-source projects for making it possible to create powerful data visualization tools easily.
