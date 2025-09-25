# Mass Shooting Visualizer

Orangeliquid Mass Shooting Visualizer is a Streamlit front-end application that aims to allow the user to visualize incidents of mass shootings documented by https://massshootingtracker.site/.
Mass Shooting Tracker defines a "Mass Shooting" as "A single outburst of violence in which four or more people are shot. This is not the same as mass murder as defined by the FBI.".

The JSON data ranging from 2013-2024 was fetched via the python package curl_cffi. Once fetched, the data needed parsed and thoroughly cleaned in order to determine if each incident had an identified perpetrator. Aside from cleaning Mass Shooting Tracker's "Shooter(s)" column, some columns need type changes, flattening, and seperation of date into year, month, and day. The data was then entered into a SQLAlchemy local database for front end querying.

The two visualization pages named "Single Year Data" and "Multi-Year Data", allow the user to select their data year(s), show the dataframe, and select a X-axis variable. Once the X-axis variable is selected, the user is prompted to select their type of visualization method such as "Bar", "Pie", "Area", "Heat Map", "Scatter Plot", and "All".

A HUGE THANK YOU to Mass Shooting Tracker for the data!

Check them out here: https://massshootingtracker.site/


## Table of Contents

- [Installation](#installation)
- [Getting-Started](#getting-started)
- [Project-Insights](#project-insights)
- [Screenshots](#screenshots)
  - [Information-Page](#information-page)
  - [Single-Year-Page](#single-year-page)
  - [Multi-Year-Page](#multi-year-page)
- [License](#license)

## Installation

To run Mass Shooting Visualizer, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Orangeliquid/Mass-Shooting-Visualizer
   cd Mass_Shooting_Analysis
   ```

2. Ensure UV is downloaded:
   - If UV is not downloaded on your system, download it via pip:
   ```bash
   pip install uv
   ```
   
3. Sync dependencies with UV:
   ```bash
   uv sync
   ```

## Getting Started

1. Verify your current directory in your terminal is in Mass_Shooting_Analysis
   - in terminal run:
      ```bash
      uv run streamlit run streamlit_app.py
      ```
      
2. Your browser will not open and the web application will be displaying the "Information" Page
   - Here you will find the following information:
     - "Purpose of Project"
     - "Process of Project"
     - "Insights of Project"
     - "Final Thoughts"

3. At the top of the page, click the "Single Year Data" button
   - Select a year to visualize by clicking the dropdown and selecting your desired year
   - Click the "Show Data" box to see the selected year's dataframe
   - Select your choice of X-axis variables:
     - "Year"
     - "Month"
     - "Day"
     - "City"
     - "State"
     - "Names"
     - "Suspect_Status"
     - "Suspect_Keyword"

    - Once a X-axis variable is set, choose your desired data visualization option:
      - "Bar"
      - "Pie"
      - "Heat"
      - "Area"
      - "Scatter"
      - "All"

    - Notice that "Year" X-axis variable does not have an option for the "Area" graph
    - "Month" and "Day" X-axis variables do not have the option for the "Heat" map
    - The above mentioned X-axis variables do not work properly with each visualization mentioned

4. Select the "Multi-Year Data" button at the top fo the page
  - Select your years to visualize by draging the "Select Year Range" slider
  - Click the "Show Data" box to see the dataframe for the selected range of years
  - Select your choice of X-axis variables:
     - "Year"
     - "Month"
     - "Day"
     - "State"
     - "Suspect_Status"
     - "Suspect_Keyword"

  - Once a X-axis variable is set, choose your desired data visualization option:
    - "Bar"
    - "Pie"
    - "Heat"
    - "Area"
    - "Scatter"
    - "All"

  - Same Visualization issues as mentioned at the bottom of "Single Year Data"
  - The "Year" X-axis variable does not have an option for the "Area" graph
  - "Month" and "Day" X-axis variables do not have the option for the "Heat" map
  - The above mentioned X-axis variables do not work properly with each visualization mentioned


## Project Insights

This project offered many opportunities to gain insight on the data from the creation process alone. Spending many
hours cleaning and parsing the data has helped me become more familiar with what the data actually is and possible
patterns found in the data.

The data visualization aspect of this project solidified some of the more prominent trends I have noticed.

1. Total incidents(killed and wounded) per year have been on an upward trend from 2013-2024.
    - Starting at around 1500+ incidents in 2013, most proceeding years have raised in incident occurrence.
    - Reaching a peak in 2021 at 4100+, the proceeding years have maintained high numbers.
    - A caveat may be that the Mass Shooting Tracker site did not have as many incidents recorded for earlier
    years, or that mass shooting incidents were not be as well documented in the media back in the early 2010s.
    
2. Total incidents per month indicate that the warmer months of the year have the most incidents.
    - Starting in April and ending in September, both the bar and area graph form a distinct concave down shape.
    - My initial thought was that when the weather is nice, people tend to spend more time outdoors, which may
    lead to more incidents.

3. Total incidents per day are the highest at the start of the month.
    - These could be statistical outliers but days 1, 4, and 5 are the highest values while the proceeding days are
    similar in total incidents.
    - Day 31 is the lowest in value, but this may be due to the 31st day only being found in 7 of the 12 months.

4. Total incidents per state are highest in larger states.
    - California, Illinois, and Texas have the highest amount of incidents and by a decent margin compared to the rest
    of the 47 states.
    - California and Texas have a staggering 39+ million and 31+ million person population, but Illinois has a mere 12+ 
    million person population.
    - I figured more population would correlate to more incidents, but there is obviously more nuance to these incidents
    than population count alone.

5. 24,000+ of the 36000 total incidents have been classified as 'Suspect Unknown'
    - From the start, I noticed that the majority of these incidents list unidentified perpetrators.
    - This raises the question: Are mass shooters more likely to get away with their actions than be caught?
    - The answer isn’t clear for several reasons:
        - The data appears to be based on initial news reports, and Mass Shooting Tracker may not follow up on every 
        case to see if a perpetrator was later identified.
        - Some of the sources may not publish updates when suspects are named or arrested.
        - In some cases, law enforcement may not release the names of perpetrators publicly even after investigations 
        are complete.

## Screenshots

### Information Page

<img width="851" height="568" alt="IP1" src="https://github.com/user-attachments/assets/2958a3ac-438d-496e-9c8d-7919f9dda7e2" />
<img width="795" height="340" alt="IP2" src="https://github.com/user-attachments/assets/c2642216-db8e-4170-979d-5c2c52a8177c" />
<img width="745" height="486" alt="IP3" src="https://github.com/user-attachments/assets/d3ecf389-630a-430b-afd7-34eac5debaeb" />
<img width="755" height="745" alt="IP4" src="https://github.com/user-attachments/assets/0c44411e-66b7-4d34-918e-e9351e585836" />
<img width="592" height="865" alt="IP5" src="https://github.com/user-attachments/assets/ed5b1892-c786-43c4-ac7f-da0e9e43a0f8" />
<img width="733" height="688" alt="IP6" src="https://github.com/user-attachments/assets/ac3b52c2-7211-482c-9b98-60b6bc184e76" />
<img width="716" height="442" alt="IP7" src="https://github.com/user-attachments/assets/67521c73-6fee-4e08-8f52-8054df6602b7" />
<img width="751" height="703" alt="IP8" src="https://github.com/user-attachments/assets/cf86328d-2d7d-4320-91d0-2e3645aa11b4" />
<img width="750" height="519" alt="IP9" src="https://github.com/user-attachments/assets/7719da43-cbe5-431c-9533-42a3fd99d9aa" />
<img width="724" height="344" alt="IP10" src="https://github.com/user-attachments/assets/1a1ea6f8-7192-47d4-8242-735d59e4666b" />

### Single Year Page

<img width="814" height="537" alt="SY1" src="https://github.com/user-attachments/assets/81f6524b-768e-4af6-9801-4190949a1713" />
<img width="776" height="483" alt="SY2" src="https://github.com/user-attachments/assets/263052ae-59e0-4668-9d1f-d1b975abe125" />
<img width="787" height="649" alt="SY3" src="https://github.com/user-attachments/assets/61ec61a0-b8a1-4f9a-b1d4-ae34cb2aabda" />
<img width="769" height="658" alt="SY4" src="https://github.com/user-attachments/assets/101fce20-66bf-4a9f-842f-1ea1e8e0ea35" />
<img width="806" height="707" alt="SY5" src="https://github.com/user-attachments/assets/331c8eeb-7609-4764-a153-2e345f4da316" />
<img width="778" height="653" alt="SY6" src="https://github.com/user-attachments/assets/1248f910-1107-4273-b79a-4f9976d4a875" />
<img width="807" height="651" alt="SY7" src="https://github.com/user-attachments/assets/88f574a1-f982-4e78-ad31-6783bbc004f4" />
<img width="737" height="430" alt="SY8" src="https://github.com/user-attachments/assets/86a07725-a9aa-4f45-bebf-39bd15be0ade" />
<img width="259" height="746" alt="SY9" src="https://github.com/user-attachments/assets/a52a6ff2-b6af-4595-b354-71fb904b8be9" />

### Multi-Year Page

<img width="767" height="605" alt="MY1" src="https://github.com/user-attachments/assets/f5ede05c-3eb5-48a2-a85a-88940a3a8b3c" />
<img width="796" height="825" alt="MY2" src="https://github.com/user-attachments/assets/141149d2-2405-4899-90e4-bf81ea33ed1b" />
<img width="768" height="720" alt="MY3" src="https://github.com/user-attachments/assets/7b54e7d2-033b-4144-b5ce-e616a079e793" />
<img width="750" height="625" alt="MY4" src="https://github.com/user-attachments/assets/ebe630e5-f59e-4441-8f6b-a1e3a7d9d38d" />
<img width="752" height="418" alt="MY5" src="https://github.com/user-attachments/assets/a38b55a8-496d-4f39-b992-70b7071e56e3" />
<img width="709" height="649" alt="MY6" src="https://github.com/user-attachments/assets/cff87aa3-0172-40a1-a14c-69ab7503f186" />
<img width="252" height="742" alt="MY7" src="https://github.com/user-attachments/assets/04ced044-5f66-4a44-8840-7549e473e175" />

## License

This project is licensed under the [MIT License](LICENSE.txt).
