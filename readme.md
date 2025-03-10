# Bingo Card Generator

Creating bingo cards might seem easy at first, but generating multiple unique sheets can be a tedious and time-consuming process. This lightweight (bit odd looking) and simple script automates the task, making it effortless to generate bingo cards in just a few steps. Put your words or sentences into the wordlist.txt file an run the create.py via the terminal. It's that easy.

## How It Works

1. Add your words or phrases to *wordlist.txt* (one per line).  
2. Run the script from the terminal:  

   ```bash
   python create.py <number_of_sheets>
   ```  
   Replace `<number_of_sheets>` with the number of bingo cards you want to generate.  

3. Your bingo sheets will be created automatically! 🎲 You can copy them directly from terminal. Or you use
   ```bash
   python create.py 10 > bingo_cards.txt
   ```  
   for printing into a file.

## Enjoy & Have Fun! 