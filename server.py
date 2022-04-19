import json
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

learnData = {
   "1": {
      "part": "Ear",
      "behavior": "Slightly Bent Forward",
      "explanation": "The cat is telling you what it is playful and curious ",
      "example": "When the cat is given a new toy or seen a new thing",
   },
   "2": {
      "part": "Ear",
      "behavior": "Straight and Upright",
      "explanation": "Something has got your cat’s attention ",
      "example": "Animal in the wild do this instinctively so they could hear more and ascertain if a coming sound means danger or not.",
   },
   "3": {
      "part": "Ear",
      "behavior": "Pinned Back and Flat",
      "explanation": "The cat is very angry at something or maybe at you.",
      "example": "This gesture is most often followed by hissing or growling.",
   },
   "4": {
      "part": "Eye",
      "behavior": "Stares at You and Slowly Blinks Its Eyes",
      "explanation": "It simply means the cat adores you.",
      "example": "Humans are even fond of this slow blinking of the eyes especially when flirting with someone they admire.",
   },
   "5": {
      "part": "Eye",
      "behavior": "Dilated Pupils",
      "explanation": "A sign of excitement. When cats get excited, their pupils dilate and become larger, telling you it is excited and ready to play.",
      "example": "Often be observed when the cat is happily playing with or attacking a toy. Sometimes it can also mean defensiveness or aggression especially the look is accompanied by hissing or growling sound.",
   },
   "6": {
      "part": "Eye",
      "behavior": "Looks at You with a Slit",
      "explanation": "It's definitely angry with you over something.",
      "example": "Often given in the absence of an expected treact.",
   },
   "7": {
      "part": "Tail",
      "behavior": "Tail Wagging",
      "explanation": "A sign of frustration in the feline family rather than excitement as common with other pets.",
      "example": "When your cat wags its tail, it probably isn't happy about something. And you better avoid petting them at that instance as it can lead to a few scratches.",
   },
   "8": {
      "part": "Tail",
      "behavior": "Puffed Up Tail",
      "explanation": "It most often is frighten of something. And if  followed by hissing sound then it is preparing for attack.",
      "example": "The cat displays “Larger-than-life” attitude and sends signal to the enemy that it is scary to deal with.",
   },
   "9": {
      "part": "Tail",
      "behavior": "Curved Tail",
      "explanation": "A sign of curiosity in cats when cats have their tail curved like the question mark sign.",
      "example": "It means they are ready to explore. If you've been looking for a good time to explore your cat to a new toy or activity, whenever the tail is curved might be a good time.",
   },
   "10": {
      "id": 10,
      "part": "Tail",
      "behavior": "Twitching of the Tail",
      "explanation": "Cats twitch their tails when they are ready or excited to play.",
      "example": "It is quite similar to tail wagging but often involves lots of flicks of the tail at its tip.",
   },
   "11": {
      "part": "Tail",
      "behavior": "Tucked Away Tail",
      "explanation": "It is very nervous if it tucks its tail.",
      "example": "Running with tails in-between ones legs has always been an idiom for submission and anxiety.",
   },
}


data = {
    "1": {"question": "Q1: Which one does the cat's ears slight bent forward? (10 pt)",
          "images": ['https://www.koty.pl/wp-content/uploads/2019/08/kocie-uszka-2-864x575.jpg',
                     'https://resc-files-prod.s3.us-west-1.amazonaws.com/s3fs-public/styles/large/public/2018-12/SLC-Feral-ear-tip-9285_1.jpg?VersionId=5Se7m9aAtpsvPIoiCAklTu1Yw.y44_Zq&itok=1Q4mwc2h',
                     'https://culturafelina.com/wp-content/uploads/2018/02/angry_cat.jpg']},
    "2": {"question": "Q2: Which one is the puffed up tail? (10 pt)",
          "images": ['https://pictures-of-cats.org/wp-content/uploads/2020/06/American-ringtail-cat-2A.jpg',
                     'https://i.pinimg.com/564x/1a/c1/e5/1ac1e57b52f9764a247effd7c0df5821.jpg',
                     'https://radiomitre-la100-prod.cdn.arcpublishing.com/resizer/hZpLaZuzpW00ajz5_OTTmJGpZ_A=/1200x0/smart/cloudfront-us-east-1.images.arcpublishing.com/radiomitre/O72VFR474JFJZPR4CH27RNBUXU.jpg',
                     'https://catinfodetective.com/wp-content/uploads/2020/12/cat-4410834_1280-1-300x200.jpg',
                     'https://srbigotesdegato.com/wp-content/uploads/2019/05/bosques-de-siberia-raza-gato.jpg']},
    "3": {"question": "Q3: Select the picture(s) that the cat in a positive mood? (10 pt)",
          "images": ['https://qph.cf2.quoracdn.net/main-qimg-63eb8dd985d48fe45280355f2c2ab6cc-pjlq',
                     'https://static.onecms.io/wp-content/uploads/sites/34/2018/07/12170444/cat-rolling-over-on-back-getty-87883698.jpg',
                     'https://bloximages.newyork1.vip.townnews.com/wfsb.com/content/tncms/assets/v3/editorial/8/fb/8fb3f3bd-0c9d-5f55-be93-8960a8967993/5e5958c592f48.image.jpg',
                     'https://cdn.shopify.com/s/files/1/0344/6469/files/image_14_large.jpg?v=1484682446']},
    "4": {"question": "Q4: What's the best description of the left picture? (10 pt)",
          "images": [
              'https://www.tuxedo-cat.co.uk/wp-content/uploads/2021/07/cat-lying-on-back-with-paws-up-in-sun.jpg?ezimgfmt=rs:382x218/rscb1/ng:webp/ngcb1'],
          "choices": ["A. It's simply communicating a level of trust and confidence in your friendship.",
                      "B. If this pose is actually followed with a hissing sound or a growl, you can touch them.",
                      "C. They are mostly communicating happiness and satisfaction."]},
    "5": {"question": "Q5: Match the meaning of different cat meows. (50 pt)",
          "images": [
              "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2irskMPkz6T10bt_eadBkqQNduJnYHLRLFQ&usqp=CAU"],
          "choices": ["A. Lure their unassuming prey.",
                      "B. Dissatisfaction or a lack of interest.",
                      "C. It is hungry and will like to be fed immediately.",
                      "D. To get your attention and sometimes with cute eyes",
                      "E. A call for mating."],
          "audios": {"Low or drawn out": "https://4170audio.s3.amazonaws.com/low.wav",
                     "Soft pleading": "https://4170audio.s3.amazonaws.com/soft.wav",
                     "Trilling": "https://4170audio.s3.amazonaws.com/trilling.wav",
                     "Yowling": "https://4170audio.s3.amazonaws.com/yowling.wav",
                     "Chirping": "https://4170audio.s3.amazonaws.com/cat-bird-chirp.mp3"}},
    "6": {"question": "Review: Choose the correct one(s) from the following statements (10 pt)",
          "choices": [
              "A. If your cat want to knead on your lap, it is actual a good sign of contentment and happiness.",
              "B. Most time when your cat wiggles its butt, it's getting ready to escape.",
              "C. The cat will let out a series of short, high pitched meows to tell you it's glad you're back.",
              "D. Cats are hunters. Sometimes they make chirping sounds like criskets to lure their unassuming prey."]},
    "7": {"question": "You've already known enough about kittens, hope you will have your own cat.",
          "images": [
              'https://static-cdn.jtvnw.net/jtv_user_pictures/b6be9ae8-3433-4a32-bc20-a749781ca0f5-profile_banner-480-320x160.jpeg']}
}

solutions = [('0',10),('1',10),('12',10),('0',10),('01234',50),('023',10)] #stringfy index of correct objects

user_answers = ['0' for _ in range(len(solutions))] #initialize as empty string
user_answers[4]='012 4'

# ROUTES
@app.route('/')
def home():
   return render_template("home.html")

@app.route('/learn/<id>')
def learn(id):
   return render_template('learn.html', data=learnData[id], id=id)

@app.route('/quiz/<id>')
def quiz(id=None):
    global user_answers
    score=0
    if id==7: #compute score for score page
        for i in range(len(solutions)):
            # give partial credits
            solution_set = set(solutions[i][0])
            answer_set = set(user_answers[i])
            correct_set = solution_set.intersection(answer_set)
            score+=solutions[i][1]/len(solutions[i][0])*len(correct_set)
    print(score)
    return render_template("quiz.html", data=data[id], id=id, user_answers=user_answers, score=score)


if __name__ == '__main__':
   app.run(debug = True)




