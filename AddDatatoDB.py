import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://celebrecognize-default-rtdb.firebaseio.com/"
})

ref = db.reference('Celebs')

data = {
    "2":
        {

        "Name": "Paul Rudd",

        "Description": "Paul Rudd is an American actor known for comedy films like Clueless, Anchorman, Knocked Up, Ant-Man in the Marvel Cinematic Universe, and Living With Yourself. His boyish charm and witty delivery have made him a sought-after comedic leading man for decades.",

        "Age": "53"

        },
    "4":

        {

        "Name": "Daniel Craig",

        "Description": "Daniel Craig is an English actor best known for playing James Bond in five films from 2006's Casino Royale to 2021's No Time to Die. His rugged magnetism and gritty physicality redefined the iconic 007 role in the modern era.",

        "Age": "54"

        },

    "5":

        {

        "Name": "Harrison Ford",

        "Description": "Harrison Ford is one of Hollywood's most iconic leading men known for playing Han Solo and Indiana Jones. Other major films include Blade Runner, Witness, The Fugitive, Air Force One, and What Lies Beneath. His classic masculinity and humor defined generations of blockbusters.",

        "Age": "80"

        },

    "6":

        {

        "Name": "Mila Kunis",

        "Description": "Mila Kunis is an American actress known for playing Jackie on That '70s Show and voicing Meg on Family Guy. Her film roles include Black Swan, Forgetting Sarah Marshall, Bad Moms, Oz the Great and Powerful, and Luckiest Girl Alive.",

        "Age": "39"

        },

    "17":

        {

        "Name": "Denzel Washington",

        "Description": "Denzel Washington is a two-time Academy Award winning American actor known for powerful roles in Glory, Malcolm X, Training Day, Fences, Flight, and portraying civil rights icons. He has extraordinary on-screen presence and gravitas.",

        "Age": "68"

        },
    "21":

        {

        "Name": "Liam Neeson",

        "Description": "Liam Neeson is an acclaimed Irish actor known for Schindler's List, Michael Collins, Taken and Batman Begins. He has been nominated for an Oscar, BAFTA and three Golden Globes thanks to his uncompromising intensity and gravitas on screen.",

        "Age": "70"

        },

    "22":

        {

        "Name": "Charlize Theron",

        "Description": "Charlize Theron is an Academy Award winning South African actress known for playing complex, conflicted women in films like Monster, Mad Max: Fury Road, Bombshell, Tully, Atomic Blonde, and The Devil's Advocate.",

        "Age": "47"

        },

    "23":

        {

        "Name": "Joaquin Phoenix",

        "Description": "Joaquin Phoenix is an enigmatic, fiercely committed American actor known for Walk the Line, Gladiator, Her, The Master, Joker (won Oscar), and documentaries on animal rights. He sharply eschews celebrity culture in Hollywood.",

        "Age": "48"

        },

    "29":

        {

        "Name": "Julianne Moore",

        "Description": "Julianne Moore is an acclaimed American actress who won the Oscar for Still Alice. She is also known for Boogie Nights, Magnolia, Hannibal Lecter, Far From Heaven, The Hours, The Big Lebowski, and portraying feminist icon Gloria Steinem.",

        "Age": "62"

        },
        
    "30":

        {

        "Name": "Edward Norton",

        "Description": "Edward Norton is an acclaimed American actor known for his standout performances in films Primal Fear, American History X, Fight Club, Birdman, and The Grand Budapest Hotel. He has received three Oscar nominations thanks to his commitment and intensity.",

        "Age": "53"

        },

    "37":

        {

        "Name": "Mindy Kaling",

        "Description": "Mindy Kaling is an American actress, comedian, and writer known for The Office, the series she created The Mindy Project, Late Night with Mindy Kaling, and films like Ocean's 8 and Inside Out. Her witty personality and comedic observations about life make her incredibly likable.",

        "Age": "43"

        },

    "39":

        {

        "Name": "Donald Glover",

        "Description": "Donald Glover is an American actor, writer, comedian and musician who performs under the name Childish Gambino. He has found success in comedy series like Community, films like The Martian, Solo: A Star Wars Story, and releasing genre-blending music.",

        "Age": "39"

        }

}

for key,value in data.items():
    ref.child(key).set(value)
