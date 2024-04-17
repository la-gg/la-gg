# Python Code Sample

Welcome to my code sample repository! This repository contains a brief demonstration of my coding ability in python. Feel free to explore the code and documentation.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [License](#license)
- [Contact](#contact)

## Introduction

This code sample demonstrates of my proficiency in python. It provides a clear example of my coding style,  and adherence to best practices.

## Project Structure

This project is organized as follows:

- `Tabela-Os_Invasores.xlsx`: Excel file documenting the landowners in Brazil whose farms overlap Indigenous land. [de Olho nos Ruralistas ‘Os Invasores’ report](https://deolhonosruralistas.com.br/2023/05/11/report-invaders-reveals-companies-and-sectors-behind-overlaps-in-indigenous-lands-in-brazil/)
  
- `Crosswalk.csv`: CSV file created using `Crosswalk.py`, which contains the translated column names of the Excel sheet.
  
- `Crosswalk.py`: Python script creating a crosswalk.csv file to translate the column names of `Tabela-Os_Invasores.xlsx` from Portuguese to English with contextual clues & help of Deep L.
  
- `Cleaning.py`: Python script for translating column names of `Tabela-Os_Invasores.xlsx`, and cleaning data (changing units from hectares to square miles, removing extraneous columns).
  
- `Plotting.py`: Python script for generating histograms to visualize patterns in the data.
  
- `invasions_by_people.jpg`: Histogram showing the number of farms overlapping Indigenous land by group.
  
- `invasions_by_demarcation.jpg`: Histogram showing the number of farms overlapping Indigenous land for each phase of demarcation.

- `LICENSE`: The license file containing the terms and conditions for using the project.

- `README.md`: The README file providing an overview of the project, its structure, and instructions for usage.
  
- **LICENSE**: The license file.

- **README.md**: The README file providing an overview of the project, its structure, and instructions for usage.

## Usage

To run the code sample, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/la-gg/la-gg.git
    ```

2. Run the Python scripts in the following order:

    ```bash
    python scripts/Crosswalk.py
    python scripts/Cleaning.py
    python scripts/Plotting.py
    ```

3. Once executed, the output files (`invasions_by_people.jpg`, `invasions_by_demarcation.jpg`) will be generated.

4. You can then explore the generated histograms to visualize patterns in the data.

Note: Make sure to execute the scripts in the specified order for proper functioning.

## Features

## Features

This code sample project offers the following features:

1. **Data Translation**: The `Crosswalk.py` script translates the column names of the `Tabela-Os_Invasores.xlsx` Excel file from Portuguese to English, providing clarity and consistency in data interpretation.

2. **Data Cleaning**: The `Cleaning.py` script cleans and preprocesses the data from `Tabela-Os_Invasores.xlsx`, ensuring data quality and usability for analysis.

3. **Data Visualization**: The `Plotting.py` script generates informative histograms to visualize patterns in the data, including the number of farms overlapping Indigenous land by group and the number of farms overlapping Indigenous land for each phase of demarcation, aiding in data exploration and interpretation.

4. **Source Link**: The project includes a direct link to the source of the `Tabela-Os_Invasores.xlsx` file, providing transparency and accessibility to the original data source.

5. **Reproducibility**: With clear instructions for usage and a straightforward project structure, the code sample ensures reproducibility, allowing users to easily run the scripts and generate the same output files on their local machines.

These features collectively demonstrate the effectiveness of the code sample in processing, analyzing, and visualizing data related to land ownership and Indigenous land overlaps in Brazil.

## Technologies Used

This code sample uses python, and the pandas, Matplotlib, and Seaborn libraries.


## License

This project is licensed under the Creative Commons Attribution 1.0 Universal License - see the [LICENSE](LICENSE) file for details.

## Contact

- **LinkedIn:** [https://www.linkedin.com/in/alice-lele/]

Feel free to reach out if you have any questions, or feedback!


