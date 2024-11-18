#Creates a list that hold 10 different questions objects

import questionClass #imports the file that holds the Questions class



def makelist(): #here i made a list of 10 different Question objects by calling the questionClass file and choosing the Questions function
    questionsList = [questionClass.Questions('How many days are in a lunar year?', '354', '365', '243','379','354'),
                     questionClass.Questions('What is the largest planet?', 'Mars', 'Jupiter', 'Earth', 'Pluto', 'Jupiter' ),
                     questionClass.Questions("What is the largest kind of whale?", "Orca whale", "Humpback whale", "Beluga whale", "Blue whale", "Blue whale"),
                     questionClass.Questions("Which dinosaur could fly?", "Triceratops", "Tyrannosaurus Rex", "Pteranodon", "Diplodocus","Pteranodon"),
                     questionClass.Questions("Which of these Winnie the Pooh characters is a donkey?", "Pooh", "Eeyore", "Piglet", "Kanga", "Eeyore"),
                     questionClass.Questions("What is the hottest planet?", "Mars", "Pluto", "Earth", "Venus", "Venus"),
                     questionClass.Questions("Which dinosaur had the largest brain compared to body size?", "Troodon", "Stegosaurus", "Ichthyosaurus", "Gigantoraptor", "Troodon"),
                     questionClass.Questions("What is the largest type of penguins?", "Chinstrap penguins", "Macaroni penguins", "Emperor penguins", "White-flippered penguins", "Emperor penguins"),
                     questionClass.Questions("Which children's story character is a monkey?", "Winnie the Pooh", "Curious George", "Horton", "Goofy", "Curious George"),
                     questionClass.Questions("How long is a year on Mars?", "550 Earth days", "498 Earth days", "126 Earth days", "687 Earth days", "687 Earth days")]
    
    return questionsList #returns the list that will be imported into the driver program 






                     
                     

    
    
                         


    

    






