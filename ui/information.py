import streamlit as st


def display_information():
    st.header("""
    All Data Sourced from: https://massshootingtracker.site
    """)

    st.subheader("Purpose of Project")
    st.write("""
    The visualization of data enables us to gain useful insight that may not be easily noticed by looking at the data
    alone. A data frame or excell workbook filled with rows and columns of data is great and can offer insight when
    looking at specific parts of the data, but what about the whole picture? My aim for this project is to take over
    6000 entries of data gathered from Mass Shooting Tracker and make the data more digestible via
    visualization.
    """)

    st.subheader("Process of Project")
    st.write("""
    1. Gather all data, via downloading JSON, from 2013-2024 from the Mass Shooting Tracker website.
    
    2. Parse through the data and determine what needs to be cleaned.
        - My first goal was to determine a way to measure total killed/wounded based on suspect being identified.
        I took a look at the 'Shooters' column in hopes of finding cleanly formatted information on possible perpetrators.
        - 'Shooters' column found on website is actually called 'names' and is quite messy when you actually look at it.
        - There are many typos found within 'names', below are my findings found within 'names' column that I used
        to determine that the shooter is unknown for this incident.
    """)

    st.code(
        """
        unknown_suspect_keywords_after_2019 = [
            "gunman unknown",
            "gunman unkown",
            "gunman unidentified",
            "gunmen unidentified",
            "suspect unidentified",
            "gunmen unknown",
            "gunmen unkown",
            "gunman: unidentified",
            "gunmen: unidentified",
        ]

        unknown_suspect_keywords_before_2020 = [
            "unknown",
            "unkown",
            "two unknown",
            "unidentified",
            "suspect unidentified",
        ]""",
        language="python"
    )

    st.caption("*There may be other discrepancies/naming keywords that I have failed to identify*")

    st.write("""
    - After determining a metric to define unknown perpetrators, I created the 'suspect_status' and 'suspect_keyword'
    column for each entry to later track this information.
    - If any of the keywords found within the code above(unknown_suspect_keywords_after_2019,
    unknown_suspect_keywords_before_2020) are in the 'names' column for an entry, the 'suspect_status'
    will be 'Suspect Unknown' and the 'suspect_keyword' from the code will be entered(ex:'gunman unknown').
    - For 'names' entries that have data that does not match the metric described above, 'suspect_status' will be set to
    'Suspect Identified' and 'suspect_keyword' will be set to 'no keyword'.
    - The parsing logic does differ a bit depending on the year of the data, below I supply my logic used to parse
    the 'names' column depending on year of data.
    """)

    st.code(
        """entry = entry.lower()

    if year > 2019:
        for keyword in unknown_suspect_keywords_after_2019:
            if keyword in entry:
                return "Suspect Unknown", keyword
        for keyword in identifying_suspect_keywords:
            if keyword in entry:
                return "Suspect Identified", keyword

        return "No Suspect Information", "no keyword"
    else:
        for keyword in unknown_suspect_keywords_before_2020:
            if entry.startswith(keyword):
                return "Suspect Unknown", keyword

        return "Suspect Identified", "no keyword"
    """,
        language="python"
    )

    st.write("""
    - Lastly, to stress the variance of data entered into the 'names' column found on the website, below I leave my 
    findings for each year. I audited each year by searching these keywords on the website and making sure the code 
    reflected what was on the site for consistency.
    """)

    st.code(
        """
    2013 -> 194 "unknown" -> 1 "Suspect unidentified" -> 2 "Unidentified" 
         = 197 total unknown
         
    2014 -> 211 "unknown" -> 8 entries with "Unkown" -> 1 entry of "Two Unknown"
         = 220 total unknown
         
    2015 -> 289 "unknown" -> 4 "unidentified" 
         = 293 total unknown
         
    2016 -> 316 "unknown" 
         = 316 total unknown
         
    2017 -> 331 "unknown" -> 2 "unkown" -> 1 "unidentified" 
         = 334 total unknown
         
    2018 -> 286 "unknown" -> 3 "unkown" -> 5 "unidentified" 
         = 294 total unknown
         
    2019 -> 331 "unknown" -> 7 "unkown" -> 25 "unidentified" 
         = 363 total unknown
    ----------------------- Naming Conventions Change past 2019 -----------------------------------------------------
    2020 -> gunman unidentified: 10, gunman: unidentified: 9, gunman unknown: 500,
         gunmen unknown: 16, gunman unkown: 1
         = 536 total unknown
         
    2021 -> gunman unknown: 457, gunmen unknown: 39, gunman: unidentified: 15,
         gunman unidentified: 23, gunmen: unidentified: 3, gunman unkown: 1 
         = 538 total unknown
         
    2022 -> gunman unknown: 450, gunman unidentified: 21, gunmen unknown: 29, 
         gunman: unidentified: 17 gunman unkown: 3, gunmen: unidentified: 2 
         = 522 total unknown
         
    2023 -> gunman unknown: 423, gunman: unidentified: 15, gunmen unknown: 22, 
         gunman unidentified: 7 suspect unidentified: 3, gunmen: unidentified: 1 
         = 471 total unknown
         
    2024 -> gunman unknown: 292, gunmen unknown: 8, gunman: unidentified: 4, 
         gunman unidentified: 4 suspect unidentified: 3 
         = 311 total unknown
    """,
        language="python"
    )

    st.write("""
    - Additionally, 'names' data needed to be flattened into a single string instead of a list.
    - The 'names' column was not the only bit of cleaning that needed to be done. The 'date' column needed to be broken
    down into 'year', 'month', and 'day'.
    - This allows for 3 more variables to be visualized later.
    - A final note on cleaning, 'killed' and 'wounded' entries needed to be converted to integers.
    
    3. Data must be entered into SQLAlchemy database for later querying.
    - Once entered into the database, all entries from 2013-2024 are accessible for querying.
    
    4. Create the front end for the user to visualize and manipulate the data via Altair graphs.
    - Upon accessing the Mass Shooting Visualizer, the user will be met with this 'Information' page and two other
    buttons at the top of the page reading 'Single Year Data' and 'Multi-Year Data'.
    - Both of the later pages mentioned above will allow the user to select their desired X-axis variable found 
    within each entry from the database.
    
    - X-axis variable for 'Single Year Data':
        - 'Year'
        - 'Month'
        - 'Day'
        - 'City'
        - 'State'
        - 'Names'
        - 'Suspect_Status'
        - 'Suspect_Keyword'
    
    - X-axis variables for 'Multi-Year Data':
        - 'Year'
        - 'Month'
        - 'Day'
        - 'State'
        - 'Suspect_Status'
        - 'Suspect_Keyword'
    
    - Once an X-axis variable has been selected the user is prompted to select their desired chart type:
        - 'Bar'
        - 'Pie'
        - 'Area'
        - 'Heat Map'
        - 'Scatter Plot'
        - 'All'
    """)

    st.subheader("Insights of Project")
    st.write("""
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
    """)

    st.subheader("Final Thoughts")
    st.write("""
    Orangeliquid Mass Shooting Visualizer was conceived by my yearning to become a better backend programmer.
    The gathering, cleaning, parsing, and storing of data gets the fire burning inside of me and allows me to get truly
    immersed in any project. I figured that coupling this with a very interesting topic such as mass shooting 
    incidents would allow me to further enhance my data analysis skills. The visualization components of this project
    allowed me to get more familiar with front end logic and data manipulation. The most satisfying part of the project
    is seeing all of the graphs displayed in unison, helping create some sort of order out of such a large data set.
    
    To those that may read this, feel free to draw your own conclusions from this project, and by all means, 
    explore and modify the code to make it your own.
    """)
