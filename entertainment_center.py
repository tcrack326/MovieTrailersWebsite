import media
import fresh_tomatoes


#all the movies with title, year, director, stars, story, poster image, and youtube trailer
inception = media.Movie("Inception",
                        "2010",
                        "Christopher Nolan",
                        ["Leonardo DiCaprio","Joseph Gordon-Levitt","Ellen Page"],
                        "Dom Cobb is a skilled thief, the absolute best in the dangerous art of extraction, stealing valuable secrets from deep within the subconscious during the dream state, when the mind is at its most vulnerable",
                        "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
                        "https://www.youtube.com/watch?v=8hP9D6kZseM")


how_to_train_your_dragon = media.Movie("How to Train Your Dragon",
                                       "2010",
                                       "Dean Deblois, Chris Sanders",
                                       ["Jay Baruchel", "Gerard Butler", "Christopher Mintz-Plasse"],
                                       "A hapless young Viking who aspires to hunt dragons becomes the unlikely friend of a young dragon himself, and learns there may be more to the creatures than he assumed.",
                                       "http://upload.wikimedia.org/wikipedia/en/9/99/How_to_Train_Your_Dragon_Poster.jpg",
                                       "https://www.youtube.com/watch?v=oKiYuIsPxYk")


avengers = media.Movie("The Avengers",
                       "2012",
                       "Joss Whedon",
                       ["Robert Downey Jr.", "Chris Evans", "Scarlett Johansson"],
                       "Earth's mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.",
                       "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8")

about_time = media.Movie("About Time",
                         "2013",
                         "Richard Curtis",
                         ["Domhnall Gleeson", "Rachel McAdams", "Bill Nighy"],
                         "At the age of 21, Tim discovers he can travel in time and change what happens and has happened in his own life. His decision to make his world a better place by getting a girlfriend turns out not to be as easy as you might think.",
                         "http://upload.wikimedia.org/wikipedia/en/8/88/About_Time_Poster.jpg",
                         "https://www.youtube.com/watch?v=7OIFdWk83no")

city_of_god = media.Movie("City of God",
                          "2002",
                          "Fernando Meirelles, Katia Lund",
                          ["Alexandre Rodrigues", "Matheus Nachtergaele", "Leandro Firmino"],
                          "Two boys growing up in a violent neighborhood of Rio de Janeiro take different paths: one becomes a photographer, the other a drug dealer.",
                          "http://upload.wikimedia.org/wikipedia/en/1/10/CidadedeDeus.jpg",
                          "https://www.youtube.com/watch?v=ioUE_5wpg_E")

wallE = media.Movie("WALL-E",
                    "2008",
                    "Andrew Stanton",
                    ["Ben Burtt","Elissa Knight","Jeff Garlin"],
                    "In the distant future, a small waste collecting robot inadvertently embarks on a space journey that will ultimately decide the fate of mankind.",
                    "http://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
                    "https://www.youtube.com/watch?v=ZisWjdjs-gM")                    

snatch = media.Movie("Snatch",
                     "2000",
                     "Guy Ritchie",
                     ["Jason Statham","Brad Pitt","Benicio Del Toro"],
                     "Unscrupulous boxing promoters, violent bookmakers, a Russian gangster, incompetent amateur robbers, and supposedly Jewish jewelers fight to track down a priceless stolen diamond.",
                     "http://upload.wikimedia.org/wikipedia/fi/b/b1/Snatch_Movie_Poster.jpg",
                     "https://www.youtube.com/watch?v=Q8jbt0wBkMI")

spaceOdyssey = media.Movie("2001: A Space Odyssey",
                           "1968",
                           "Stanley Kubrick",
                           ["Keir Dullea","Gary Lockwood","William Sylvester"],
                           "Humanity finds a mysterious, obviously artificial, object buried beneath the Lunar surface and, with the intelligent computer H.A.L. 9000, sets off on a quest.",
                           "http://upload.wikimedia.org/wikipedia/en/e/ef/2001_A_Space_Odyssey_Style_B.jpg",
                           "https://www.youtube.com/watch?v=E8TABIFAN4o")

laconfidential = media.Movie("L.A. Confidential",
                             "1997",
                             "Curtis Hanson",
                             ["Kevin Spacey", "Russel Crowe", "Guy Pearce"],
                             "As corruption grows in 1950s LA, three policemen - one strait-laced, one brutal, and one sleazy - investigate a series of murders with their own brand of justice.",
                             "http://upload.wikimedia.org/wikipedia/en/d/d8/La_confidential.jpg",
                             "https://www.youtube.com/watch?v=5nnFof4KpKY")


dark_knight = media.Movie("The Dark Knight",
                          "2008",
                          "Christopher Nolan",
                          ["Christian Bale","Heath Ledger","Aaron Eckhart","Maggie Gyllenhaal","Michael Caine","Gary Oldman","Morgan Freeman"],
                          "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, the caped crusader must come to terms with one of the greatest psychological tests of his ability to fight injustice.",
                          "http://upload.wikimedia.org/wikipedia/en/8/83/Dark_knight_rises_poster.jpg",
                          "https://www.youtube.com/watch?v=yQ5U8suTUw0")
                          
#add all the movies to the array movies to pass to fresh_tomatoes

movies = [inception, how_to_train_your_dragon, avengers, city_of_god, wallE, about_time, snatch, spaceOdyssey, laconfidential, dark_knight]

#pass to fresh_tomatoes to create the web page with the movies above
fresh_tomatoes.open_movies_page(movies)
