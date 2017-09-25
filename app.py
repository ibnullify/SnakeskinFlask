#Ibnul Jahan
#SoftDev1 pd7
#HW04 -- Fill Up Yer Flask
#2017-09-25

#here lies our setup
#includes importing flask
from flask import Flask 
app = Flask(__name__)


#This is a basic page as not to scare the wee computer beginners
@app.route("/")
def hello_world():
	return """<b>Heyo, you've reached the best page in the world.</b><p>There's no real reason to go, but check out some of the other sites like <a href="/rebel">/rebel</a> and <a href="/thisacat">/thisacat</a><br>
<br>If you're feeling really cool, check <a href="/pikachu">this</a> out"""

#/thisacat page
@app.route("/thisacat")
def text_print():
	return 'Hah, you would have thought this would be a cat! If you really want a cat, click <a href="static/cat.jpg">here</a>'

#/rebel page
@app.route("/rebel")
def dont_look_down():
        rtn = "Hey, you've reached this page. I would really appreciate it if you didn't scroll down. Thanks! \n"
        for x in range(100):
                rtn += "<br/>"
        rtn += "<h1>You're a rebel. I like you.</h1>"
	return rtn

#/pikachu page
@app.route("/pikachu")
def pika():
	return """Hey, look what I drew!<br>
<pre>
quu..__
 $$$b  `---.__
  "$$b        `--.                          ___.---uuudP
   `$$b           `.__.------.__     __.---'      $$$$"              .
     "$b          -'            `-.-'            $$$"              .'|
       ".                                       d$"             _.'  |
         `.   /                              ..."             .'     |
           `./                           ..::-'            _.'       |
            /                         .:::-'            .-'         .'
           :                          ::''\          _.'            |
          .' .-.             .-.           `.      .'               |
          : /'$$|           .@"$\           `.   .'              _.-'
         .'|$u$$|          |$$,$$|           |  <            _.-'
         | `:$$:'          :$$$$$:           `.  `.       .-'
         :                  `"--'             |    `-.     
        :##.       ==             .###.       `.      `.    `
        |##:                      :###:        |        >     >
        |#'     `..'`..'          `###'        x:      /     /
         \                                   xXX|     /    ./
          \                                xXXX'|    /   ./
          /`-.                                  `.  /   /
         :    `-  ...........,                   | /  .'
         |         ``:::::::'       .            |<    `.
         |             ```          |           x| \ `.:``.
         |                         .'    /'   xXX|  `:`M`M':.
         |    |                    ;    /:' xXXX'|  -'MMMMM:'
         `.  .'                   :    /:'       |-'MMMM.-'
          |  |                   .'   /'        .'MMM.-'
          `'`'                   :  ,'          |MMM<
            |                     `'            |tbap
             \                                  :MM.-'
              \                 |              .''
               \.               `.            /
                /     .:::::::.. :           /
               |     .:::::::::::`.         /
               |   .:::------------\       /
              /   .''               >::'  /
              `',:                 :    .'
                                    
</pre>"""

#Here we call our app and make it run
if __name__=="__main__":
	app.debug = True
	app.run()
