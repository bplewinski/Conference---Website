/*
Function returns the group name from the user's choice of options and displays
their vote in an alert box
 */
function submitPoll() {
    let groupName = "";
    let message = "Thank you for voting for ";
    let radioGroup = document.getElementsByName('poll');

    for (let i = 0; i < radioGroup.length; i++) {
        if (radioGroup[i].checked) {
            groupName = radioGroup[i].value;
        }
    }

    if (groupName == "") {
        message = "Please select a nominee.";
    } else {
        message = message + groupName;
    }
    alert(message);

    // ================  Begin storing values in local storage to keep track of user votes for each group ==============
    // If the value is null then votes are set to 0
    if (localStorage.getItem("group1") === null) {
        localStorage.setItem("group1", "0");
    }
    if (localStorage.getItem("group2") === null) {
        localStorage.setItem("group2", "0");
    }
    if (localStorage.getItem("group3") === null) {
        localStorage.setItem("group3", "0");
    }

    // Get the value from local storage
    let value1 = parseInt(localStorage.getItem("group1"));
    let value2 = parseInt(localStorage.getItem("group2"));
    let value3 = parseInt(localStorage.getItem("group3"));

    // Assign value to vote counts
    let vote1 = value1;
    let vote2 = value2;
    let vote3 = value3;

    // Increment votes if checked
    if (document.getElementById('Brian').checked) {
        vote1++;
    }
    if (document.getElementById('Peiyin').checked) {
        vote2++;
    }
    if (document.getElementById('Nacho').checked) {
        vote3++;
    }

    //Write the value back to local storage
    localStorage.setItem("group1", vote1.toString());
    localStorage.setItem("group2", vote2.toString());
    localStorage.setItem("group3", vote3.toString());
}
/*
Function displays the value in local storage upon the page loading
 */
function pollVotes() {
    let total = " votes: "
    document.getElementById("group1").innerHTML = total + localStorage.getItem(localStorage.key(0));
    document.getElementById("group2").innerHTML = total + localStorage.getItem(localStorage.key(1));
    document.getElementById("group3").innerHTML = total + localStorage.getItem(localStorage.key(2));
}
