var names_events = {
    "incorrect_lines": ["Incorrect lines", "#cc0000"],
    "correct_lines" : ["Correct lines",  "#7CFC00"],
    "correct_figures" : ["Finished figures", "#00cc00"],
};

function show_data(id_text, data) {
    document.getElementById(id_text).innerHTML = `${names_events[id_text][0]}: ${data}`;
};

function highlight_result(id_text) {
    document.getElementById(id_text).style.backgroundColor = names_events[id_text][1];
};

function back_to_normal_background() {
    document.getElementById("incorrect_lines").style.backgroundColor = "white";
    document.getElementById("correct_lines").style.backgroundColor = "white";
}