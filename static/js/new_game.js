$("#new_game").on("click", evt => {
    // Prevent the default action of the button
    evt.preventDefault();

    // Reload the page
    if (confirm("Are you sure you want to start a new game?")){
        location.reload();
    };
});