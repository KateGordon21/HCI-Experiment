var currentLoopedSound;

function toggleElements(previousPageName, newPageName, loopSound, selectSound) {
    // Pause and reset the current looped sound
    if (currentLoopedSound) {
        currentLoopedSound.pause();
        currentLoopedSound.currentTime = 0;
    }

    // Play the select sound if provided
    if (selectSound != null) {
        var sound = document.getElementById(selectSound);
        sound.play();
    }

    var previousPage = document.getElementById(previousPageName);
    var newPage = document.getElementById(newPageName);

    // Toggle visibility of elements
    previousPage.style.display = "none";
    newPage.style.display = "block";

    document.body.style.backgroundColor = (newPageName === 'healthAndSafetyPage') ? '#000' : '#ffffff';

    // Play the new looped sound
    currentLoopedSound = document.getElementById(loopSound);

    currentLoopedSound.addEventListener("ended", function () {
        this.currentTime = 0;
        this.play();
    });

    currentLoopedSound.play(); // Start playing the sound
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('pressA').addEventListener('click', function() {
        document.querySelector('#healthAndSafetyPage').style.display = 'none';
        document.querySelector('#loadingPage').style.display = 'block';
        var audio = document.getElementById("startSound");
        audio.play();
    });

    var wiiStartSound = document.getElementById('startSound');
    wiiStartSound.addEventListener('ended', function() {
    toggleElements('loadingPage', 'homePage', 'mainMenuSound', null);
    });

    document.getElementById('startButton').addEventListener('click', function() {
        toggleElements('homePage', 'informedConsent', 'shopSound', 'selectSound');
    });
});

function playAudioAndRedirect(url) {
    var audio = document.getElementById("selectSound");
    audio.play();
    setTimeout(function () {
        window.location.href = url;
    }, audio.duration * 1000); // Redirect after the duration of the audio
}

// Animation for loading
var squares = document.querySelectorAll('.loading-square');
var indices = [0, 1, 2, 4, 7, 6, 5, 3];

async function switchColor() {
    for (let i = 0; i < indices.length; i++) {
        if(squares[indices[i]].classList.contains('blue'))
        {
            squares[indices[i]].classList.remove('blue');
            squares[indices[i]].classList.add('black');
            await new Promise(resolve => setTimeout(resolve, 76));
            squares[indices[i]].classList.remove('black');
            squares[indices[i]].classList.add('blue');
        }
        else if(squares[indices[i]].classList.contains('medium-blue'))
        {
            squares[indices[i]].classList.remove('medium-blue');
            squares[indices[i]].classList.add('black');
            await new Promise(resolve => setTimeout(resolve, 76));
            squares[indices[i]].classList.remove('black');
            squares[indices[i]].classList.add('medium-blue');
        }
        else
        {
            squares[indices[i]].classList.remove('light-blue');
            squares[indices[i]].classList.add('black');
            await new Promise(resolve => setTimeout(resolve, 76));
            squares[indices[i]].classList.remove('black');
            squares[indices[i]].classList.add('light-blue');
        }

    }

    setTimeout(switchColor, 0); // Call the function again after the sequence is completed
}

// Start the animation
switchColor();