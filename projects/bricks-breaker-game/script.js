var Timer = document.querySelector(".timer");
var ttime = 30;
setInterval(function () {
  Timer.innerHTML = `TIME: ${ttime}`;
  if (ttime > 0) {
    ttime -= 1;
    if (ttime < 3) Timer.style.color = "red";
  } else shutdown();
}, 1000);

const colors = ["#008080", "#6A5ACD"];
const time = 5;
var lost = false;
var moveLeft = false,
  moveRight = false;
// var x = Math.floor(Math.random() * (299 - 1 + 1)) + 1,
//   y = Math.floor(Math.random() * (400 - 1 + 1)) + 1
var x = 200,
  y = 200;
var stepX = 2,
  stepY = -2;
var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
var bar = {
  x: 100,
  y: 394,
  width: 100,
  height: 6,
};

var blocs = [];
function fillTable() {
  for (let i = 0; i < 20; i++) {
    for (let j = 0; j < 10; j++) {
      blocs.push({
        x: 20 * i,
        y: 20 * j,
        width: 19,
        height: 19,
      });
    }
  }
}
fillTable();
document.body.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") moveLeft = true;
  else if (e.key === "ArrowRight") moveRight = true;
  else if (e.key === "Enter" && lost) {
    lost = false;
    ttime = 30;
    Timer.style.color = "blue";
    // x = Math.floor(Math.random() * (299 - 1 + 1)) + 1;
    // y = Math.floor(Math.random() * (400 - 1 + 1)) + 1;
    (x = 200), (y = 200);
    stepX = 2;
    stepY = -2;
    document.getElementsByClassName("shutdown")[0].classList.remove("show");
    play();
  }
});
document.body.addEventListener("keyup", (e) => {
  if (e.key === "ArrowLeft") moveLeft = false;
  else if (e.key === "ArrowRight") moveRight = false;
});
const play = () => {
  var interval = setInterval(() => {
    if (!lost) {
      move();
      draw();

      if (
        ((x + 10 >= bar.x && x + 10 <= bar.x + bar.width) ||
          (x - 10 >= bar.x && x - 10 <= bar.x + bar.width)) &&
        y + 10 === bar.y
      ) {
        stepY *= -1;
        if (moveLeft && Math.sign(stepX) === 1) stepX *= -1;
        else if (moveRight && Math.sign(stepX) === -1) stepX *= -1;
      }
      if ((x + 10 === bar.x || x - 10 === bar.x + bar.width) && y + 10 > bar.y)
        stepX *= -1;

      if (x + 10 >= c.width || x - 10 <= 0) stepX *= -1;
      if (y - 10 <= 0) stepY *= -1;
      if (y + 10 > c.height + 20) lost = true;
      clearBloc();
      win();
    } else {
      console.log("lost");
      clearInterval(interval);
      fillTable();
      shutdown();
    }
  }, time);
};

play();

function draw() {
  ctx.clearRect(0, 0, c.width, c.height);
  ctx.beginPath();
  ctx.arc(x, y, 10, 0, Math.PI * 2);
  ctx.fillStyle = "black";
  ctx.strokeStyle = "#000";
  ctx.stroke();
  ctx.fill();
  ctx.closePath();
  x += stepX;
  y += stepY;
  ctx.fillRect(bar.x, bar.y, bar.width, bar.height);
  restartBlocks();
}

const move = () => {
  if (moveLeft) {
    if (bar.x > 0) bar.x -= 2;
  }
  if (moveRight) {
    if (bar.x + bar.width < c.width) bar.x += 2;
  }
};
const shutdown = () => {
  document.getElementsByClassName("shutdown")[0].classList.add("show");
  // ttime = 30;
  // Timer.style.color = "blue";
};
const win = () => {
  if (blocs.length == 0 && ttime > 0) {
    document.getElementsByClassName("shutdown")[1].classList.add("show");
    // ttime = 30;
    // Timer.style.color = "blue";
  }
};
console.log(Timer);

////add some blocks in game

function restartBlocks() {
  var rec = c.getContext("2d");
  rec.fillStyle = "red";
  blocs.forEach((bloc) => {
    rec.fillRect(bloc.x, bloc.y, bloc.width, bloc.height);
  });
  // rec.fillRect(bloc.x+100, bloc.y, bloc.width, bloc.height);
}
function clearBloc() {
  blocs = blocs.filter(
    (bloc) =>
      !(
        bloc.x + bloc.width > x &&
        x > bloc.x &&
        bloc.y + bloc.height > y &&
        y > bloc.y
      )
  );
}
