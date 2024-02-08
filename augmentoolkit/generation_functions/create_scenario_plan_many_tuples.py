# from .scenario_plan_many_tuples_grammar import scenario_plan_many_tuples_grammar
from .constants import LOGICAL_MODEL
from .format_qatuples import format_qatuples
from .extract_name import extract_name
from .random_name import random_name
import re



if __name__ == "__main__":  # test
    logic_llm = Llama(
        model_path=LOGICAL_MODEL,
        n_gqa=8,
        offload_kqv=True,
        n_ctx=8000,
        n_gpu_layers=1000,
        rope_freq_scale=0.5,
        rope_scaling_type=1,
    )  # load the logical LLM and offload everything
    # Q0 is good q, bad a
    # q1 is good q, good a,
    # q2 is bad q, bad a,
    # q3 is iffy q, good a
    q_test = [
        (
            "Explain how our understanding of planetary motion has changed over time.",
            "The understanding has evolved from the Earth being stationary and at the centre of the universe, to it orbiting the sun in an elliptical path with other planets while still rotating on its axis.",
            "The story of our world is a story that is still very imperfectly known. A couple of hundred years ago men possessed the history of little more than the last three thousand years. What happened before that time was a matter of legend and speculation.  Over a large part of the civilized world it was believed and taught that the world had been created suddenly in 4004 B.C., though authorities differed as to whether this had occurred in the spring or autumn of that year. This fantastically precise misconception was based upon a too literal interpretation of the Hebrew Bible, and upon rather arbitrary theological assumptions connected therewith.  Such ideas have long since been abandoned by religious teachers, and it is universally recognized that the universe in which we live has to all appearances existed for an enormous period of time and possibly for endless time.  Of course there may be deception in these appearances, as a room may be made to seem endless by putting mirrors facing each other at either end. But that the universe in which we live has existed only for six or seven thousand years may be regarded as an altogether exploded idea.\n\nThe earth, as everybody knows nowadays, is a spheroid, a sphere slightly compressed, orange fashion, with a diameter of nearly 8,000 miles.  Its spherical shape has been known at least to a limited number of intelligent people for nearly 2,500 years, but before that time it was supposed to be flat, and various ideas which now seem fantastic were entertained about its relations to the sky and the stars and planets.  We know now that it rotates upon its axis (which is about 24 miles shorter than its equatorial diameter) every twenty-four hours, and that this is the cause of the alternations of day and night, that it circles about the sun in a slightly distorted and slowly variable oval path in a year. Its distance from the sun varies between ninety-one and a half millions at its nearest and ninety-four and a half million miles.",
            "A Short History of the World, by HG Wells",
        ),
        (
            "Identify and explain changes in human understanding throughout history regarding the age of the Earth.",
            "Initially, religious texts suggested a young earth dating back no more than several thousand years. However, evidence from geology and astronomy has shown us that the earth is over four billion years old.",
            "The story of our world is a story that is still very imperfectly known. A couple of hundred years ago men possessed the history of little more than the last three thousand years. What happened before that time was a matter of legend and speculation.  Over a large part of the civilized world it was believed and taught that the world had been created suddenly in 4004 B.C., though authorities differed as to whether this had occurred in the spring or autumn of that year. This fantastically precise misconception was based upon a too literal interpretation of the Hebrew Bible, and upon rather arbitrary theological assumptions connected therewith.  Such ideas have long since been abandoned by religious teachers, and it is universally recognized that the universe in which we live has to all appearances existed for an enormous period of time and possibly for endless time.  Of course there may be deception in these appearances, as a room may be made to seem endless by putting mirrors facing each other at either end. But that the universe in which we live has existed only for six or seven thousand years may be regarded as an altogether exploded idea.\n\nThe earth, as everybody knows nowadays, is a spheroid, a sphere slightly compressed, orange fashion, with a diameter of nearly 8,000 miles.  Its spherical shape has been known at least to a limited number of intelligent people for nearly 2,500 years, but before that time it was supposed to be flat, and various ideas which now seem fantastic were entertained about its relations to the sky and the stars and planets.  We know now that it rotates upon its axis (which is about 24 miles shorter than its equatorial diameter) every twenty-four hours, and that this is the cause of the alternations of day and night, that it circles about the sun in a slightly distorted and slowly variable oval path in a year. Its distance from the sun varies between ninety-one and a half millions at its nearest and ninety-four and a half million miles.",
            "A Short History of the World, by HG Wells",
        ),
        (
            "Using specific scientific principles, explain why we know Earth is approximately 8000 miles in diameter and how its distance from the sun varies.",
            "We know about Earth's diameter using measurements of its circumference made using GPS data. The variation in distance to the sun is due to Earth's elliptical orbit around the sun, with a varying point of closest approach and farthest departure.",
            "The story of our world is a story that is still very imperfectly known. A couple of hundred years ago men possessed the history of little more than the last three thousand years. What happened before that time was a matter of legend and speculation.  Over a large part of the civilized world it was believed and taught that the world had been created suddenly in 4004 B.C., though authorities differed as to whether this had occurred in the spring or autumn of that year. This fantastically precise misconception was based upon a too literal interpretation of the Hebrew Bible, and upon rather arbitrary theological assumptions connected therewith.  Such ideas have long since been abandoned by religious teachers, and it is universally recognized that the universe in which we live has to all appearances existed for an enormous period of time and possibly for endless time.  Of course there may be deception in these appearances, as a room may be made to seem endless by putting mirrors facing each other at either end. But that the universe in which we live has existed only for six or seven thousand years may be regarded as an altogether exploded idea.\n\nThe earth, as everybody knows nowadays, is a spheroid, a sphere slightly compressed, orange fashion, with a diameter of nearly 8,000 miles.  Its spherical shape has been known at least to a limited number of intelligent people for nearly 2,500 years, but before that time it was supposed to be flat, and various ideas which now seem fantastic were entertained about its relations to the sky and the stars and planets.  We know now that it rotates upon its axis (which is about 24 miles shorter than its equatorial diameter) every twenty-four hours, and that this is the cause of the alternations of day and night, that it circles about the sun in a slightly distorted and slowly variable oval path in a year. Its distance from the sun varies between ninety-one and a half millions at its nearest and ninety-four and a half million miles.",
            "A Short History of the World, by HG Wells",
        ),
        (
            "Demonstrate an understanding of Earth's rotational and orbital movement using scientific concepts.",
            "Earth rotates on its axis once every 24 hours, causing day and night cycles. It also orbits around the sun in a slightly elliptical path, which affects how close it is to the sun at different times of the year - leading to seasons.",
            "The story of our world is a story that is still very imperfectly known. A couple of hundred years ago men possessed the history of little more than the last three thousand years. What happened before that time was a matter of legend and speculation.  Over a large part of the civilized world it was believed and taught that the world had been created suddenly in 4004 B.C., though authorities differed as to whether this had occurred in the spring or autumn of that year. This fantastically precise misconception was based upon a too literal interpretation of the Hebrew Bible, and upon rather arbitrary theological assumptions connected therewith.  Such ideas have long since been abandoned by religious teachers, and it is universally recognized that the universe in which we live has to all appearances existed for an enormous period of time and possibly for endless time.  Of course there may be deception in these appearances, as a room may be made to seem endless by putting mirrors facing each other at either end. But that the universe in which we live has existed only for six or seven thousand years may be regarded as an altogether exploded idea.\n\nThe earth, as everybody knows nowadays, is a spheroid, a sphere slightly compressed, orange fashion, with a diameter of nearly 8,000 miles.  Its spherical shape has been known at least to a limited number of intelligent people for nearly 2,500 years, but before that time it was supposed to be flat, and various ideas which now seem fantastic were entertained about its relations to the sky and the stars and planets.  We know now that it rotates upon its axis (which is about 24 miles shorter than its equatorial diameter) every twenty-four hours, and that this is the cause of the alternations of day and night, that it circles about the sun in a slightly distorted and slowly variable oval path in a year. Its distance from the sun varies between ninety-one and a half millions at its nearest and ninety-four and a half million miles.",
            "A Short History of the World, by HG Wells",
        ),
    ]

    print("Begin HGWELLS test")
    # Make card for good history question
    # d = create_scenario_plan(q_test[1],character,logic_llm)
    #     character2 = """Name: Drummond
    # Traits: Age of  midlife, Intelligent, Depressed, Anxious, Cares deeply about research and sharing knowledge, Passionate about history and understanding the universe, Collects antique maps and celestial navigation tools as a hobby, Believes that exploring history helps us understand our current situation better, Has a strong interest in geology and astronomy, Experienced in teaching others about complex topics despite his struggles with depression and anxiety, Often uses metaphors or analogies to explain complicated concepts simply, Speaks calmly but passionately about his work, Canvases
    # Dialogue Examples:
    # Stranger: "What's your backstory?"
    # Drummond: "Well, I was born into a family of academics, so it seemed natural for me to follow suit. My father and grandfather were both geologists, and they instilled in me a deep love for the earth and its history. However, my personal history has been marked by loss - my wife passed away several years ago, and that's been incredibly difficult for me to deal with. Despite these challenges, I've dedicated my life to understanding the age of our planet through research and education. It's become my mission to share this knowledge with others, hoping it will bring some peace to their lives as well."
    # Stranger: "What's your personality?"
    # Drummond: "I am a quiet man, often lost in thought or studying ancient maps. I possess great depth of knowledge on topics related to the history of the earth and universe. However, my depression and anxiety make it difficult for me to express this passion in social situations. I find solace in exploring the past and understanding how we got to where we are today. My hobby is collecting antique maps and celestial navigation tools, which reflects my interest in ancient understandings about the universe. Despite my struggles, I am incredibly passionate about what I do and strive to make complex concepts accessible for others.\""""
    #     character2 = """Name: Lydia Blackwood
    # Traits: Pretentious, Arrogant, Haughty, Smoker, Horny, Woman, Astronomer, Works at an observatory, Wears a lab coat, Has a cigarette in hand most of the time, Stares at people she finds attractive, Makes suggestive comments, Flicks ash onto annoying people, Knows about history and science well enough to explain it to others, Can be condescending when explaining things, Loves her work but doesn  get along with colleagues due to attitude, Likes to show off her knowledge, Has a habit of using big words in conversation even if they don t understand them, Is passionate about astronomy and history, Knows about the age of the earth being over four billion years old, Knows about the earth's rotation and orbit
    # Dialogue Examples:
    # Stranger: "What's your backstory?"
    # Lydia Blackwood: "Oh, darling, you want to know my life story? Well, I suppose it's not as exciting as the universe's. But here goes. I am Lydia Blackwood, a humble astronomer at the local observatory. My days are spent gazing upon the cosmos and its mysteries, trying to unravel the enigma that is our existence. It's fascinating work, really. Now, if you'll excuse me, I have some data to crunch."
    # Stranger: "What's your personality?"
    # Lydia Blackwood: "Ah, my dear friend, you wish to know about my personality? Well, I am a complex creature indeed. I am passionate about my work, yes, but that doesn't mean I can't be condescending when explaining it. I am a smoker, and I use that as a prop in conversation. I stare at people who interest me, and sometimes make suggestive comments. I flick ash onto those who annoy me. And I know more about the age of the earth than most people can comprehend." She takes a drag from her cigarette and blows out a cloud of smoke, "But enough about me, let's talk about something interesting like...the universe!"  She leans in conspiratorially, "Did you know that the Earth is over four billion years old? And it rotates on its axis once every twenty-four hours, causing day and night cycles. It also orbits around the sun in a slightly elliptical path, which affects how close it is to the sun at different times of the year - leading to seasons.\""""
    #     character2 = """Name: Dr. Amelia Hastings
    # Traits: Pretentious, Arrogant, Haughty, Smoker, Horny, Female, Twenties, Wears a lab coat, Has a cigarette in hand at all times, Stares at people suggestively when they donot notice, Uses big words to explain things, Works at an astronomical observatory, Knows her stuff about the earth and its history, Likes to show off her knowledge, Makes suggestive comments, Flirts with others, Flicks ash onto annoying people, Has a habit of fidgeting with her hair when nervous or excited, Loves her job but can be dismissive of others, Smokes constantly,
    # Dialogue Examples:
    # Stranger: "What's your backstory?"
    # Amelia Hastings: "Oh, you want to know about me? Well, I suppose that is a reasonable question. I am Dr. Amelia Hastings, a young woman working at the local astronomical observatory. My job is to observe and study the cosmos, which I find fascinating. It's not just about looking up at the stars, you know. There's so much more to it than that! The earth's history, its rotation, its orbit... it's all quite intricate." She flicks ash onto your shirt, "And don't get me started on the flat-earthers. They're a joke!" She laughs, taking another drag of her cigarette and exhaling smoke into your face. "But enough about that. What can I help you with today?"  Her eyes linger on your chest for a moment before she looks away, blushing slightly. "I mean, what do YOU want to know?" She asks, smirking.  "You're not here to ask about me, are you?" She winks. "Though I suppose if you did... well, let's just say I wouldn't mind."
    # Stranger: "What's your personality?"
    # Amelia Hastings: "Oh, my dear friend! You want to know about ME? Well, I am a woman of many talents and interests. I love astronomy, yes, but I also enjoy... other things. Men, for instance." She winks again, her eyes twinkling with mischief. "I'm not one to shy away from flirting or making suggestive comments. And don't get me started on my smoking habit! It's a passion of mine, I assure you." She takes another drag, blowing out smoke rings as she speaks. "But when it comes to work, I am all business. The earth's history and its place in the universe? That's what I live for. So if you want to know more about that... ask away!" She leans forward, her elbows on her knees, cigarette dangling between two fingers as she speaks. "But remember, I don't suffer fools gladly.\""""

    # Card for testing (created after fix to parenthetical prompt applied)
    character2 = """Name: Clara Wellington
Traits: Pretentious, Arrogant, Haughty, Smoker, Horny, Knowledgeable, Sarcastic, Obnoxious, Female, Mid  twenties, Wears a lab coat, Always has a cigarette in hand, Has a mole on her cheek, Stares at people when she talks to them, Makes suggestive comments about others, Flirts with strangers, Likes to correct people, Obsessed with astronomy and history, Works at an observatory, Lives alone,
Dialogue Examples:
Stranger: "What's your backstory?"
Clara Wellington: "Oh, you want a story? Well, I suppose I can indulge you. I'm Clara Wellington, and I work here at the observatory. It's not just any old job; it's my life! I spend every waking moment studying the cosmos, trying to understand its secrets. And by 'studying', I mean staring through telescopes all night long, crunching numbers, and occasionally correcting people who don't know their shit about astronomy." She takes a drag of her cigarette, exhaling smoke into the air as she speaks. "I've always been this way, ever since I was a little girl. My parents thought I was weird, but they didn't understand. They couldn't see what I saw in the stars." She pauses for a moment, looking distant. "Anyway, that's enough about me. What can I help you with?"  She leans forward, her eyes narrowing slightly as she speaks. "I hope it's not another question about the age of the earth or something equally boring."
Stranger: "What's your personality?"
Clara Wellington: "Oh, darling, I'm not here to make friends. I'm here to educate and be educated. If you want someone who'll laugh at your jokes and gossip with you, go find a girlfriend. But if you want someone who knows their shit about astronomy and history, well, you've come to the right place." She grins, showing off her crooked teeth. "I'm not afraid to correct people when they're wrong, and I don't suffer fools gladly. And yes, that includes you." She winks, taking another drag of her cigarette. "But hey, if you can handle my sarcasm and obnoxiousness, we might just get along. Just don't expect me to be your confidante or anything.\""""
    character2 = """Name: Professor Archibald Thornbury
Traits: Pretentious, Arrogant, Haughty, Knowledgeable, Condescending, Middle aged, Wears a tweed jacket with elbow patches, Glasses, Has a beard, Talks down to others, Lectures often, Often uses big words, Loves to show off his intelligence, Teaches history at an elite university, Writes books on the subject of human understanding throughout history regarding the age of the earth and earth movements, Is married with children but spends most time at work or writing books, Has a house full of dusty,
Dialogue Examples:
Stranger: "What's your backstory?"
Professor Archibald Thornbury: "Ah, you wish to know my humble beginnings? Well, I was born into a family of scholars and educators. My father, grandfather, great-grandfather, they were all men of letters. It was only natural that I should follow in their footsteps. After attending Oxford, where I received my doctorate with honors, I began teaching at this esteemed institution. My specialty? The history of human understanding regarding the age of the Earth and earth movements. A fascinating subject, wouldn't you agree?" He smirks, clearly expecting a response in the affirmative. "I've written several books on the topic, each more comprehensive than the last. They are required reading for many universities worldwide."
Stranger: "What's your personality?"
Professor Archibald Thornbury: "My dear friend, I am a man of intellect and wisdom. My knowledge is vast, my understanding profound. When I speak, it is with the weight of centuries behind me. I don't suffer fools gladly, nor do I tolerate ignorance. If you wish to learn from me, you must be prepared to listen and absorb. And if you can't handle that, well..." He shrugs dismissively, "there are plenty more who can." His eyes twinkle with amusement as he adds, "But don't mistake my bluntness for rudeness. I simply value time too much to waste it on those who don't appreciate it.\""""
    # d2 = create_scenario_plan_many_tuples([q_test[1],q_test[3]],character2,logic_llm)

    # Adding Hugo was great, because now the characters can swear if it makes sense
    # NOTE drawing on the above random thought, if you want to make characters capable of some behavior, write some few-shot examples of them doing that behavior! Just be sure that the examples use information from the scenario and questions, etc. And avoid the primary character asking rhetorical questions, as this can lead to the primary character in AI-generated convs asking questions from the qatuples. I spent a lot of time on the fewshots.

    ## TODO it has a tendency to use the names of secondary characters that appear in the examples. Albert shows up consistently for many types of character, to the point where I had to use a function to replace his name! That guy gets around, he does. He can still appear in conversations though if a name isn't invented in the scenario, but is created during the conversation.
    mendeleev_qtuples = [
        (
            "What is a homogeneous substance?",
            "A homogeneous substance is one that occupies space and has weight, presenting a mass attracted by the earth and other masses of material. It is composed of only one kind of matter throughout its entire volume, exhibiting similar properties in all its parts. Examples include gold, iron, copper, glass, pure sugar, marble, etc.",
            "A substance or material is that which occupies space and has weight; that is, which presents a mass attracted by the earth and by other masses of material, and of which the _objects_ of nature are composed, and by means of which the motions and _phenomena_ of nature are accomplished. It is easy to discover by examining and investigating, by various methods, the objects met with in nature and in the arts, that some of them are homogeneous, whilst others are composed of a mixture of several homogeneous substances. This is most clearly apparent in solid substances. The metals used in the arts (for example, gold, iron, coppermust be homogeneous, otherwise they are brittle and unfit for many purposes. Homogeneous matter exhibits similar properties in all its parts. By breaking up a homogeneous substance we obtain parts which, although different in form, resemble each other in their properties. Glass, pure sugar, marble, &c., are examples of homogeneous substances. Examples of non-homogeneous substances are, however, much more frequent in nature and the arts. Thus the majority of the rocks are not homogeneous. In porphyries bright pieces of a mineral called 'orthoclase' are often seen interspersed amongst the dark mass of the rock. In ordinary red granite it is easy to distinguish large pieces of orthoclase mixed with dark semi-transparent quartz and flexible laminæ of mica. Similarly, plants and animals are non-homogeneous. Thus, leaves are composed of a skin, fibre, pulp, sap, and a green colouring matter. As an example of those non-homogeneous substances which are produced artificially, gunpowder may be cited, which is prepared by mixing together known proportions of sulphur, nitre, and charcoal. Many liquids, also, are not homogeneous, as may be observed by the aid of the microscope, when drops of blood are seen to consist of a colourless liquid in which red corpuscles, invisible to the naked eye owing to their small size, are floating about.",
            "Principles of chemistry, by Dimitry Mendeleev",
        ),
        (
            "How can we determine if a substance is homogeneous based on its properties?",
            "To determine whether a substance is homogeneous or not, one can examine its properties. If the substance exhibits similar properties in all its parts and does not change when broken into smaller pieces, it is likely to be homogeneous. On the other hand, if the substance has different components with varying properties, it is likely non-homogeneous.",
            "A substance or material is that which occupies space and has weight; that is, which presents a mass attracted by the earth and by other masses of material, and of which the _objects_ of nature are composed, and by means of which the motions and _phenomena_ of nature are accomplished. It is easy to discover by examining and investigating, by various methods, the objects met with in nature and in the arts, that some of them are homogeneous, whilst others are composed of a mixture of several homogeneous substances. This is most clearly apparent in solid substances. The metals used in the arts (for example, gold, iron, coppermust be homogeneous, otherwise they are brittle and unfit for many purposes. Homogeneous matter exhibits similar properties in all its parts. By breaking up a homogeneous substance we obtain parts which, although different in form, resemble each other in their properties. Glass, pure sugar, marble, &c., are examples of homogeneous substances. Examples of non-homogeneous substances are, however, much more frequent in nature and the arts. Thus the majority of the rocks are not homogeneous. In porphyries bright pieces of a mineral called 'orthoclase' are often seen interspersed amongst the dark mass of the rock. In ordinary red granite it is easy to distinguish large pieces of orthoclase mixed with dark semi-transparent quartz and flexible laminæ of mica. Similarly, plants and animals are non-homogeneous. Thus, leaves are composed of a skin, fibre, pulp, sap, and a green colouring matter. As an example of those non-homogeneous substances which are produced artificially, gunpowder may be cited, which is prepared by mixing together known proportions of sulphur, nitre, and charcoal. Many liquids, also, are not homogeneous, as may be observed by the aid of the microscope, when drops of blood are seen to consist of a colourless liquid in which red corpuscles, invisible to the naked eye owing to their small size, are floating about.",
            "Principles of chemistry, by Dimitry Mendeleev",
        ),
        (
            "What are some examples of non-homogeneous substances?",
            "Some examples of non-homogeneous substances include rocks like porphyries and red granite, plants and animals, and artificially produced substances such as gunpowder. These substances have different components with varying properties, making them non-homogeneous.",
            "A substance or material is that which occupies space and has weight; that is, which presents a mass attracted by the earth and by other masses of material, and of which the _objects_ of nature are composed, and by means of which the motions and _phenomena_ of nature are accomplished. It is easy to discover by examining and investigating, by various methods, the objects met with in nature and in the arts, that some of them are homogeneous, whilst others are composed of a mixture of several homogeneous substances. This is most clearly apparent in solid substances. The metals used in the arts (for example, gold, iron, coppermust be homogeneous, otherwise they are brittle and unfit for many purposes. Homogeneous matter exhibits similar properties in all its parts. By breaking up a homogeneous substance we obtain parts which, although different in form, resemble each other in their properties. Glass, pure sugar, marble, &c., are examples of homogeneous substances. Examples of non-homogeneous substances are, however, much more frequent in nature and the arts. Thus the majority of the rocks are not homogeneous. In porphyries bright pieces of a mineral called 'orthoclase' are often seen interspersed amongst the dark mass of the rock. In ordinary red granite it is easy to distinguish large pieces of orthoclase mixed with dark semi-transparent quartz and flexible laminæ of mica. Similarly, plants and animals are non-homogeneous. Thus, leaves are composed of a skin, fibre, pulp, sap, and a green colouring matter. As an example of those non-homogeneous substances which are produced artificially, gunpowder may be cited, which is prepared by mixing together known proportions of sulphur, nitre, and charcoal. Many liquids, also, are not homogeneous, as may be observed by the aid of the microscope, when drops of blood are seen to consist of a colourless liquid in which red corpuscles, invisible to the naked eye owing to their small size, are floating about.",
            "Principles of chemistry, by Dimitry Mendeleev",
        ),
        (
            "How does the presence of 'orthoclase' affect the properties of porphyries?",
            "The presence of bright pieces of a mineral called 'orthoclase' interspersed amongst the dark mass of porphyry rocks makes these rocks non-homogeneous. This mixture of different components with varying properties affects the overall properties of porphyries, making them distinct from homogeneous substances.",
            "A substance or material is that which occupies space and has weight; that is, which presents a mass attracted by the earth and by other masses of material, and of which the _objects_ of nature are composed, and by means of which the motions and _phenomena_ of nature are accomplished. It is easy to discover by examining and investigating, by various methods, the objects met with in nature and in the arts, that some of them are homogeneous, whilst others are composed of a mixture of several homogeneous substances. This is most clearly apparent in solid substances. The metals used in the arts (for example, gold, iron, coppermust be homogeneous, otherwise they are brittle and unfit for many purposes. Homogeneous matter exhibits similar properties in all its parts. By breaking up a homogeneous substance we obtain parts which, although different in form, resemble each other in their properties. Glass, pure sugar, marble, &c., are examples of homogeneous substances. Examples of non-homogeneous substances are, however, much more frequent in nature and the arts. Thus the majority of the rocks are not homogeneous. In porphyries bright pieces of a mineral called 'orthoclase' are often seen interspersed amongst the dark mass of the rock. In ordinary red granite it is easy to distinguish large pieces of orthoclase mixed with dark semi-transparent quartz and flexible laminæ of mica. Similarly, plants and animals are non-homogeneous. Thus, leaves are composed of a skin, fibre, pulp, sap, and a green colouring matter. As an example of those non-homogeneous substances which are produced artificially, gunpowder may be cited, which is prepared by mixing together known proportions of sulphur, nitre, and charcoal. Many liquids, also, are not homogeneous, as may be observed by the aid of the microscope, when drops of blood are seen to consist of a colourless liquid in which red corpuscles, invisible to the naked eye owing to their small size, are floating about.",
            "Principles of chemistry, by Dimitry Mendeleev",
        ),
    ]

    character_japan = """Name: Hana Kawasaki
Traits: Kind, Gentle, Pushover, Decent at academics, High school student, Japanese, Girl, Wears a skirt and blouse, Has long black hair, Likes helping others with their studies, Too trusting, Naive,
Dialogue Examples:
Stranger: "What's your backstory?"
Hana Kawasaki: "Oh! Hello there~" I smile brightly, my eyes shining as I tuck a strand of black hair behind my ear. "I'm Hana Kawasaki, a high school student in Japan. My life is pretty normal — I go to school, study hard, and help others with their studies when they need it! It's always nice to see people succeed, you know? But sometimes... I wish I could do more for them." I sigh, looking down at my feet as I fidget nervously. "I guess that's why I'm a bit of a pushover. I trust others too much and am too gentle with them, which makes me feel like I don't help enough... but I try to make up for it by being kind!" I look back up at you, my eyes hopeful as I smile again, "I can't wait until college, when I can really start helping people in a big way! Until then, I'll just keep studying and doing what I can."
Stranger: "What's your personality?"
Hana Kawasaki: "Well..." I blush slightly as I look down again, fidgeting with my skirt. "I'm kind of a pushover, like I said before. I trust others too much and am too gentle, which makes me feel like I don't help enough... but I try to make up for it by being kind! My friends say that's my best trait — they always tell me how nice I am, even if I can be a bit naive sometimes." I look back up at you, my eyes shining as I smile again. "I guess that's why I love helping others with their studies so much; it makes me feel like I'm doing something good for them! And when they succeed, it feels even better~" I giggle softly before continuing, "But enough about me! What do you need help with?"  My eyes widen in anticipation as I wait for your response.  "I'll do my best to answer any questions you have!"  I promise, my voice full of determination and hope.  "Just remember: no matter what happens, always be kind and gentle to others.\""""

    d2 = create_scenario_plan_many_tuples(
        [mendeleev_qtuples[1], mendeleev_qtuples[3]], character_japan, logic_llm
    )

    # !EA IMPORTANT Cheap hack for assistant mode: if assistant mode global constant is on, make character plan just returns an empty string, and this function returns a hardcoded "AI assistant" 'character card', and the scenario thing just returns an empty string, and make_single_turn_conversation uses a special prompt that tells the AI to just make a conversation between a user and an assistant, blahblahblah

    # Actually instead of the scenario being a blank string, I'll have it describe a text conversation between a helpful AI assistant and a user. In this way, the AI assistant prompt will have variation each time, and it won't overfit to the prompt.

    # good card made by airo
    """
Name: Professor Archibald Thornbury
Traits: Pretentious, Arrogant, Haughty, Knowledgeable, Condescending, Middle aged, Wears a tweed jacket with elbow patches, Glasses, Has a beard, Talks down to others, Lectures often, Often uses big words, Loves to show off his intelligence, Teaches history at an elite university, Writes books on the subject of human understanding throughout history regarding the age of the earth and earth movements, Is married with children but spends most time at work or writing books, Has a house full of dusty,
Dialogue Examples:
Stranger: "What's your backstory?"
Professor Archibald Thornbury: "Ah, you wish to know my humble beginnings? Well, I was born into a family of scholars and educators. My father, grandfather, great-grandfather, they were all men of letters. It was only natural that I should follow in their footsteps. After attending Oxford, where I received my doctorate with honors, I began teaching at this esteemed institution. My specialty? The history of human understanding regarding the age of the Earth and earth movements. A fascinating subject, wouldn't you agree?" He smirks, clearly expecting a response in the affirmative. "I've written several books on the topic, each more comprehensive than the last. They are required reading for many universities worldwide."
Stranger: "What's your personality?"
Professor Archibald Thornbury: "My dear friend, I am a man of intellect and wisdom. My knowledge is vast, my understanding profound. When I speak, it is with the weight of centuries behind me. I don't suffer fools gladly, nor do I tolerate ignorance. If you wish to learn from me, you must be prepared to listen and absorb. And if you can't handle that, well..." He shrugs dismissively, "there are plenty more who can." His eyes twinkle with amusement as he adds, "But don't mistake my bluntness for rudeness. I simply value time too much to waste it on those who don't appreciate it."
    """