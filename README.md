# BirthdayNamesServer
Birthday Party Names as a python local server where one page is to create/change the party information and another is used to display the party information
The url extension for each page is:
- /BlueRoom
- /RedRoom
- /OrangeRoom
- /YellowRoom

The page will auto refresh every second to fetch new changes that come from the main page at '/' This includes updating the CSS and background video


Requires Flask
- pip install Flask

Run server with 
python -m flask run --host=0.0.0.0
