import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '930', '18', 'Ave', 'SW']

# Check is command line arguments were passed
if len(sys.argv) > 1:
    # ['mapit.py', '930', '18', 'Ave', 'SW'] -> '930 18 Ave SW'
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()
    
    # https://www.google.ca/maps/place/<ADDRESS>
    webbrowser.open('https://www.google.ca/maps/place/' + address)
