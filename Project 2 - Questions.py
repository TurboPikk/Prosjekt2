q1 = "Q1. What is the capital of Norway?"
q2 = "Q2.What is the currency of Norway?"
q3 = "Q3.What is the largest city in Norway?"
q4 = "Q4.When is constitution day (the national day) of Norway?"
q5 = "Q5.What color is the background of the Norwegian flag?"
q6 = "Q6.How many countries does Norway border?"
q7 = "Q7.What is the name of the university in Trondheim?"
q8 = "Q8.How long is the border between Norway and Russia?"
q9 = "Q9.Where in Norway is Stavanger?"
q10 = "Q10.From which Norwegian city did the world famous composer Edvard Grieg come?"

o1 = {
    "a" : "Bergen",
    "b" : "Oslo",
    "c" : "Stavanger",
    "d" : "Trondheim"
}

o2 = {
    "a" : "Euro",
    "b" : "Pound",
    "c" : "Krone",
    "d" : "Deutsche Mark"
}

o3 = {
    "a" : "Oslo",
    "b" : "Stavanger",
    "c" : "Bergen",
    "d" : "Trondheim"
}

o4 = {
    "a" : "27thMay",
    "b" : "17thMay",
    "c" : "17thApril",
    "d" : "27thApril"
}

o5 = {
    "a" : "Red",
    "b" : "White",
    "c" : "Blue",
    "d" : "Yellow"
}

o6 = {
    "a" : "1",
    "b" : "2",
    "c" : "3",
    "d" : "4"
}

o7 = {
    "a" : "UiS",
    "b" : "UiO",
    "c" : "NMBU",
    "d" : "NTNU"
}

o8 = {
    "a" : "96 km",
    "b" : "196 km",
    "c" : "296 km",
    "d" : "396 km"
}

o9 = {
    "a" : "North",
    "b" : "South",
    "c" : "South-west",
    "d" : "South-east"
}

o10 = {
    "a" : "Oslo",
    "b" : "Bergen",
    "c" : "Stavanger",
    "d" : "Tromsø"
}

solution = ["b", "c", "a", "b", "a", "c", "d", "b", "c", "b"]

def options(dictionary):
    for element in dictionary:
        print(element, ":", dictionary[element])
    return



y = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
x = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10]

