# MarchMadness
This calculator uses Massey's Method for team ranking to determine the ranking of all NCAA basketball teams (mens and womens) to be used to predict the outcomes of the March Madness Tournament. Intended for those good at coding and bad at sports.

How to use:
1. Clone repository
 ```
git clone https://github.com/mradfo/MarchMadness.git
```
3. Install required packages. Additionally install python if not already installed.
```pip install -r requirements.txt```
4. Run main.py
```
python main.py
```
6. Respond to all command line prompts. You may have to Google some information about the start and end of the basketball season you are looking to calculate rankings for.
7. Wait. The ranking.py file scrapes the CBS Sports website for all of the scores of all of the games played on each day of the basketball season. There is a new webpage for each day, so this takes a few minutes to complete for an entire season. The command line will print out the current date, so you can track the progress of the program.
8. Results will be stored in a folder in the current directory titled "results".
9. Once a results file exists, you can run
```
python compare.py
```
to compare 2 teams against each other. You will need to respond to command line prompts there as well.

Notes:
1. If anything stops working, the CBS sports website may have changed the HTML within their website. Since this program relies on web scraping, it will break if this happens. Open a new issue in GitHub if you notice this.
2. The error checking is not very robust here, so enter the command line arguments in the exact format that is described.
