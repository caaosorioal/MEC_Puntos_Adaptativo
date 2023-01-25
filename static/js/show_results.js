var names_events = {
    "incorrect_lines": ["Incorrect lines", "#cc0000"],
    "correct_lines" : ["Correct lines",  "#7CFC00"],
    "correct_figures" : ["Finished figures", "#00cc00"],
};

function show_data(id_text, data) {
    var n_figures = winning_lines.length;
    var str_message = `${names_events[id_text][0]}: ${data}`;
    
    if (id_text == "correct_figures"){
        str_message = `You've found: ${data} figures (Out of a total of ${n_figures})`;
    } 

    document.getElementById(id_text).innerHTML = str_message;
    
};

function highlight_result(id_text) {
    document.getElementById(id_text).style.backgroundColor = names_events[id_text][1];
};

function back_to_normal_background() {
    document.getElementById("incorrect_lines").style.backgroundColor = "white";
    document.getElementById("correct_lines").style.backgroundColor = "white";
}