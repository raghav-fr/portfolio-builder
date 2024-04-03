let display=1;
function popup(){
    skillitem=document.getElementById("skd1");
    skillbtn=document.getElementById("skbtn");
    if(display==1){
        skillitem.classList.add("popup");
        skillbtn.classList.add("btnrotate");
        display=0;
    }
    else{
        skillitem.classList.remove("popup");
        skillbtn.classList.remove("btnrotate");
        display=1;
    }

}
const sections = document.querySelectorAll('.section');
const previousButton = document.querySelector('#svg1');
const nextButton = document.querySelector('#svg2');
const line1=document.querySelector(".line1");
const line2=document.querySelector(".line2");
let currentIndex = 0;

function showCurrentSection() {
  sections.forEach((section, index) => {
    if (index === currentIndex) {
      section.style.display = 'block';
    } else {
      section.style.display = 'none';
    }
  });

  // Hide/show previous and next buttons based on current index
  if (currentIndex === 0) {
    line2.style.height='191px';
    previousButton.style.display = 'none';
  } else {
    line2.style.height='113px';
    previousButton.style.display = 'block';
  }

  if (currentIndex === sections.length - 1) {
    line1.style.height='371px';
    line1.style.bottom='179px';
    nextButton.style.display = 'none';
  } else {
    line1.style.height='291px';
    line1.style.bottom='258px';
    nextButton.style.display = 'block';
  }
}

function prev() {
  currentIndex = (currentIndex - 1 + sections.length) % sections.length;
  showCurrentSection();
}

function next() {
  currentIndex = (currentIndex + 1) % sections.length;
  showCurrentSection();
}

// Show initial section
showCurrentSection();

var progressBarOptions = {
  rootMargin: '0px',
  threshold: 0
};

window.addEventListener('scroll', function() {
  var content = document.getElementById('content');
  var progressBar = document.getElementById('progress');
  var progressTopic = document.getElementById('topic');
  var windowHeight = window.innerHeight;
  var contentSections = document.querySelectorAll('.cs');
  var scrollPosition = window.scrollY;

  // Find the position of the progress bar relative to the viewport
  var progressTopicTop = progressTopic.getBoundingClientRect().top;
  var progressTopicHeight = progressTopic.clientHeight;
  var progressBarTop = progressTopicTop + progressTopicHeight;

  // Calculate progress when scrolling past the progress bar topic
  if (scrollPosition >= progressBarTop) {
    var maxScroll = content.clientHeight - windowHeight;
    var scrolledPast = scrollPosition - progressBarTop;
    var progress = (maxScroll - scrolledPast) / maxScroll * 100;
    console.log(progress)
    if(progress>5){
      progressBar.style.width = progress + '%';
    }
  } else {
    progressBar.style.width = '100%'; // Reset progress bar width
  }
});

