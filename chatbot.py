import nltk
import text2emotion as te
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from tkinter import *
import numpy
import tflearn
import tensorflow
import random
import json
import pickle

#defines variables
inputcounter = 0
outputcounter = 0
input1 = ""
input2 = ""
input3 = ""
inplabel1 = ""
inplabel2 = ""
inplabel3 = ""
output1 = ""
output2 = ""
output3 = ""
outlabel1 = ""
outlabel2 = ""
outlabel3 = ""
happy = 0
angry = 0
suprise = 0
fear = 0
sad = 0
GUI = Tk()
GUI.title("Therabuddy")


with open("intents.json") as file:
    data = json.load(file)
try:
    with open("data.pickle", "rb") as f:
        words, labels, training, output = pickle.load(f)
except:
    words  = []
    labels  = []
    docs_x = []
    docs_y = []
    for intent in data["intents"]:
        for pattern in intent["patterns"]:
            wrds = nltk.word_tokenize(pattern)
            words.extend(wrds)
            docs_x.append(wrds)
            docs_y.append(intent["tag"])

        if intent["tag"] not in labels:
            labels.append(intent["tag"])

    words = [stemmer.stem(w.lower()) for w in words if w not in "?"]
    words = sorted(list(set(words)))

    lables  = sorted(labels)
    training = []
    output = []

    out_empty = [0 for _ in range(len(labels))]

    for x, doc in enumerate(docs_x):
        bag = []
        wrds = [stemmer.stem(w) for w in doc]
        for w in words:
            if w in wrds:
                bag.append(1)
            else:
                bag.append(0)

        output_row = out_empty[:]
        output_row[labels.index(docs_y[x])] = 1

        training.append(bag)
        output.append(output_row)

    training = numpy.array(training)
    output = numpy.array(output)

    with open("data.pickle", "wb") as f:
        pickle.dump((words, labels, training, output), f)



net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation = "softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load("model.tflearn")
except:
    model.fit(training, output, n_epoch = 1000, batch_size = 8, show_metric = True)
    model.save("model.tflearn")


def bag_of_words(s, words):

    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1

    return numpy.array(bag)

def chat():
    def quit():
            #gets rid of page and calls message to be sent
        GUI.destroy()
        import createmessage

    def emotion():
            #calculates the emotion for the users inputs
        global happy
        global angry
        global suprise
        global fear
        global sad
        emotion = str(te.get_emotion(inputEntry.get()))
            # happy
        happyinp = int((emotion[10]))
        happy = happy + happyinp
            # angry
        angryinp = int((emotion[24]))
        angry = angry + angryinp
            # suprise
        supriseinp = int((emotion[41]))
        suprise = suprise + supriseinp
            # sad
        sadinp = int((emotion[53]))
        sad = sad + sadinp
            # fear
        fearinp = int((emotion[66]))
        fear = fear + fearinp
        display()

    def display():
        global inputcounter
        global input1
        global input2
        global input3
        if inputcounter == 0:
            inputcounter = inputcounter + 1
            input1 = inputEntry.get()
            message1()
        elif inputcounter == 1:
            inputcounter = inputcounter + 1
            input2 = inputEntry.get()
            message2()
        elif inputcounter == 2:
            inputcounter = inputcounter + 1
            input3 = inputEntry.get()
            message3()
        elif inputcounter == 3:
            inputcounter = inputcounter + 1
            input1 = inputEntry.get()
            message4()
        elif inputcounter == 4:
            inputcounter = 2
            input2 = inputEntry.get()
            message5()
        # creates banner at top of screen for name and logo
    banner = Label(text="Therabuddy",
                    width=50,
                    height=1,
                    bg="lightblue",
                    font="arial"
                    )
    banner.pack()
        #creates label to show users where to type
    inputTxt = Label(text = "You:").place(x = 670, y =600)
        #creates entry for users to type into
    global inputEntry
    inputEntry = Entry(width = 30)
    inputEntry.place(x = 700, y = 600)
        #create
    enterInput = Button(text = "enter", command = display).place(x = 900, y = 600)
    exit = Button(text="quit", command=quit).place(x = 700, y = 700)
    inplabel1 = Label(text = "")
    inplabel1.place(x = 900, y = 500)
    inplabel2 = Label(text = "")
    inplabel2.place(x = 900, y = 300)
    inplabel3 = Label(text = "")
    inplabel3.place(x = 900, y = 100)
    outlabel1 = Label(text = "")
    outlabel1.place(x = 700, y = 550)
    outlabel2 = Label(text = "")
    outlabel2.place(x = 700, y = 400)
    outlabel3 = Label(text = "")
    outlabel3.place(x = 700, y = 200)




    def message1():
        global input1
        inplabel1.configure(text = input1, bg = "lightblue")
        output()
    def message2():
        global input2
        inplabel2.configure(text = input1, bg = "lightblue")
        inplabel1.configure(text = input2, bg = "lightblue")
        output()
    def message3():
        global input3
        inplabel3.configure(text = input1, bg = "lightblue")
        inplabel2.configure(text = input2)
        inplabel1.configure(text = input3)
        output()
    def message4():
        global input1
        inplabel3.configure(text = input2)
        inplabel2.configure(text = input3)
        inplabel1.configure(text = input1)
        output()
    def message5():
        global input2
        inplabel3.configure(text = input3)
        inplabel2.configure(text = input1)
        inplabel1.configure(text = input2)
        output()



    def output():
        global outputcounter
        global output1
        global output2
        global output3
        global input1
        global input2
        global input3
        if outputcounter == 0:
            outputcounter = outputcounter + 1
            results = model.predict([bag_of_words(input1, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:

                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg["responses"]
                print(random.choice(responses))

            else:
                output1 = "i didnt get that. Try again"
            displayoutput1()
        elif outputcounter == 1:
            outputcounter = outputcounter + 1
            results = model.predict([bag_of_words(input2, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:

                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg["responses"]
                output2 = random.choice(responses)

            else:
                output2 = "i didnt get that. Try again"
            displayoutput2()
        elif outputcounter == 2:
            outputcounter = outputcounter + 1
            results = model.predict([bag_of_words(input3, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:

                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg["responses"]
                output3 = random.choice(responses)

            else:
                output3 = "i didnt get that. Try again"
            displayoutput3()
        elif outputcounter == 3:
            outputcounter = outputcounter + 1
            results = model.predict([bag_of_words(input1, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:

                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg["responses"]
                output1 = random.choice(responses)

            else:
                output1 = "i didnt get that. Try again"
            displayoutput4()
        elif outputcounter == 4:
            outputcounter = 2
            results = model.predict([bag_of_words(input2, words)])[0]
            results_index = numpy.argmax(results)
            tag = labels[results_index]
            if results[results_index] > 0.7:

                for tg in data["intents"]:
                    if tg["tag"] == tag:
                        responses = tg["responses"]
                output2 = random.choice(responses)

            else:
                output2 = "i didnt get that. Try again"
            #displayoutput5()


    def displayoutput1():
        global output1
        outlabel1.configure(text = output1, bg = "green")
    def displayoutput2():
        global output2
        outlabel2.configure(text = output1, bg = "green")
        outlabel1.configure(text = output2, bg = "green")
    def displayoutput3():
        global output3
        outlabel3.configure(text = output1, bg = "green")
        outlabel2.configure(text = output2)
        outlabel1.configure(text = output3)
    def displayoutput4():
        global output1
        outlabel3.configure(text = output2)
        outlabel2.configure(text = output3)
        outlabel1.configure(text = output1)
    def displayoutput5():
        global output2
        outlabel3.configure(text = output3)
        outlabel2.configure(text = output1)
        outlabel1.configure(text = output2)
    GUI.mainloop()

chat()


