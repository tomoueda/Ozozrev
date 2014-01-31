#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
login = """
<html>
	<title> Oz Oz Revolution ! </title>
	<link href="/css/bootstrap.css" rel="stylesheet">
	<script src='https://cdn.firebase.com/v0/firebase.js'></script>
	<link rel="stylesheet" type="text/css" href="css/format.css">
	<script src="js/game-map2.js"></script>
	<body id='bod'>
		<div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">Welcome to Oz</a>
        </div>
      </div>
      </div>
      <br></br>
    <form id='log' class="form-horizontal">
    	<div class="control-group">
    		<div class="controls">
    		<br></br>
    			<input type="text" id="username" placeholder="enter username">

    		 </div>
    		 <br></br>
    		 <div class="control-group">
    		 <div class="controls">
    		 <button id="sub" onclick="clicker(); return false" type="button" class="btn"> Sign In </button>
    		</div>
    	</div>

    	</div>
    </form>
    <br></br>
    <div> <canvas id='myCanvas' width='800' height='500'></canvas> </div>
    </div>
    <div id='hp'> </div>
    </div>

    <script>
        //Sending username to DataBase
            var hp = 800;
            document.getElementById("hp").innerHTML = hp;
            var myDataRef = new Firebase('https://ozoz.firebaseio.com/');
            var connectedRef = new Firebase('https://ozoz.firebaseio.com/.info/connected');
            var myUserRef = myDataRef.push();
            redraw();
            var c =document.getElementById("myCanvas");
            var ctx=c.getContext("2d");
            var map = new gameMap();

            var imgd = document.createElement("img");
            var imgd2 = document.createElement("img");
            var imgr = document.createElement("img");
            var imgr2 = document.createElement("img");
            var imgl = document.createElement("img");
            var imgl2 = document.createElement("img");
            var imgu = document.createElement("img");
            var imgu2 = document.createElement("img");
            var sonicd = document.createElement("img");
            var sonicr = document.createElement("img");
            var sonicl = document.createElement("img");
            var sonicu = document.createElement("img");

            imgd.src = "img/down-1-colored.png";
            imgd2.src = "img/down-2-colored.png";
            imgr.src = "img/right-1-colored.png";
            imgr2.src = "img/right-2-colored.png";
            imgl.src = "img/left-1-colored.png";
            imgl2.src = "img/left-2-colored.png";
            imgu.src = "img/up-1-colored.png";
            imgu2.src = "img/up-2-colored.png";
            sonicd.src = "img/sonicwave-down.gif";
            sonicr.src = "img/sonicwave-right.gif";
            sonicl.src = "img/sonicwave-left.gif";
            sonicu.src = "img/sonicwave-up.gif";

            var stance = new Array();
            stance[0] = imgd;
            stance[1] = imgd2;
            stance[2] = imgr;
            stance[3] = imgr2;
            stance[4] = imgl;
            stance[5] = imgl2;
            stance[6] = imgu;
            stance[7] = imgu2;

            var width = c.width;
			var height = c.height;
			var wave = undefined
			var posx = 0;
			var posy = 0;
			var usr = undefined
			var child = undefined
			var mikaWidth = 120;
			var mikaHeight = 100;
			drawBack()

            function clicker() {
                var user = document.getElementById('username').value;
                var childRef = myDataRef.child(user);
                childRef.push();
                childRef.set({x:posx,y:posy,stan:0, beam:0, wavey:0});
                ctx.drawImage(imgd, posx, posy, mikaWidth, mikaHeight);
                usr = user;
                child = childRef
                connectedRef.on('value', function(isOnline) {
			    	if (isOnline.val()) {
			    	    childRef.onDisconnect().remove();
			    	}
			    });
                document.getElementById('log').style.display = 'none';
            }
            

			function drawBack() {
				ctx.drawImage(map.canvas, 0, 0, width, height, 0, 0, width, height);
			}

			function leftArrowPressed() {
				if (posx - 10 > 0) {
					c.width = c.width;
					posx = posx - 10;
					drawBack();
					wave = 2;
					if (hp >= 0) {
						child.update({x:posx, y:posy, stan:4, wavey:wave});
						ctx.drawImage(imgl, posx, posy, mikaWidth, mikaHeight);
						setTimeout(function(){left()}, 200);
					}
			    }
			}

			function left() {
			    if (posx - 10 > 0) {
			        posx = posx - 10;
			        drawBack();
			        wave = 2;
			        child.update({x:posx, y:posy, stan:5, wavey:wave});
			        ctx.drawImage(imgl2, posx, posy, mikaWidth, mikaHeight);
			    }
			}

			function rightArrowPressed() {
				if (posx + 110 < width) {
					c.width = c.width;
					posx = posx + 10;
					drawBack();
					wave = 1;
					if (hp >= 0) {
						child.update({x:posx, y:posy, stan:2, wavey:wave});
						ctx.drawImage(imgr, posx, posy, mikaWidth, mikaHeight);
						setTimeout(function(){right()}, 200);
					}
			    }
			}

			function right() {
			    if (posx + 10 > 0) {
			        posx = posx + 10;
			        drawBack();
			        wave = 1;
			        child.update({x:posx, y:posy, stan:3, wavey:wave});
			        ctx.drawImage(imgr2, posx, posy, mikaWidth, mikaHeight);
			    }
			}

			function downArrowPressed() {
				if (posy + 110 < height) {
					c.width = c.width;
					posy = posy + 10;
					drawBack();
					wave = 0;
					if (hp >= 0) {
						child.update({x:posx, y:posy, stan:0, wavey:wave});
						ctx.drawImage(imgd, posx, posy, mikaWidth, mikaHeight);
						setTimeout(function(){down()}, 200);
					}
				}
			}

			function down() {
			    if (posy + 110 < height) {
			        posy = posy + 10;
			        drawBack();
			        wave = 0;
			        child.update({x:posx, y:posy, stan:1, wavey:wave});
			        ctx.drawImage(imgd2, posx, posy, mikaWidth, mikaHeight);
			    }
			}

			function upArrowPressed() {
				if (posy - 10 > 0) {
					c.width = c.width;
					posy = posy - 10;
					drawBack();
					wave = 3;
					if (hp >= 0) {
						child.update({x:posx, y:posy, stan:6, wavey:wave});
						ctx.drawImage(imgu, posx, posy, mikaWidth, mikaHeight);
						setTimeout(function(){up()}, 200);
					}
				}
			}

			function up() {
			    if (posy - 10 > 0) {
			        posy = posy - 10;
			        drawBack();
			        wave = 3;
			        child.update({x:posx, y:posy, stan:7, wavey:wave});
			        ctx.drawImage(imgu2, posx, posy, mikaWidth, mikaHeight);
			    }
			}

			function redraw() {
			    myDataRef.on('value', function(snapshot) {
			    	    drawBack();
			    	    snapshot.forEach(function(childSnapshot) {
			    	    	    var temp = stance[childSnapshot.val().stan]
			    	    	    var tempx = childSnapshot.val().x;
			    	    	    var tempy = childSnapshot.val().y;
			    	    	    var tempB = childSnapshot.val().beam;
			    	    	    var tempW = childSnapshot.val().wavey;
			    	    	    ctx.drawImage(temp, tempx, tempy, mikaWidth, mikaHeight);
			    	    	    if (tempB == 1) {
			    	    	        sonicWave(tempx, tempy, tempW);
			    	    	        attack(tempx, tempy, tempW);
			    	    	    }
			    	    	});
			    	});
			}

			function attack(dx, dy, wavey) {
			    var x = undefined
			    var y = undefined
			    if (wavey == 0) {
			        var temp = mikaHeight/2;
			        x = dx;
			        y = dy + temp;
			    } else if (wavey == 1) {
			        var temp = mikaWidth/3;
			        x = dx + temp;
			        y = dy;
			    } else if (wavey == 2) {
			        var temp = mikaWidth/3;
			        x = dx - temp;
			        y = dy;
			    } else if (wavey == 3) {
			        var temp = mikaHeight/2;
			        x = dx;
			        y = dy - temp;
			    }
			    var farx = x + mikaWidth;
			    var fary = y + mikaHeight;
			    if (posx > x && posx < farx && posy > y && posy < fary) {
			        hp = hp - 10;
			        document.getElementById("hp").innerHTML = hp;
			        if (hp == 0) {
			            alert("you died, you are a ghost now");
			            child.remove();
			        }
			    }
			}

			function sonicWave(dx, dy, wavey) {
			    if (wavey == 0) {
			        var temp = mikaHeight/2;
			        ctx.drawImage(sonicd, dx, dy + temp, mikaWidth, mikaHeight);
			    } else if (wavey == 1) {
			        var temp = mikaWidth/3;
			        ctx.drawImage(sonicr, dx + temp, dy, mikaWidth, mikaHeight);
			    } else if (wavey == 2) {
			        var temp = mikaWidth/3;
			        ctx.drawImage(sonicl, dx - temp, dy, mikaWidth, mikaHeight);
			    } else if (wavey == 3) {
			        var temp = mikaHeight/2;
			        ctx.drawImage(sonicu, dx, dy - temp, mikaWidth, mikaHeight);
			    }
			}

			document.onkeydown = function(evt) {
			    evt = evt || window.event;
			    switch (evt.keyCode) {
			        case 37:
			            leftArrowPressed();
			            break;
			        case 38:
			            upArrowPressed();
			            break;
			        case 39:
			            rightArrowPressed();
			            break;
			        case 40:
			            downArrowPressed();
			            break;
			        case 13:
			            evt.preventDefault();
			            return false;
			            break;
			        case 32:
			            if (hp >= 0) {
			            child.update({beam: 1});
			            sonicWave(posx, posy, wave);
			            setTimeout(function() {
			            	child.update({beam: 0})
			            	}, 500);
			            break;
			            }
			    }
			};
		</script>
	</body>
</html>
"""

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(login)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
