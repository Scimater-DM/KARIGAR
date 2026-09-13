console.log("KARIGAR app.js loaded");


/* =========================================================
   SAATHI
   ========================================================= */

function openSaathi() {

    console.log("Opening Saathi");

    const panel = document.getElementById("saathiPanel");
    const overlay = document.getElementById("saathiOverlay");

    if (!panel) {
        console.error("Saathi panel not found.");
        return;
    }

    if (!overlay) {
        console.error("Saathi overlay not found.");
        return;
    }

    panel.classList.add("is-open");
    overlay.classList.add("is-open");

    panel.setAttribute("aria-hidden", "false");

    document.body.classList.add("saathi-open");
}


function closeSaathi() {

    console.log("Closing Saathi");

    const panel = document.getElementById("saathiPanel");
    const overlay = document.getElementById("saathiOverlay");

    if (!panel || !overlay) {
        return;
    }

    panel.classList.remove("is-open");
    overlay.classList.remove("is-open");

    panel.setAttribute("aria-hidden", "true");

    document.body.classList.remove("saathi-open");
}


/* =========================================================
   SAATHI ACTIONS
   ========================================================= */

function saathiAction(action) {

    if (action === "Tell my story") {

        const name = prompt(
            "Saathi: What is your name?"
        );

        if (!name) return;

        const craft = prompt(
            "Saathi: What craft do you make?"
        );

        if (!craft) return;

        const place = prompt(
            "Saathi: Where are you from?"
        );

        if (!place) return;

        const story =
            `${name} is a craftsperson from ${place} who creates ${craft}. ` +
            `Their work carries the skill, character and story of their craft tradition.`;

        const result = document.getElementById("saathiStoryResult");

if (result) {
    result.innerHTML = `
        <span class="eyebrow">YOUR STORY DRAFT</span>
        <h3>${story}</h3>
        <p>AI drafts. You decide.</p>
        <button
            type="button"
            class="button button--primary"
            onclick="closeSaathi()"
        >
            Keep this draft ↗
        </button>
    `;

    result.classList.add("is-visible");
}

        return;
    }


    const messages = {

        "Price my work":
            "Saathi can help you think through a fair price for your craft.",

        "Show my work":
            "Saathi can help prepare your craft for discovery.",

        "Find buyers":
            "Saathi can help you think about reaching the right buyers."

    };


    alert(
        messages[action] ||
        "Saathi is ready to help."
    );
}


/* =========================================================
   SAATHI VOICE
   ========================================================= */

function startSaathiVoice() {

    const Recognition =
        window.SpeechRecognition ||
        window.webkitSpeechRecognition;


    if (!Recognition) {

        alert(
            "Voice interaction is not supported in this browser yet."
        );

        return;
    }


    const recognition = new Recognition();

    recognition.lang = "en-IN";

    recognition.interimResults = false;

    recognition.maxAlternatives = 1;


    recognition.onstart = function () {

        document.body.classList.add(
            "saathi-listening"
        );

    };


    recognition.onresult = function (event) {

        const transcript =
            event.results[0][0].transcript;


        document.body.classList.remove(
            "saathi-listening"
        );


        alert(
            "Saathi heard:\n\n" +
            transcript +
            "\n\n" +
            "Prototype response:\n" +
            "I can help you with your next step."
        );

    };


    recognition.onerror = function () {

        document.body.classList.remove(
            "saathi-listening"
        );


        alert(
            "Voice input couldn't be completed."
        );

    };


    recognition.onend = function () {

        document.body.classList.remove(
            "saathi-listening"
        );

    };


    try {

        recognition.start();

    } catch (error) {

        console.error(
            "Saathi voice error:",
            error
        );

    }

}


/* =========================================================
   KEYBOARD
   ========================================================= */

document.addEventListener(
    "keydown",
    function (event) {

        if (event.key === "Escape") {

            closeSaathi();

        }

    }
);