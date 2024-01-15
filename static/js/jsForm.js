/*
Function returns true or false after sorting the checked radio buttons
to help determine if the form can be submitted or not.
 */
function submitReturn() {

    let sesh1 = document.getElementsByName("diet");
    let sesh2 = document.getElementsByName("exercise");
    let sesh3 = document.getElementsByName("wellbeing");

    let choice1;
    let choice2;
    let choice3;

    let valid = true;
    let newWin;
    let message = "";

    //if user checks a radio button it will be stored in each choice
    for (let i = 0; i < 3; i++) {
        if (sesh1[i].checked) {
            choice1 = sesh1[i].value;
        }
        if (sesh2[i].checked) {
            choice2 = sesh2[i].value;
        }
        if (sesh3[i].checked) {
            choice3 = sesh3[i].value;
        }
    }

    //if user chooses workshop B(micros/macros), radio buttons in session 2 will be unchecked.
    if (choice1 === "micros/macros") {
        if (choice2 === "cardio" || choice2 === "weights" || choice2 === "recovery") {
            document.getElementById('cardio').checked = false;
            document.getElementById('weights').checked = false;
            document.getElementById('recovery').checked = false;
            message = message + "\nSorry, the 'recovery' workshop must be chosen " +
                "when choosing the 'lifestyle' workshop."
            valid = false;
        }
    }
    //if user checks workshop F(recovery), workshop G(stress) or I(relationships) will be unchecked
    if (choice2 === "recovery") {
        if (choice3 === "stress" || choice3 === "relationships") {
            document.getElementById('stress').checked = false;
            document.getElementById('relationships').checked = false;
            message = message + "<p>Sorry, but when choosing 'recovery' workshop, you are required to " +
                "take the 'lifestyle workshop in session 3, as they go hand in hand.</p>";

            valid = false;
        }
    }
    //else workshop H(lifestyle) can only be checked with workshop F(recovery) and vice versa.
    else {
        if (choice3 === "lifestyle") {
            message = message + "<p>Sorry, but when choosing 'lifestyle' workshop, you are required to " +
                "take the 'recovery workshop in session 2, as they go hand in hand.</p>";
            valid = false;
        }
    }
    if (!valid) {
        let width = 500;
        let height = 400;
        let left = window.screenLeft;

        let top = window.screenTop;
        left = left + ((window.innerWidth - width) / 2);
        top = top + ((window.innerHeight - height) / 2);

        let attributes = "width=" + width + ",height=" + height + ",left=" + left + ",top=" + top;
        newWin = window.open("", "", attributes);
        newWin.document.write(message);
    }

    // ================  Begin creating cookie array of values from registration from ==============
    //checking for correct idnumber
    let idNum = document.getElementById("idnumber").value;
    let title = document.getElementById("title").value;
    let fName = document.getElementById("first").value;
    let lName = document.getElementById("last").value;
    let address = document.getElementById("address1").value;
    let city = document.getElementById("city").value;
    let state = document.getElementById("state").value;
    let zip = document.getElementById("zip").value;
    let phone = document.getElementById("phone").value;
    let email = document.getElementById("email").value;
    let job = document.getElementById("position").value;
    let company = document.getElementById("company").value;

    if (idNum !== "123456") {
        valid = false;
        alert("Sorry, but that ID number isn't valid.");
    } else {
        let cookieString = "title:" + title + "|first:" + fName + "|last:" + lName + "|address1:" + address +
            "|city:" + city + "|state:" + state + "|zip:" + zip + "|phone:" + phone +
            "|email:" + email + "|position:" + job + "|company:" + company +
            "|diet:" + choice1 + "|exercise:" + choice2 + "|wellbeing:" + choice3;
        document.cookie = idNum + "=" + cookieString;
        console.log(document.cookie);
    }
    return valid;
}

/*
Checking for the cookies
 */
function checkCookie() {
    let allCookies = document.cookie;
    console.log(allCookies);

    // ================  First, parse all the cookies to find a specific cookie ==============
    // Parse the cookie and search for the id number
    let found = false;
    let keyValPair = []                                     // Creating an array to hold a key and a value
    let userData = null;
    let cookieArray = allCookies.split(";");        // Array of cookies - There will be more than one cookie.
    console.log(cookieArray);

    for (let i = 0; i < cookieArray.length; i++) {          // Iterate through array to look at each cookie
        keyValPair = cookieArray[i].split("=");     // Create an array of a specific key and value
        keyValPair[0] = keyValPair[0].trim();               // Get rid of the leading blanks
        keyValPair[1] = keyValPair[1].trim();
        console.log(keyValPair);

        // Let's look for a specific cookie.
        let idNum = document.getElementById("idnumber").value;
        if (keyValPair[0] === idNum) {                   // Test to see if it is the cookie we are looking for.
            userData = keyValPair[1];                    // A cookie exists for this idNum, so we can use the data.
            found = true;
        }
    }

    // ================  Next, parse the "value" of the cookie to yield key-value pairs ==============

    if (found) {
        // Now, we need to parse the user's data
        let userkey = null;
        let uservalue = null;
        let keyvalTempArray;

        let userDataKVPs = userData.split('|');
        console.log(userDataKVPs);

        for (let j = 0; j < userDataKVPs.length; j++) {
            keyvalTempArray = userDataKVPs[j].split(':');
            userkey = keyvalTempArray[0];
            console.log(userkey);
            uservalue = keyvalTempArray[1];
            console.log(uservalue);


            if (userkey === "diet") {
                let dietButtons = document.getElementsByName(userkey);
                for (let i = 0; i < 3; i++) {
                    if (dietButtons[i].value === uservalue) {
                        dietButtons[i].checked = true;
                        console.log(dietButtons);
                    }
                }
            }
            else if (userkey === "exercise") {
                let exerciseButtons = document.getElementsByName(userkey);
                for (let i = 0; i < 3; i++) {
                    if (exerciseButtons[i].value === uservalue) {
                        exerciseButtons[i].checked = true;
                        console.log(exerciseButtons);
                    }
                }
            }
            else if (userkey === "wellbeing") {
                let wellButtons = document.getElementsByName(userkey);
                for (let i = 0; i < 3; i++) {
                    if (wellButtons[i].value === uservalue) {
                        wellButtons[i].checked = true;
                    }
                }
            }
            else {
                document.getElementById(userkey).value = uservalue;
            }
        }
    }
}
