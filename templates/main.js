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
        toggleElements('healthAndSafetyPage', 'homePage', 'mainMenuSound', 'startSound');
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