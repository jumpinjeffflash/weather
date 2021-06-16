import streamlit as st

st.write("""
# Severe weather dashboard
""")

# Options: Current severe weather alerts or previous storms:

option = st.sidebar.selectbox("Please make your selection:", ('Severe Weather Update', 'Historical Hurricanes/Storms'), 0)

# Severe Weather Update charts:

if option == 'Severe Weather Update':
    
    st.write("""## Today's severe weather watches & tornado outlook""")
    
    st.write("""### Current severe weather watches""")
    st.write("""Watches give advance notice about development of severe weather. A warning is issued when hazardous weather is occurring, is about to occur or is likely to occur:""")
    st.image('https://www.spc.noaa.gov/products/watch/validww.png', width=675)
    st.write("""(Tornado watches are red. Severe thunderstorm watches are blue)""")
    
    st.write("""### Today's tornado threat""")
    st.write("""This shows the probability of a tornado within 25 miles of a point:""")
    st.image('https://www.spc.noaa.gov/products/outlook/day1probotlk_torn.gif', width=675)
    
    st.write("""## Storm Outlook for the next two days""")
    st.write("""This categorical graphic depicts general thunderstorm areas (TSTM-light green) and up to five risk types (defined below) based on the coverage and intensity of organized severe weather such as supercells, squall lines, and multicell thunderstorm complexes:""")
    st.image('https://www.spc.noaa.gov/products/outlook/day2otlk_0600.gif', width=675)
    st.write("""Category Definitions:""")
    st.image('https://i.ibb.co/VvQMWNv/risk-categories.png')
    
    st.write("""## Future Hurricane Radar""")
    st.write("""The graphic below displays all currently active tropical cyclones, and disturbances with tropical cyclone formation potential over the next 48 hours...""")
    st.image('https://www.nhc.noaa.gov/xgtwo/two_atl_2d0.png')
    
    st.write("""...and this graphic displays all currently active tropical cyclones, and disturbances with tropical cyclone formation potential over the next five days:""")
    st.image('https://www.nhc.noaa.gov/xgtwo/two_atl_5d0.png')

### st.write("""## Watchings & Warnings: BILL""")
### st.write("""The NHC Track Forecast Cone below represents the probable track of the center of a tropical cyclone, and is formed by enclosing the area swept out by a set of circles along the forecast track (at 12, 24, 36 hours, etc). The size of each circle is set so that two-thirds of historical official forecast errors over a 5-year sample fall within the circle.""")
### st.image('https://www.nhc.noaa.gov/storm_graphics/AT02/AL022021_5day_cone_no_line_and_wind.png')

# Hurricanes/Storms via TroPYcal:

if option == 'Historical Hurricanes/Storms':
    
    st.write("""## Notable hurricanes from previous years""")
    st.write("""(Plots from TroPYcal via Python, text from Wikipedia)""")
    
    st.write("""### Hurricane Michael (October 2018)""")
    st.image('https://i.ibb.co/R01XXXj/hurricane-michael-2018.png')
    st.write("""Hurricane Michael was the first Category 5 hurricane to strike the contiguous United States since Andrew in 1992. It was the third-most intense Atlantic hurricane to make landfall in the contiguous United States in terms of pressure, behind the 1935 Labor Day hurricane and Hurricane Camille in 1969. It was the first Category 5 hurricane on record to impact the Florida Panhandle, the fourth-strongest landfalling hurricane in the contiguous United States, in terms of wind speed, and the most intense hurricane on record to strike the United States in the month of October.""")
    
    st.write("""### Hurricane Irma (August-September 2017)""")
    st.image('https://i.ibb.co/0CtNgZn/hurricane-irma-2017.png')
    st.write("""Hurricane Irma was a Cape Verde hurricane that caused widespread destruction across its path in September 2017. Irma was the first Category 5 hurricane to strike the Leeward Islands on record, followed by Maria two weeks later. At the time, it was considered as the most powerful hurricane on record in the open Atlantic region, outside of the Caribbean Sea and Gulf of Mexico until it was surpassed by Hurricane Dorian two years later. It was also the third strongest Atlantic hurricane at landfall ever recorded, just behind the 1935 Labor Day Hurricane and Hurricane Dorian.""")
    
    st.write("""### Hurricane Harvey (August-September 2017)""")
    st.image('https://i.ibb.co/fYYc1vT/hurricane-harvey-2017.png')
    st.write("""Hurricane Harvey was a Category 4 hurricane that made landfall on Texas and Louisiana in August 2017, causing catastrophic flooding and more than 100 deaths. It is tied with 2005's Hurricane Katrina as the costliest tropical cyclone on record, primarily from catastrophic rainfall-triggered flooding in the Houston metropolitan area and Southeast Texas. It was the first major hurricane to make landfall in the United States since Wilma in 2005, ending a record 12-year span in which no hurricanes made landfall at the intensity of a major hurricane throughout the country.""")
        
    st.write("""### Hurricane Wilma (October 2005)""")
    st.image('https://i.ibb.co/Chkf9hK/hurricane-wilma-2005.png')
    st.write("""Hurricane Wilma was the most intense tropical cyclone ever recorded in the Atlantic basin, and the second-most intense tropical cyclone recorded in the Western Hemisphere, after Hurricane Patricia in 2015. Part of the record-breaking 2005 Atlantic hurricane season, which included three of the ten most intense Atlantic hurricanes ever, Wilma was the twenty-second storm, thirteenth hurricane, sixth major hurricane, fourth Category 5 hurricane, and the second-most destructive hurricane of the 2005 season.""")
    
    st.write("""### Hurricane Katrina (August 2005)""")
    st.image('https://i.ibb.co/ZVv3NR1/hurricane-katrina-2005.png')
    st.write("""Hurricane Katrina was a large Category 5 Atlantic hurricane that caused over 1,800 deaths and $125 billion in damage in August 2005, particularly in the city of New Orleans and the surrounding areas. It was at the time the costliest tropical cyclone on record and is now tied with 2017's Hurricane Harvey. The storm was the twelfth tropical cyclone, the fifth hurricane, and the third major hurricane of the 2005 Atlantic hurricane season, as well as the fourth-most intense Atlantic hurricane on record to make landfall in the contiguous United States.""")